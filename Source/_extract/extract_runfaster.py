# -*- coding: utf-8 -*-
"""Extract Run Faster PDF into Source Texts/Run Faster/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runfaster.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run Faster")

# Print page P ~= PDF index P+1
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 3, 7),
    ("02 - Decade.md", "Decade", 7, 12),
    ("03 - Introduction.md", "Introduction", 12, 13),
    ("04 - Who You Are and How You Got Here.md", "Who You Are & How You Got Here", 13, 23),
    ("05 - Ethics Codes and Other Jokes.md", "Ethics, Codes, & Other Jokes", 23, 35),
    ("06 - The Spice of Runners Lives.md", "The Spice of Runners' Lives", 35, 45),
    ("07 - More Than Skin Deep.md", "More Than Skin Deep", 45, 63),
    ("08 - Construction Kits.md", "Construction Kits", 63, 89),
    ("09 - The Mess of Metahumanity.md", "The Mess of Metahumanity", 89, 125),
    ("10 - Into the Night.md", "Into the Night", 125, 145),
    ("11 - As You As You Can Be.md", "As You As You Can Be", 145, 173),
    ("12 - Who You Know.md", "Who You Know", 173, 197),
    ("13 - Bosses and Betrayers.md", "Bosses & Betrayers", 197, 213),
    ("14 - A Dump of Ones Own.md", "A Dump of One's Own", 213, 229),
    ("15 - Pack Your Kit.md", "Pack Your Kit", 229, 257),
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
        if re.match(r"^>>?\s*RUN FASTER", s, re.I):
            continue
        if re.match(r"^<<?\s*.*\d+\s*$", s) and ("<<" in s or ">>" in s):
            continue
        if "InMediaRes Productions LLC" in s:
            continue
        lines.append(s)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def main():
    pdf = pypdf.PdfReader(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)
    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep:
            if p.stat().st_size == 0 or p.name.startswith(("08 - A Run", "13 - Domestically")):
                p.unlink(missing_ok=True)
                print("removed", p.name)

    for fname, title, start, end in SECTIONS:
        parts = [pdf.pages[i].extract_text() or "" for i in range(start, min(end, len(pdf.pages)))]
        body = clean("\n\n".join(parts)) or f"(No extractable text. PDF ~{start}-{end-1}.)\n"
        md = (
            f"# {title}\n\n"
            f"**Source:** Run Faster | `Source/PDF/runfaster.pdf` | "
            f"PDF page index {start}-{end - 1}\n\n{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        (OUT / fname).write_text(md, encoding="utf-8")
        print("wrote", fname, (OUT / fname).stat().st_size)

    index = """# Run Faster

Player companion: character options and alternate creation methods. PDF: `Source/PDF/runfaster.pdf` (258 pages).

Extractor: `Source/_extract/extract_runfaster.py`. Formatter: `Source/_extract/format_runfaster.py`.

Note: Prior INDEX listed "A Run on the Wild Side" and "Domestically Disturbed"; those titles are not in the PDF TOC. Chapters below match print TOC.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 3-6 |
| 2 | [Decade](02%20-%20Decade.md) | 7-11 (fiction) |
| 3 | [Introduction](03%20-%20Introduction.md) | 12 |
| 4 | [Who You Are & How You Got Here](04%20-%20Who%20You%20Are%20and%20How%20You%20Got%20Here.md) | 13-22 |
| 5 | [Ethics, Codes, & Other Jokes](05%20-%20Ethics%20Codes%20and%20Other%20Jokes.md) | 23-34 |
| 6 | [The Spice of Runners' Lives](06%20-%20The%20Spice%20of%20Runners%20Lives.md) | 35-44 |
| 7 | [More Than Skin Deep](07%20-%20More%20Than%20Skin%20Deep.md) | 45-62 |
| 8 | [Construction Kits](08%20-%20Construction%20Kits.md) | 63-88 |
| 9 | [The Mess of Metahumanity](09%20-%20The%20Mess%20of%20Metahumanity.md) | 89-124 |
| 10 | [Into the Night](10%20-%20Into%20the%20Night.md) | 125-144 |
| 11 | [As You As You Can Be](11%20-%20As%20You%20As%20You%20Can%20Be.md) | 145-172 |
| 12 | [Who You Know](12%20-%20Who%20You%20Know.md) | 173-196 |
| 13 | [Bosses & Betrayers](13%20-%20Bosses%20and%20Betrayers.md) | 197-212 |
| 14 | [A Dump of One's Own](14%20-%20A%20Dump%20of%20Ones%20Own.md) | 213-228 |
| 15 | [Pack Your Kit](15%20-%20Pack%20Your%20Kit.md) | 229-256 |

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
