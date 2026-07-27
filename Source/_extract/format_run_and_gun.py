# -*- coding: utf-8 -*-
"""Format Run & Gun Source Texts (conservative pass).

Re-run extract_run_and_gun.py first if chapters were over-formatted.
Promotes curated section headers, strips footers/splash titles, light prose
reflow. Does NOT auto-promote every ALL CAPS line to ### (PDF reading order
and table captions make that unreliable).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")

H2 = {
    "TABLE OF CONTENTS",
    "BLADES",
    "CLUBS",
    "EXOTIC MELEE WEAPONS",
    "IMPROVISED MELEE WEAPONS",
    "RANGED WEAPONS",
    "ARROWHEADS",
    "EXOTIC RANGED WEAPONS",
    "TASERS",
    "HOLD-OUTS",
    "LIGHT PISTOLS",
    "HEAVY PISTOLS",
    "MACHINE PISTOLS",
    "SUBMACHINE GUNS",
    "ASSAULT RIFLES",
    "SNIPER RIFLES",
    "SHOTGUNS",
    "MACHINE GUNS",
    "CANNONS/LAUNCHERS",
    "LASER WEAPONS",
    "FLAMETHROWERS",
    "WEAPON ACCESSORIES",
    "AMMO",
    "WHY WE WEAR IT",
    "HIGH-FASHION ARMOR CLOTHING",
    "SPECIALTY ARMOR",
    "ENVIRONMENTAL PROTECTION",
    "CUSTOMIZATIONS AND OPTIONS",
    "SIXTH WORLD COMBAT TACTICS",
    "REALITIES OF TACTICAL TEAMWORK",
    "APPLYING THE LESSONS",
    "THE TOOLS OF THE TRADE",
    "PUTTING THE HURT ON",
    "OPTIONS FOR DEADLIER OR LESS LETHAL COMBAT",
    "MORE CALLED SHOTS",
    "AMMO-SPECIFIC CALLED SHOTS",
    "LOCATION, LOCATION, LOCATION.",
    "LOCATION, LOCATION, LOCATION",
    "AMMO WHAMMY!",
    "MORE ACTIONS!",
    "INTERRUPT ACTIONS",
    "COMBAT EDGE",
    "NEW QUALITIES",
    "POSITIVE QUALITIES",
    "NEGATIVE QUALITY",
    "NEGATIVE QUALITIES",
    "MARTIAL ART STYLES",
    "MARTIAL ART TECHNIQUES",
    "IT'S ALL ABOUT HOW AND WHERE YOU HIT",
    "FIXIN' ALL THE BROKEN DREK",
    "MAKING THE BLIND SEE AND THE DEAF HEAR",
    "BROKEN WEAPONS",
    "ALL THE OTHER BROKEN DREK",
    "INTRODUCTION",
    "WORLDLY HAZARDS",
    "HEAT",
    "KILLING FROST",
    "POLLUTION",
    "RADIATION",
    "BENEATH THE SEAS",
    "ABOVE THE SKIES",
    "BIGGER PROBLEMS",
    "QUALITIES",
    "ADVANCED DEMOLITIONS",
    "RULES FOR TAKING DOWN BUILDINGS",
    "RULES FOR EXPLOSIVES AND VEHICLES",
    "RULES FOR BREACHING/CUTTING",
    "COOKING EXPLOSIVES",
    "EXPLOSIVES",
    "DETONATORS",
    "EXPLOSIVE ACCESSORIES",
    "GEAR QUALITIES",
    "RUN & GUN TABLES",
    "RUN AND GUN TABLES",
    "SENSEI'S THOUGHTS ON: FIGHTING",
    "ON WEAPONS",
    "ON ARMOR AND PROTECTION",
    "ON TACTICS AND TEAMWORK",
    "ON MANHANDLING AND SKULLCRACKING",
    "ON THINGS THAT GO BOOM",
    "ON 'SNEAKY BASTARDS'",
    "FINAL THOUGHTS",
}

JOIN_PAIRS = [
    (("KILLSHOTS", "AND MORE"), None),  # splash; strip
    (("ARMOR &", "PROTECTION"), None),
    (("TACTICS", "& TOOLS"), None),
    (("STAYING", "ALIVE"), None),
    (("BLOW UP", "GOOD"), None),
    (("PUTTING THE", "HURT ON"), "PUTTING THE HURT ON"),
    (("OPTIONS FOR DEADLIER", "OR LESS LETHAL COMBAT"), "OPTIONS FOR DEADLIER OR LESS LETHAL COMBAT"),
    (("IT'S ALL ABOUT HOW", "AND WHERE YOU HIT"), "IT'S ALL ABOUT HOW AND WHERE YOU HIT"),
    (("FIXIN' ALL THE", "BROKEN DREK"), "FIXIN' ALL THE BROKEN DREK"),
    (("MARTIAL ART", "STYLES"), "MARTIAL ART STYLES"),
    (("MARTIAL ART", "TECHNIQUES"), "MARTIAL ART TECHNIQUES"),
    (("HIGH-FASHION ARMOR", "CLOTHING"), "HIGH-FASHION ARMOR CLOTHING"),
    (("CUSTOMIZATIONS AND", "OPTIONS"), "CUSTOMIZATIONS AND OPTIONS"),
    (("SIXTH WORLD COMBAT", "TACTICS"), "SIXTH WORLD COMBAT TACTICS"),
    (("REALITIES OF TACTICAL", "TEAMWORK"), "REALITIES OF TACTICAL TEAMWORK"),
    (("THE TOOLS OF", "THE TRADE"), "THE TOOLS OF THE TRADE"),
    (("ADVANCED", "DEMOLITIONS"), "ADVANCED DEMOLITIONS"),
    (("RULES FOR TAKING", "DOWN BUILDINGS"), "RULES FOR TAKING DOWN BUILDINGS"),
    (("RULES FOR EXPLOSIVES", "AND VEHICLES"), "RULES FOR EXPLOSIVES AND VEHICLES"),
    (("RULES FOR", "BREACHING/CUTTING"), "RULES FOR BREACHING/CUTTING"),
    (("COOKING", "EXPLOSIVES"), "COOKING EXPLOSIVES"),
    (("EXPLOSIVE", "ACCESSORIES"), "EXPLOSIVE ACCESSORIES"),
    (("GEAR", "QUALITIES"), "GEAR QUALITIES"),
    (("WORLDLY", "HAZARDS"), "WORLDLY HAZARDS"),
    (("BENEATH THE", "SEAS"), "BENEATH THE SEAS"),
    (("ABOVE THE", "SKIES"), "ABOVE THE SKIES"),
    (("BIGGER", "PROBLEMS"), "BIGGER PROBLEMS"),
    (("HOSTILE", "EXTRACTION"), None),
    (("FIGHT FOR", "YOUR LIFE"), None),
    (("WHAT YOU DON'T KNOW", "KILLS YOU"), None),
]

SPLASH_STRIP = {
    "ARSENAL",
    "ARMOR AND PROTECTION",
    "ARMOR & PROTECTION",
    "TACTICS AND TOOLS",
    "TACTICS & TOOLS",
    "KILLSHOTS AND MORE",
    "MARTIAL ARTS",
    "STAYING ALIVE",
    "BLOW UP GOOD",
    "HOSTILE EXTRACTION",
    "CATSPAW",
    "FIGHT FOR YOUR LIFE",
    "WHAT YOU DON'T KNOW KILLS YOU",
    "FIXIN' ALL THE BROKEN DREK",
}

TABLEISH = {
    "ACC",
    "REACH",
    "DV",
    "AP",
    "AVAIL",
    "COST",
    "ITEM",
    "MODE",
    "AMMO",
    "RC",
    "NAME",
    "PAGE",
    "ARMOR",
    "ARMOR RATING",
    "RATING",
    "CAPACITY",
    "SLOTS",
    "ESSENCE",
    "THRESHOLD",
    "MODIFIER",
    "DAMAGE",
    "DAM",
    "TYPE",
    "SKILL",
    "AVAILABILITY",
    "WIRELESS",
    "SIZE",
    "EXAMPLES",
}

CHAPTER_FOOTER_RE = re.compile(
    r"^(?:\d{1,3}\s+)?"
    r"(?:Catspaw|Fight for Your Life|What You Don't Know Kills You|"
    r"Arsenal|Armor(?:\s*&\s*|\s+and\s+)Protection|Tactics(?:\s*&\s*|\s+and\s+)Tools|"
    r"Killshots and More|Martial Arts|Fixin'?\s*All the Broken Drek|"
    r"Staying Alive|Blow Up Good|Hostile Extraction|Run\s*&\s*Gun Tables|"
    r"Contents(?:\s*/\s*|\s*&\s*)Credits)"
    r"(?:\s+\d{1,3})?$",
    re.I,
)

SKIP_FILES = {"INDEX.md", "01 - Contents and Credits.md"}
SMALL = {"of", "the", "a", "an", "and", "to", "for", "in", "on", "or", "vs"}


def titleize(s: str) -> str:
    special = {
        "IT'S ALL ABOUT HOW AND WHERE YOU HIT": "It's All About How and Where You Hit",
        "FIXIN' ALL THE BROKEN DREK": "Fixin' All the Broken Drek",
        "ON 'SNEAKY BASTARDS'": "On 'Sneaky Bastards'",
        "SENSEI'S THOUGHTS ON: FIGHTING": "Sensei's Thoughts On: Fighting",
        "AMMO WHAMMY!": "Ammo Whammy!",
        "MORE ACTIONS!": "More Actions!",
        "LOCATION, LOCATION, LOCATION.": "Location, Location, Location",
        "LOCATION, LOCATION, LOCATION": "Location, Location, Location",
        "RUN & GUN TABLES": "Run & Gun Tables",
        "OPTIONS FOR DEADLIER OR LESS LETHAL COMBAT": "Options for Deadlier or Less Lethal Combat",
        "CANNONS/LAUNCHERS": "Cannons/Launchers",
        "RULES FOR BREACHING/CUTTING": "Rules for Breaching/Cutting",
        "PUTTING THE HURT ON": "Putting the Hurt On",
    }
    if s in special:
        return special[s]
    parts = s.replace("&", "and").split()
    out: list[str] = []
    for i, w in enumerate(parts):
        tw = w.title()
        if i > 0 and tw.lower() in SMALL:
            tw = tw.lower()
        out.append(tw)
    return " ".join(out)


SIDEBAR_CAPS = {
    "REALISM VS. COMBAT ABSTRACTION",
    "REALISM VS. COMBAT ABSTRACTION:",
    "STRIKING A BALANCE",
    "THE LITTLE THINGS",
    "MODIFIERS, MODIFIERS, MODIFIERS!",
    "ALL ABOUT FLAMETHROWERS",
    "TARGET SIZE MODIFIERS",
    "MOVEMENT PENALTIES BY SPEED",
}

# Common single-cell table labels that must not join into prose.
TABLE_CELL_WORDS = {
    "Minuscule",
    "Tiny",
    "Small",
    "Average",
    "Bulky",
    "Large",
    "Huge",
}


def is_tableish(s: str) -> bool:
    u = s.strip().upper()
    if u in TABLEISH:
        return True
    if u.rstrip(":") in {x.rstrip(":") for x in SIDEBAR_CAPS}:
        return True
    if s.strip() in TABLE_CELL_WORDS:
        return True
    if re.match(r"^[\d.,+\-()/¥RFAPSxXL]+\s*$", s.strip()):
        return True
    if re.match(r"^\(?STR\s*[+x]", s.strip(), re.I):
        return True
    if re.match(r"^\d+[PRF]\b", s.strip()):
        return True
    if "¥" in s or s.strip().endswith("SR5"):
        return True
    return False


def is_standalone_caps(s: str) -> bool:
    """ALL CAPS title/header line, allowing trailing colon/punct."""
    t = s.strip()
    if not t or len(t) > 80:
        return False
    core = t.rstrip(":").strip()
    if not core or core.upper() != core:
        return False
    if not any(c.isalpha() for c in core):
        return False
    if is_tableish(core) and len(core.split()) == 1:
        return True
    words = core.split()
    if not words:
        return False
    return all(re.match(r"^[A-Z0-9][A-Z0-9'\"\-./&!,]*\.?$", w) for w in words)


def is_jackpoint_handle(s: str) -> bool:
    """Author tag after a JackPoint comment block."""
    if not s or len(s) > 40:
        return False
    if s.startswith(">") or s.startswith("#") or s.startswith("|"):
        return False
    if is_tableish(s):
        return False
    # typical handles: Hard Exit, Slamm-0!, /dev/grrl, Netcat, Stone
    if s.startswith("/") and " " not in s.strip():
        return True
    words = s.split()
    if len(words) > 4:
        return False
    # mostly Title Case / nickname, not a full sentence
    if s.endswith(".") or s.endswith("?") or s.endswith(","):
        return False
    if any(w.lower() in {"the", "and", "with", "from", "that", "this"} for w in words):
        return False
    return True


def join_pairs(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        a = lines[i].strip()
        b = lines[i + 1].strip() if i + 1 < len(lines) else ""
        matched = False
        for (p1, p2), joined in JOIN_PAIRS:
            if a.upper() == p1.upper() and b.upper() == p2.upper():
                if joined is not None:
                    out.append(joined)
                i += 2
                matched = True
                break
        if not matched:
            out.append(lines[i])
            i += 1
    return out


def promote_and_strip(lines: list[str], chapter_title: str) -> list[str]:
    out: list[str] = []
    title_u = chapter_title.upper().replace("&", "AND")
    for line in lines:
        s = line.strip()
        if not s:
            out.append("")
            continue
        if CHAPTER_FOOTER_RE.match(s):
            continue
        u = s.upper()
        if u in SPLASH_STRIP and (
            u.replace("&", "AND") == title_u.replace("&", "AND")
            or u == title_u
        ):
            continue
        if u in H2:
            out.extend(["", "## " + titleize(u), ""])
            continue
        out.append(line)
    return out


def reflow_prose(lines: list[str]) -> list[str]:
    out: list[str] = []
    buf: list[str] = []
    prev_was_gt = False

    def flush() -> None:
        nonlocal buf
        if not buf:
            return
        para = " ".join(x.strip() for x in buf)
        para = re.sub(r" {2,}", " ", para)
        out.append(para)
        buf = []

    for line in lines:
        stripped = line.strip()

        if not stripped:
            flush()
            out.append("")
            prev_was_gt = False
            continue

        if stripped.startswith("#") or stripped.startswith("**Source:**"):
            flush()
            out.append(stripped)
            prev_was_gt = False
            continue

        if stripped == ">" or stripped.startswith("> "):
            flush()
            out.append(stripped)
            prev_was_gt = True
            continue

        # JackPoint handle after comment
        if prev_was_gt and is_jackpoint_handle(stripped):
            flush()
            out.append(stripped)
            prev_was_gt = False
            continue

        if stripped.startswith("|") or is_tableish(stripped):
            flush()
            out.append(stripped)
            prev_was_gt = False
            continue

        if stripped.startswith("## "):
            flush()
            out.append(stripped)
            prev_was_gt = False
            continue

        # Keep ALL CAPS titles, sidebar headers, and table headers atomic
        if is_standalone_caps(stripped) or is_tableish(stripped):
            flush()
            out.append(stripped)
            prev_was_gt = False
            continue

        # Lowercase lines: normal PDF wraps join into the current
        # paragraph; after an interrupt flush they stay atomic so
        # deinterleave can stitch them past captions/tables.
        if stripped[0].islower():
            if buf:
                buf.append(stripped)
            else:
                flush()
                out.append(stripped)
            prev_was_gt = False
            continue

        buf.append(stripped)
        prev_was_gt = False

    flush()
    return out


def format_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        return
    title = lines[0][2:].strip()
    body_start = 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1
    source_line = ""
    if body_start < len(lines) and lines[body_start].startswith("**Source:**"):
        source_line = lines[body_start]
        body_start += 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1

    body = join_pairs(lines[body_start:])
    body = promote_and_strip(body, title)
    # Skip heavy reflow for TOC and tables
    if path.name not in {"01 - Contents and Credits.md", "14 - Run and Gun Tables.md"}:
        body = reflow_prose(body)

    cleaned: list[str] = []
    blank = 0
    for ln in body:
        if not ln.strip():
            blank += 1
            if blank <= 2:
                cleaned.append("")
            continue
        blank = 0
        cleaned.append(ln)
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()

    parts = [f"# {title}", ""]
    if source_line:
        parts.extend([source_line, ""])
    parts.extend(cleaned)
    md = "\n".join(parts).strip() + "\n"
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        md = md.replace(a, b)
    path.write_text(md, encoding="utf-8")
    print("formatted", path.name)


def main() -> None:
    import sys

    targets = [Path(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else None
    paths = targets if targets else sorted(ROOT.glob("*.md"))
    for path in paths:
        if path.name in SKIP_FILES:
            continue
        if not path.is_absolute():
            path = ROOT / path.name
        format_file(path)

    if targets:
        return

    idx = ROOT / "INDEX.md"
    if idx.exists():
        t = idx.read_text(encoding="utf-8")
        t = t.replace(
            "- [ ] Format (headings, JackPoint comments, tables; strip leftover headers)",
            "- [x] Format (headings, JackPoint comments, tables; strip leftover headers)",
        )
        # if already marked x from prior pass, fine
        idx.write_text(t.replace("\u2014", "-").replace("—", "-"), encoding="utf-8")
        print("updated INDEX.md")


if __name__ == "__main__":
    main()
