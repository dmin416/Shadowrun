# -*- coding: utf-8 -*-
"""Extract Splintered State PDF into Source Texts/Splintered State/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(
    r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\pdfcoffee.com_shadowrun-5e-splintered-state-pdf-free.pdf"
)
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Splintered State")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Mid-page splits handled specially in main().
# TOC page N ~= PDF index N-1.
SECTIONS: list[tuple[str, str, int, int]] = [
    ("01 - Shadowrun Splintered State.md", "Shadowrun: Splintered State", 0, 2),
    ("02 - Contents & Credits.md", "Contents & Credits", 2, 3),
    ("03 - Everyone Wants to Change the World.md", "Everyone Wants to Change the World", 3, 4),
    ("04 - Politics and Paydata.md", "Politics and Paydata", 4, 8),
    ("05 - Scene 0 Rounded Up.md", "Scene 0: Rounded Up", 7, 11),
    ("06 - Scene 1 You Know the Drill.md", "Scene 1: You Know the Drill", 10, 14),
    ("07 - Scene 2 Without a Hitch.md", "Scene 2: Without a Hitch", 13, 18),
    ("08 - Scene 3 Lying Down on the Job.md", "Scene 3: Lying Down on the Job", 17, 21),
    ("09 - Scene 4 A Knock at the Door.md", "Scene 4: A Knock at the Door", 20, 28),
    ("10 - Scene 5 Caveat Venditor.md", "Scene 5: Caveat Venditor", 27, 35),
    ("11 - Scene 6 Friends with High Prices.md", "Scene 6: Friends with High Prices", 34, 43),
    (
        "12 - Scene 7 Threading the Needle (Optional).md",
        "Scene 7: Threading the Needle (Optional)",
        42,
        52,
    ),
    ("13 - Picking Up the Pieces.md", "Picking Up the Pieces", 51, 53),
    ("14 - Legwork.md", "Legwork", 52, 55),
    ("15 - Matrix Legwork.md", "Matrix Legwork", 54, 55),
    ("16 - Cast of Shadows.md", "Cast of Shadows", 54, 62),
    ("17 - But No One Wants to Die.md", "But No One Wants to Die", 62, 64),
    ("18 - Player Handouts.md", "Player Handouts", 64, 74),
]

# Mid-page body starts (matched AFTER clean() joins multi-line titles)
SCENE_STARTS: dict[int, str] = {
    7: r"(?im)^SCENE 0: ROUNDED UP\s*\nSCAN THIS",
    10: r"(?im)^SCENE 1: YOU KNOW THE DRILL\s*\nSCAN THIS",
    13: r"(?im)^SCENE 2: WITHOUT A HITCH\s*\nSCAN THIS",
    17: r"(?im)^SCENE 3: LYING DOWN ON THE JOB\s*\nSCAN THIS",
    20: r"(?im)^SCENE 4: A KNOCK AT THE DOOR\s*\nSCAN THIS",
    27: r"(?im)^SCENE 5: CAVEAT VENDITOR\s*\nSCAN THIS",
    34: r"(?im)^SCENE 6: FRIENDS WITH HIGH PRICES\s*\nSCAN THIS",
    42: r"(?im)^SCENE 7: THREADING THE NEEDLE \(OPTIONAL\)\s*\nSCAN THIS",
}

PICKING_START = r"(?im)^PICKING UP\s*\nTHE PIECES\s*$"
CAST_START = r"(?im)^CAST OF SHADOWS\s*$"


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
        "\xad": "",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = text.replace("�", "")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>\s*SPLINTERED STATE\s*<<\s*$", s, re.I):
            continue
        # running headers / footers
        if re.match(r"^>>\s*SPLINTERED STATE\s*<<", s, re.I):
            continue
        if re.match(
            r"^(?:\d+\s+)?SCENE\s+\d+:.+\s+\d+\s*$",
            s,
            re.I,
        ):
            continue
        if re.match(r"^\d+\s+SCENE\s+\d+:", s, re.I):
            continue
        if re.match(
            r"^(?:\d+\s+)?(?:PLOT SYNOPSIS|LEGWORK|Matrix Legwork|CAST OF SHADOWS|"
            r"PICKING UP THE PIECES|BUT NO ONE WANTS TO DIE|ADVENTURE BACKGROUND)\s+\d+\s*$",
            s,
            re.I,
        ):
            continue
        if re.match(
            r"^\d+\s+(?:PLOT SYNOPSIS|LEGWORK|Matrix Legwork|CAST OF SHADOWS|"
            r"PICKING UP THE PIECES|ADVENTURE BACKGROUND)\s*$",
            s,
            re.I,
        ):
            continue
        lines.append(s)

    text = "\n".join(lines)
    joins = [
        (r"(?im)^EVERYONE WANTS TO\s*\nCHANGE THE WORLD\s*$", "EVERYONE WANTS TO CHANGE THE WORLD"),
        (r"(?im)^POLITICS\s*\n&\s*PAYDATA\s*$", "POLITICS & PAYDATA"),
        (r"(?im)^SCENE 0:\s*\nROUNDED UP\s*$", "SCENE 0: ROUNDED UP"),
        (r"(?im)^SCENE 1: YOU\s*\nKNOW THE DRILL\s*$", "SCENE 1: YOU KNOW THE DRILL"),
        (r"(?im)^SCENE 2:\s*\nWITHOUT A HITCH\s*$", "SCENE 2: WITHOUT A HITCH"),
        (r"(?im)^SCENE 3: LYING\s*\nDOWN ON THE JOB\s*$", "SCENE 3: LYING DOWN ON THE JOB"),
        (r"(?im)^SCENE 4: A KNOCK\s*\nAT THE DOOR\s*$", "SCENE 4: A KNOCK AT THE DOOR"),
        (r"(?im)^SCENE 5:\s*\nCAVEAT VENDITOR\s*$", "SCENE 5: CAVEAT VENDITOR"),
        (r"(?im)^SCENE 6: FRIENDS\s*\nWITH HIGH PRICES\s*$", "SCENE 6: FRIENDS WITH HIGH PRICES"),
        (
            r"(?im)^SCENE 7: THREADING\s*\nTHE NEEDLE \(OPTIONAL\)\s*$",
            "SCENE 7: THREADING THE NEEDLE (OPTIONAL)",
        ),
        (r"(?im)^PICKING UP\s*\nTHE PIECES\s*$", "PICKING UP THE PIECES"),
        (r"(?im)^BUT NO ONE WANTS TO\s*\nDIE\s*$", "BUT NO ONE WANTS TO DIE"),
        (
            r"(?im)^HANDOUT #2:\s*\nREASSEMBLED PROJECT DAYBREAK FILES\s*$",
            "HANDOUT #2: REASSEMBLED PROJECT DAYBREAK FILES",
        ),
        (
            r"(?im)^'IMAGINARY' ANNIE GOLDSMITH,\s*\nINVISIBLE ESQUIRE\s*$",
            "'IMAGINARY' ANNIE GOLDSMITH, INVISIBLE ESQUIRE",
        ),
        (r"(?im)^LONE STAR SECURITY\s*\nSERVICES WAGE MAGE\s*$", "LONE STAR SECURITY SERVICES WAGE MAGE"),
    ]
    for pat, repl in joins:
        text = re.sub(pat, repl, text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def split_on(page: str, heading_re: str) -> tuple[str, str]:
    raw = clean(page)
    m = re.search(heading_re, raw)
    if not m:
        return raw, ""
    return raw[: m.start()].rstrip() + "\n", raw[m.start() :].lstrip()


def strip_leading_title(body: str, title: str) -> str:
    body = re.sub(rf"(?i)\A{re.escape(title)}\s*\n+", "", body, count=1)
    for banner in (
        "CONTENTS",
        "CREDITS",
        "CONTENTS & CREDITS",
        "EVERYONE WANTS TO CHANGE THE WORLD",
        "POLITICS & PAYDATA",
        "POLITICS AND PAYDATA",
        "ADVENTURE BACKGROUND",
        "SCENE 0: ROUNDED UP",
        "SCENE 1: YOU KNOW THE DRILL",
        "SCENE 2: WITHOUT A HITCH",
        "SCENE 3: LYING DOWN ON THE JOB",
        "SCENE 4: A KNOCK AT THE DOOR",
        "SCENE 5: CAVEAT VENDITOR",
        "SCENE 6: FRIENDS WITH HIGH PRICES",
        "SCENE 7: THREADING THE NEEDLE (OPTIONAL)",
        "PICKING UP THE PIECES",
        "LEGWORK",
        "MATRIX LEGWORK",
        "CAST OF SHADOWS",
        "BUT NO ONE WANTS TO DIE",
        "PLAYER HANDOUTS",
        "SHADOWRUN",
        "SPLINTERED",
        "STATE",
    ):
        body = re.sub(rf"(?i)\A{re.escape(banner)}\s*\n+", "", body, count=1)
    return body


def page_text(doc: fitz.Document, i: int) -> str:
    return doc[i].get_text("text") or ""


def main() -> None:
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    # Precompute mid-page splits
    splits: dict[int, tuple[str, str]] = {}
    for idx, pat in SCENE_STARTS.items():
        before, after = split_on(page_text(doc, idx), pat)
        if not after.strip():
            print(f"WARNING: scene split failed on idx {idx}")
        splits[idx] = (before, after)

    pick_before, pick_after = split_on(
        page_text(doc, 51), r"(?im)^PICKING UP THE PIECES\s*\nMONEY"
    )
    if not pick_after.strip():
        print("WARNING: picking split fell back")
        pick_before, pick_after = split_on(
            page_text(doc, 51), r"(?im)^PICKING UP THE PIECES\s*$"
        )

    cast_before, cast_after = split_on(page_text(doc, 54), CAST_START)
    if not cast_after.strip():
        print("WARNING: cast split failed")

    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size < 400:
            p.unlink()
            print("removed stub", p.name)

    for fname, title, start, end in SECTIONS:
        parts: list[str] = []
        span = f"PDF page index {start}-{end - 1}"

        if fname.startswith("04 -"):
            parts = [page_text(doc, i) for i in range(4, 7)]
            parts.append(splits[7][0])
            span = "PDF page index 4-7 (before Scene 0)"
        elif fname.startswith("05 -"):
            parts = [splits[7][1]]
            parts.extend(page_text(doc, i) for i in range(8, 10))
            parts.append(splits[10][0])
            span = "PDF page index 7-10 (before Scene 1)"
        elif fname.startswith("06 -"):
            parts = [splits[10][1]]
            parts.extend(page_text(doc, i) for i in range(11, 13))
            parts.append(splits[13][0])
            span = "PDF page index 10-13 (before Scene 2)"
        elif fname.startswith("07 -"):
            parts = [splits[13][1]]
            parts.extend(page_text(doc, i) for i in range(14, 17))
            parts.append(splits[17][0])
            span = "PDF page index 13-17 (before Scene 3)"
        elif fname.startswith("08 -"):
            parts = [splits[17][1]]
            parts.extend(page_text(doc, i) for i in range(18, 20))
            parts.append(splits[20][0])
            span = "PDF page index 17-20 (before Scene 4)"
        elif fname.startswith("09 -"):
            parts = [splits[20][1]]
            parts.extend(page_text(doc, i) for i in range(21, 27))
            parts.append(splits[27][0])
            span = "PDF page index 20-27 (before Scene 5)"
        elif fname.startswith("10 -"):
            parts = [splits[27][1]]
            parts.extend(page_text(doc, i) for i in range(28, 34))
            parts.append(splits[34][0])
            span = "PDF page index 27-34 (before Scene 6)"
        elif fname.startswith("11 -"):
            parts = [splits[34][1]]
            parts.extend(page_text(doc, i) for i in range(35, 42))
            parts.append(splits[42][0])
            span = "PDF page index 34-42 (before Scene 7)"
        elif fname.startswith("12 -"):
            parts = [splits[42][1]]
            parts.extend(page_text(doc, i) for i in range(43, 51))
            parts.append(pick_before)
            span = "PDF page index 42-51 (before Picking Up the Pieces)"
        elif fname.startswith("13 -"):
            parts = [pick_after]
            span = "PDF page index 51 (Picking Up the Pieces body)"
            if not "".join(parts).strip():
                parts = [page_text(doc, 51)]
        elif fname.startswith("14 -"):
            parts = [page_text(doc, 52), page_text(doc, 53)]
            span = "PDF page index 52-53"
        elif fname.startswith("15 -"):
            parts = [cast_before]
            span = "PDF page index 54 (Matrix Legwork)"
        elif fname.startswith("16 -"):
            parts = [cast_after]
            parts.extend(page_text(doc, i) for i in range(55, 62))
            span = "PDF page index 54-61"
        else:
            parts = [page_text(doc, i) for i in range(start, min(end, len(doc)))]
            span = f"PDF page index {start}-{end - 1}"

        body = clean("\n\n".join(p for p in parts if p is not None))
        body = strip_leading_title(body, title)
        # Drop duplicate scene banner at top; keep SCAN THIS
        body = re.sub(
            r"(?im)\A(?:SCENE\s+\d+:[^\n]+\n)+(?=SCAN THIS)",
            "",
            body,
            count=1,
        )
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                f"Likely image-only or blank. See {span}.)\n"
            )

        md = (
            f"# {title}\n\n"
            f"**Source:** Splintered State | "
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
    index = f"""# Splintered State

Adventure: Seattle politics, Project Daybreak, and competing interests around Seth Dietrich.

**PDF:** `Source/PDF/{PDF.name}` ({len(doc)} pages; TOC page ≈ PDF index + 1)

Source Texts extracted via `Source/_extract/extract_splintered_state.py` (pymupdf).
Formatting: `Source/_extract/format_splintered_state.py`.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
{rows}

Note: Scene transitions and Matrix Legwork / Cast of Shadows / Picking Up the Pieces are mid-page splits.

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
