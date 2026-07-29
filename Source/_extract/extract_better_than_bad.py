# -*- coding: utf-8 -*-
"""Extract Better Than Bad PDF into Source Texts/Better Than Bad/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\better-than-bad-pdf.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Better Than Bad")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Printed page N ~= PDF index N for this book (cover blanks = 0-1).
SECTIONS = [
    ("01 - Contents & Credits.md", "Contents & Credits", 2, 4),
    ("02 - JackPoint.md", "JackPoint", 4, 5),
    ("03 - Introduction.md", "Introduction", 5, 6),  # split below with credits
    ("04 - Friends Will Be Friends.md", "Friends Will Be Friends", 6, 10),
    ("05 - Lights in the Darkness.md", "Lights in the Darkness", 10, 26),
    ("06 - Fixer-Upper Opportunities.md", "Fixer-Upper Opportunities", 26, 68),
    ("07 - Pretoria, Hurrah.md", "Pretoria, Hurrah", 68, 114),
    ("08 - Mining For Gold.md", "Mining For Gold", 114, 118),
    ("09 - Jacaranda Citizens.md", "Jacaranda Citizens", 118, 140),
    ("10 - Being Less Bad.md", "Being Less Bad", 140, 156),
    ("11 - Building a Hooder.md", "Building a Hooder", 156, 165),
    ("12 - Hooder Runs.md", "Hooder Runs", 165, 169),
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
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")
    text = text.replace("\t", " ")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*BETTER THAN BAD\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^<<\s*BETTER THAN BAD\s*>>\s*$", s, re.I):
            continue
        # Running headers/footers: "10    LIGHTS IN THE DARKNESS >>"
        if re.match(
            r"^\d+\s+[A-Z0-9,&'\- ]{3,50}>>\s*$",
            s,
        ):
            continue
        if re.match(
            r"^<<\s*[A-Z0-9,&'\- ]{3,50}\s+\d+\s*$",
            s,
        ):
            continue
        if re.match(
            r"^\d+\s+>>\s*[A-Z0-9,&'\- ]{3,50}<<\s*$",
            s,
        ):
            continue
        if re.match(
            r"^>>\s*[A-Z0-9,&'\- ]{3,50}<<\s+\d+\s*$",
            s,
        ):
            continue
        if re.match(r"^[A-Z0-9,&'\- ]{3,50}>>\s*$", s) and "CONTENTS" in s.upper():
            continue
        lines.append(s)

    text = "\n".join(lines)
    # Join common two-line chapter banners
    text = re.sub(
        r"(?im)^FRIENDS WILL\s*\nBE FRIENDS\s*$",
        "FRIENDS WILL BE FRIENDS",
        text,
    )
    text = re.sub(
        r"(?im)^MINING\s*\nFOR GOLD\s*$",
        "MINING FOR GOLD",
        text,
    )
    text = re.sub(
        r"(?im)^THE FINE\s*\nART OF HOODING\s*$",
        "THE FINE ART OF HOODING",
        text,
    )
    text = re.sub(
        r"(?im)^PRETORIA-WITWA-?\s*\nTERSRAND-VAAL\s*\nMETROPLEX\s*$",
        "PRETORIA-WITWATERSRAND-VAAL METROPLEX",
        text,
    )
    text = re.sub(
        r"(?im)^BETTER THAN BAD\s*\nHOODER\s*\nRUNS\s*$",
        "HOODER RUNS",
        text,
    )
    text = re.sub(
        r"(?im)^IF YOU CAN'T GET\s*\nWHAT YOU WANT,\s*\nTRY FOR WHAT YOU NEED\s*$",
        "IF YOU CAN'T GET WHAT YOU WANT, TRY FOR WHAT YOU NEED",
        text,
    )
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def split_credits_and_intro(page5: str) -> tuple[str, str]:
    raw = clean(page5)
    m = re.search(r"(?im)^INTRODUCTION\s*$", raw)
    if not m:
        return "", raw
    credits = raw[: m.start()].rstrip() + "\n"
    intro = raw[m.start() :].lstrip()
    intro = re.sub(r"(?im)^INTRODUCTION\s*\n+", "", intro, count=1)
    return credits, intro


def strip_leading_title(body: str, title: str) -> str:
    # Allow & / punctuation variance
    esc = re.escape(title.upper())
    esc = esc.replace(r"\&", r"\s*&\s*")
    esc = esc.replace(r"\-", r"[\- ]?")
    body = re.sub(rf"(?im)^{esc}\s*\n+", "", body, count=1)
    return body


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    page5 = doc[5].get_text("text") or ""
    credits_tail, intro_body = split_credits_and_intro(page5)

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size < 300:
            p.unlink()
            print("removed stub", p.name)

    for fname, title, start, end in SECTIONS:
        if fname.startswith("01 -"):
            parts = [doc[i].get_text("text") or "" for i in range(2, 4)]
            body = clean("\n\n".join(parts))
            if credits_tail.strip():
                body = body.rstrip() + "\n\n" + credits_tail.lstrip()
            body = strip_leading_title(body, "BETTER THAN BAD CREDITS")
            # Keep TOC readable; drop repeated book title smash at end of p2
            body = re.sub(
                r"(?im)^BETTER THAN BAD\s*\nCONTENTS\s*\n&\s*CREDITS\s*$",
                "",
                body,
            )
            span = "PDF page index 2-3 + credits from idx 5"
        elif fname.startswith("03 -"):
            body = intro_body if intro_body.strip() else clean(page5)
            span = "PDF page index 5 (Introduction)"
        else:
            parts = [
                doc[i].get_text("text") or ""
                for i in range(start, min(end, len(doc)))
            ]
            body = clean("\n\n".join(parts))
            body = strip_leading_title(body, title)
            # JackPoint page carries CONTENTS & CREDITS running header
            if fname.startswith("02 -"):
                body = re.sub(
                    r"(?im)^4\s+CONTENTS\s*&\s*CREDITS\s*>>\s*\n+",
                    "",
                    body,
                )
            span = f"PDF page index {start}-{end - 1}"

        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only or blank. See {span}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** Better Than Bad | "
            f"`Source/PDF/{PDF.name}` | {span}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    index_rows = "\n".join(
        f"| {n} | [{title}]({fname.replace(' ', '%20')}) | {start}-{end - 1} |"
        for n, (fname, title, start, end) in enumerate(SECTIONS, 1)
    )
    index = f"""# Better Than Bad

Hooding / runs with a conscience; Pretoria setting.

**PDF:** `Source/PDF/{PDF.name}` ({len(doc)} pages; print page ≈ PDF index for body).

Extractor: `Source/_extract/extract_better_than_bad.py` (pymupdf).

Note: print page 5 holds **Credits** then **Introduction**; extract splits that page.
JackPoint is print/PDF idx 4 (outline TOC listed it as 5).

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{index_rows}

## Pipeline status

- [x] Extract
- [ ] Format
- [ ] Loss-check
- [ ] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("\u2013", "-").replace("—", "-"),
        encoding="utf-8",
    )
    print("updated INDEX.md")
    doc.close()


if __name__ == "__main__":
    main()
