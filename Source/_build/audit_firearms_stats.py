"""Compare Firearms.md catalog stats against Core / RnG / SL source tables."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
ENCY = (ROOT / "Encyclopedia" / "Firearms.md").read_text(encoding="utf-8")


def norm_num(s: str) -> str:
    s = s.strip()
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = s.replace(" ", "")
    s = s.replace("¥", "")
    s = s.replace(",", "")
    s = s.lower()
    # unify dashes for none
    if s in {"-", "--", "—", "–", ""}:
        return "-"
    return s


def parse_ency_rows():
    rows = []
    for line in ENCY.splitlines():
        if not line.startswith("|"):
            continue
        if "| Core |" not in line and "| RnG |" not in line and "| SL |" not in line and "| SL-CorpSec |" not in line:
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 12:
            continue
        # Name Src Skill Acc DV AP Mode RC Ammo Avail Cost Rules
        rows.append(
            {
                "name": parts[0],
                "src": parts[1],
                "skill": parts[2],
                "acc": parts[3],
                "dv": parts[4],
                "ap": parts[5],
                "mode": parts[6],
                "rc": parts[7],
                "ammo": parts[8],
                "avail": parts[9],
                "cost": parts[10],
                "rules": parts[11] if len(parts) > 11 else "",
                "raw": line,
            }
        )
    return rows


def find_ency(name_sub: str, rows):
    ns = name_sub.lower()
    hits = [r for r in rows if ns in r["name"].lower()]
    return hits


# Parse Core markdown tables in Firearms section
core = (ROOT / "Source Texts/Shadowrun Fifth Edition Core Rulebook/21 - Street Gear.md").read_text(
    encoding="utf-8"
)
sec = core[core.find("### Firearms") : core.find("### Firearm Accessories")]
core_rows = []
for line in sec.splitlines():
    if not line.startswith("| ") or line.startswith("| ---") or "Acc |" in line or line.startswith("| Tasers") or line.startswith("| Hold") or line.startswith("| Light") or line.startswith("| Heavy") or line.startswith("| Machine") or line.startswith("| Submachine") or line.startswith("| Assault") or line.startswith("| Sniper") or line.startswith("| Shotguns") or line.startswith("| Special") or line.startswith("| Cannons"):
        continue
    parts = [p.strip() for p in line.strip("|").split("|")]
    if len(parts) < 8:
        continue
    name = parts[0]
    if name in {"Grenade Launcher", "w/ flechettes"} or name.startswith("w/"):
        # keep grenade launcher under Alpha separately
        if name == "Grenade Launcher":
            core_rows.append(
                {
                    "name": "Ares Alpha (grenade launcher)",
                    "acc": parts[1],
                    "dv": parts[2],
                    "ap": parts[3],
                    "mode": parts[4],
                    "rc": parts[5],
                    "ammo": parts[6],
                    "avail": parts[7],
                    "cost": parts[8] if len(parts) > 8 else "-",
                }
            )
        continue
    core_rows.append(
        {
            "name": name,
            "acc": parts[1],
            "dv": parts[2],
            "ap": parts[3],
            "mode": parts[4],
            "rc": parts[5],
            "ammo": parts[6],
            "avail": parts[7],
            "cost": parts[8] if len(parts) > 8 else "-",
        }
    )

ency = parse_ency_rows()
print(f"Ency {len(ency)} Core-source-table {len(core_rows)}")

mismatches = []
missing = []
for cr in core_rows:
    hits = find_ency(cr["name"].split("(")[0].strip(), ency)
    # prefer exact-ish
    hit = None
    for h in hits:
        if cr["name"].lower() in h["name"].lower() or h["name"].lower().startswith(cr["name"].lower().split()[0].lower()):
            # better match
            if norm_num(cr["name"]) == norm_num(h["name"]) or cr["name"].lower() in h["name"].lower():
                hit = h
                break
    if not hit:
        # try exact name match
        for h in ency:
            if h["name"].lower() == cr["name"].lower():
                hit = h
                break
    if not hit:
        # special Alpha GL
        if "grenade" in cr["name"].lower():
            hits = [h for h in ency if "alpha" in h["name"].lower() and "grenade" in h["name"].lower()]
            hit = hits[0] if hits else None
    if not hit:
        missing.append(cr["name"])
        continue
    fields = ["acc", "dv", "ap", "mode", "rc", "ammo", "avail", "cost"]
    diffs = []
    for f in fields:
        a, b = norm_num(cr[f]), norm_num(hit[f])
        # normalize mode separators
        if f == "mode":
            a = a.replace("/", "").replace(" ", "")
            b = b.replace("/", "").replace(" ", "")
        if f == "ammo":
            a = a.replace(" ", "")
            b = b.replace(" ", "")
        if a != b:
            # allow yen symbol already stripped; allow (e) variants
            diffs.append(f"{f}: src={cr[f]!r} ency={hit[f]!r}")
    if diffs:
        mismatches.append((cr["name"], hit["name"], diffs))

print("\nCORE missing in ency:", missing)
print(f"CORE stat mismatches: {len(mismatches)}")
for name, ename, diffs in mismatches:
    print(f"  {name} -> {ename}")
    for d in diffs:
        print(f"     {d}")

# List all ency Core names for Alpha GL presence
print("\nAlpha-related ency rows:")
for h in ency:
    if "alpha" in h["name"].lower():
        print(" ", h["name"], h["acc"], h["dv"], h["ammo"], h["avail"], h["cost"])

# HL-13 configs
print("\nHL-13-related:")
for h in ency:
    if "hl-13" in h["name"].lower() or "hl13" in h["name"].lower():
        print(" ", h["name"], h["acc"], h["dv"], h["mode"], h["ammo"])

# Beretta / Northstar / Vogel / Pup
print("\nKey SL names:")
for key in ("northstar", "pup", "vogel", "whammy", "happiness", "stalwart", "artemis", "frontier", "enforcer", "boom", "tingler", "sting", "ghost", "coral", "gemini", "praetorian", "infiltrator", "flash", "tsunami", "s-3k", "m23a2", "trackstopper", "pep", "gas gun"):
    hits = [h["name"] for h in ency if key in h["name"].lower()]
    print(f"  {key}: {hits or 'NONE'}")

# Rules emptiness
empty_rules = [h["name"] for h in ency if not h["rules"].strip() or h["rules"].strip() == "-"]
print(f"\nEmpty Rules cells: {len(empty_rules)}")
for n in empty_rules:
    print(" ", n)

# Secondary rows with Avail/Cost dash that are OK
print(f"\nTotal ency: {len(ency)}")
