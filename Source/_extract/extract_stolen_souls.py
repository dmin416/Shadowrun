# -*- coding: utf-8 -*-
"""Extract Stolen Souls PDF into Source Texts/Stolen Souls/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\stolensouls.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Stolen Souls")

# TOC uses 1-based PDF page numbers. Ranges are 0-based start inclusive, end exclusive.
SECTIONS = [
    ("01 - Shadowrun Stolen Souls.md", "Shadowrun: Stolen Souls", 0, 3),
    ("02 - Contents and Credits.md", "Contents & Credits", 3, 5),
    ("03 - Freedom Isn't Free.md", "Freedom Isn't Free", 5, 9),
    ("04 - JackPoint.md", "JackPoint", 9, 10),
    ("05 - Introduction.md", "Introduction", 10, 11),
    ("06 - Check Your Head.md", "Check Your Head", 11, 43),
    ("07 - Searching for the Source.md", "Searching for the Source", 43, 79),
    ("08 - Rewiring Minds.md", "Rewiring Minds", 79, 95),
    ("09 - Persuasion and Power.md", "Persuasion and Power", 95, 99),
    ("10 - Loaded C-Suites of New York.md", "Loaded C-Suites of New York", 99, 117),
    ("11 - Manhattan Vital Stats (2075).md", "Manhattan Vital Stats (2075)", 117, 125),
    ("12 - Horizon, Evo, and Shiawase.md", "Horizon, Evo, and Shiawase", 125, 139),
    ("13 - The Gremlins that Come Between Us.md", "The Gremlins that Come Between Us", 139, 143),
    ("14 - Stealing Living Goods.md", "Stealing Living Goods", 143, 171),
    ("15 - Extractor's Toolkit.md", "Extractor's Toolkit", 171, 193),
    ("16 - Game Information.md", "Game Information", 193, 197),
    ("17 - Stolen Souls Tables.md", "Stolen Souls Tables", 197, 202),
]


def clean(text: str) -> str:
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
        "\xad": "",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
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
        if re.match(r"^>>?\s*STOLEN SOULS", s, re.I):
            continue
        if re.match(r"^<<?\s*", s) and ("<<" in s or s.startswith("<<")):
            continue
        if re.match(r"^CONTENTS\s*/?\s*CREDITS\s*$", s, re.I):
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
        if p.name not in keep and p.stat().st_size < 120:
            print("removed", repr(p.name))
            p.unlink()

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
            f"**Source:** Stolen Souls | `Source/PDF/stolensouls.pdf` | "
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
        link = fname.replace(" ", "%20").replace("&", "%26").replace("'", "%27")
        index_rows.append(f"{i}. [{title}]({link}) (PDF pp. {start + 1}-{end})")

    index = f"""# Stolen Souls

CFD metaplot opener: extractions and Manhattan.

**PDF:** `Source/PDF/stolensouls.pdf` ({len(pdf.pages)} pages).
**Extractor:** `Source/_extract/extract_stolen_souls.py`
**Formatter:** `Source/_extract/format_stolen_souls.py`
**QA:** `Source/_extract/qa_stolen_souls.py`

## Sections

{chr(10).join(index_rows)}

## Pipeline status

- [x] Extract (all 17 chapters + INDEX)
- [x] Format (`format_stolen_souls.py`)
- [x] Loss-check vs PDF (`stolen_souls_qa_report.md`)
- [x] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("—", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
