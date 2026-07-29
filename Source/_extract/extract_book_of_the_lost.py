# -*- coding: utf-8 -*-
"""Extract Book of the Lost PDF into Source Texts/Book of the Lost/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Book of the Lost.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Book of the Lost")

# TOC uses 1-based PDF page numbers. Ranges are 0-based start inclusive, end exclusive.
SECTIONS = [
    ("01 - Shadowrun Book of the Lost.md", "Shadowrun: Book of the Lost", 0, 2),
    ("02 - Contents.md", "Contents", 2, 3),
    ("03 - Credits.md", "Credits", 3, 4),
    ("04 - JackPoint.md", "JackPoint", 4, 5),
    ("05 - Introduction.md", "Introduction", 5, 6),
    ("06 - The Damage Done, and Then the Dealer.md", "The Damage Done, and Then the Dealer", 6, 10),
    ("07 - Deck Building.md", "Deck Building", 10, 24),
    ("08 - Aligning the Court.md", "Aligning the Court", 24, 32),
    ("09 - Using Themes and Motifs.md", "Using Themes and Motifs", 32, 36),
    ("10 - Items and Objects.md", "Items and Objects", 36, 50),
    ("11 - People.md", "People", 50, 66),
    ("12 - Taco Temple.md", "Taco Temple", 66, 78),
    ("13 - Codes and Puzzles.md", "Codes and Puzzles", 78, 96),
    ("14 - Cards as Augury.md", "Cards as Augury", 96, 108),
    ("15 - Power of the Cards.md", "Power of the Cards", 108, 120),
    ("16 - Character Trove.md", "Character Trove", 120, 138),
]


def clean(text: str) -> str:
    # Em/en dashes at line breaks are intentional breaks, not soft hyphens.
    text = re.sub(r"[\u2014\u2013—–]\s*\n\s*", " - ", text)
    text = re.sub(r"[\u2014\u2013—–]", "-", text)
    repl = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\xa0": " ",
        "\u2022": "-",
        "\xad": "",  # soft hyphen
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    # Real soft wraps: "com-\nplete" -> "complete"
    text = re.sub(r"([A-Za-z]{2,})-\n([a-z]{2,})", r"\1\2", text)
    text = text.replace("\f", "\n")
    lines = []
    for line in text.splitlines():
        s = line.rstrip()
        if not s:
            lines.append("")
            continue
        if s in {"<", "<<", ">>"}:
            continue
        # Keep lone ">" for JackPoint comment markers
        if re.match(r"^>>?\s*BOOK OF THE LOST", s, re.I):
            continue
        if re.match(r"^<<?\s*", s) and ("<<" in s or s.startswith("<<")):
            continue
        if re.match(r"^CONTENTS/CREDITS\s*$", s, re.I):
            continue
        if re.match(r"^\d+\s+[A-Z][A-Z /,&'-]{3,}\s*>>?\s*$", s):
            continue
        if re.match(r"^>>?\s*.*<<\s*\d+\s*$", s):
            continue
        lines.append(s)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def main():
    pdf = pypdf.PdfReader(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)
    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size < 80:
            p.unlink()
            print("removed stub", p.name)

    for fname, title, start, end in SECTIONS:
        parts = [
            pdf.pages[i].extract_text() or ""
            for i in range(start, min(end, len(pdf.pages)))
        ]
        body = clean("\n\n".join(parts))
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                "Likely image-only cover/art. See PDF pages "
                f"~{start + 1}-{end}.)\n"
            )
        md = (
            f"# {title}\n\n"
            f"**Source:** Book of the Lost | `Source/PDF/Book of the Lost.pdf` | "
            f"PDF pages {start + 1}-{end} (idx {start}-{end - 1})\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, path.stat().st_size)

    index_rows = []
    for i, (fname, title, start, end) in enumerate(SECTIONS, 1):
        link = fname.replace(" ", "%20")
        index_rows.append(
            f"{i}. [{title}]({link}) (PDF pp. {start + 1}-{end})"
        )

    index = f"""# Book of the Lost

Sixth World Tarot campaign book: plot hooks and adventure seeds.

**PDF:** `Source/PDF/Book of the Lost.pdf` ({len(pdf.pages)} pages).
**Extractor:** `Source/_extract/extract_book_of_the_lost.py`
**Formatter:** `Source/_extract/format_book_of_the_lost.py`
**QA:** `Source/_extract/qa_book_of_the_lost.py`

## Sections

{chr(10).join(index_rows)}

## Pipeline status

- [x] Extract (all 16 chapters + INDEX)
- [x] Format (`format_book_of_the_lost.py`)
- [x] Loss-check vs PDF (`book_of_the_lost_qa_report.md`)
- [x] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("—", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
