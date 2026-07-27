# -*- coding: utf-8 -*-
"""Audit COMPLETED.md claims for actual substance."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")


def enc_audit() -> None:
    print("=== ENCYCLOPEDIA ===")
    root = ROOT / "Encyclopedia"
    files = [
        "Melee Weapons.md",
        "Projectile Weapons.md",
        "Firearms.md",
        "Exotic Weapons.md",
        "Weapon Accessories.md",
        "Ammunition.md",
        "Grenades and Explosives.md",
        "Armor and Clothing.md",
        "Armor Modifications.md",
        "Cyberware.md",
        "Bioware.md",
        "Nanotech and Geneware.md",
        "Commlinks and Electronics.md",
        "Cyberdecks and Programs.md",
        "Rigger Gear.md",
        "Sensors and Optics.md",
        "Medical Gear.md",
        "Drugs Toxins and Chemicals.md",
        "Magical Goods.md",
        "Vehicles.md",
        "Drones.md",
        "Vehicle and Drone Modifications.md",
        "Identity and Documentation.md",
        "Lifestyles and Safehouses.md",
        "Tools Kits and Survival.md",
        "Security and Surveillance.md",
        "INDEX.md",
    ]
    for f in files:
        p = root / f
        if not p.exists():
            print(f"MISSING {f}")
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        lines = t.count("\n") + 1
        flags = []
        low = t.lower()
        if lines < 40:
            flags.append("SHORT")
        if "to be filled" in low or "not yet filled" in low or "stub" in low[:500]:
            flags.append("STUB_LANG")
        unchecked = t.count("- [ ]")
        if unchecked:
            flags.append(f"open_todos={unchecked}")
        ver = bool(re.search(r"verified from|^\*\*Verified", t, re.I | re.M))
        # UNVERIFIED / conflict callouts
        unver = len(re.findall(r"UNVERIFIED|unverified|print conflict|CONFLICT", t))
        rows = sum(
            1
            for L in t.splitlines()
            if L.startswith("|") and "---" not in L and not L.lower().startswith("| stat")
        )
        # empty catalog smell: few pipes
        if rows < 5 and f != "INDEX.md":
            flags.append("FEW_TABLE_ROWS")
        flag_s = ",".join(flags) if flags else "OK"
        print(
            f"{f:42} L={lines:5} rows~{rows:4} ver={ver} flags={unver} {flag_s}"
        )


def mech_audit() -> None:
    print("\n=== MECHANICS ===")
    root = ROOT / "Mechanics"
    paths = [
        "Dice and Tests.md",
        "Edge.md",
        "Character Creation/Overview.md",
        "Character Creation/Priority System.md",
        "Character Creation/Metatype.md",
        "Character Creation/Attributes.md",
        "Character Creation/Magic and Resonance.md",
        "Character Creation/Skills.md",
        "Character Creation/Resources and Gear.md",
        "Character Creation/Qualities.md",
        "Character Creation/Contacts.md",
        "Character Creation/Finishing Touches.md",
        "Combat/Overview.md",
        "Combat/Initiative.md",
        "Combat/Action Economy.md",
    ]
    for f in paths:
        p = root / f
        t = p.read_text(encoding="utf-8", errors="replace")
        lines = t.count("\n") + 1
        flags = []
        low = t.lower()
        open_boxes = t.count("- [ ]")
        if open_boxes:
            flags.append(f"open_check={open_boxes}")
        if lines < 50:
            flags.append("SHORT")
        if "must-include" in low and open_boxes:
            flags.append("INCOMPLETE_CHECKLIST")
        if "outline" in low and "only" in low:
            flags.append("OUTLINE")
        if "TODO" in t:
            flags.append("TODO")
        # inventory/schema presence (done-file convention)
        has_inv = "Inventory" in t or "## Inventory" in t
        has_schema = "Schema" in t or "## Schema" in t
        has_table = "|---" in t or "| ---" in t
        meta = []
        if has_inv:
            meta.append("inv")
        if has_schema:
            meta.append("schema")
        if has_table:
            meta.append("tables")
        # content density: non-empty lines
        nonempty = sum(1 for L in t.splitlines() if L.strip())
        flag_s = ",".join(flags) if flags else "OK"
        print(
            f"{f:48} L={lines:5} nonempty={nonempty:4} [{'|'.join(meta)}] {flag_s}"
        )


def source_audit() -> None:
    print("\n=== SOURCE TEXTS ===")
    books = [
        ("Run and Gun", 14),
        ("Rigger 5", 15),
        ("Street Grimoire", 14),
        ("Forbidden Arcana", 12),
        ("Run Faster", 15),
        ("Street Lethal", 10),
        ("Howling Shadows", 17),
        ("Serrated Edge", 16),
    ]
    for name, expect in books:
        d = ROOT / "Source Texts" / name
        idx = d / "INDEX.md"
        chapters = sorted(d.glob("*.md"))
        chapters = [c for c in chapters if c.name != "INDEX.md"]
        # exclude 00 briefs from count optionally
        thin = []
        emptyish = []
        for c in chapters:
            t = c.read_text(encoding="utf-8", errors="replace")
            lines = t.count("\n") + 1
            chars = len(re.sub(r"\s+", "", t))
            if lines < 20 or chars < 500:
                thin.append(f"{c.name}(L={lines},c={chars})")
            if chars < 100:
                emptyish.append(c.name)
        idx_t = idx.read_text(encoding="utf-8") if idx.exists() else ""
        pipe = {
            "extract": "[x] Extract" in idx_t or "- [x] Extract" in idx_t,
            "format": "[x] Format" in idx_t,
            "loss": "[x] Loss-check" in idx_t,
            "done": "[x] Done-check" in idx_t,
        }
        if name == "Serrated Edge":
            pipe = {
                "extract": "[x] Extract" in idx_t,
                "format": "[x] Formatting" in idx_t or "[x] Format" in idx_t,
                "loss": "N/A",
                "done": "[x] Gear/stat audit" in idx_t or "[x] GM adventure" in idx_t,
            }
        print(
            f"{name:20} chapters={len(chapters)} expect~{expect} "
            f"pipe={pipe} thin={len(thin)} empty={len(emptyish)}"
        )
        for x in thin[:8]:
            print(f"  THIN: {x}")
        if len(thin) > 8:
            print(f"  ... +{len(thin)-8} more thin")


def spot_mech_quality_names() -> None:
    """Qualities.md should list many Core qualities."""
    print("\n=== QUALITIES SPOT ===")
    p = ROOT / "Mechanics/Character Creation/Qualities.md"
    t = p.read_text(encoding="utf-8")
    # common Core positives/negatives
    samples = [
        "Ambidextrous",
        "Analytical Mind",
        "Aptitude",
        "Bilingual",
        "Exceptional Attribute",
        "Lucky",
        "Magician",
        "Addiction",
        "Allergy",
        "Astral Beacon",
        "Bad Luck",
        "Blind",
        "Code of Honor",
        "Dependents",
        "Elf Poser",
        "Gremlins",
        "Incompetent",
        "SINner",
    ]
    miss = [s for s in samples if s.lower() not in t.lower()]
    print(f"sample qualities missing: {miss or 'none'}")
    print(f"file lines={t.count(chr(10))+1}")


def spot_priority_table() -> None:
    print("\n=== PRIORITY SPOT ===")
    p = ROOT / "Mechanics/Character Creation/Priority System.md"
    t = p.read_text(encoding="utf-8")
    for s in ["Priority", "Metatype", "Attributes", "Magic", "Skills", "Resources", "Technomancer", "Adept"]:
        print(f"  {s}: {'yes' if s.lower() in t.lower() else 'NO'}")


if __name__ == "__main__":
    enc_audit()
    mech_audit()
    source_audit()
    spot_mech_quality_names()
    spot_priority_table()
