# -*- coding: utf-8 -*-
"""Normalize section headings in Seattle Sprawl chapter extracts."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl")

H2 = {
    "OVERVIEW",
    "THE SHAPE OF THE CITY",
    "THE CULTURE",
    "SPECIAL OCCASIONS",
    "CRIME SCENE",
    "WHERE TO SHOP",
    "WHERE TO SQUAT",
    "YOU WON'T FIND THIS ELSEWHERE",
    "YOU WONT FIND THIS ELSEWHERE",
    "OPPOSITION REPORT",
    "HELP WANTED",
    "GANGS",
    "ORGANIZED CRIME",
    "DOWNTOWN",
    "BELLEVUE",
    "TACOMA",
    "EVERETT",
    "RENTON",
    "AUBURN",
    "SNOHOMISH",
    "FORT LEWIS",
    "REDMOND",
    "PUYALLUP",
    "COUNCIL ISLAND",
    "OUTREMER",
    "BAINBRIDGE ISLAND",
    "VASHON ISLAND",
    "FOX ISLAND",
    "MCNEIL ISLAND",
    "ANDERSON ISLAND",
    "THE SEATTLE UNDERGROUND",
    "WHIRLWIND TOUR",
}

H2_TITLE = {
    "Special Occasions",
    "Crime Scene",
    "Where to Shop",
    "Where To Squat",
    "You Won't Find This Elsewhere",
    "Opposition Report",
    "Help Wanted",
}

SKIP = {"01 - Contents and Credits.md", "INDEX.md"}


def titleize(s: str) -> str:
    if s.upper() in {"YOU WONT FIND THIS ELSEWHERE", "YOU WON'T FIND THIS ELSEWHERE"}:
        return "You Won't Find This Elsewhere"
    small = {"of", "the", "a", "an", "and", "to", "for", "in", "on"}
    parts = s.split()
    out: list[str] = []
    for i, w in enumerate(parts):
        if w.isupper() and len(w) > 1:
            tw = w.title()
            if i > 0 and tw.lower() in small:
                tw = tw.lower()
            out.append(tw)
        else:
            out.append(w)
    return " ".join(out)


def main() -> None:
    for path in sorted(ROOT.glob("*.md")):
        if path.name in SKIP:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        out: list[str] = []
        for line in lines:
            s = line.strip()
            if s.upper().startswith("NATIVE FOR"):
                out.extend(["", '## Native for "Quiet Death"', ""])
                continue
            if s.upper() in H2:
                out.extend(["", "## " + titleize(s.upper()), ""])
                continue
            if s in H2_TITLE:
                heading = s.replace("Where To Squat", "Where to Squat")
                out.extend(["", "## " + heading, ""])
                continue
            if re.match(r"^POSTED BY:", s, re.I):
                out.extend(["", "### " + s, ""])
                continue
            out.append(line)
        body = "\n".join(out)
        body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
        for a, b in (("\u2014", "-"), ("\u2013", "-")):
            body = body.replace(a, b)
        path.write_text(body, encoding="utf-8")
        print("formatted", path.name)


if __name__ == "__main__":
    main()
