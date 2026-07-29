# -*- coding: utf-8 -*-
"""Extract Market Panic PDF into Source Texts/Market Panic/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\marketpanic.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Market Panic")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Print page N ~= PDF index N-1 (cover blank PDF 0-1).
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents & Credits", 0, 6),
    ("02 - The First Day of the Rest of Your Life.md", "The First Day of the Rest of Your Life", 6, 10),
    ("03 - Droning On.md", "Droning On", 10, 28),
    ("04 - Courting Disaster.md", "Courting Disaster", 28, 38),
    ("05 - Ares Macrotechnology.md", "Ares Macrotechnology", 38, 58),
    ("06 - Aztechnology.md", "Aztechnology", 58, 72),
    ("07 - EVO.md", "EVO", 72, 88),
    ("08 - Horizon.md", "Horizon", 88, 104),
    ("09 - Mitsuhama.md", "Mitsuhama", 104, 118),
    ("10 - NeoNET.md", "NeoNET", 118, 134),
    ("11 - Renraku.md", "Renraku", 134, 156),
    ("12 - Saeder-Krupp.md", "Saeder-Krupp", 156, 178),
    ("13 - Shiawase.md", "Shiawase", 178, 192),
    ("14 - Wuxing.md", "Wuxing", 192, 210),
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
        "\u2026": "...",
        "\ufeff": "",
        "\xad": "",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if not s:
            lines.append("")
            continue
        if re.match(r"^>>\s*SHADOWRUN\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^>>\s*MARKET PANIC\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^<<\s*MARKET PANIC\s*>>\s*\d+\s*$", s, re.I):
            continue
        if re.match(r"^>>\s*.+?\s*<<\s*\d+\s*$", s):
            continue
        if re.match(r"^\d+\s+>>\s*.+?\s*<<\s*$", s):
            continue
        if re.match(r"^MARKET PANIC\s+\d+\s*$", s, re.I):
            continue
        if re.match(r"^\d+\s+MARKET PANIC\s*$", s, re.I):
            continue
        if re.match(r"^MARKET PANIC\s*$", s, re.I):
            continue
        if re.match(r"^SHADOWRUN\s*$", s, re.I):
            continue
        lines.append(s)

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep:
            p.unlink()
            print("removed", p.name)

    banners = [
        "CONTENTS & CREDITS",
        "CONTENTS AND CREDITS",
        "THE FIRST DAY OF THE REST OF YOUR LIFE",
        "THE FIRST DAY OF THE",
        "REST OF YOUR LIFE",
        "DRONING ON",
        "COURTING DISASTER",
        "ARES MACROTECHNOLOGY",
        "AZTECHNOLOGY",
        "EVO",
        "HORIZON",
        "MITSUHAMA",
        "NEONET",
        "RENRAKU",
        "SAEDER-KRUPP",
        "SHIAWASE",
        "WUXING",
    ]

    for fname, title, start, end in SECTIONS:
        parts = [doc[i].get_text("text") or "" for i in range(start, min(end, len(doc)))]
        body = clean("\n\n".join(parts))
        for banner in banners:
            body = re.sub(rf"(?im)^{re.escape(banner)}\s*\n+", "", body, count=1)

        span = f"PDF page index {start}-{end - 1}"
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only cover/art. See {span}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** Market Panic | "
            f"`Source/PDF/{PDF.name}` | {span}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    index_rows = "\n".join(
        f"| {n} | [{title}]({fname.replace(' ', '%20')}) | {start}-{end - 1} |"
        for n, (fname, title, start, end) in enumerate(SECTIONS, 1)
    )
    index = f"""# Market Panic

Big Ten megacorp campaign book during CFD-era fallout.

**PDF:** `Source/PDF/{PDF.name}` ({len(doc)} pages). Cover/blank PDF idx 0-1.

**Extractor:** `Source/_extract/extract_market_panic.py`
**Formatter:** `Source/_extract/format_market_panic.py`
**QA:** `Source/_extract/qa_market_panic.py`

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{index_rows}

## Pipeline status

- [x] Extract
- [ ] Format
- [ ] Loss-check
- [ ] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("\u2013", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")
    doc.close()


if __name__ == "__main__":
    main()
