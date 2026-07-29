# -*- coding: utf-8 -*-
"""Extract Lockdown PDF into Source Texts/Lockdown/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrun-lockdown-pdf.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Lockdown")

# TOC uses 1-based PDF page numbers. Ranges are 0-based start inclusive, end exclusive.
SECTIONS = [
    ("01 - Shadowrun Lockdown.md", "Shadowrun: Lockdown", 0, 2),
    ("02 - Contents & Credits.md", "Contents & Credits", 2, 6),
    ("03 - JackPoint.md", "JackPoint", 6, 7),
    ("04 - Introduction.md", "Introduction", 7, 8),
    ("05 - Harbor Heist.md", "Harbor Heist", 8, 12),
    ("06 - A Runner's Guide to Boston.md", "A Runner's Guide to Boston", 12, 78),
    ("07 - Locking the Hub.md", "Locking the Hub", 78, 106),
    ("08 - Inside the QZ A Wanderer's Guide.md", "Inside the QZ: A Wanderer's Guide", 106, 150),
    ("09 - Beantown Bound.md", "Beantown Bound", 150, 162),
    ("10 - Trainyard Troubles.md", "Trainyard Troubles", 162, 172),
    ("11 - Digging Deeper.md", "Digging Deeper", 172, 184),
    ("12 - Bringing Down the House.md", "Bringing Down the House", 184, 198),
    ("13 - Game Information.md", "Game Information", 198, 228),
    ("14 - Familiar Faces.md", "Familiar Faces", 228, 236),
    ("15 - Special Thanks.md", "Special Thanks", 236, 242),
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
        if re.match(r"^>>?\s*LOCKDOWN", s, re.I):
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
            if p.stat().st_size < 120 or "\u2019" in p.name:
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
            f"**Source:** Lockdown | `Source/PDF/shadowrun-lockdown-pdf.pdf` | "
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

    index = f"""# Lockdown

Boston quarantine / CFD plot sourcebook.

**PDF:** `Source/PDF/shadowrun-lockdown-pdf.pdf` ({len(pdf.pages)} pages).
**Extractor:** `Source/_extract/extract_lockdown.py`
**Formatter:** `Source/_extract/format_lockdown.py`
**QA:** `Source/_extract/qa_lockdown.py`

## Sections

{chr(10).join(index_rows)}

## Pipeline status

- [x] Extract (all 15 chapters + INDEX)
- [x] Format (`format_lockdown.py`)
- [x] Loss-check vs PDF (`lockdown_qa_report.md`)
- [x] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("—", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
