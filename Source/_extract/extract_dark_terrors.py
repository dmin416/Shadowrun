# -*- coding: utf-8 -*-
"""Extract Dark Terrors PDF into Source Texts/Dark Terrors/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\darkterrors.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Dark Terrors")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# PDF TOC page N ~= PDF index N-1. Printed book page ≈ PDF index for mid-book.
SECTIONS: list[tuple[str, str, int, int]] = [
    ("01 - Shadowrun Dark Terrors.md", "Shadowrun: Dark Terrors", 0, 2),
    ("02 - Contents & Credits.md", "Contents & Credits", 2, 6),
    ("03 - JackPoint.md", "JackPoint", 4, 5),
    ("04 - Introduction.md", "Introduction", 5, 6),
    ("05 - Darker than Shadows.md", "Darker than Shadows", 6, 10),
    ("06 - The Heart of the Hive.md", "The Heart of the Hive", 10, 34),
    ("07 - Marooned Spirits.md", "Marooned Spirits", 34, 52),
    ("08 - Paint It Blacker.md", "Paint It Blacker", 52, 70),
    ("09 - Monads and CFD.md", "Monads and CFD", 70, 88),
    ("10 - The Hidden Faction.md", "The Hidden Faction", 88, 98),
    ("11 - Revelations.md", "Revelations", 98, 102),
    ("12 - Followers of the Elder God.md", "Followers of the Elder God", 102, 120),
    ("13 - Dwellers of the Deep Foundations.md", "Dwellers of the Deep Foundations", 120, 134),
    ("14 - The Ghoul Queen and Her People.md", "The Ghoul Queen and Her People", 134, 170),
    ("15 - Untamed Metaplanes.md", "Untamed Metaplanes", 170, 182),
    ("16 - Rules Index.md", "Rules Index", 182, 186),
]


def clean(text: str) -> str:
    repl = {
        "\u2014": "-",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\xa0": " ",
        "\u2022": "*",
        "\uf0b7": "*",
        "\ufeff": "",
        "\ufffd": "",
        "\xad": "",
        "\u2026": "...",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = text.replace("�", "")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")
    # normalize JackPoint markers
    text = re.sub(r"^>\s*$", ">", text, flags=re.M)
    text = re.sub(r"^>\t\s*", ">\n", text, flags=re.M)

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*DARK TERRORS\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^>>\s*DARKER THAN SHADOWS\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^>>\s*REVELATIONS\s*<<\s*$", s, re.I):
            continue
        # "<< CHAPTER    N" / "N    CONTENTS & CREDITS >>"
        if re.match(r"^<<\s*.+?\s+\d+\s*$", s):
            continue
        if re.match(r"^\d+\s+.+?\s*>>\s*$", s):
            continue
        if re.match(r"^<<\s*CONTENTS\s*&\s*CREDITS\s+\d+\s*$", s, re.I):
            continue
        lines.append(s)

    text = "\n".join(lines)
    joins = [
        (r"(?im)^CONTENTS\s*\n&\s*CREDITS\s*$", "CONTENTS & CREDITS"),
        (r"(?im)^DARKER THAN\s*\nSHADOWS\s*$", "DARKER THAN SHADOWS"),
        (r"(?im)^SCARRED MINDS\s*\nAND CRUMBLING\s*\nTOWERS\s*$", "SCARRED MINDS AND CRUMBLING TOWERS"),
        (r"(?im)^FRAGMENTS\s*\nOF BEYOND\s*$", "FRAGMENTS OF BEYOND"),
        (
            r"(?im)^POSTED BY: SOMEONE SMART\s*\nENOUGH TO AVOID A BYLINE ON THIS\s*$",
            "POSTED BY: SOMEONE SMART ENOUGH TO AVOID A BYLINE ON THIS",
        ),
        (
            r"(?im)^OPTIONAL RULES: PLAYABLE\s*\nFREE INSECT SPIRIT\s*$",
            "OPTIONAL RULES: PLAYABLE FREE INSECT SPIRIT",
        ),
        (
            r"(?im)^EXCERPT FROM ARES INTEL REPORT\s*$",
            "EXCERPT FROM ARES INTEL REPORT",
        ),
    ]
    for pat, repl in joins:
        text = re.sub(pat, repl, text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def split_credits_and_intro(page: str) -> tuple[str, str]:
    raw = clean(page)
    m = re.search(r"(?im)^INTRODUCTION\s*$", raw)
    if not m:
        return raw, ""
    return raw[: m.start()].rstrip() + "\n", raw[m.start() :].lstrip()


def strip_leading_title(body: str, title: str) -> str:
    body = re.sub(rf"(?i)\A{re.escape(title)}\s*\n+", "", body, count=1)
    for banner in (
        "CONTENTS & CREDITS",
        "CONTENTS",
        "CREDITS",
        "DARK TERRORS CREDITS",
        "JACKPOINT",
        "INTRODUCTION",
        "DARKER THAN SHADOWS",
        "THE HEART OF THE HIVE",
        "MAROONED SPIRITS",
        "PAINT IT BLACKER",
        "MONADS AND CFD",
        "THE HIDDEN FACTION",
        "REVELATIONS",
        "FOLLOWERS OF THE ELDER GOD",
        "DWELLERS OF THE DEEP FOUNDATIONS",
        "THE GHOUL QUEEN AND HER PEOPLE",
        "UNTAMED METAPLANES",
        "RULES INDEX",
        "DARK TERRORS",
        "FRAGMENTS OF BEYOND",
    ):
        body = re.sub(rf"(?i)\A{re.escape(banner)}\s*\n+", "", body, count=1)
    return body


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    page5 = doc[5].get_text("text") or ""
    credits_part, intro_part = split_credits_and_intro(page5)

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size < 400:
            p.unlink()
            print("removed stub", p.name)

    for fname, title, start, end in SECTIONS:
        if fname.startswith("02 -"):
            parts = [doc[i].get_text("text") or "" for i in range(2, 4)]
            parts.append(credits_part)
            body = clean("\n\n".join(parts))
            span = "PDF page index 2-3 + credits on 5"
        elif fname.startswith("03 -"):
            body = clean(doc[4].get_text("text") or "")
            span = "PDF page index 4"
        elif fname.startswith("04 -"):
            body = intro_part if intro_part.strip() else clean(page5)
            span = "PDF page index 5 (Introduction)"
        else:
            parts = [
                doc[i].get_text("text") or ""
                for i in range(start, min(end, len(doc)))
            ]
            body = clean("\n\n".join(parts))
            span = f"PDF page index {start}-{end - 1}"

        body = strip_leading_title(body, title)
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only or blank. See {span}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** Dark Terrors | "
            f"`Source/PDF/{PDF.name}` | {span}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    rows = "\n".join(
        f"| {n:02d} | [{title}]({fname.replace(' ', '%20')}) | {start}-{end - 1} |"
        for n, (fname, title, start, end) in enumerate(SECTIONS, 1)
    )
    index = f"""# Dark Terrors

CFD-era horror / threats plot book.

**PDF:** `Source/PDF/{PDF.name}` ({len(doc)} pages; TOC page ≈ PDF index + 1)

Source Texts extracted via `Source/_extract/extract_dark_terrors.py` (pymupdf).
Formatting: `Source/_extract/format_dark_terrors.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{rows}

Note: print page 5 (PDF idx 5) holds **Credits** then **Introduction**; extract splits that page. JackPoint is PDF idx 4.

## Pipeline status

- [x] Extract
- [ ] Format
- [ ] Loss-check
- [ ] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("\u2013", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")
    doc.close()


if __name__ == "__main__":
    main()
