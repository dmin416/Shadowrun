"""Parse RnG end-of-book firearm tables and compare to Firearms.md."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
ENCY = (ROOT / "Encyclopedia" / "Firearms.md").read_text(encoding="utf-8")
tables = (ROOT / "Source/_extract/rng_tables.txt").read_text(encoding="utf-8")

# Isolate TASERS through FLAMETHROWERS sections in compiled tables
start = tables.find("HOLD-OUT PISTOLS")
# actually start earlier at TASERS if present
t0 = tables.find("\nTASERS\n")
if t0 < 0:
    t0 = tables.find("TASERS\n")
t1 = tables.find("\nAMMO\n")
chunk = tables[t0:t1]

# Parse vertical tables: ITEM ... fields stacked
# Pattern used: ITEM\nACC\nDV\n... then name\nacc\ndv...
# Easier approach: use known field order after each PAGE header section.

def norm(s: str) -> str:
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = re.sub(r"\s+", "", s)
    return s.lower().replace("¥", "").replace(",", "")


def ency_map():
    m = {}
    for line in ENCY.splitlines():
        if not line.startswith("|"):
            continue
        if not any(s in line for s in ("| Core |", "| RnG |", "| SL |", "| SL-CorpSec |")):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 11:
            continue
        m[parts[0]] = {
            "acc": parts[3],
            "dv": parts[4],
            "ap": parts[5],
            "mode": parts[6],
            "rc": parts[7],
            "ammo": parts[8],
            "avail": parts[9],
            "cost": parts[10],
        }
    return m


EM = ency_map()


def find_ency(name: str):
    nl = name.lower()
    # direct
    for k, v in EM.items():
        if k.lower() == nl:
            return k, v
    for k, v in EM.items():
        if nl in k.lower() or k.lower() in nl:
            return k, v
    # token
    tokens = set(re.findall(r"[a-z0-9]+", nl))
    best = None
    best_score = 0
    for k, v in EM.items():
        kt = set(re.findall(r"[a-z0-9]+", k.lower()))
        score = len(tokens & kt)
        if score > best_score and score >= max(2, len(tokens) - 1):
            best_score = score
            best = (k, v)
    return best


# Extract RnG-only items from chapter pages 29-50 names we already have,
# and pull their ACC blocks from rng_firearms.txt

rng = (ROOT / "Source/_extract/rng_firearms.txt").read_text(encoding="utf-8")
# From PAGE 29 to WEAPON ACCESSORIES
sec = rng[rng.find("===== PAGE 29 =====") : rng.find("WEAPON ACCESSORIES")]

# Find each ACC DV AP MODE RC AMMO AVAIL COST block
blocks = []
lines = sec.splitlines()
i = 0
while i < len(lines):
    if lines[i].strip().startswith("ACC") and "DV" in lines[i] and "MODE" in lines[i]:
        # name above
        j = i - 1
        name_parts = []
        while j >= 0:
            s = lines[j].strip()
            if not s or s.startswith(">") or s.startswith("Standard") or s.startswith(">>") or s.startswith("<<") or "ARSENAL" in s or "PAGE" in s:
                break
            if s.startswith("Note") or s.startswith("The ") or s.startswith("When ") or s.startswith("*") or "¥" in s:
                break
            upperish = sum(c.isupper() for c in s) >= max(1, sum(c.islower() for c in s))
            if upperish and len(s) > 2:
                name_parts.insert(0, s)
                j -= 1
            else:
                break
        # next non-empty line(s) until Standard/Note/>/blank section - stats often one line
        k = i + 1
        while k < len(lines) and not lines[k].strip():
            k += 1
        stat_lines = []
        while k < len(lines):
            s = lines[k].strip()
            if not s:
                if stat_lines:
                    break
                k += 1
                continue
            if s.startswith("Standard") or s.startswith("Note") or s.startswith(">") or s.startswith("The ") or s.startswith(">>") or s.startswith("<<") or s.startswith("ACC"):
                break
            # stop if next weapon header all caps and previous stats exist
            if stat_lines and sum(c.isupper() for c in s) > sum(c.islower() for c in s) and not re.search(r"\d", s) and "¥" not in s and len(s) > 3:
                break
            stat_lines.append(s)
            k += 1
            if len(stat_lines) >= 3 and "¥" in "".join(stat_lines):
                # often stats wrap; keep going until yen then maybe stop after
                if "¥" in s:
                    break
        if name_parts and stat_lines:
            blocks.append((" ".join(name_parts), " ".join(stat_lines)))
        i = k
        continue
    i += 1

print(f"Parsed RnG chapter stat blocks: {len(blocks)}")
missing = []
for name, stats in blocks:
    if name in {"ULTIMAX"}:  # Ultimax MMG
        name = "ULTIMAX MMG"
    hit = find_ency(name)
    if not hit:
        missing.append((name, stats))
        print(f"MISSING: {name} | {stats}")
    else:
        ename, er = hit
        # rough check cost present in both
        if "¥" in stats:
            cost = re.search(r"([\d,\.]+)\s*¥", stats)
            if cost:
                c = cost.group(1).replace(",", "")
                ec = re.sub(r"[^\d]", "", er["cost"])
                if c != ec and name not in {"NITAMA SPORTER"}:  # known conflict handled
                    # skip known chapter-prefer items
                    print(f"COST DIFF: {name} src={c} ency={ename} {er['cost']}")

print(f"\nMissing count: {len(missing)}")

# SL chapter paren weapons with ACC DAM blocks
sl = (ROOT / "Source/_extract/sl_firearms.txt").read_text(encoding="utf-8")
# Only Expanded Arsenal firearm section: from KRIME TINGLER to before ACCESSORIES / ADDITIONAL CLIP
a0 = sl.find("KRIME TINGLER (TASERS)")
a1 = sl.find("ADDITIONAL CLIP/MAGAZINE")
sl_sec = sl[a0:a1]
sl_blocks = re.findall(
    r"^([A-Z0-9][A-Z0-9 /'\-\.\"]+)\(([A-Za-z /]+)\)\s*\nACC DAM AP MODE RC AMMO AVAIL COST\n([^\n]+(?:\n(?![A-Z]{3,})[^\n]+)*)",
    sl_sec,
    re.M,
)
print(f"\nSL chapter firearm blocks: {len(sl_blocks)}")
sl_missing = []
for name, cat, stats in sl_blocks:
    cat_u = cat.upper()
    if any(x in cat_u for x in ("BLADE", "CLUB", "BOW", "ACCESSORY", "MODIFICATION", "ARMOR")):
        continue
    if "MELEE" in cat_u:
        continue
    hit = find_ency(name.strip())
    # HL-13 configs named differently
    if not hit and name.strip() in {"PERSONAL DEFENSE WEAPON", "URBAN ASSAULT", "SNIPER SUPPORT"}:
        hit = find_ency("HL-13 (" + name.strip().title().replace("Defense Weapon", "Defense Weapon"))
        if not hit:
            # try contains
            for k in EM:
                if name.strip().lower() in k.lower():
                    hit = (k, EM[k])
                    break
    if not hit:
        # Triple without Krime
        hit = find_ency("Krime " + name.strip())
    if not hit:
        sl_missing.append((name.strip(), cat, stats.strip().splitlines()[0]))
        print(f"SL MISSING: {name.strip()} ({cat}) | {stats.strip().splitlines()[0]}")

print(f"SL missing count: {len(sl_missing)}")

# Check Core Colt M23 present
print("\nColt M23 ency:")
for k in EM:
    if "m23" in k.lower():
        print(" ", k, EM[k])
