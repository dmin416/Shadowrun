# -*- coding: utf-8 -*-
"""Extract The Complete Trog PDF into Source Texts/Complete Trog/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\completetrog.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Complete Trog")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Printed page N ~= PDF index N-1 (cover/blank PDF 0-1).
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 5),
    ("02 - Introduction.md", "Introduction", 5, 6),
    ("03 - JackPoint.md", "JackPoint", 6, 8),
    ("04 - Belinda.md", "Belinda", 8, 12),
    ("05 - What Are You.md", "What Are You?", 12, 20),
    ("06 - Living as a Trog In.md", "Living as a Trog In...", 20, 60),
    ("07 - True Blue Trog.md", "True Blue Trog", 60, 65),
    ("08 - Working As a Trog In.md", "Working As a Trog In...", 65, 98),
    ("09 - Trog Heroes.md", "Trog Heroes", 98, 122),
    ("10 - Trog Enemies.md", "Trog Enemies", 122, 132),
    ("11 - Trog Runners.md", "Trog Runners", 132, 164),
    ("12 - United We Stomp.md", "United We Stomp", 164, 184),
    ("13 - Everything Trog.md", "Everything Trog", 184, 194),
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
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*THE COMPLETE TROG\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^<<\s*THE COMPLETE TROG\s*>>\s*$", s, re.I):
            continue
        # "30    LIVING AS A TROG IN... >>"
        if re.match(r"^\d+\s+[A-Z0-9].*>>\s*$", s):
            continue
        # "<< WORKING AS A TROG IN...    97"
        if re.match(r"^<<\s+.+\s+\d+\s*$", s):
            continue
        if re.match(r"^THE COMPLETE TROG\s*$", s, re.I):
            continue
        lines.append(s)

    text = "\n".join(lines)
    joins = [
        (r"(?im)^CONTENTS\s*\n&\s*CREDITS\s*$", "CONTENTS & CREDITS"),
        (r"(?im)^THE BLACK FOREST\s*\nTROLL REPUBLIC\s*$", "THE BLACK FOREST TROLL REPUBLIC"),
        (r"(?im)^WHAT ARE YOU\?\s*$", "WHAT ARE YOU?"),
        (r"(?im)^LIVING AS A TROG IN\.\.\.\s*$", "LIVING AS A TROG IN..."),
        (r"(?im)^WORKING AS A TROG IN\.\.\.\s*$", "WORKING AS A TROG IN..."),
        (r"(?im)^WORKING AS A TROG IN�\s*$", "WORKING AS A TROG IN..."),
        (r"(?im)^UNITED WE STOMP\s*$", "UNITED WE STOMP"),
        (r"(?im)^EVERYTHING TROG\s*$", "EVERYTHING TROG"),
        (r"(?im)^TRUE BLUE TROG\s*$", "TRUE BLUE TROG"),
        (r"(?im)^TROG HEROES\s*$", "TROG HEROES"),
        (r"(?im)^TROG ENEMIES\s*$", "TROG ENEMIES"),
        (r"(?im)^TROG RUNNERS\s*$", "TROG RUNNERS"),
    ]
    for pat, repl in joins:
        text = re.sub(pat, repl, text)
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

    for fname, title, start, end in SECTIONS:
        parts = [doc[i].get_text("text") or "" for i in range(start, min(end, len(doc)))]
        body = clean("\n\n".join(parts))
        # strip leading chapter banner that duplicates H1
        for banner in (
            title.upper(),
            title.upper().replace("...", ""),
            "CONTENTS & CREDITS",
            "WHAT ARE YOU?",
            "LIVING AS A TROG IN...",
            "WORKING AS A TROG IN...",
            "TRUE BLUE TROG",
            "TROG HEROES",
            "TROG ENEMIES",
            "TROG RUNNERS",
            "UNITED WE STOMP",
            "EVERYTHING TROG",
            "INTRODUCTION",
            "JACKPOINT",
            "BELINDA",
        ):
            body = re.sub(rf"(?im)^{re.escape(banner)}\s*\n+", "", body, count=1)

        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only or blank. See PDF page index {start}-{end - 1}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** The Complete Trog | "
            f"`Source/PDF/{PDF.name}` | PDF page index {start}-{end - 1}\n\n"
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
    index = f"""# The Complete Trog

Ork and troll culture, life, and character options.
PDF: `Source/PDF/{PDF.name}` ({len(doc)} pages). Cover/blank PDF idx 0-1.

Source Texts extracted via `Source/_extract/extract_complete_trog.py` (pymupdf).
Formatting: `Source/_extract/format_complete_trog.py`.

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
