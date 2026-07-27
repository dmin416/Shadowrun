# -*- coding: utf-8 -*-
"""Deeper perfection audit for COMPLETED claims."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")


def qualities_coverage() -> None:
    print("=== QUALITIES COVERAGE ===")
    t = (ROOT / "Mechanics/Character Creation/Qualities.md").read_text(encoding="utf-8")
    # Core SR5 positive qualities (common list)
    positives = [
        "Ambidextrous",
        "Analytical Mind",
        "Aptitude",
        "Astral Chameleon",
        "Bilingual",
        "Blandness",
        "Catlike",
        "Codeslinger",
        "Double Jointed",
        "Exceptional Attribute",
        "First Impression",
        "Focused Concentration",
        "Gearhead",
        "Guts",
        "High Pain Tolerance",
        "Home Ground",
        "Human-Looking",
        "Indomitable",
        "Juryrigger",
        "Lucky",
        "Magical Resistance",
        "Mentor Spirit",
        "Natural Athlete",
        "Natural Hardening",
        "Natural Immunity",
        "Photographic Memory",
        "Quick Healer",
        "Resistance to Pathogens",
        "Spirit Affinity",
        "Toughness",
        "Will to Live",
    ]
    negatives = [
        "Addiction",
        "Allergy",
        "Astral Beacon",
        "Bad Luck",
        "Bad Rep",
        "Code of Honor",
        "Codeblock",
        "Combat Paralysis",
        "Dependents",
        "Distinctive Style",
        "Elf Poser",
        "Gremlins",
        "Incompetent",
        "Insomnia",
        "Loss of Confidence",
        "Ork Poser",
        "Prejudiced",
        "Scorched",
        "Sensitive System",
        "Simsense Vertigo",
        "SINner",
        "Social Stress",
        "Spirit Bane",
        "Uncouth",
        "Uneducated",
        "Unsteady Hands",
        "Weak Immune System",
    ]
    # Magician/Adept are Priority grants not qualities in SR5 Core qualities chapter
    # Blind is not a separate Core quality (Impaired Sense / etc.)
    pm = [q for q in positives if q.lower() not in t.lower()]
    nm = [q for q in negatives if q.lower() not in t.lower()]
    print("missing positives:", pm or "none")
    print("missing negatives:", nm or "none")
    # how many ### headings under qualities
    heads = re.findall(r"^### (.+)$", t, re.M)
    print("### headings:", len(heads), heads[:5], "...")


def action_economy() -> None:
    print("\n=== ACTION ECONOMY ===")
    t = (ROOT / "Mechanics/Combat/Action Economy.md").read_text(encoding="utf-8")
    must = [
        "Free Actions",
        "Simple Actions",
        "Complex Actions",
        "Interrupt",
        "Call a Shot",
        "Fire Weapon",
        "Reload",
        "Sprint",
        "Observe in Detail",
        "Drop Object",
        "Drop Prone",
        "Speak",
    ]
    for m in must:
        print(f"  {m}: {'yes' if m.lower() in t.lower() else 'MISSING'}")
    # count listed actions roughly
    bullets = len(re.findall(r"^\| [^|]+\|", t, re.M))
    print(f"  table rows~{bullets}")


def field_block_counts() -> None:
    print("\n=== FIELD-BLOCK CATALOGS ===")
    for rel in [
        "Encyclopedia/Rigger Gear.md",
        "Encyclopedia/Magical Goods.md",
        "Encyclopedia/Exotic Weapons.md",
        "Encyclopedia/Drones.md",
        "Encyclopedia/Cyberdecks and Programs.md",
        "Encyclopedia/Nanotech and Geneware.md",
        "Encyclopedia/Commlinks and Electronics.md",
        "Encyclopedia/Medical Gear.md",
    ]:
        t = (ROOT / rel).read_text(encoding="utf-8")
        # patterns: **Name** or ### Name or lines starting with Cat:
        cats = len(re.findall(r"^Cat\s*\|", t, re.M))
        cat_field = len(re.findall(r"^\| Cat \|", t, re.M))
        # entry headers like ### or #### under Catalog
        h3 = len(re.findall(r"^### ", t, re.M))
        h4 = len(re.findall(r"^#### ", t, re.M))
        # SKU lines with Avail
        avail = len(re.findall(r"Avail", t))
        # block pattern: **Something** followed soon by Src
        blocks = len(re.findall(r"(?m)^\*\*[^*]+\*\*\s*$", t))
        print(
            f"{rel:45} h3={h3:3} h4={h4:3} bold_heads={blocks:3} Avail_mentions={avail:3}"
        )


def unverified_scan() -> None:
    print("\n=== UNVERIFIED / CONFLICT CALLOUTS ===")
    root = ROOT / "Encyclopedia"
    for p in sorted(root.glob("*.md")):
        if p.name == "INDEX.md":
            continue
        t = p.read_text(encoding="utf-8")
        hits = []
        for pat in [
            r"UNVERIFIED[^\n]{0,80}",
            r"unverified[^\n]{0,80}",
            r"print conflict[^\n]{0,80}",
            r"no local PDF[^\n]{0,80}",
            r"DEFERRED[^\n]{0,60}",
            r"deferred[^\n]{0,60}",
        ]:
            for m in re.finditer(pat, t, re.I):
                hits.append(m.group(0)[:90])
        if hits:
            print(f"\n{p.name} ({len(hits)}):")
            for h in hits[:6]:
                print(f"  - {h}")
            if len(hits) > 6:
                print(f"  ... +{len(hits)-6}")


def combat_pages_claim() -> None:
    print("\n=== COMBAT PAGES MUST-INCLUDE ===")
    for rel in [
        "Mechanics/Combat/Overview.md",
        "Mechanics/Combat/Initiative.md",
        "Mechanics/Combat/Action Economy.md",
    ]:
        t = (ROOT / rel).read_text(encoding="utf-8")
        inv = re.search(r"(?s)## Inventory.*?\n---", t)
        block = inv.group(0) if inv else ""
        open_x = block.count("- [ ]")
        done_x = block.count("- [x]")
        print(f"{rel}: inventory [x]={done_x} [ ]={open_x}")


def chargen_inventories() -> None:
    print("\n=== CHARGEN INVENTORY OPEN BOXES ===")
    d = ROOT / "Mechanics/Character Creation"
    for p in sorted(d.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        inv = re.search(r"(?s)## Inventory.*?(?:\n---|\n## )", t)
        block = inv.group(0) if inv else t[:800]
        open_x = len(re.findall(r"- \[ \]", block))
        done_x = len(re.findall(r"- \[x\]", block))
        status = "OK" if open_x == 0 else "OPEN"
        print(f"{p.name:35} [x]={done_x:2} [ ]={open_x:2} {status}")


def source_done_reports() -> None:
    print("\n=== DONE REPORT ARTIFACTS ===")
    for rel in [
        "Source/_extract/rng_chapter_check_report.md",
        "Source/_extract/qa_six_books.py",
        "Source/_extract/seattle_loss_check.md",
    ]:
        p = ROOT / rel
        print(f"{rel}: {'exists' if p.exists() else 'MISSING'}")


def melee_firearms_sanity() -> None:
    print("\n=== WEAPON CATALOG SANITY ===")
    for rel, names in [
        (
            "Encyclopedia/Melee Weapons.md",
            ["Katana", "Combat Knife", "Club", "Sword", "Shock Glove", "Monofilament Whip"],
        ),
        (
            "Encyclopedia/Firearms.md",
            ["Ares Predator", "AK-97", "Remington", "Ingram", "Panther", "Yamaha"],
        ),
        (
            "Encyclopedia/Vehicles.md",
            ["Honda", "Ford", "Eurocar", "Harley", "GMC"],
        ),
    ]:
        t = (ROOT / rel).read_text(encoding="utf-8")
        miss = [n for n in names if n.lower() not in t.lower()]
        print(f"{rel}: miss={miss or 'none'}")


if __name__ == "__main__":
    qualities_coverage()
    action_economy()
    field_block_counts()
    unverified_scan()
    combat_pages_claim()
    chargen_inventories()
    source_done_reports()
    melee_firearms_sanity()
