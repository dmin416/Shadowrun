# -*- coding: utf-8 -*-
"""Extract Hard Targets PDF into Source Texts/Hard Targets/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Hard_Targets.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Hard Targets")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Printed page N ~= PDF index N-1 (cover blank PDF 0-1).
SECTIONS = [
    ("01 - Shadowrun Hard Targets.md", "Shadowrun: Hard Targets", 0, 2),
    ("02 - Table of Contents.md", "Table of Contents", 2, 4),
    ("03 - Credits.md", "Credits", 3, 4),
    ("04 - JackPoint.md", "JackPoint", 4, 5),
    ("05 - Introduction.md", "Introduction", 5, 6),
    ("06 - Justice for Hire.md", "Justice for Hire", 6, 10),
    ("07 - Desperate Times.md", "Desperate Times", 10, 42),
    ("08 - ...And Desperate Measures.md", "...And Desperate Measures", 42, 62),
    ("09 - Killers, Saviors, and Hunters.md", "Killers, Saviors, and Hunters", 62, 76),
    ("10 - Slow and Steady Death.md", "Slow and Steady Death", 76, 80),
    ("11 - Havana Dale A Todo Meter!.md", "Havana: Dale A Todo Meter!", 80, 144),
    ("12 - Chameleon.md", "Chameleon", 144, 148),
    ("13 - Becoming Death.md", "Becoming Death", 148, 178),
    ("14 - The Wetwork Toolkit.md", "The Wetwork Toolkit", 178, 198),
    ("15 - Game Information.md", "Game Information", 198, 208),
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
        "\u2026": "...",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*HARD TARGETS\s*<<\s*$", s, re.I):
            continue
        # ">> INTRODUCTION <<    5" / "10    >> DESPERATE TIMES <<"
        if re.match(r"^>>\s*.+?\s*<<\s*\d+\s*$", s):
            continue
        if re.match(r"^\d+\s+>>\s*.+?\s*<<\s*$", s):
            continue
        if re.match(r"^>>\s*.+?\s*<<\s*$", s) and "HARD TARGETS" not in s.upper():
            # chapter banner alone; strip (H1 already has title)
            continue
        lines.append(s)

    text = "\n".join(lines)
    joins = [
        (r"(?im)^A WORKMAN IS\s*\nONLY AS GOOD\s*\nAS HIS TOOLS\s*$", "A WORKMAN IS ONLY AS GOOD AS HIS TOOLS"),
        (r"(?im)^WETWORK\s*\nAND TEAMWORK\s*$", "WETWORK AND TEAMWORK"),
        (r"(?im)^HARD TARGETS CREDITS\s*$", "HARD TARGETS CREDITS"),
    ]
    for pat, repl in joins:
        text = re.sub(pat, repl, text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def split_toc_and_credits(page3: str) -> tuple[str, str]:
    raw = clean(page3)
    m = re.search(r"(?im)^HARD TARGETS CREDITS\s*$", raw)
    if not m:
        m = re.search(r"(?im)^CREDITS\s*$", raw)
    if not m:
        return raw, ""
    return raw[: m.start()].rstrip() + "\n", raw[m.start() :].lstrip()


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    page3 = doc[3].get_text("text") or ""
    toc_tail, credits_body = split_toc_and_credits(page3)

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep:
            p.unlink()
            print("removed", p.name)

    for fname, title, start, end in SECTIONS:
        if fname.startswith("02 -"):
            parts = [doc[2].get_text("text") or "", toc_tail]
            body = clean("\n\n".join(parts))
            span = "PDF page index 2-3 (TOC; credits split to next file)"
        elif fname.startswith("03 -"):
            body = credits_body if credits_body.strip() else clean(page3)
            body = re.sub(r"(?im)^HARD TARGETS CREDITS\s*\n+", "", body, count=1)
            span = "PDF page index 3 (credits block)"
        elif fname.startswith("01 -"):
            parts = [doc[i].get_text("text") or "" for i in range(start, min(end, len(doc)))]
            body = clean("\n\n".join(parts))
            if not body.strip():
                body = (
                    "(Cover/title pages; little or no extractable text. "
                    f"See PDF page index {start}-{end - 1}.)\n"
                )
            span = f"PDF page index {start}-{end - 1}"
        else:
            parts = [doc[i].get_text("text") or "" for i in range(start, min(end, len(doc)))]
            body = clean("\n\n".join(parts))
            span = f"PDF page index {start}-{end - 1}"

        # strip leading banner matching title
        for banner in (
            title.upper(),
            title.upper().replace("...", ""),
            "INTRODUCTION",
            "JACKPOINT",
            "JUSTICE FOR HIRE",
            "DESPERATE TIMES",
            "...AND DESPERATE MEASURES",
            "AND DESPERATE MEASURES",
            "KILLERS, SAVIORS, AND HUNTERS",
            "SLOW AND STEADY DEATH",
            "HAVANA: DALE A TODO METER!",
            "CHAMELEON",
            "BECOMING DEATH",
            "THE WETWORK TOOLKIT",
            "GAME INFORMATION",
            "TABLE OF CONTENTS",
            "CREDITS",
        ):
            body = re.sub(rf"(?im)^{re.escape(banner)}\s*\n+", "", body, count=1)

        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only or blank. See {span}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** Hard Targets | "
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
    index = f"""# Hard Targets

Wetwork guide: assassination trade, Havana, wetwork gear and character options.
PDF: `Source/PDF/{PDF.name}` ({len(doc)} pages). Cover/blank PDF idx 0-1.

Source Texts extracted via `Source/_extract/extract_hard_targets.py` (pymupdf).
Formatting: `Source/_extract/format_hard_targets.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{index_rows}

Note: print page ~4 holds TOC continuation and **Credits**; extract splits that page.

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
