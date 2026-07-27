# -*- coding: utf-8 -*-
"""Extract Rigger 5.0 PDF into Source Texts/Rigger 5/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Rigger 5")

# Print page N ~= PDF index N. (filename, title, start_inclusive, end_exclusive)
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 5),
    ("02 - Introduction.md", "Introduction", 5, 6),
    ("03 - Home Security.md", "Home Security", 6, 10),
    ("04 - Hot Rubber and Cold Steel.md", "Hot Rubber and Cold Steel", 10, 24),
    ("05 - All the Angles.md", "All the Angles", 24, 32),
    ("06 - On the Bleeding Edge.md", "On the Bleeding Edge", 32, 36),
    ("07 - The Order of Chaos.md", "The Order of Chaos", 36, 40),
    ("08 - Demolition Derby.md", "Demolition Derby", 40, 78),
    ("09 - Ruling the Waves.md", "Ruling the Waves", 78, 94),
    ("10 - Air Superiority.md", "Air Superiority", 94, 110),
    ("11 - One Rig to Rule Them All.md", "One Rig to Rule Them All", 110, 116),
    ("12 - The Automated Army.md", "The Automated Army", 116, 150),
    ("13 - Building the Perfect Beast.md", "Building the Perfect Beast", 150, 172),
    ("14 - Maximum Pursuit.md", "Maximum Pursuit", 172, 184),
    ("15 - Tables.md", "Compiled Tables", 184, 193),
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
        if re.match(r"^>>?\s*RIGGER 5", s, re.I):
            continue
        if re.match(r"^>>?\s*CONTENTS?\s*&?\s*CREDITS", s, re.I):
            continue
        if re.match(r"^\d+\s+>>?\s*CONTENTS", s, re.I):
            continue
        if re.match(r"^>>?\s*[A-Z].*<<\s+\d+\s*$", s):
            continue
        if re.match(r"^\d+\s+>>?\s*.*<<\s*$", s):
            continue
        if re.match(r"^>>?\s*COMPILED TABLES", s, re.I):
            continue
        if re.match(r"^>>?\s*MAXIMUM PURSUIT", s, re.I):
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
            body = (
                "(No extractable text on these PDF pages. "
                f"See PDF pages ~{start}-{end - 1}.)\n"
            )
        md = (
            f"# {title}\n\n"
            f"**Source:** Rigger 5.0 | `Source/PDF/rigger5.pdf` | "
            f"PDF page index {start}-{end - 1}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    index = """# Rigger 5.0

Vehicles, drones, and rigger rules expansion. PDF: `Source/PDF/rigger5.pdf` (194 pages).

Extractor: `Source/_extract/extract_rigger5.py`. Formatter: `Source/_extract/format_rigger5.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 2-4 |
| 2 | [Introduction](02%20-%20Introduction.md) | 5 |
| 3 | [Home Security](03%20-%20Home%20Security.md) | 6-9 |
| 4 | [Hot Rubber and Cold Steel](04%20-%20Hot%20Rubber%20and%20Cold%20Steel.md) | 10-23 |
| 5 | [All the Angles](05%20-%20All%20the%20Angles.md) | 24-31 |
| 6 | [On the Bleeding Edge](06%20-%20On%20the%20Bleeding%20Edge.md) | 32-35 |
| 7 | [The Order of Chaos](07%20-%20The%20Order%20of%20Chaos.md) | 36-39 |
| 8 | [Demolition Derby](08%20-%20Demolition%20Derby.md) | 40-77 |
| 9 | [Ruling the Waves](09%20-%20Ruling%20the%20Waves.md) | 78-93 |
| 10 | [Air Superiority](10%20-%20Air%20Superiority.md) | 94-109 |
| 11 | [One Rig to Rule Them All](11%20-%20One%20Rig%20to%20Rule%20Them%20All.md) | 110-115 |
| 12 | [The Automated Army](12%20-%20The%20Automated%20Army.md) | 116-149 |
| 13 | [Building the Perfect Beast](13%20-%20Building%20the%20Perfect%20Beast.md) | 150-171 |
| 14 | [Maximum Pursuit](14%20-%20Maximum%20Pursuit.md) | 172-183 |
| 15 | [Compiled Tables](15%20-%20Tables.md) | 184-192 |

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
