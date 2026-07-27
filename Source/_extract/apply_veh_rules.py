# -*- coding: utf-8 -*-
"""Apply cleaned Std Equipment Rules onto Encyclopedia/Vehicles.md catalog rows."""
import json
import re
from pathlib import Path

ENC = Path(r"C:\Users\admin\Desktop\Shadowrun\Encyclopedia\Vehicles.md")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

blocks = json.loads((OUT / "veh_std_blocks.json").read_text(encoding="utf-8"))

POLLUTION = re.compile(
    r"\s+(?:"
    r"CARS|TRUCKS|HAULERS|VANS|RVS|LIMOS|"
    r"DYNAMIT \(GROUNDCRAFT\)|PRESERVE \(GROUNDCRAFT\)|OUTBACK \(GROUNDCRAFT\)|"
    r"COMMERCIAL D-SERIES \(GROUNDCRAFT\)|COMMERCIAL DD \(GROUNDCRAFT\)|"
    r"MINOTAUR \(GROUNDCRAFT\)|MANTA RAY \(WATERCRAFT\)|WAVESKIPPER \(WATERCRAFT\)|"
    r"AQUAVIDA 2 \(WATERCRAFT\)|AIRRANGER HEAVY \(WATERCRAFT\)|"
    r"AGULAR GX-3AT \(ROTORCRAFT\)|BLOHM & VOSS CLASSIC 111|"
    r"AIRBUS .LIFT-TICKET.|"
    r"SAILCRAFT.*"
    r").*$"
)


def clean_equip(s: str) -> str:
    if not s or s.strip() in ("-", ""):
        return ""
    s = s.replace("\ufffd", "").replace("Ñ", "¥").replace("�", "")
    s = POLLUTION.sub("", s)
    s = re.sub(r"\s+", " ", s).strip(" ,;")
    return s


def clean_notes(s: str) -> str:
    if not s:
        return ""
    s = s.replace("\ufffd", "¥").replace("Ñ", "¥").replace("�", "¥")
    s = re.sub(r"\s+", " ", s).strip()
    if s.startswith(">"):
        return ""
    return s[:450]


rules_map = {}
for b in blocks:
    hint = (b.get("name_hint") or "").upper().strip()
    if not hint or hint in ("?", "STD.", "EQUIPMENT"):
        continue
    hint = re.sub(r"\s+", " ", hint)
    if "WAGON" in hint and hint.startswith("ST"):
        hint = "STORMWAGON"
    # normalize fancy quotes in hints
    hint = hint.replace("Ô", '"').replace("Ö", '"').replace('"', '"')
    equip = clean_equip(b.get("equip") or "")
    notes = clean_notes(b.get("notes") or "")
    if not equip and not notes:
        continue
    parts = []
    if equip:
        parts.append("Std Equip: " + equip)
    if notes:
        parts.append("Notes: " + notes)
    rules_map[hint] = "; ".join(parts)

# Manual corrections from PDF where auto pollution/wrong
rules_map["KVP-28"] = "Std Equip: Secondary propulsion (hovercraft)"
rules_map["OUTBACK"] = (
    "Std Equip: Amenities (squatter), Extreme environment mod (hot), "
    "off-road suspension, satellite uplink, suncell"
)
rules_map["CHINOOK"] = (
    "Std Equip: Amenities (squatter), extreme environment modification (cold), "
    "satellite uplink, suncell"
)
rules_map["PRESERVE"] = (
    "Std Equip: Amenities (squatter), gridlink, satellite uplink, suncell"
)
rules_map["MUSTANG"] = "Std Equip: Smart Tires, Amphibious Operation"
rules_map["GLADIUS"] = "Std Equip: Rigger adaptation"
rules_map["TRIDENT"] = (
    "Std Equip: Amenities (middle), improved economy, satellite link, SunCell"
)
rules_map["TRITON"] = (
    "Std Equip: Amenities (middle), improved economy, satellite link"
)
rules_map["COMMERCIAL D-COMPACT"] = "Std Equip: Special equipment"
rules_map["COMMERCIAL D-SERIES"] = (
    "Std Equip: Gridlink, gridlink override, maneuver autosoft (2), special equipment"
)
rules_map["STALLION"] = (
    "Std Equip: Heavy weapon mount (external, turret, manual) top, "
    "two standard weapon mounts (external, fixed, remote) rear"
)
rules_map["MINOTAUR"] = (
    "Std Equip: Heavy weapon mount (external, turret, manual) top, "
    "standard weapon mount (external, fixed, remote) rear"
)
rules_map["STORMWAGON"] = (
    "Std Equip: Light system allows those subscribed to use the Sensor rating as their limit "
    "for relevant tests; additional entry/exit port (assault ramp, rear) firing ports; "
    "special equipment (advanced lightbar)"
)

