# -*- coding: utf-8 -*-
"""Extract Seattle Sprawl (Emerald Shadows) PDF into Source Texts/Seattle Sprawl/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\seattlesprawl.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Printed page numbers match PDF idx for body content (TOC is printed pp. 2-5).
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 6),
    ("02 - Whirlwind Tour.md", "Whirlwind Tour", 6, 10),
    ("03 - Emerald Shadows.md", "Emerald Shadows", 10, 13),
    ("04 - Downtown.md", "Downtown", 13, 18),
    ("05 - Bellevue.md", "Bellevue", 18, 24),
    ("06 - Tacoma.md", "Tacoma", 24, 30),
    ("07 - Everett.md", "Everett", 30, 34),
    ("08 - Renton.md", "Renton", 34, 39),
    ("09 - Auburn.md", "Auburn", 39, 45),
    ("10 - Snohomish.md", "Snohomish", 45, 52),
    ("11 - Fort Lewis.md", "Fort Lewis", 52, 57),
    ("12 - Redmond.md", "Redmond", 57, 62),
    ("13 - Puyallup.md", "Puyallup", 62, 67),
    ("14 - Council Island.md", "Council Island", 67, 72),
    ("15 - Outremer.md", "Outremer", 72, 83),
    ("16 - The Seattle Underground.md", "The Seattle Underground", 83, 88),
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
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    # join hyphenated line breaks
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        # running headers / footers
        if re.match(r"^\d+\s+EMERALD SHADOWS\s*>>\s*$", s, re.I):
            continue
        if re.match(r"^<<\s*EMERALD SHADOWS\s+\d+\s*$", s, re.I):
            continue
        if re.match(r"^\d+\s+CONTENTS\s*&\s*CREDITS\s*>>\s*$", s, re.I):
            continue
        if re.match(r"^<<\s*CONTENTS\s*&\s*CREDITS\s+\d+\s*$", s, re.I):
            continue
        if re.match(r"^SHADOWRUN:\s*SEATTLE SPRAWL\s*$", s, re.I):
            continue
        if re.match(r"^CONTENTS\s*$", s, re.I) and not lines:
            # keep TOC heading when it appears mid-block; strip lone cover label only at very start of page dumps if needed
            pass
        if re.match(r"^CONTENTS\s*&\s*CREDITS\s*$", s, re.I):
            continue
        if re.match(r"^\d+\s+[A-Z][A-Z /&'-]+\s*>>\s*$", s):
            # e.g. "42    AUBURN >>"
            continue
        if re.match(r"^<<\s+[A-Z][A-Z /&'-]+\s+\d+\s*$", s):
            continue
        if re.match(r"^>>\s*SEATTLE SPRAWL\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^SHADOWRUN:\s*SEATTLE SPRAWL\s*$", s, re.I):
            continue
        if re.match(r"^EMERALD\s*$", s, re.I) or re.match(r"^SHADOWS\s*$", s, re.I):
            continue
        lines.append(s)

    text = "\n".join(lines)
    # join two-line section title common in this PDF
    text = re.sub(
        r"(?im)^YOU WON'?T FIND\s*\nTHIS ELSEWHERE\s*$",
        "YOU WON'T FIND THIS ELSEWHERE",
        text,
    )
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    for fname, title, start, end in SECTIONS:
        parts: list[str] = []
        for i in range(start, min(end, len(doc))):
            parts.append(doc[i].get_text("text") or "")
        body = clean("\n\n".join(parts))
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                "Likely image-only or blank. See PDF pages "
                f"~{start}-{end - 1}.)\n"
            )
        md = (
            f"# {title}\n\n"
            f"**Source:** Seattle Sprawl / Emerald Shadows | "
            f"`Source/PDF/seattlesprawl.pdf` | PDF page index {start}-{end - 1}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    index_rows = "\n".join(
        f"| {n} | [{title}]({fname.replace(' ', '%20')}) | {start}-{end - 1} |"
        for n, (fname, title, start, end) in enumerate(SECTIONS, 1)
    )
    index = f"""# Seattle Sprawl (Emerald Shadows)

District / locale guide. PDF: `Source/PDF/seattlesprawl.pdf` ({len(doc)} pages).
Cover/title pages PDF idx 0-1 are image-only.

Source Texts extracted via `Source/_extract/extract_seattle_sprawl.py` (pymupdf).

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{index_rows}

## District chapter pattern (typical)

Most district chapters use: Special Occasions - Crime Scene - Where to Shop - Where to Squat - You Won't Find This Elsewhere - Opposition Report - Help Wanted.

Outremer (ch. 15) covers Bainbridge, Vashon, Fox, McNeil, and Anderson Islands.

## Related

- Encyclopedia INDEX: adventure/locale kit, not a core gear catalog
- Serrated Edge: Denver adventure extract (same Source Texts pipeline)

## Pipeline status

- [x] Extract (raw chapter markdown from PDF)
- [ ] Format (headings, JackPoint comments, tables; strip leftover headers)
- [ ] Loss-check vs PDF
- [ ] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("\u2013", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
