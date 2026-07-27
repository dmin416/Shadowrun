# -*- coding: utf-8 -*-
"""Extract Forbidden Arcana PDF into Source Texts/Forbidden Arcana/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\forbiddenarcana.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Forbidden Arcana")

SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 5),
    ("02 - Introduction.md", "Introduction", 5, 6),
    ("03 - A Walk in the Park.md", "A Walk in the Park", 6, 10),
    ("04 - Seeing the Invisible World.md", "Seeing the Invisible World", 10, 30),
    ("05 - Magic Mastery.md", "Magic Mastery", 30, 54),
    ("06 - Tea and Sympathy.md", "Tea & Sympathy", 54, 58),
    ("07 - Traditions.md", "Traditions", 58, 106),
    ("08 - Blood Magic.md", "Blood Magic", 106, 138),
    ("09 - Breath of the Wild.md", "Breath of the Wild", 138, 142),
    ("10 - Where the Wild Things Are.md", "Where the Wild Things Are", 142, 184),
    ("11 - Advanced Alchemy.md", "Advanced Alchemy", 184, 211),
    ("12 - Index.md", "Index", 211, 217),
]


def clean(text: str) -> str:
    repl = {
        "\u2014": "-", "\u2013": "-", "—": "-", "–": "-",
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\ufb01": "fi", "\ufb02": "fl", "\xa0": " ",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    lines = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>?\s*FORBIDDEN ARCANA", s, re.I):
            continue
        if re.match(r"^<<?\s*.*\d+\s*$", s) and ("<<" in s or ">>" in s):
            continue
        if re.match(r"^\d+\s+CONTENTS", s, re.I):
            continue
        lines.append(s)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def main():
    pdf = pypdf.PdfReader(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)
    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size == 0:
            p.unlink()

    for fname, title, start, end in SECTIONS:
        parts = [pdf.pages[i].extract_text() or "" for i in range(start, min(end, len(pdf.pages)))]
        body = clean("\n\n".join(parts)) or f"(No extractable text. PDF ~{start}-{end-1}.)\n"
        md = (
            f"# {title}\n\n"
            f"**Source:** Forbidden Arcana | `Source/PDF/forbiddenarcana.pdf` | "
            f"PDF page index {start}-{end - 1}\n\n{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        (OUT / fname).write_text(md, encoding="utf-8")
        print("wrote", fname, (OUT / fname).stat().st_size)

    index = """# Forbidden Arcana

Advanced / weird magic options. PDF: `Source/PDF/forbiddenarcana.pdf` (218 pages).

Extractor: `Source/_extract/extract_forbiddenarcana.py`. Formatter: `Source/_extract/format_forbiddenarcana.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 2-4 |
| 2 | [Introduction](02%20-%20Introduction.md) | 5 |
| 3 | [A Walk in the Park](03%20-%20A%20Walk%20in%20the%20Park.md) | 6-9 |
| 4 | [Seeing the Invisible World](04%20-%20Seeing%20the%20Invisible%20World.md) | 10-29 |
| 5 | [Magic Mastery](05%20-%20Magic%20Mastery.md) | 30-53 |
| 6 | [Tea & Sympathy](06%20-%20Tea%20and%20Sympathy.md) | 54-57 |
| 7 | [Traditions](07%20-%20Traditions.md) | 58-105 |
| 8 | [Blood Magic](08%20-%20Blood%20Magic.md) | 106-137 |
| 9 | [Breath of the Wild](09%20-%20Breath%20of%20the%20Wild.md) | 138-141 |
| 10 | [Where the Wild Things Are](10%20-%20Where%20the%20Wild%20Things%20Are.md) | 142-183 |
| 11 | [Advanced Alchemy](11%20-%20Advanced%20Alchemy.md) | 184-210 |
| 12 | [Index](12%20-%20Index.md) | 211-216 |

## Pipeline status

- [x] Extract
- [x] Format
- [ ] Loss-check
- [ ] Done-check
"""
    (OUT / "INDEX.md").write_text(index.replace("\u2014", "-").replace("—", "-"), encoding="utf-8")
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