md = ENC.read_text(encoding="utf-8")
lines = md.splitlines(keepends=True)
out = []
updated = 0


def find_rules_for_name(name: str) -> str:
    name_c = name.strip()
    candidates = []
    for hint, rules in rules_map.items():
        if hint == "TRAILBLAZER":
            if "Jeep Trailblazer" in name_c:
                return rules
            continue
        if hint == "STALLION":
            if name_c.startswith("Dodge Stallion"):
                return rules
            continue
        if hint == "TRAILER":
            if "General" in name_c and "Trailer" in name_c:
                return rules
            continue
        if hint in ("HUGHES STALLION WK-4",) or "HUGHES STALLION" in hint:
            if "Hughes Stallion" in name_c:
                return rules
            continue
        # skip empty
        tok = hint.split()[-1].strip('"')
        if len(tok) >= 4 and tok.lower() in name_c.lower():
            # avoid short false positives
            if tok.lower() in ("series", "general", "model", "line", "heavy"):
                if hint.lower() not in name_c.lower() and tok.lower() not in name_c.lower():
                    continue
            candidates.append((len(hint), len(tok), rules, hint))
        elif hint.replace("-", " ").lower() in name_c.lower():
            candidates.append((len(hint), len(hint), rules, hint))
    if not candidates:
        return ""
    candidates.sort(reverse=True)
    return candidates[0][2]


for line in lines:
    if not line.startswith("| "):
        out.append(line if line.endswith("\n") else line + "\n")
        continue
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    if len(parts) < 15:
        out.append(line if line.endswith("\n") else line + "\n")
        continue
    name, sub, src = parts[0], parts[1], parts[2]
    if name in ("Name",) or name.startswith("---") or src not in ("Core", "R5", "SS", "HT*"):
        out.append(line if line.endswith("\n") else line + "\n")
        continue

    if src == "HT*":
        new_rules = "Hard Targets SKU (no local PDF); stats from R5 compiled table only."
    else:
        new_rules = find_rules_for_name(name) or "-"

    if new_rules != "-":
        updated += 1
    parts[14] = new_rules.replace("|", "/")
    out.append("| " + " | ".join(parts) + " |\n")

text = "".join(out)
text = text.replace("\u2014", "-")
text = text.replace("| KVP-28 |", "| Mostrans KVP-28 |")
# Waveskipper is Core SR5 table; R5 also reprints Std Equip blank
text = text.replace("| Yamaha Waveskipper | - | R5 |", "| Yamaha Waveskipper | - | Core |")
text = text.replace(
    "| Yamaha Waveskipper | - | Core | 5 | 3 | 2 | 10 | 4 | 1 | - | 1 | - | 10,000¥ | p. 84 |",
    "| Yamaha Waveskipper | - | Core | 5 | 3 | 2 | 10 | 4 | 1 | - | 1 | - | 10,000¥ | p. 464, SR5 |",
)

ENC.write_text(text, encoding="utf-8")
print("rows with non-dash rules", updated)
print("rules_map keys", len(rules_map))

# Verify bad cross-links gone
for ln in text.splitlines():
    if "Pods decrease" in ln and "Horseman" not in ln:
        print("BAD pods:", ln[:120])
    if "Assembly Time Improvement, Gyro Stabilization" in ln and "Cyclops" not in ln:
        print("BAD gyro:", ln[:120])
    if "Smart Tires, Amphibious Operation" in ln and "Mustang" not in ln and "Water Strider" not in ln:
        print("BAD mustang-rules:", ln[:120])
