# -*- coding: utf-8 -*-
"""Extract Bullets & Bandages PDF into Source Texts/Bullets and Bandages/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Bullets_&_Bandages.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Bullets and Bandages")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Printed page N ~= PDF index N-1 for this PDF.
SECTIONS = [
    ("01 - Shadowrun Bullets & Bandages.md", "Shadowrun: Bullets & Bandages", 0, 1),
    ("02 - JackPoint.md", "JackPoint", 1, 2),
    ("03 - Primum Non Nocere.md", "Primum Non Nocere", 2, 3),
    ("04 - Collateral Nuyen.md", "Collateral Nuyen", 3, 4),
    ("05 - Combat Medicine 101.md", "Combat Medicine 101", 4, 8),
    ("06 - Game Information.md", "Game Information", 8, 12),
    ("07 - Advanced Biotech Rules.md", "Advanced Biotech Rules", 12, 23),
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
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*SHADOWRUN\s*<<\s*$", s, re.I):
            continue
        if re.match(r"^<<\s*BULLETS\s*&\s*BANDAGES\s+\d+\s*$", s, re.I):
            continue
        if re.match(r"^BULLETS\s*&\s*BANDAGES\s+\d+\s*$", s, re.I):
            continue
        lines.append(s)

    text = "\n".join(lines)
    # join smashed two-line titles common in this PDF
    joins = [
        (r"(?im)^PRIMUM NON\s*\nNOCERE\s*$", "PRIMUM NON NOCERE"),
        (r"(?im)^COLLATERAL\s*\nNUYEN\s*$", "COLLATERAL NUYEN"),
        (r"(?im)^ADVANCED\s*\nBIOTECH RULES\s*$", "ADVANCED BIOTECH RULES"),
        (
            r"(?im)^BIOTECH, KNOWLEDGE\s*\nSKILLS, AND DATA SEARCH\s*\n\(OPTIONAL RULE\)\s*$",
            "BIOTECH, KNOWLEDGE SKILLS, AND DATA SEARCH (OPTIONAL RULE)",
        ),
        (
            r"(?im)^CARE UNDER FIRE\s*\n\(OPTIONAL RULES\)\s*$",
            "CARE UNDER FIRE (OPTIONAL RULES)",
        ),
        (
            r"(?im)^ARMOR AND ARMOR\s*\nMODIFICATIONS\s*$",
            "ARMOR AND ARMOR MODIFICATIONS",
        ),
        (r"(?im)^BUILDING A\s*\nMEDIC CHARACTER\s*$", "BUILDING A MEDIC CHARACTER"),
        (
            r"(?im)^USING TRAUMA PATCHES\s*\nAND CRASH\s*$",
            "USING TRAUMA PATCHES AND CRASH",
        ),
        (
            r"(?im)^ADVANCED MEDKIT\s*\nAND AUTODOC RULES\s*$",
            "ADVANCED MEDKIT AND AUTODOC RULES",
        ),
        (
            r"(?im)^NEW DRUGS, TOXINS,\s*\nAND PATHOGENS\s*$",
            "NEW DRUGS, TOXINS, AND PATHOGENS",
        ),
        (
            r"(?im)^PNEUMATIC ANTI-SHOCK\s*\nGARMENTS\s*$",
            "PNEUMATIC ANTI-SHOCK GARMENTS",
        ),
        (
            r"(?im)^AEROQUIP M\.E\.D\.-1\s*\n\"DUSTOFF\"\s*$",
            'AEROQUIP M.E.D.-1 "DUSTOFF"',
        ),
        (
            r"(?im)^SHIAWASE CADUCEUS\s*\n\"CAD\" 7\s*$",
            'SHIAWASE CADUCEUS "CAD" 7',
        ),
    ]
    for pat, repl in joins:
        text = re.sub(pat, repl, text)
    # DocWagon glance: subsidiaries list glued to body paragraph
    text = re.sub(
        r"(Apex Pharmaceuticals)\s+(Founded in)",
        r"\1\n\n\2",
        text,
    )
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def split_fiction_and_collateral(page3: str) -> tuple[str, str]:
    """PDF page 3 (print ~4) holds end of fiction then Collateral Nuyen."""
    raw = clean(page3)
    m = re.search(r"(?im)^COLLATERAL NUYEN\s*$", raw)
    if not m:
        # fallback: start of DocWagon glance
        m = re.search(r"(?im)^DOCWAGON AT A GLANCE\s*$", raw)
        if m:
            return raw[: m.start()].rstrip() + "\n", "COLLATERAL NUYEN\n\n" + raw[m.start() :]
        return raw, ""
    fiction = raw[: m.start()].rstrip() + "\n"
    collateral = raw[m.start() :].lstrip()
    return fiction, collateral


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    page3 = doc[3].get_text("text") or ""
    fiction_tail, collateral_body = split_fiction_and_collateral(page3)

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep:
            # remove obsolete empty stubs only
            if p.stat().st_size < 200:
                p.unlink()
                print("removed stub", p.name)

    for fname, title, start, end in SECTIONS:
        if fname.startswith("03 -"):
            parts = [doc[2].get_text("text") or "", fiction_tail]
            body = clean("\n\n".join(parts))
            # drop duplicate chapter banner after H1
            body = re.sub(r"(?im)^PRIMUM NON NOCERE\s*\n+", "", body, count=1)
            span = "PDF page index 2-3 (fiction ends mid-page 3)"
        elif fname.startswith("04 -"):
            body = collateral_body if collateral_body.strip() else clean(page3)
            body = re.sub(r"(?im)^COLLATERAL NUYEN\s*\n+", "", body, count=1)
            span = "PDF page index 3 (from Collateral Nuyen)"
        else:
            parts = [doc[i].get_text("text") or "" for i in range(start, min(end, len(doc)))]
            body = clean("\n\n".join(parts))
            # strip leading chapter title that duplicates H1
            esc = re.escape(title.upper().replace("&", r"\s*&\s*"))
            body = re.sub(rf"(?im)^{esc}\s*\n+", "", body, count=1)
            span = f"PDF page index {start}-{end - 1}"

        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only or blank. See {span}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** Bullets & Bandages | "
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
    index = f"""# Bullets and Bandages

Medical / combat support gear and rules. PDF: `Source/PDF/{PDF.name}` ({len(doc)} pages).

Source Texts extracted via `Source/_extract/extract_bullets_bandages.py` (pymupdf).
Formatting: `Source/_extract/format_bullets_bandages.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{index_rows}

Note: print page ~4 holds the end of **Primum Non Nocere** fiction and the start of **Collateral Nuyen**; extract splits that page.

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
