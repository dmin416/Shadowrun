# -*- coding: utf-8 -*-
"""
Extract every Std./Standard Equipment (+ Notes) from R5 vehicle chapters,
map to Vehicles.md rows, rewrite Rules cleanly.
"""
import fitz
import re
from pathlib import Path

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
ENC = Path(r"C:\Users\admin\Desktop\Shadowrun\Encyclopedia\Vehicles.md")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

r5 = fitz.open(PDF / "rigger5.pdf")
text = ""
page_breaks = []
for i in range(40, 110):
    page_breaks.append(len(text))
    text += f"\n<<<PAGE {i+1}>>>\n" + r5.load_page(i).get_text("text")

text_n = text.replace("\u2014", "-").replace("Ñ", "¥").replace("�", "")

# Find all Std/Standard Equipment blocks
pat = re.compile(r"(?:Standard|Std\.?)\s*\n?\s*Equipment\s*\n?", re.I)
blocks = []
for m in pat.finditer(text_n):
    pre = text_n[max(0, m.start() - 600) : m.start()]
    after = text_n[m.end() : m.end() + 500]
    # equipment lines
    equip_lines = []
    notes_lines = []
    mode = "equip"
    for ln in after.splitlines():
        raw = ln
        ln = ln.strip()
        if not ln:
            if equip_lines and mode == "equip":
                # allow one blank; if already have content, peek next
                continue
            continue
        if ln.startswith("<<<PAGE"):
            break
        if ln.startswith(">>") or ln.startswith("<<"):
            break
        if re.match(r"^Notes?$", ln, re.I):
            mode = "notes"
            continue
        if mode == "notes":
            # stop on new vehicle header-ish
            if re.match(r"^[A-Z0-9][A-Z0-9 \-/'\"\.]{3,50}$", ln) and len(ln) < 55:
                if not any(
                    w in ln.lower()
                    for w in (
                        "decrease",
                        "increase",
                        "adds",
                        "passenger",
                        "handling",
                        "speed",
                        "accel",
                        "seats",
                        "weapon",
                        "mount",
                        "pod",
                    )
                ):
                    break
            if ln.startswith(">"):
                break
            notes_lines.append(ln)
            continue
        # equip mode: stop on clear next vehicle title (ALL CAPS long) or HANDL table header
        if ln in ("HANDL", "NAME", "SPEED", "ACCEL", "BODY", "ARM", "ARMOR", "PILOT", "SENS", "SEATS", "AVAIL", "COST"):
            break
        if re.match(r"^[A-Z0-9][A-Z0-9 \-/'\"\.]{5,55}$", ln) and len(ln) < 55 and equip_lines:
            # next vehicle name
            break
        if re.match(r"^[A-Z][A-Za-z].{10,}$", ln) and equip_lines and not any(
            c in ln for c in (",", "(", ")", "x ", "+", "/")
        ):
            # flavor sentence starting after equip
            if ln[0].isupper() and " " in ln and not ln.isupper():
                # likely prose - stop unless looks like equip continuation
                if not any(
                    k in ln.lower()
                    for k in (
                        "mount",
                        "amenities",
                        "rigger",
                        "weapon",
                        "gridlink",
                        "satellite",
                        "smuggling",
                        "enhancement",
                        "adaptation",
                        "suspension",
                        "manual",
                        "drone",
                        "armor",
                        "life support",
                        "oil slick",
                        "smoke",
                        "road strip",
                        "signature",
                        "flamer",
                        "flash",
                        "anti-theft",
                        "gun port",
                        "ram plate",
                        "entry",
                        "enviroseal",
                        "gyro",
                        "smart tire",
                        "tracked",
                        "amphibious",
                        "metahuman",
                        "off-road",
                        "multifuel",
                        "secondary",
                        "hovercraft",
                        "special equipment",
                        "maneuver",
                        "autosoft",
                        "suncell",
                        "extreme",
                    )
                ):
                    break
        equip_lines.append(ln)

    equip = re.sub(r"\s+", " ", " ".join(equip_lines)).strip(" ,;")
    notes = re.sub(r"\s+", " ", " ".join(notes_lines)).strip()
    # strip pollution: if equip contains a known next-vehicle ALLCAPS run, cut
    equip = re.split(r"\s(?=[A-Z]{3,}(?:[\- ][A-Z0-9]+){1,6}\s+[A-Z])", equip)[0].strip(" ,;")
    # Determine vehicle name from pre: look for NAME (TYPE) or ALL CAPS line
    name = None
    pre_lines = [ln.strip() for ln in pre.splitlines() if ln.strip() and not ln.startswith("<<<")]
    for ln in reversed(pre_lines[-25:]):
        if re.search(r"\((?:GROUNDCRAFT|WATERCRAFT|AIRCRAFT|HOVERCRAFT|ROTORCRAFT|LTAV|LAV|VEHICLE)\)", ln, re.I):
            name = re.sub(r"\s*\(.*$", "", ln).strip()
            break
        if ln.isupper() and 3 < len(ln) < 60 and not ln.startswith(">"):
            if ln not in ("HANDL", "SPEED", "ACCEL", "BODY", "ARM", "ARMOR", "PILOT", "SENS", "SEATS", "AVAIL", "COST", "NAME", "STD.", "EQUIPMENT", "NOTES"):
                name = ln.title() if ln.isupper() else ln
                # keep better casing later
                name = ln
                break
        if re.match(r"^[A-Z][A-Za-z0-9].{2,50}$", ln) and not ln.startswith("The ") and not ln.startswith(">"):
            # possible Title Case vehicle name
            if any(c.islower() for c in ln) and len(ln.split()) <= 8:
                # only if recent
                name = ln
                break
    blocks.append({"name_hint": name or "", "equip": equip, "notes": notes, "pre_tail": " | ".join(pre_lines[-8:])})

print("blocks", len(blocks))
for b in blocks:
    print("---", b["name_hint"][:50] if b["name_hint"] else "?")
    print("  E:", b["equip"][:140])
    if b["notes"]:
        print("  N:", b["notes"][:100])

# Save
import json

OUT.joinpath("veh_std_blocks.json").write_text(
    json.dumps(blocks, indent=2, ensure_ascii=False), encoding="utf-8"
)
