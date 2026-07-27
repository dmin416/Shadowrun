# -*- coding: utf-8 -*-
"""Extract Howling Shadows PDF into Source Texts/Howling Shadows/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\howlingshadows.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Howling Shadows")

SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 5),
    ("02 - Introduction.md", "Introduction", 5, 6),
    ("03 - No Justice No Peace.md", "No Justice, No Peace", 6, 10),
    ("04 - Nature is a Bitch.md", "Nature is a Bitch", 10, 24),
    ("05 - Untamed Security.md", "Untamed Security", 24, 38),
    ("06 - Mundane Critters.md", "Mundane Critters", 38, 48),
    ("07 - A Dingobat Ate My Baby.md", "A Dingobat Ate My Baby", 48, 52),
    ("08 - Paranormal Animals.md", "Paranormal Animals", 52, 92),
    ("09 - Mutants and Toxic Critters.md", "Mutants & Toxic Critters", 92, 114),
    ("10 - Extraplanar Travelers.md", "Extraplanar Travelers", 114, 138),
    ("11 - A Run in the Woods.md", "A Run in the Woods", 138, 142),
    ("12 - Technocritters.md", "Technocritters", 142, 150),
    ("13 - Protosapients.md", "Protosapients", 150, 158),
    ("14 - Drakes.md", "Drakes", 158, 166),
    ("15 - Building Mans Best Friend.md", "Building Man's Best Friend", 166, 188),
    ("16 - Game Information.md", "Game Information", 188, 198),
    ("17 - Critter Tables.md", "Critter Tables", 198, 201),
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
        if re.match(r"^>>?\s*HOWLING SHADOWS", s, re.I):
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
            f"**Source:** Howling Shadows | `Source/PDF/howlingshadows.pdf` | "
            f"PDF page index {start}-{end - 1}\n\n{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        (OUT / fname).write_text(md, encoding="utf-8")
        print("wrote", fname, (OUT / fname).stat().st_size)

    index = """# Howling Shadows

Critters, paracritters, and animal threats. PDF: `Source/PDF/howlingshadows.pdf` (202 pages).

Extractor: `Source/_extract/extract_howlingshadows.py`. Formatter: `Source/_extract/format_howlingshadows.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 2-4 |
| 2 | [Introduction](02%20-%20Introduction.md) | 5 |
| 3 | [No Justice, No Peace](03%20-%20No%20Justice%20No%20Peace.md) | 6-9 |
| 4 | [Nature is a Bitch](04%20-%20Nature%20is%20a%20Bitch.md) | 10-23 |
| 5 | [Untamed Security](05%20-%20Untamed%20Security.md) | 24-37 |
| 6 | [Mundane Critters](06%20-%20Mundane%20Critters.md) | 38-47 |
| 7 | [A Dingobat Ate My Baby](07%20-%20A%20Dingobat%20Ate%20My%20Baby.md) | 48-51 |
| 8 | [Paranormal Animals](08%20-%20Paranormal%20Animals.md) | 52-91 |
| 9 | [Mutants & Toxic Critters](09%20-%20Mutants%20and%20Toxic%20Critters.md) | 92-113 |
| 10 | [Extraplanar Travelers](10%20-%20Extraplanar%20Travelers.md) | 114-137 |
| 11 | [A Run in the Woods](11%20-%20A%20Run%20in%20the%20Woods.md) | 138-141 |
| 12 | [Technocritters](12%20-%20Technocritters.md) | 142-149 |
| 13 | [Protosapients](13%20-%20Protosapients.md) | 150-157 |
| 14 | [Drakes](14%20-%20Drakes.md) | 158-165 |
| 15 | [Building Man's Best Friend](15%20-%20Building%20Mans%20Best%20Friend.md) | 166-187 |
| 16 | [Game Information](16%20-%20Game%20Information.md) | 188-197 |
| 17 | [Critter Tables](17%20-%20Critter%20Tables.md) | 198-200 |

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
