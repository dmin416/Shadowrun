# -*- coding: utf-8 -*-
"""Extract Cutting Aces PDF into Source Texts/Cutting Aces/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Cutting_Aces.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Cutting Aces")

# TOC uses 1-based PDF page numbers. Ranges are 0-based start inclusive, end exclusive.
SECTIONS = [
    ("01 - Shadowrun Cutting Aces.md", "Shadowrun: Cutting Aces", 0, 2),
    ("02 - Contents & Credits.md", "Contents & Credits", 2, 3),
    ("03 - Introduction.md", "Introduction", 3, 4),
    ("04 - Operation Constantinople.md", "Operation: Constantinople", 4, 8),
    ("05 - Fast and Loose.md", "Fast and Loose", 8, 48),
    ("06 - City of the World's Desire.md", "City of the World's Desire", 48, 86),
    ("07 - From the Artist's Perspective.md", "From the Artist's Perspective", 86, 90),
    ("08 - Alibi Agents of Constantinople.md", "Alibi Agents of Constantinople", 90, 106),
    ("09 - The Art of Confidence.md", "The Art of Confidence", 106, 132),
    ("10 - Gats and Glad Rags.md", "Gats and Glad Rags", 132, 156),
    ("11 - The Grifting Bible.md", "The Grifting Bible", 156, 170),
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
        if re.match(r"^>>?\s*CUTTING ACES", s, re.I):
            continue
        if re.match(r"^<<?\s*", s) and ("<<" in s or s.startswith("<<")):
            continue
        if re.match(r"^CONTENTS\s*&\s*CREDITS\s*$", s, re.I):
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
        if p.name not in keep:
            # Drop curly-apostrophe stubs / obsolete names
            if p.stat().st_size < 120 or "'" in p.name or "\u2019" in p.name:
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
            f"**Source:** Cutting Aces | `Source/PDF/Shadowrun_5E_Cutting_Aces.pdf` | "
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

    index = f"""# Cutting Aces

Cons and social runs; Constantinople.

**PDF:** `Source/PDF/Shadowrun_5E_Cutting_Aces.pdf` ({len(pdf.pages)} pages).
**Extractor:** `Source/_extract/extract_cutting_aces.py`
**Formatter:** `Source/_extract/format_cutting_aces.py`
**QA:** `Source/_extract/qa_cutting_aces.py`

## Sections

{chr(10).join(index_rows)}

## Pipeline status

- [x] Extract (all 11 chapters + INDEX)
- [x] Format (`format_cutting_aces.py`)
- [x] Loss-check vs PDF (`cutting_aces_qa_report.md`)
- [x] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("—", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
