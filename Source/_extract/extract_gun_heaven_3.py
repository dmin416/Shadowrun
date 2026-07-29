# -*- coding: utf-8 -*-
"""Extract Gun Heaven 3 PDF into Source Texts/Gun Heaven 3/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Gun_H(e)aven_3.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Gun Heaven 3")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Print page N ~= PDF index N-1.
SECTIONS: list[tuple[str, str, int, int]] = [
    ("01 - Shadowrun Gun H(e)aven 3.md", "Shadowrun: Gun H(e)aven 3", 0, 1),
    ("02 - JackPoint.md", "JackPoint", 1, 2),
    ("03 - New Weapon UpgradesTraits.md", "New Weapon Upgrades/Traits", 2, 3),
    (
        "04 - Using This Book with Shadowrun, Fifth Edition.md",
        "Using This Book with Shadowrun, Fifth Edition",
        2,
        3,
    ),
    ("05 - Colt New Model Revolver.md", "Colt New Model Revolver", 3, 4),
    ("06 - Colt Agent Special.md", "Colt Agent Special", 4, 5),
    ("07 - Colt Future Frontier.md", "Colt Future Frontier", 5, 6),
    ("08 - Fianchetti Military 100.md", "Fianchetti Military 100", 6, 7),
    ("09 - Cavalier Evanator.md", "Cavalier Evanator", 7, 8),
    ("10 - Remington Suppressor.md", "Remington Suppressor", 8, 9),
    ("11 - Krime Spree.md", "Krime Spree", 9, 10),
    ("12 - Ares Sigma-3.md", "Ares Sigma-3", 10, 11),
    ("13 - Cavalier Arms Gladius.md", "Cavalier Arms Gladius", 11, 12),
    ("14 - Shiawase Arms Monsoon.md", "Shiawase Arms Monsoon", 12, 13),
    ("15 - Colt Inception.md", "Colt Inception", 13, 14),
    ("16 - Krupp Arms Kriegfaust.md", "Krupp Arms Kriegfaust", 14, 15),
    ("17 - SBd-44.md", "SBd-44", 15, 16),
    ("18 - Krime Boss.md", "Krime Boss", 16, 17),
    ("19 - Winchester Model 201.md", "Winchester Model 201", 17, 18),
    ("20 - Winchester Model 2066.md", "Winchester Model 2066", 18, 19),
    ("21 - Winchester Model 2054.md", "Winchester Model 2054", 19, 20),
    ("22 - Shiawase Arms Rain.md", "Shiawase Arms Rain", 20, 21),
    ("23 - Cavalier Falchion.md", "Cavalier Falchion", 21, 22),
    ("24 - Springfield 2003.md", "Springfield 2003", 22, 23),
    ("25 - Winchester Model 2024.md", "Winchester Model 2024", 23, 24),
    ("26 - Marlin 3468SS.md", "Marlin 3468SS", 24, 25),
    ("27 - Springfield M1A.md", "Springfield M1A", 25, 26),
    ("28 - M1 Garand.md", "M1 Garand", 26, 27),
    (
        "29 - Springfield Model 1855 Reproduction.md",
        "Springfield Model 1855 Reproduction",
        27,
        28,
    ),
    ("30 - Marlin 3041 BL.md", "Marlin 3041 BL", 28, 29),
    ("31 - Marlin X71.md", "Marlin X71", 29, 30),
    ("32 - Marlin 79S.md", "Marlin 79S", 30, 31),
    ("33 - Ultimax Rain Forest Carbine.md", "Ultimax Rain Forest Carbine", 31, 32),
    ("34 - Winchester Model 2067.md", "Winchester Model 2067", 32, 33),
    ("35 - Krime Wave.md", "Krime Wave", 33, 34),
    ("36 - Krime Bomb.md", "Krime Bomb", 34, 35),
    ("37 - Shiawase Arms Incinerator.md", "Shiawase Arms Incinerator", 35, 36),
    ("38 - Gun Stats (SR5).md", "Gun Stats (SR5)", 36, 37),
    ("39 - Gun Stats (SR4A).md", "Gun Stats (SR4A)", 37, 38),
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
        "\u00a5": "¥",
        "\ufffd": "",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    # common mojibake / control leftovers
    text = text.replace("�", "")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*SHADOWRUN\s*<<\s*$", s, re.I):
            continue
        if re.match(
            r"^<<\s*GUN\s*H\(E\)AVEN\s*3(?:\s*>>.*)?\s+\d+\s*$",
            s,
            re.I,
        ):
            continue
        if re.match(r"^<<\s*GUN\s*H\(E\)AVEN\s*3\s+\d+\s*$", s, re.I):
            continue
        if re.match(r"^GUN\s*H\(E\)AVEN\s*3\s+\d+\s*$", s, re.I):
            continue
        lines.append(s)

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def split_upgrades_and_using(page: str) -> tuple[str, str]:
    raw = clean(page)
    m = re.search(
        r"(?im)^USING THIS BOOK WITH SHADOWRUN,\s*FIFTH EDITION\s*$",
        raw,
    )
    if not m:
        return raw, ""
    upgrades = raw[: m.start()].rstrip() + "\n"
    using = raw[m.start() :].lstrip()
    return upgrades, using


def strip_leading_title(body: str, title: str) -> str:
    # Exact title line
    esc = re.escape(title.upper())
    body = re.sub(rf"(?im)^{esc}\s*\n+", "", body, count=1)
    # Stats page banners
    body = re.sub(
        r"(?im)^GUN H\(E\)AVEN 3 STATS \(SR5\)\s*\n+",
        "",
        body,
        count=1,
    )
    body = re.sub(
        r"(?im)^GUN H\(E\)AVEN 3 STATS \(SR4A\)\s*\n+",
        "",
        body,
        count=1,
    )
    body = re.sub(
        r"(?im)^NEW WEAPON UPGRADES/TRAITS\s*\n+",
        "",
        body,
        count=1,
    )
    body = re.sub(
        r"(?im)^USING THIS BOOK WITH SHADOWRUN,\s*FIFTH EDITION\s*\n+",
        "",
        body,
        count=1,
    )
    body = re.sub(r"(?im)^JACKPOINT\s*\n+", "", body, count=1)
    body = re.sub(r"(?im)^CREDITS\s*\n+", "", body, count=1)
    return body


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    page2 = doc[2].get_text("text") or ""
    upgrades_body, using_body = split_upgrades_and_using(page2)

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size < 300:
            p.unlink()
            print("removed stub", p.name)

    for fname, title, start, end in SECTIONS:
        if fname.startswith("03 -"):
            body = upgrades_body
            span = "PDF page index 2 (New Weapon Upgrades/Traits)"
        elif fname.startswith("04 -"):
            body = using_body if using_body.strip() else clean(page2)
            span = "PDF page index 2 (Using This Book...)"
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
            f"**Source:** Gun Heaven 3 | "
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
    index = f"""# Gun Heaven 3

Extra weapons catalog (dual-statted SR5 / SR4A).

**PDF:** `Source/PDF/{PDF.name}` ({len(doc)} pages; print page ≈ PDF index + 1)

Source Texts extracted via `Source/_extract/extract_gun_heaven_3.py` (pymupdf).
Formatting: `Source/_extract/format_gun_heaven_3.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{rows}

Note: print page 3 (PDF idx 2) holds **New Weapon Upgrades/Traits** and **Using This Book with Shadowrun, Fifth Edition**; extract splits that page.

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
