"""Audit Firearms.md completeness against Core / RnG / SL extracts."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
ENCY = (ROOT / "Encyclopedia" / "Firearms.md").read_text(encoding="utf-8")


def ency_names() -> list[str]:
    out = []
    for line in ENCY.splitlines():
        if line.startswith("|") and any(
            s in line for s in ("| Core |", "| RnG |", "| SL |", "| SL-CorpSec |")
        ):
            out.append(line.split("|")[1].strip())
    return out


def normalize(s: str) -> str:
    s = s.lower()
    s = s.replace("“", '"').replace("”", '"').replace("’", "'")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    # drop leading brand noise variants
    for prefix in ("the ",):
        if s.startswith(prefix):
            s = s[len(prefix) :]
    return s


def found(target: str, hay: list[str]) -> bool:
    t = normalize(target)
    # strip parenthetical config suffixes for fuzzy
    t_base = re.sub(r"\s*\(.*$", "", t).strip()
    for h in hay:
        hn = normalize(h)
        if t in hn or hn in t or t_base in hn or hn in t_base:
            return True
        # token overlap for close names
        tt, hh = set(t.split()), set(hn.split())
        if len(tt) >= 2 and tt.issubset(hh):
            return True
    return False


# --- Core ---
core = (ROOT / "Source Texts/Shadowrun Fifth Edition Core Rulebook/21 - Street Gear.md").read_text(
    encoding="utf-8"
)
sec = core[core.find("### Firearms") : core.find("### Firearm Accessories")]
core_bold = [m for m in re.findall(r"\*\*([^*]+):\*\*", sec) if m != "Wireless"]
core_table = []
for line in sec.splitlines():
    if not line.startswith("| "):
        continue
    name = line.split("|")[1].strip()
    if name in {
        "Tasers",
        "Hold-Outs",
        "Light Pistols",
        "Heavy Pistols",
        "Machine Pistols",
        "Submachine Guns",
        "Assault Rifles",
        "Sniper Rifles",
        "Shotguns",
        "Special Weapons",
        "Machine Guns",
        "Cannons/Launchers",
        "Grenade Launcher",
        "w/ flechettes",
        "Acc",
        "---",
    }:
        continue
    if name.startswith("-") or name == "Acc":
        continue
    core_table.append(name)

# --- RnG chapter (taser through flamethrower) ---
rng = (ROOT / "Source/_extract/rng_firearms.txt").read_text(encoding="utf-8")
# start at TASERS page content
rng_start = rng.find("===== PAGE 29 =====")
rng_end = rng.find("WEAPON ACCESSORIES")
rng_sec = rng[rng_start:rng_end] if rng_start >= 0 else rng
rng_names = []
lines = rng_sec.splitlines()
for i, line in enumerate(lines):
    if re.match(r"^ACC\b", line.strip()):
        parts = []
        j = i - 1
        while j >= 0:
            s = lines[j].strip()
            if not s or s.startswith(">") or s.startswith("Standard") or s.startswith(">>") or s.startswith("<<"):
                break
            if "PAGE" in s or "ARSENAL" in s or s.startswith("Note:") or s.startswith("The ") or s.startswith("When "):
                break
            upperish = sum(c.isupper() for c in s) >= max(1, sum(c.islower() for c in s))
            if upperish and len(s) > 2 and "¥" not in s:
                parts.insert(0, s)
                j -= 1
            else:
                break
        if parts:
            rng_names.append(" ".join(parts))

# RnG secondary configs from tables
rng_secondary = [
    "AK-98 Grenade Launcher",
    "HK XM30 Carbine",
    "HK XM30 Sniper",
    "HK XM30 LMG",
    "HK XM30 Shotgun",
    "HK XM30 Grenade Launcher",
    "Nitama Optimum II Shotgun",
    "Ares Alpha Grenade Launcher",
]

# --- SL summary table weapons ---
sl = (ROOT / "Source/_extract/sl_firearms.txt").read_text(encoding="utf-8")
# RANGED WEAPONS summary block
m = re.search(r"RANGED WEAPONS\nWEAPON ACC DAM.*?\n(.*?)=====", sl, re.S)
sl_summary = []
if m:
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("*") or line.startswith("POSTED"):
            continue
        # name is everything before first digit-ish stat - crude: split on multiple spaces hard
        # lines look like: Winchester Airbow 5 10P –2 SS — 1(ml) 10R 800¥
        # Take leading alpha words until a lone digit
        toks = line.split()
        name_toks = []
        for t in toks:
            if re.match(r"^\d", t) or t in {"As", "as"} and name_toks:
                # careful: "Narcoject One" ok; "As toxin" starts damage
                if t.lower() in {"as"} or re.match(r"^\d", t):
                    break
            if t.startswith("*"):
                break
            name_toks.append(t)
        if name_toks:
            sl_summary.append(" ".join(name_toks))

# SL paren-style chapter headings
sl_paren = re.findall(
    r"^([A-Z0-9][A-Z0-9 /'\-\.]+)\(([A-Za-z /]+)\)\s*$",
    sl,
    re.M,
)
sl_firearm_paren = []
keep_cats = (
    "PISTOL",
    "TASER",
    "SMG",
    "RIFLE",
    "SHOT",
    "MACHINE",
    "LAUNCH",
    "CARBINE",
    "GUN",
    "CANNON",
    "WEAPON",
    "HOLD",
)
for name, cat in sl_paren:
    cu = cat.upper()
    if any(k in cu for k in keep_cats) and "BLADE" not in cu and "CLUB" not in cu and "BOW" not in cu:
        sl_firearm_paren.append(f"{name.strip()} ({cat.strip()})")

# CorpSec
corp = (ROOT / "Source/_extract/sl_corpsec_arsenal.txt").read_text(encoding="utf-8")
corp_guns = [
    "Defense-Com Hold Out Pistol",
    "Defense-Com Taser",
    'Remington 995 "Buzzsaw"',
    "Stoner-Ares M-22A1",
    "Ingram Supermach 200",
    "Nemesis Arms Man Catcher",
    "Man-Catcher ammo",
    "ArmTech PTL-02",
    "HEAP Torpedo",
    "Depth Charge Torpedo",
]

hay = ency_names()
print(f"ENCY rows: {len(hay)}")

def report(label: str, expected: list[str]) -> list[str]:
    missing = [e for e in expected if not found(e, hay)]
    print(f"\n=== {label}: {len(expected)} expected, {len(missing)} missing ===")
    for m in missing:
        print(f"  MISSING: {m}")
    return missing


miss = []
miss += report("Core bold", core_bold)
miss += report("Core table", core_table)
miss += report("RnG chapter", rng_names)
miss += report("RnG secondary", rng_secondary)
miss += report("SL paren firearms", sl_firearm_paren)
miss += report("SL summary (all ranged in table)", sl_summary)
miss += report("CorpSec guns", corp_guns)

# Projectile-only in SL summary should be missing intentionally
print("\n=== intentional non-firearm in SL summary (Airbow etc.) ===")
for s in sl_summary:
    if "airbow" in normalize(s) or "trollbow" in normalize(s):
        print(" ", s, "-> firearm file?", found(s, hay))

print(f"\nTotal missing reports (with dupes): {len(miss)}")
unique = []
for m in miss:
    if not any(normalize(m) == normalize(u) for u in unique):
        unique.append(m)
print(f"Unique missing: {len(unique)}")
for u in unique:
    print(" *", u)
