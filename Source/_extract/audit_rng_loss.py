# -*- coding: utf-8 -*-
"""Quick loss-check for Run & Gun Source Texts vs PDF."""
from __future__ import annotations

from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")

SECTIONS = [
    ("01 - Contents and Credits.md", 1, 5),
    ("02 - Catspaw.md", 5, 9),
    ("03 - Fight for Your Life.md", 9, 10),
    ("04 - What You Don't Know Kills You.md", 10, 17),
    ("05 - Arsenal.md", 17, 55),
    ("06 - Armor and Protection.md", 55, 87),
    ("07 - Tactics and Tools.md", 87, 105),
    ("08 - Killshots and More.md", 105, 127),
    ("09 - Martial Arts.md", 127, 142),
    ("10 - Fixin All the Broken Drek.md", 142, 143),
    ("11 - Staying Alive.md", 143, 169),
    ("12 - Blow Up Good.md", 169, 197),
    ("13 - Hostile Extraction.md", 197, 201),
    ("14 - Run and Gun Tables.md", 201, 213),
]

KEYS = [
    "Highland Forge",
    "Victorinox",
    "AK-98",
    "Ruthenium",
    "PI-Tac",
    "RG1",
    "Acrobatic Defender",
    "Radiation Sponge",
    "ANFO",
    "Bounding Overwatch",
    "Form-Fitting",
    "Blasting Cap",
    "Garrote",
    "Ares Redline",
]


def main() -> None:
    doc = fitz.open(str(PDF))
    print("=== size ratio PDF chars vs MD body ===")
    for fname, start, end in SECTIONS:
        pdf_t = "".join((doc[i].get_text("text") or "") for i in range(start, end))
        md = (OUT / fname).read_text(encoding="utf-8")
        body = md
        if "**Source:**" in md:
            body = md.split("**Source:**", 1)[1]
            body = body.split("\n", 1)[1] if "\n" in body else body
        ratio = len(body) / max(1, len(pdf_t))
        em = ("\u2014" in md) or ("—" in md)
        print(f"{fname[:42]:42} pdf={len(pdf_t):6} md={len(body):6} ratio={ratio:.2f} em={em}")

    combo = "".join((OUT / f).read_text(encoding="utf-8") for f, _, _ in SECTIONS)
    print("\n=== key terms across all chapters ===")
    for k in KEYS:
        hit = k.lower() in combo.lower()
        print(f"  {k}: {'YES' if hit else 'MISSING'}")

    # chapter page coverage: every PDF page 1..212 should appear in some section
    covered = set()
    for _, start, end in SECTIONS:
        covered.update(range(start, end))
    missing = [i for i in range(1, 213) if i not in covered]
    print("\nmissing PDF idx 1-212:", missing or "none")


if __name__ == "__main__":
    main()
