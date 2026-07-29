# -*- coding: utf-8 -*-
"""Data Trails landmark sweep."""
from pathlib import Path
import re

MD = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Data Trails")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\datatrails_sweep_report.md")

LANDMARKS = {
    "01 - Contents and Credits.md": ["Jason Andrew", "CZ Wright", "GOD Speaks", "Mastering the Matrix"],
    "02 - Introduction.md": ["World in Your Pocket", "Resonance realms", "Principles of Insanity"],
    "03 - GOD Speaks.md": ["CZ Wright", "Lurker", "Agent Birdwatcher", "brick your brain"],
    "04 - The World in Your Pocket.md": ["PubGrid", "grids", "NYCNet"],
    "05 - True Hackers, Lusers & Dirtballs.md": ["Choson Ring", "Walking People", "Strictures"],
    "06 - On the Bleeding Edge.md": ["Positive Qualities", "Negative Qualities"],
    "07 - Born to Hack.md": ["Paths to Hackerdom", "Hacker Hobbyist"],
    "08 - Killer Apps & Razor Forms.md": ["Complex Forms", "Echoes", "Derezz"],
    "09 - The Guts of the Matrix.md": ["Cyberdeck", "Modules", "Commlink"],
    "10 - The All-Seeing Eye of GOD.md": ["Bloodhound", "DemiGOD", "Security Spider"],
    "11 - Corporate Sponsorship.md": ["Jason Andrew"],
    "12 - The Perfect Host.md": ["What Is a Host", "Game Information", "IC"],
    "13 - Deeper and Deeper.md": ["Foundation", "Beneath the Looking Glass", "Deep Run"],
    "14 - Body Hunt.md": ["Scott Schletz", "Windhowler"],
    "15 - Principles of Insanity.md": ["Creating an AI Character", "E-Ghosts", "Dissonants", "UV Host"],
    "16 - Mastering the Matrix.md": ["Garbage In", "Trackback", "Matrix Combat"],
}

lines = ["# Data Trails landmark sweep\n\n", "| File | Missing | Em | JP inv | Verdict |\n|---|---|---|---|---|\n"]
for fname, lms in LANDMARKS.items():
    p = MD / fname
    t = p.read_text(encoding="utf-8") if p.exists() else ""
    low = t.lower()
    miss = [m for m in lms if m.lower() not in low]
    em = t.count("\u2014") + t.count("\u2013") + t.count("\u2026")
    inv = len(re.findall(r"^> (?!\*\*).+\n> \*\*[^*]+\*\*\s*$", t, re.M))
    verdict = "PASS" if not miss and em == 0 and inv == 0 else "FIX"
    lines.append(f"| {fname} | {len(miss)} {miss[:3]} | {em} | {inv} | {verdict} |\n")

OUT.write_text("".join(lines), encoding="utf-8")
print(OUT.read_text(encoding="utf-8"))
