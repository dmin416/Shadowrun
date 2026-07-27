# -*- coding: utf-8 -*-
"""Deeper Seattle Sprawl loss checks: hyphen joins + TOC name spot checks."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = fitz.open(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\seattlesprawl.pdf")
ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl")

SECTIONS = [
    ("02 - Whirlwind Tour.md", 6, 10),
    ("03 - Emerald Shadows.md", 10, 13),
    ("04 - Downtown.md", 13, 18),
    ("05 - Bellevue.md", 18, 24),
    ("06 - Tacoma.md", 24, 30),
    ("07 - Everett.md", 30, 34),
    ("08 - Renton.md", 34, 39),
    ("09 - Auburn.md", 39, 45),
    ("10 - Snohomish.md", 45, 52),
    ("11 - Fort Lewis.md", 52, 57),
    ("12 - Redmond.md", 57, 62),
    ("13 - Puyallup.md", 62, 67),
    ("14 - Council Island.md", 67, 72),
    ("15 - Outremer.md", 72, 83),
    ("16 - The Seattle Underground.md", 83, 88),
]

CHECKS = {
    "04 - Downtown.md": [
        "Disassemblers",
        "Halloweeners",
        "Finnigan",
        "Orlov",
        "Eye of the Needle",
        "Remembrance",
        "Troll Killers",
    ],
    "05 - Bellevue.md": [
        "Lake Acids",
        "Nova Rich",
        "405 Hellhounds",
        "Leather Devils",
        "Ciarniello",
    ],
    "06 - Tacoma.md": [
        "Shotozumi",
        "Gianelli",
        "Fenris Nacht",
        "Crying Wall",
        "Silcox",
        "Kumon",
    ],
    "07 - Everett.md": ["Traveler Jones", "Naval", "Triad"],
    "08 - Renton.md": ["Night Hunters", "Black Friday", "Family Day"],
    "09 - Auburn.md": ["Boeing", "White River", "Stuck", "Green River"],
    "10 - Snohomish.md": ["Silverfoot", "Harvest", "NatVat", "Thrashers"],
    "11 - Fort Lewis.md": ["Zoological", "Two Spikes", "commissary", "Parkland"],
    "12 - Redmond.md": [
        "Brain Eaters",
        "Crimson Crush",
        "Funhouse",
        "Hollywood",
        "Kalanyr",
        "Rusted Stilettos",
    ],
    "13 - Puyallup.md": ["Jimmy Kincaid", "Special Occasions"],
    "14 - Council Island.md": ["Mercer", "First Nations", "Salish"],
    "15 - Outremer.md": [
        "Bainbridge",
        "Vashon",
        "Fox Island",
        "McNeil",
        "Anderson",
        "Puget Pirates",
    ],
    "16 - The Seattle Underground.md": [
        "Skraacha",
        "Prop 23",
        "Renraku",
        "Night of Woe",
        "Ork Underground",
    ],
}


def alnum(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def main() -> None:
    print("=== HYPHEN-JOIN CHECK (PDF word-break vs MD) ===")
    any_hard = False
    for fname, a, b in SECTIONS:
        pdf = "\n".join(PDF[i].get_text("text") or "" for i in range(a, b))
        md = (ROOT / fname).read_text(encoding="utf-8")
        md_alnum = alnum(md)
        misses: list[str] = []
        for m in re.finditer(r"([A-Za-z]{3,})-\s*\n\s*([a-z]{2,})", pdf):
            joined = (m.group(1) + m.group(2)).lower()
            if joined not in md_alnum:
                misses.append(joined)
        misses = sorted(set(misses))
        status = "OK" if not misses else f"{len(misses)} MISS"
        if misses:
            any_hard = True
        print(f"{fname}: {status}")
        for j in misses[:15]:
            print(f"  - {j}")

    print("\n=== TOC / NAME SPOT CHECK ===")
    for fname, names in CHECKS.items():
        t = (ROOT / fname).read_text(encoding="utf-8")
        miss = [n for n in names if n.lower() not in t.lower()]
        print(f"{fname}: {'OK' if not miss else 'MISSING ' + str(miss)}")

    # Section header presence for districts
    print("\n=== STANDARD SECTION HEADERS ===")
    needed = [
        "Special Occasions",
        "Crime Scene",
        "Where to Shop",
        "Where to Squat",
        "You Won't Find This Elsewhere",
        "Opposition Report",
        "Help Wanted",
        "at a Glance",
    ]
    for fname, a, b in SECTIONS:
        if fname.startswith("02") or fname.startswith("03"):
            continue
        t = (ROOT / fname).read_text(encoding="utf-8")
        miss = [n for n in needed if n.lower() not in t.lower()]
        # Outremer / Council may lack some
        print(f"{fname}: {'OK' if not miss else 'missing ' + str(miss)}")

    print("\nany_hard_hyphen_misses=", any_hard)


if __name__ == "__main__":
    main()
