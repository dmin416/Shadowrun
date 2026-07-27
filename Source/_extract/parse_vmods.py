# -*- coding: utf-8 -*-
"""Parse R5 vehicle modification tables into JSON + markdown body."""
import fitz
import json
import re
from pathlib import Path

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

r5 = fitz.open(PDF / "rigger5.pdf")
# Pages with vehicle mod tables (print ~154-171 -> PDF often +0/+1)
text = ""
for i in range(152, 172):
    text += f"\n<<<P{i+1}>>>\n" + r5.load_page(i).get_text("text")
text = text.replace("\u2014", "-").replace("Ñ", "¥").replace("�", "")

# Also dump drone mod attribute costs from chapter
drone_text = ""
for i in range(121, 128):
    drone_text += r5.load_page(i).get_text("text")
drone_text = drone_text.replace("\u2014", "-").replace("Ñ", "¥")

# Known section headers for vehicle mods
SECTIONS = [
    "POWER TRAIN MODIFICATIONS",
    "PROTECTION",
    "WEAPONS",
    "BODY",
    "ELECTROMAGNETIC",
    "COSMETIC",
    "VEHICLE EQUIPMENT",
]

# Parse sequential table rows: Name, Slots, Threshold, Tools, Skill, Avail, Cost
# Skill column is often "—" or blank in extract as "—"

lines = [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.startswith("<<<")]

# Manual structured extraction from known table dumps - more reliable
# Re-read each table page as structured blocks using regex on full page text

mods = []


def parse_table_block(block: str, category: str):
    """Parse MODIFICATION / SLOTS / ... columns stacked."""
    # Split by looking for cost lines containing ¥ or % or formula words
    # Simpler: walk lines after header
    ls = [ln.strip() for ln in block.splitlines() if ln.strip()]
    # find header
    try:
        i = ls.index("MODIFICATION")
    except ValueError:
        return
    # skip header fields
    i += 1
    while i < len(ls) and ls[i] in (
        "SLOTS",
        "THRESHOLD",
        "TOOLS",
        "SKILL",
        "AVAIL",
        "COST",
        "NAME",
    ):
        i += 1
    while i < len(ls):
        name = ls[i]
        if name.startswith(">>") or name.startswith("<<"):
            break
        if name.upper() in SECTIONS or name in (
            "PROTECTION",
            "WEAPONS",
            "BODY",
            "ELECTROMAGNETIC",
            "COSMETIC",
            "AMENITIES",
        ):
            break
        if name in ("MODIFICATION", "SLOTS", "THRESHOLD", "TOOLS", "SKILL", "AVAIL", "COST"):
            i += 1
            continue
        # Collect fields until we have cost (has ¥ or % or x )
        fields = []
        j = i + 1
        while j < len(ls) and len(fields) < 8:
            f = ls[j]
            if f.startswith(">>") or f.startswith("<<"):
                break
            # next mod name heuristic: previous field looked like cost and this looks like title
            fields.append(f)
            j += 1
            # cost detection
            if (
                "¥" in f
                or "%" in f
                or re.search(r"x\s*\d", f, re.I)
                or re.match(r"^(Body|Accel|Handl|Speed|Vehicle|Rating)", f)
                or f.endswith("¥")
                or "nuyen" in f.lower()
            ):
                # sometimes cost spans 2 lines
                if j < len(ls) and (
                    ls[j].endswith("¥")
                    or "x " in ls[j]
                    or ls[j].startswith("Body")
                    or ls[j].startswith("Vehicle")
                    or ls[j].startswith("Rating")
                    or ls[j].startswith("Accel")
                    or ls[j].startswith("Handl")
                    or ls[j].startswith("Speed")
                ):
                    # check if still cost continuation
                    if not re.match(r"^[A-Z][A-Za-z].{3,}", ls[j]) or any(
                        k in ls[j] for k in ("x ", "¥", "Body", "Vehicle", "Rating", "Accel", "Handl", "Speed", "%")
                    ):
                        if "¥" in ls[j] or "%" in ls[j] or "x" in ls[j]:
                            fields.append(ls[j])
                            j += 1
                break
        # Expected: slots, thresh, tools, skill, avail, cost (6) - sometimes rating sublines first
        # Handle "Rating 1" as part of name
        while fields and re.match(r"^(Rating \d|Body .+|Amphibious|Hovercraft|Rotor|Tracked|Walker)$", fields[0]):
            name = name + " / " + fields.pop(0)
        if len(fields) >= 6:
            slots, thresh, tools, skill, avail = fields[:5]
            cost = " ".join(fields[5:])
            mods.append(
                {
                    "cat": category,
                    "name": re.sub(r"\s+", " ", name),
                    "slots": slots,
                    "thresh": thresh,
                    "tools": tools,
                    "skill": skill.replace("—", "-").replace("ù", "-"),
                    "avail": avail.replace("—", "-").replace("ù", "-"),
                    "cost": cost.replace("Ñ", "¥").replace("—", "-"),
                }
            )
            i = j
            continue
        i += 1


# Extract by category from page texts
pages = {
    "Power Train": list(range(158, 160)),
    "Protection": list(range(159, 161)),
    "Weapons": list(range(160, 164)),
    "Body": list(range(163, 167)),
    "Electromagnetic": list(range(166, 170)),
    "Cosmetic": list(range(169, 172)),
}

# Better approach: dump raw table pages and parse with handcrafted regex per known structure
raw_tables = {}
for i in range(158, 172):
    raw_tables[i + 1] = r5.load_page(i).get_text("text")

OUT.joinpath("vmod_raw_tables.json").write_text(
    json.dumps({str(k): v for k, v in raw_tables.items()}, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

# Vehicle equipment (non-slot)
veh_equip = [
    {"name": "Morphing license plate", "avail": "8F", "cost": "1,000¥"},
    {"name": "Spoof chip", "avail": "8F", "cost": "500¥"},
    {"name": "Spike strip (road strip)", "avail": "8R", "cost": "200¥"},
    {"name": "Zapper strip", "avail": "12R", "cost": "2,500¥"},
    {"name": "Tracking strip", "avail": "8R", "cost": "600¥"},
    {"name": "Off-road tires", "avail": "6", "cost": "400¥/tire"},
    {"name": "Racing tires", "avail": "6", "cost": "250¥/tire"},
    {"name": "Run flat tires", "avail": "4", "cost": "250¥/tire"},
]

OUT.joinpath("vmod_equip.json").write_text(
    json.dumps(veh_equip, indent=2), encoding="utf-8"
)
print("raw tables saved", list(raw_tables.keys()))
print("drone text len", len(drone_text))
OUT.joinpath("vmod_drone_ch.txt").write_text(drone_text, encoding="utf-8")
