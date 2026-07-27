# -*- coding: utf-8 -*-
"""Kill Code deep landmark sweep (RnG-style)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
MD_DIR = ROOT / "Source Texts" / "Kill Code"
OUT = ROOT / "Source" / "_extract" / "killcode_landmark_report.md"

# landmarks that MUST appear (case-insensitive substring)
LANDMARKS = {
    1: [
        "Kill Code Credits",
        "Writing: Addie Gia",
        "Introduction",
        "Double Decker",
        "So You Want To Be A Hacker",
        "Rule Index",
        "2018 The Topps Company",
    ],
    2: [
        "The Matrix is not a place",
        "So You Want to Be a Hacker",
        "Dips and Chips",
        "Null Sign",
        "Core of Consciousness",
    ],
    3: [
        "By TJ Lachlan",
        "headman's axe",
        "Moharik",
        "Melanie Cotton",
        "Augustus Charles Ames",
        "Coriolis",
        "BuildSec",
        "Mashalla",
        "dissonant cyberzombie",  # wait that's ch7 - remove
        "NeoNET",
        "monster's smile",
    ],
    4: [
        "Draconic Networking",
        "Terasca",
        "Jolene Price",
        "Echo Mirage",
        "Psychotrope",
        "Reckless Hacking",
        "Calibration",
        "Denial Of Service",
        "I Am The Firewall",
        "Haywire",
        "Intervene",
        "Masquerade",
        "Popup",
        "Squelch",
        "Subvert Infrastructure",
        "Tag",
        "Watchdog",
        "Foundation Hosts",
        "Industry Hosts",
        "Destination Hosts",
        "Nested Hosts",
        "Outdated Hosts",
        "Offline Hosts",
        "Rogue Hosts",
        "Patrol IC",
        "One Hundred",
    ],
    5: [
        "Estaban",
        "Zapper Rounds",
        "Looper Rounds",
        "Fuzzy Rounds",
        "E0-E0",
        "ArrowLink",
        "Boom Boom Bunnies",
        "CoS",
        "Douser",
        "DumDum",
        "Faceless",
        "Booster Cloud",
        "Multiprogram",
        "Booster Chip",
        "Trode Patch",
        "Fuchi Cyber-N",
        "Cyber-Ex",
        "Shadow Warrior",
        "Evo Sublime",
        "Destiny Blade",
        "Aztechnology Defender",
        "Kitbashed Sleeper",
        "Cry Wolf",
        "Datajack Plus",
        "EARRS",
        "Cranial Shield",
        "MCT BioLink",
        "Flicker",
        "Sleuther",
        "Blue Goo",
        "Cyber-6",
        "Skirmisher",
        "Horizon Flow",
        "Last Chance",
        "Co-Pilot",
        "Door Gunner",
        "ECM-Warrior",
        "Mercury-Alpha",
        "Picador",
    ],
    6: [
        "Deck Builder",
        "Impenetrable Logic",
        "Rootkit",
        "Silence Is Golden",
        "aVRse",
        "Basement Dweller",
        "Buddy System",
        "Down the Rabbit Hole",
        "Echo Chamber",
        "Frostbite",
        "Information Auctioneer",
        "Lazy Fingers",
        "Well, Actually",
        "Bootstrap Cliché",
        "Hacking Savant",
        "Ath133t",
        "Techno-Rigger",
    ],
    7: [
        "By Amy Veeres",
        "Respec",
        "Netcat",
        "Makoto Shiranui",
        "code gold",
        "dissonant cyberzombie",
        "morkhan",
        "dozen children",
    ],
    8: [
        "Clockwork",
        "Sourcerer",
        "Technoshaman",
        "Machinist",
        "Cyberadept",
        "Overdrive",
        "LOTO",
        "Hyperthreading",
        "Sprite Pet",
        "Sourceror",
    ],
    9: [
        "Arc Feedback",
        "Bootleg Program",
        "Host Emulator",
        "Mirrored Persona",
        "Weaken Encryption",
        "Better on the Net",
        "Natural Hacker",
        "Brittle",
        "Companion Sprite",
        "Generalist Sprite",
        "Active Analytics",
        "Aegis",
        "Communion",
        "01 (The World Tree)",
        "Shooter",
    ],
    10: [
        "Virtual Tribe",
        "Strictures",
        "Attendance",
        "Infosharing",
        "Replanting the Tree",
        "Summer_Knights",
        "TechnoRiggers",
        "Resonant Church",
        "Flash Tribes",
    ],
    11: [
        "Hunting Technomancers",
        "Trace Icon",
        "Deckers",
        "Riggers",
        "Enemy Profiles",
        "Dissonants",
        "Corporates",
    ],
    12: [
        "Tombstones",
        "Kernel Panic",
        "The Factory",
        "Out of Band",
        "Human Malice",
        "Morphinae",
        "Apophenians",
        "Erisians",
        "Forced Heuristics",
        "Causal Nexus",
        "Dissonance Spike",
    ],
    13: [
        "Null Sect",
        "What Do They Want",
        "How They Operate",
        "Who They Are",
        "Where They Are",
        "How Do We Fight Back",
        "Hitsec Burn",
    ],
    14: [
        "Pistons",
        "GOD (Usually)",
        "Protosapients",
        "Known Universe",
        "SINtax Lair",
        "Kingdom of Velkar",
        "Mitsuhama",
        "Wuxing",
    ],
    15: [
        "Yogi",
        "Pachyderms",
        "Testudines",
        "Gef",
        "iPodo",
        "Energizer",
        "G33k0s",
        "Rybbyts",
        "Techworms",
        "Dot-Camel",
        "E-Fish",
        "Ravagers",
        "Migaloo",
        "Power Mungers",
        "Sense Eaters",
        "Glitches",
        "SIN Eaters",
        "Noisestorm",
        "Black-Off",
        "Red Spread",
        "Un-Grey-tful",
        "Clear-Out",
        "Overseers",
        "Ax S. Grant",
        "Hitsec Burn",
        "Derrick Owen Slattery",
    ],
    16: [
        "Complex Forms",
        "Echoes",
        "Qualities",
        "Sprites",
        "Paragons",
        "Cyberdecks",
        "Virtual Tribes",
    ],
}

FILES = {
    1: "01 - Contents and Credits.md",
    2: "02 - Introduction.md",
    3: "03 - Double Decker.md",
    4: "04 - So You Want To Be A Hacker.md",
    5: "05 - Dips & Chips.md",
    6: "06 - Disk Jockeys & Lightstream Riders.md",
    7: "07 - Parallel Processing.md",
    8: "08 - Data Streams.md",
    9: "09 - In the Flow.md",
    10: "10 - A Million Icons Bloom.md",
    11: "11 - Diving Under.md",
    12: "12 - Infinite Realms.md",
    13: "13 - Null Sign.md",
    14: "14 - Into the Wild.md",
    15: "15 - The Core of Consciousness.md",
    16: "16 - Rule Index.md",
}

# fix landmark mistake for ch3
LANDMARKS[3] = [x for x in LANDMARKS[3] if "cyberzombie" not in x.lower()]


def main() -> None:
    lines = ["# Kill Code landmark sweep\n\n"]
    lines.append("| # | File | Missing landmarks | Em | Verdict |\n|---|---|---|---|---|\n")
    detail = []
    for num, fname in FILES.items():
        path = MD_DIR / fname
        text = path.read_text(encoding="utf-8")
        low = text.lower()
        miss = [lm for lm in LANDMARKS[num] if lm.lower() not in low]
        em = text.count("\u2014") + text.count("\u2013") + text.count("\u2026")
        # also flag ASCII en-dash lookalikes used as em? skip
        verdict = "PASS" if not miss and em == 0 else ("FIX landmarks" if miss else "FIX em")
        lines.append(
            f"| {num:02d} | {fname} | {len(miss)} | {em} | {verdict} |\n"
        )
        if miss:
            detail.append(f"\n## Ch{num:02d} missing\n")
            for m in miss:
                detail.append(f"- `{m}`\n")

    # Extra targeted checks
    detail.append("\n## Targeted spot checks\n")
    checks = [
        (4, "Denial Of Service", "Cybercombat + Logic"),
        (4, "Denial Of Service", "Computer + Intuition"),
        (4, "Patrol IC", "every 10 points of Overwatch"),
        (5, "Cry Wolf", "Cry Wolf"),
        (6, "Rootkit", "device rating"),
        (8, "LOTO", "LOTO"),
        (15, "Power Munger", "W"),
        (16, "aVRse", "aVRse"),
    ]
    for num, section, needle in checks:
        text = (MD_DIR / FILES[num]).read_text(encoding="utf-8")
        ok = needle.lower() in text.lower()
        detail.append(f"- Ch{num:02d} `{needle}` near {section}: {'OK' if ok else 'MISS'}\n")

    # JackPoint attribution sanity: orphan handles (handle with empty following?)
    detail.append("\n## JackPoint structure issues\n")
    for num in (4, 5, 8, 10, 13, 14, 15):
        text = (MD_DIR / FILES[num]).read_text(encoding="utf-8")
        # handle followed by another handle with no body
        bad = re.findall(
            r"(> \*\*[^*]+\*\*\n)(> \*\*[^*]+\*\*)",
            text,
        )
        # handle whose next line is not >
        orphans = []
        blocks = re.split(r"(?=^> \*\*)", text, flags=re.M)
        for b in blocks:
            if not b.startswith("> **"):
                continue
            blines = b.strip().splitlines()
            if len(blines) < 2:
                orphans.append(blines[0][:60])
                continue
            if not blines[1].startswith(">"):
                orphans.append(blines[0][:60] + " (body not quoted)")
        detail.append(
            f"- Ch{num:02d}: consecutive empty JP pairs={len(bad)}; "
            f"orphan/malformed={len(orphans)}"
            + (f" e.g. {orphans[:3]}" if orphans else "")
            + "\n"
        )

    OUT.write_text("".join(lines + detail), encoding="utf-8")
    print(OUT.read_text(encoding="utf-8")[:4000])


if __name__ == "__main__":
    main()
