# -*- coding: utf-8 -*-
"""Audit Vehicles.md completeness vs R5 TOC + compiled + Core + other PDFs."""
import fitz
import re
from pathlib import Path

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
ENC = Path(r"C:\Users\admin\Desktop\Shadowrun\Encyclopedia\Vehicles.md")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

veh_md = ENC.read_text(encoding="utf-8")

# R5 TOC vehicle names from pages 3-4
r5 = fitz.open(PDF / "rigger5.pdf")
toc = r5.load_page(2).get_text("text") + "\n" + r5.load_page(3).get_text("text")
# Extract lines that look like vehicle entries under World of Wheels through Air Superiority
# From earlier TOC dump we have the list - parse between Demolition Derby and Automated Army
start = toc.find("WORLD OF WHEELS")
end = toc.find("THE AUTOMATED ARMY")
section = toc[start:end] if start >= 0 else toc

# Also get air superiority from page 4
toc2 = r5.load_page(3).get_text("text") + "\n" + r5.load_page(4).get_text("text")
start2 = toc2.find("RULING THE WAVES")
end2 = toc2.find("ONE RIG TO RULE")
section2 = toc2[start2:end2] if start2 >= 0 else ""

all_toc = section + "\n" + section2
# vehicle-like: lines with letters that aren't section headers and have page numbers at end
toc_vehicles = []
for ln in all_toc.splitlines():
    ln = ln.strip()
    if not ln:
        continue
    m = re.match(r"^(.+?)\s+(\d+)\s*$", ln)
    if not m:
        continue
    name, page = m.group(1).strip(), m.group(2)
    # skip section headers (all caps short, or known sections)
    if name.upper() == name and len(name) < 25 and " " not in name.strip():
        continue
    skip = {
        "Motorcycles",
        "Cars",
        "Trucks",
        "Big Boys",
        "Personal Watercraft",
        "Powerboats",
        "Sailboats",
        "Yachts",
        "Submersibles",
        "Airplanes",
        "Rotorcraft",
        "LAVs",
        "LTAVs",
        "Drones",
        "Haulers",
        "Municipal/Construction",
        "Corpsec/Police/Military",
        "Sailcraft – sort of",
        "Sailcraft - sort of",
        "Personal Motorized Vehicle",
        "Wet and Wild",
        "Flying the Unfriendly Skies",
        "Air Superiority",
        "Ruling the Waves",
        "World of Wheels",
        "Demolition Derby",
        "Airstream Traveler Line Motorhomes",
        "GMC Commercial G-series",
        "GMC Commercial D-series",
        "Saeder-Krupp Konstructors",
    }
    # Keep GMC Commercial etc as they are vehicles - remove from skip the series ones
    if name in (
        "Motorcycles",
        "Cars",
        "Trucks",
        "Big Boys",
        "Personal Watercraft",
        "Powerboats",
        "Sailboats",
        "Yachts",
        "Submersibles",
        "Airplanes",
        "Rotorcraft",
        "LAVs",
        "LTAVs",
        "Drones",
        "Haulers",
        "Municipal/Construction",
        "Corpsec/Police/Military",
        "Personal Motorized Vehicle",
    ):
        continue
    if re.match(r"^(Wet |Flying |Air Superiority|Ruling |World |Demolition)", name):
        continue
    toc_vehicles.append((name, page))

print("TOC vehicle-ish entries:", len(toc_vehicles))
missing = []
for name, page in toc_vehicles:
    # fuzzy: last significant token
    tokens = [t for t in re.split(r"[\s/\-\"\']+", name) if len(t) >= 4]
    tokens = sorted(tokens, key=len, reverse=True)
    found = False
    for t in tokens[:3]:
        if t.lower() in veh_md.lower():
            found = True
            break
    # also try full-ish
    if not found and name.split()[-1].lower() in veh_md.lower():
        found = True
    if not found:
        missing.append((name, page))

print("MISSING vs TOC:")
for m in missing:
    print(" ", m)

# Core table names
core = fitz.open(PDF / "shadowrunfiftheditioncorerulebook_V2.pdf")
core_t = ""
for i in range(467, 472):
    core_t += core.load_page(i).get_text("text")
# Find Waveskipper etc
for n in [
    "Waveskipper",
    "Otter",
    "Trinity",
    "Cutlass",
    "Lamprey",
    "Electronaut",
    "Nightwing",
    "Cessna",
    "Tundra",
    "Dragon",
    "Hound",
    "Wasp",
    "Venture",
    "Banshee",
    "Commuter",
    "Scoot",
    "Scorpion",
    "Growler",
    "Mirage",
    "Jackrabbit",
    "Spirit",
    "Shin-Hyung",
    "Westwind",
    "Americar",
    "Concordat",
    "Nightsky",
    "Gopher",
    "Bulldog",
    "Rover",
    "Roadmaster",
]:
    in_core = n in core_t
    in_md = n.lower() in veh_md.lower()
    if in_core and not in_md:
        print("CORE MISS", n)

# Other PDFs with vehicle tables
print("\nOther PDF vehicle table hits:")
for pdfn in [
    "streetlethal.pdf",
    "completetrog.pdf",
    "runandgun.pdf",
    "runfaster.pdf",
    "seattlesprawl.pdf",
    "marketpanic.pdf",
    "howlingshadows.pdf",
    "darkterrors.pdf",
    "serratededge.pdf",
]:
    path = PDF / pdfn
    if not path.exists():
        continue
    doc = fitz.open(path)
    for i in range(len(doc)):
        t = doc.load_page(i).get_text("text")
        if "Handling" in t and "Speed" in t and "Seats" in t and ("Avail" in t or "AVAIL" in t):
            # skip if mostly drones
            if "drone" in t.lower()[:200] and "vehicle" not in t.lower()[:200]:
                continue
            snippet = t[:150].replace("\n", " ")
            print(f"  {pdfn} p{i+1}: {snippet[:100]}")

# Count Rules that look wrongly copied (Horseman notes on wrong vehicles)
wrong = []
for line in veh_md.splitlines():
    if "Pods decrease Handling" in line and "Horseman" not in line:
        wrong.append(line[:80])
    if "Assembly Time Improvement, Gyro Stabilization" in line and "Cyclops" not in line and "Riverine" in line:
        wrong.append("Riverine wrong: " + line[:60])
print("\nSuspicious Rules rows:", len(wrong))
for w in wrong[:15]:
    print(" ", w)
