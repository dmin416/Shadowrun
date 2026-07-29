# -*- coding: utf-8 -*-
"""Extract Aetherology PDF into Source Texts/Aetherology/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Aetherology.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Aetherology")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Print page N ~= PDF index N-1.
# Mid-page splits: Greater Beings (idx 28), Rules (idx 31).
SECTIONS: list[tuple[str, str, int, int]] = [
    ("01 - Shadowrun Aetherology.md", "Shadowrun: Aetherology", 0, 1),
    ("02 - JackPoint.md", "JackPoint", 1, 2),
    ("03 - Astral Sea.md", "Astral Sea", 2, 3),
    ("04 - Metaplanes.md", "Metaplanes", 3, 29),
    ("05 - Greater Beings in Astral Space.md", "Greater Beings in Astral Space", 28, 32),
    ("06 - Rules.md", "Rules", 31, 39),
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
        "\uf0b7": "*",
        "\ufeff": "",
        "\ufffd": "",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = text.replace("�", "")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*SHADOWRUN\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^<<\s*AETHEROLOGY\s*>>\s*\d*\s*$", s, re.I):
            continue
        if re.match(r"^AETHEROLOGY\s+\d+\s*$", s, re.I):
            continue
        lines.append(s)

    text = "\n".join(lines)
    # join smashed multi-line titles
    joins = [
        (r"(?im)^GREATER BEINGS IN\s*\nASTRAL SPACE\s*$", "GREATER BEINGS IN ASTRAL SPACE"),
        (r"(?im)^DWELLER ON\s*\nTHE THRESHOLD\s*$", "DWELLER ON THE THRESHOLD"),
        (r"(?im)^ARGILLACEOUS LANDS\s*\nOF THE EAST\s*$", "ARGILLACEOUS LANDS OF THE EAST"),
        (r"(?im)^THE ELEMENTAL\s*\nPLANE OF WATER\s*$", "THE ELEMENTAL PLANE OF WATER"),
        (
            r"(?im)^AZZORLOTH, THE BRIDGE\s*\nBETWEEN WORLDS\s*$",
            "AZZORLOTH, THE BRIDGE BETWEEN WORLDS",
        ),
        (
            r"(?im)^ROGGOTH['']?SHOTH,?\s*\nLAND BEYOND DEATH\s*$",
            "ROGGOTH'SHOTH, LAND BEYOND DEATH",
        ),
        (
            r"(?im)^MOONS OVER THE\s*\nSHADOW METAPLANE\s*$",
            "MOONS OVER THE SHADOW METAPLANE",
        ),
        (
            r"(?im)^DR\. GORDON['']?S\s*\nMETAPLANAR TERMINOLOGY\s*$",
            "DR. GORDON'S METAPLANAR TERMINOLOGY",
        ),
        (
            r"(?im)^INTERPRETED BY MAGISTER\s*$",
            "INTERPRETED BY MAGISTER",
        ),
        (
            r"(?im)^COUNTRY OF MIDDEN\s*\nAND DRUMLIN\s*$",
            "COUNTRY OF MIDDEN AND DRUMLIN",
        ),
        (
            r"(?im)^ONE MORE ASTRAL PHENOMENA\s*\nJUST CAME TO MIND\s*$",
            "ONE MORE ASTRAL PHENOMENA JUST CAME TO MIND",
        ),
        (
            r"(?im)^WE JUST REMEMBERED\s*\nANOTHER ASTRAL PHENOMENA\s*$",
            "WE JUST REMEMBERED ANOTHER ASTRAL PHENOMENA",
        ),
        (
            r"(?im)^EXCERPTED FROM\s*\nDR\. GORDON['']?S WRITINGS\s*$",
            "EXCERPTED FROM DR. GORDON'S WRITINGS",
        ),
        (
            r"(?im)^TRANSFER ENERGY \(ESSENCE\)\s*$",
            "TRANSFER ENERGY (ESSENCE)",
        ),
    ]
    for pat, repl in joins:
        text = re.sub(pat, repl, text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def split_on_heading(page: str, heading_re: str) -> tuple[str, str]:
    raw = clean(page)
    m = re.search(heading_re, raw)
    if not m:
        return raw, ""
    before = raw[: m.start()].rstrip() + "\n"
    after = raw[m.start() :].lstrip()
    return before, after


def strip_leading_title(body: str, title: str) -> str:
    # Only strip at the very start of the body (no MULTILINE ^).
    esc = re.escape(title.upper())
    body = re.sub(rf"(?i)\A{esc}\s*\n+", "", body, count=1)
    for banner in (
        "JACKPOINT",
        "CREDITS",
        "GREATER BEINGS IN ASTRAL SPACE",
        "RULES",
        "ASTRAL SEA",
        "METAPLANES",
    ):
        body = re.sub(rf"(?i)\A{re.escape(banner)}\s*\n+", "", body, count=1)
    return body


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    page28 = doc[28].get_text("text") or ""
    meta_tail, greater_head = split_on_heading(
        page28, r"(?im)^GREATER BEINGS IN ASTRAL SPACE\s*$"
    )

    page31 = doc[31].get_text("text") or ""
    greater_tail, rules_head = split_on_heading(page31, r"(?im)^RULES\s*$")

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size < 300:
            p.unlink()
            print("removed stub", p.name)

    for fname, title, start, end in SECTIONS:
        if fname.startswith("04 -"):
            # Metaplanes: idx 3..27 full + pre-Greater Beings of idx 28
            parts = [doc[i].get_text("text") or "" for i in range(3, 28)]
            parts.append(meta_tail)
            body = clean("\n\n".join(parts))
            span = "PDF page index 3-28 (ends before Greater Beings)"
        elif fname.startswith("05 -"):
            # Greater Beings: mid idx 28 + idx 29-30 + pre-Rules of idx 31
            parts = [greater_head]
            parts.extend(doc[i].get_text("text") or "" for i in range(29, 31))
            parts.append(greater_tail)
            body = clean("\n\n".join(parts))
            span = "PDF page index 28-31 (before Rules)"
        elif fname.startswith("06 -"):
            parts = [rules_head]
            parts.extend(doc[i].get_text("text") or "" for i in range(32, 39))
            body = clean("\n\n".join(parts))
            span = "PDF page index 31-38"
        else:
            parts = [
                doc[i].get_text("text") or ""
                for i in range(start, min(end, len(doc)))
            ]
            body = clean("\n\n".join(parts))
            span = f"PDF page index {start}-{end - 1}"

        body = strip_leading_title(body, title)
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only or blank. See {span}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** Aetherology | "
            f"`Source/PDF/{PDF.name}` | {span}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    rows = "\n".join(
        f"| {n:02d} | [{title}]({fname.replace(' ', '%20')}) | {start}-{end - 1} |"
        for n, (fname, title, start, end) in enumerate(SECTIONS, 1)
    )
    index = f"""# Aetherology

Metaplanes / astral exploration PDF.

**PDF:** `Source/PDF/{PDF.name}` ({len(doc)} pages; print page ≈ PDF index + 1)

Source Texts extracted via `Source/_extract/extract_aetherology.py` (pymupdf).
Formatting: `Source/_extract/format_aetherology.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{rows}

Note: print pages 29 and 32 (PDF idx 28 and 31) are mid-page splits for **Greater Beings in Astral Space** and **Rules**.

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
