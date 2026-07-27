# -*- coding: utf-8 -*-
"""Extract Street Grimoire PDF into Source Texts/Street Grimoire/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\streetgrimoire.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Street Grimoire")

# Print page P ~= PDF index P+1. (filename, title, start_inclusive, end_exclusive)
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 3, 6),
    ("02 - Introduction.md", "Introduction", 6, 7),
    ("03 - Where Few Dare to Tread.md", "Where Few Dare to Tread", 7, 11),
    ("04 - Surviving Magic.md", "Surviving Magic", 11, 25),
    ("05 - Magic in the World.md", "Magic in the World", 25, 39),
    ("06 - Magical Traditions.md", "Magical Traditions", 39, 55),
    ("07 - Magical Societies.md", "Magical Societies", 55, 79),
    ("08 - Dark Magic.md", "Dark Magic", 79, 103),
    ("09 - Expanded Grimoire.md", "Expanded Grimoire", 103, 139),
    ("10 - Secrets of the Initiates.md", "Secrets of the Initiates", 139, 161),
    ("11 - Butcher's Bill.md", "Butcher's Bill", 161, 166),
    ("12 - Physical Magic.md", "Physical Magic", 166, 181),
    ("13 - The Immaterial Touch.md", "The Immaterial Touch", 181, 223),
    ("14 - Turning Lead into Nuyen.md", "Turning Lead into Nuyen", 223, 233),
]


def clean(text: str) -> str:
    repl = {
        "\u2014": "-", "\u2013": "-", "—": "-", "–": "-",
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\ufb01": "fi", "\ufb02": "fl",
        "\xa0": " ",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")
    lines = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>?\s*STREET GRIMOIRE", s, re.I):
            continue
        if "InMediaRes Productions LLC" in s:
            continue
        if re.match(r"^<<?\s*[A-Z].*\s+\d+\s*$", s):
            continue
        if re.match(r"^\d+\s+[A-Z][A-Z ].{0,40}$", s) and "<<" in s:
            continue
        lines.append(s)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main():
    pdf = pypdf.PdfReader(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)
    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size == 0:
            p.unlink()
            print("removed empty stub", p.name)

    for fname, title, start, end in SECTIONS:
        parts = []
        for i in range(start, min(end, len(pdf.pages))):
            parts.append(pdf.pages[i].extract_text() or "")
        body = clean("\n\n".join(parts))
        if not body.strip():
            body = f"(No extractable text. See PDF pages ~{start}-{end - 1}.)\n"
        md = (
            f"# {title}\n\n"
            f"**Source:** Street Grimoire | `Source/PDF/streetgrimoire.pdf` | "
            f"PDF page index {start}-{end - 1}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        (OUT / fname).write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", (OUT / fname).stat().st_size)

    index = """# Street Grimoire

Core magic expansion beyond the rulebook. PDF: `Source/PDF/streetgrimoire.pdf` (234 pages).

Extractor: `Source/_extract/extract_streetgrimoire.py`. Formatter: `Source/_extract/format_streetgrimoire.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 3-5 |
| 2 | [Introduction](02%20-%20Introduction.md) | 6 |
| 3 | [Where Few Dare to Tread](03%20-%20Where%20Few%20Dare%20to%20Tread.md) | 7-10 |
| 4 | [Surviving Magic](04%20-%20Surviving%20Magic.md) | 11-24 |
| 5 | [Magic in the World](05%20-%20Magic%20in%20the%20World.md) | 25-38 |
| 6 | [Magical Traditions](06%20-%20Magical%20Traditions.md) | 39-54 |
| 7 | [Magical Societies](07%20-%20Magical%20Societies.md) | 55-78 |
| 8 | [Dark Magic](08%20-%20Dark%20Magic.md) | 79-102 |
| 9 | [Expanded Grimoire](09%20-%20Expanded%20Grimoire.md) | 103-138 (spells + Shadow Rituals) |
| 10 | [Secrets of the Initiates](10%20-%20Secrets%20of%20the%20Initiates.md) | 139-160 |
| 11 | [Butcher's Bill](11%20-%20Butcher's%20Bill.md) | 161-165 |
| 12 | [Physical Magic](12%20-%20Physical%20Magic.md) | 166-180 |
| 13 | [The Immaterial Touch](13%20-%20The%20Immaterial%20Touch.md) | 181-222 |
| 14 | [Turning Lead into Nuyen](14%20-%20Turning%20Lead%20into%20Nuyen.md) | 223-232 |

## Pipeline status

- [x] Extract
- [ ] Format
- [ ] Loss-check
- [ ] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("—", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
