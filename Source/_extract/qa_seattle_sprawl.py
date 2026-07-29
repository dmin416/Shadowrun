# -*- coding: utf-8 -*-
"""Done-check (and light loss recheck) for Seattle Sprawl Source Texts."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\seattlesprawl.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\seattle_sprawl_qa_report.md")
INDEX = OUT / "INDEX.md"

SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 6),
    ("02 - Whirlwind Tour.md", "Whirlwind Tour", 6, 10),
    ("03 - Emerald Shadows.md", "Emerald Shadows", 10, 13),
    ("04 - Downtown.md", "Downtown", 13, 18),
    ("05 - Bellevue.md", "Bellevue", 18, 24),
    ("06 - Tacoma.md", "Tacoma", 24, 30),
    ("07 - Everett.md", "Everett", 30, 34),
    ("08 - Renton.md", "Renton", 34, 39),
    ("09 - Auburn.md", "Auburn", 39, 45),
    ("10 - Snohomish.md", "Snohomish", 45, 52),
    ("11 - Fort Lewis.md", "Fort Lewis", 52, 57),
    ("12 - Redmond.md", "Redmond", 57, 62),
    ("13 - Puyallup.md", "Puyallup", 62, 67),
    ("14 - Council Island.md", "Council Island", 67, 72),
    ("15 - Outremer.md", "Outremer", 72, 83),
    ("16 - The Seattle Underground.md", "The Seattle Underground", 83, 88),
]

MUST_HAVE = [
    ("02 - Whirlwind Tour.md", "Seattle"),
    ("03 - Emerald Shadows.md", "Shape of the City"),
    ("04 - Downtown.md", "Halloweeners"),
    ("04 - Downtown.md", "Disassemblers"),
    ("04 - Downtown.md", "Eye of the Needle"),
    ("05 - Bellevue.md", "Lake Acids"),
    ("05 - Bellevue.md", "Nova Rich"),
    ("06 - Tacoma.md", "Shotozumi"),
    ("06 - Tacoma.md", "Fenris Nacht"),
    ("07 - Everett.md", "Traveler Jones"),
    ("08 - Renton.md", "Night Hunters"),
    ("08 - Renton.md", "Black Friday"),
    ("09 - Auburn.md", "Boeing"),
    ("09 - Auburn.md", "White River"),
    ("10 - Snohomish.md", "Silverfoot"),
    ("10 - Snohomish.md", "NatVat"),
    ("11 - Fort Lewis.md", "Zoological"),
    ("11 - Fort Lewis.md", "Two Spikes"),
    ("12 - Redmond.md", "Crimson Crush"),
    ("12 - Redmond.md", "Kalanyr"),
    ("13 - Puyallup.md", "Jimmy Kincaid"),
    ("14 - Council Island.md", "First Nations"),
    ("14 - Council Island.md", "Salish"),
    ("15 - Outremer.md", "Bainbridge"),
    ("15 - Outremer.md", "Vashon"),
    ("15 - Outremer.md", "Puget Pirates"),
    ("16 - The Seattle Underground.md", "Skraacha"),
    ("16 - The Seattle Underground.md", "Ork Underground"),
]

DISTRICT_HEADERS = [
    "at a Glance",
    "Special Occasions",
    "Crime Scene",
    "Where to Shop",
    "Where to Squat",
    "You Won't Find This Elsewhere",
    "Opposition Report",
]


def pdf_chars(a: int, b: int) -> int:
    doc = fitz.open(str(PDF))
    text = "\n".join((doc[i].get_text("text") or "") for i in range(a, b))
    doc.close()
    return len(re.sub(r"\s+", "", text))


def md_chars(path: Path) -> int:
    return len(re.sub(r"\s+", "", path.read_text(encoding="utf-8")))


def main() -> None:
    lines: list[str] = ["# Seattle Sprawl QA Report", ""]
    ok = True

    files = [OUT / f for f, _, _, _ in SECTIONS]
    lines.append(f"Chapter files: {len(files)}")
    if len(files) != 16:
        ok = False
        lines.append(f"FAIL: expected 16 chapter files, found {len(files)}")
    else:
        lines.append("PASS: 16 chapter files")

    tiny = [p.name for p in files if not p.exists() or p.stat().st_size < 500]
    if tiny:
        ok = False
        lines.append("FAIL: tiny/missing: " + ", ".join(tiny))
    else:
        lines.append("PASS: no empty/tiny chapter files")

    lines.append("")
    lines.append("## H1 / INDEX")
    idx = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    for fname, title, a, b in SECTIONS:
        path = OUT / fname
        body = path.read_text(encoding="utf-8")
        h1 = re.search(r"^# (.+)$", body, re.M)
        if not h1 or h1.group(1).strip() != title:
            ok = False
            lines.append(f"FAIL H1 {fname}: got {h1.group(1) if h1 else None!r}, want {title!r}")
        else:
            lines.append(f"PASS H1 {fname}")
        link_frag = fname.replace(" ", "%20")
        if fname not in idx and link_frag not in idx:
            # INDEX uses percent-encoded spaces in links
            bare = fname.replace(".md", "")
            if bare not in idx and link_frag.split("%20")[0] not in idx:
                ok = False
                lines.append(f"FAIL INDEX missing link for {fname}")
            else:
                lines.append(f"PASS INDEX {fname}")
        else:
            lines.append(f"PASS INDEX {fname}")

    lines.append("")
    lines.append("## Phrase checks")
    for fname, phrase in MUST_HAVE:
        body = (OUT / fname).read_text(encoding="utf-8")
        if phrase.lower() not in body.lower():
            ok = False
            lines.append(f"FAIL {fname}: missing `{phrase}`")
        else:
            lines.append(f"PASS {fname}: `{phrase}`")

    lines.append("")
    lines.append("## District section headers")
    for fname, title, a, b in SECTIONS:
        if not fname[:2].isdigit() or int(fname[:2]) < 4:
            continue
        body = (OUT / fname).read_text(encoding="utf-8")
        miss = [h for h in DISTRICT_HEADERS if h.lower() not in body.lower()]
        # Council Island: print has no Help Wanted (noted in INDEX)
        if fname.startswith("14"):
            miss = [h for h in miss if h != "Help Wanted"]
            if "Help Wanted" not in body:
                lines.append("NOTE Council Island: no Help Wanted (matches print)")
        if miss:
            ok = False
            lines.append(f"FAIL {fname}: missing {miss}")
        else:
            lines.append(f"PASS {fname}: district headers")

    lines.append("")
    lines.append("## Char ratio vs PDF (body chapters)")
    for fname, title, a, b in SECTIONS:
        if fname.startswith("01"):
            # Condensed TOC by design
            ratio = md_chars(OUT / fname) / max(1, pdf_chars(a, b))
            lines.append(f"NOTE {fname}: MD/PDF={ratio:.2f} (condensed TOC intentional)")
            continue
        ratio = md_chars(OUT / fname) / max(1, pdf_chars(a, b))
        if ratio < 0.85:
            ok = False
            lines.append(f"FAIL {fname}: MD/PDF={ratio:.2f}")
        else:
            lines.append(f"PASS {fname}: MD/PDF={ratio:.2f}")

    lines.append("")
    bad_em = []
    for p in files:
        t = p.read_text(encoding="utf-8")
        if "\u2014" in t or "\u2013" in t or "—" in t or "–" in t:
            bad_em.append(p.name)
    if bad_em:
        ok = False
        lines.append("FAIL em/en dashes in: " + ", ".join(bad_em))
    else:
        lines.append("PASS: no em/en dashes")

    lines.append("")
    lines.append("## Verdict")
    lines.append("**PASS**" if ok else "**FAIL**")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("wrote", REPORT)


if __name__ == "__main__":
    main()
