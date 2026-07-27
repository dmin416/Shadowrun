# -*- coding: utf-8 -*-
"""Extract Street Lethal PDF into Source Texts/Street Lethal/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\streetlethal.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Street Lethal")

SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 5),
    ("02 - Introduction.md", "Introduction", 5, 6),
    ("03 - Proving Grounds.md", "Proving Grounds", 6, 10),
    ("04 - Expanded Arsenal.md", "Expanded Arsenal", 10, 50),
    ("05 - Military and Future Weapons.md", "Military and Future Weapons", 50, 90),
    ("06 - Opposition Report CorpSec.md", "Opposition Report: CorpSec", 90, 134),
    ("07 - At Sea.md", "At Sea", 134, 138),
    ("08 - Unconventional Warriors.md", "Unconventional Warriors", 138, 182),
    ("09 - Lethal Arts.md", "Lethal Arts", 182, 194),
    ("10 - Adventure Hooks.md", "Adventure Hooks", 194, 201),
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
        if re.match(r"^>>?\s*STREET LETHAL", s, re.I):
            continue
        if re.match(r"^<<?\s*.*\d+\s*$", s) and ("<<" in s or ">>" in s):
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
            f"**Source:** Street Lethal | `Source/PDF/streetlethal.pdf` | "
            f"PDF page index {start}-{end - 1}\n\n{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        (OUT / fname).write_text(md, encoding="utf-8")
        print("wrote", fname, (OUT / fname).stat().st_size)

    index = """# Street Lethal

Advanced combat expansion after Run & Gun. PDF: `Source/PDF/streetlethal.pdf` (202 pages).

Extractor: `Source/_extract/extract_streetlethal.py`. Formatter: `Source/_extract/format_streetlethal.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 2-4 |
| 2 | [Introduction](02%20-%20Introduction.md) | 5 |
| 3 | [Proving Grounds](03%20-%20Proving%20Grounds.md) | 6-9 |
| 4 | [Expanded Arsenal](04%20-%20Expanded%20Arsenal.md) | 10-49 |
| 5 | [Military and Future Weapons](05%20-%20Military%20and%20Future%20Weapons.md) | 50-89 |
| 6 | [Opposition Report: CorpSec](06%20-%20Opposition%20Report%20CorpSec.md) | 90-133 |
| 7 | [At Sea](07%20-%20At%20Sea.md) | 134-137 |
| 8 | [Unconventional Warriors](08%20-%20Unconventional%20Warriors.md) | 138-181 |
| 9 | [Lethal Arts](09%20-%20Lethal%20Arts.md) | 182-193 |
| 10 | [Adventure Hooks](10%20-%20Adventure%20Hooks.md) | 194-200 |

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
