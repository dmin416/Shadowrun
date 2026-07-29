# -*- coding: utf-8 -*-
"""Assemble final Encyclopedia/Vehicles.md from parsed JSON + headers."""
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\admin\Desktop\Shadowrun")
OUT = ROOT / "Source" / "_extract"
ENC = ROOT / "Encyclopedia" / "Vehicles.md"

vehicles = json.loads((OUT / "veh_parsed.json").read_text(encoding="utf-8"))

# Clean names still broken
for v in vehicles:
    n = v["name"]
    if "�" in n or "\ufffd" in n:
        if "KVP" in n:
            v["name"] = "Mostrans KVP-28"
        elif "wagon" in n.lower():
            v["name"] = "BMW Stormwagon"
        elif "series" in n:
            v["name"] = "Commercial G-series"
    # Expand a few remaining short R5 names with brand from TOC/common use
    expand = {
        "Cyclops": "Entertainment Systems Cyclops",
        "Falcon-EX": "Evo Falcon-EX",
        "Horseman": "Daihatsu-Caterpillar Horseman",
        "Kaburaya": "Yamaha Kaburaya",
        "Mustang": "Thundercloud Mustang",
        "Nightmare": "Harley-Davidson Nightmare",
        "Nodachi": "Yamaha Nodachi",
        "Revolution": "Horizon-Doble Revolution",
        "Spartan": "Buell Spartan",
        "Terrier": "Ares-Segway Terrier",
        "Zip": "Echo Motors Zip",
        "Chameleon": "GMC 442 Chameleon",
        "Dynamit": "Saab Dynamit",
        "Equus": "Hyundai Equus",
        "FunOne": "Renault-Fiat FunOne",
        "Gladius": "Saab Gladius 998 ti",
        "Longboard": "Chevrolet Longboard",
        "MetaWay": "Echo Motors MetaWay",
        "Phoenix": "GMC Phoenix",
        "Xenon": "Dodge Xenon",
        "Armadillo": "GMC Armadillo",
        "Escalade": "GMC Escalade",
        "Hauler": "Nissan Hauler",
        "Hotspur": "Tata Hotspur",
        "Minotaur": "GMC Minotaur",
        "Morgan": "Thundercloud Morgan",
        "Northstar": "Eurocar Northstar",
        "Percheron": "Ford Percheron",
        "Talon": "Toyota Talon",
        "Trailblazer": "Jeep Trailblazer",
        "Caravaner": "Dodge Caravaner",
        "Chuck Wagon": "Ares Chuck Wagon",
        "Econovan": "Ford Econovan",
        "Universe": "GMC Universe",
        "Chinook": "Airstream Chinook",
        "Outback": "Airstream Outback",
        "Preserve": "Airstream Preserve",
        "Conestoga Trailblazer": "Conestoga Trailblazer",
        "Hellhound": "Mack Hellhound",
        "Omnibus": "Omni Motors Omnibus",
        "Minnesota": "Universal Hovercraft Minnesota",
        "Minsk": "Mostrans Minsk",
        "Vodyanoy": "Vodyanoy Assault Hovercraft",
        "Blitzkrieg": "BMW Blitzkrieg",
        "Charger": "Dodge Charger",
        "Command (General)": "Dodge General (Command)",
        "Goliath": "Dodge Goliath",
        "i8 Interceptor": "BMW i8 Interceptor",
        "Luxus": "BMW Luxus",
        "Rhino": "Dodge Rhino",
        "Teufelkatze": "BMW Teufelkatze",
        "Trailer (General)": "Dodge General Trailer",
        "Wolf II": "Ruhrmetall Wolf II",
        "Electronaut": "Vulkan Electronaut",
        "Commuter": "Federated-Boeing Commuter",
        "Hound": "Ares Hound",
        "Gryphon": "GMC Gryphon",
        "LZP-2070": "Luftschiffbau LZP-2070",
        "Sea Sprite": "Dassault Sea Sprite",
        "SKA-008": "S-K Aerospace SKA-008",
        "Agular GX-2": "Aztechnology Agular GX-2",
        "Agular GX-3AT": "Aztechnology Agular GX-3AT",
        '"Krime Wing"': 'Evo-Krime "Krime Wing"',
        '"Lift-Ticket" ALS-699': 'Airbus "Lift-Ticket" ALS-699',
        '"Mothership" LAVH': 'Renegade Works "Mothership" LAVH',
        "PBY-70 Catalina II": 'Federated-Boeing PBY-70 "Catalina II"',
        "Nightrunner": "Aztech Nightrunner",
        "Cottonmouth": "Sea Ray Cottonmouth",
        "Waterking": "Evo Waterking",
        "Waterbug": "Mitsubishi Waterbug",
        "Water Strider": "Evo Water Strider",
        "Zodiac Scorpio": "Zodiac Scorpio",
        "Stingray": "Kawasaki Stingray",
        "Manta Ray": "Kawasaki Manta Ray",
        "AirRanger": "American Airboat AirRanger",
        "AirRanger Heavy": "American Airboat AirRanger Heavy",
        "Lake King": "Sun Tracker Lake King",
        "Kingfisher": "UltraMarine Kingfisher",
        "Elysium": "Corsair Elysium",
        "Panther": "Corsair Panther",
        "Trident": "Corsair Trident",
        "Classic 111": "Blohm & Voss Classic 111",
        "Mobius": "Lurssen Mobius",
        "Aquavida 1": "Evo Aquavida 1",
        "Aquavida 2": "Evo Aquavida 2",
        "Riverine Military": "GMC Riverine (Military)",
        "Riverine Police": "GMC Riverine (Police)",
        "Riverine Security": "GMC Riverine (Security)",
        "Triton": "GMC Triton",
    }
    if v["name"] in expand:
        v["name"] = expand[v["name"]]

# Rules policy: keep only for R5/HT*; clear Core/SS auto-noise; drop empty Std Equip
for v in vehicles:
    src = v.get("src") or ""
    rules = (v.get("rules") or "").strip()
    if src in ("Core", "SS"):
        v["rules"] = ""
    elif rules in ("Std Equip: -", "Std Equip:", "-"):
        v["rules"] = ""
    elif rules.startswith("Std Equip: -;"):
        v["rules"] = rules.replace("Std Equip: -; ", "").replace("Std Equip: -;", "")

CAT_ORDER = [
    "MOTORCYCLES",
    "CARS",
    "TRUCKS",
    "TRACTOR/TRAILERS",
    "HOVERCRAFT",
    "BUSES",
    "WATERCRAFT",
    "SECURITY/POLICE/MILITARY",
    "AIRCRAFT",
]

SIMILAR = """
| Listed vehicle | Similar models (same stats; branding only unless GM tweaks) |
| --- | --- |
| Dodge Scoot | Hyundai Hopper, Entertainment Systems Papoose |
| Harley-Davidson Scorpion | BMW Blitzen, Gaz-Niki Titan |
| Yamaha Growler | Evo Falcon, Gaz-Niki Wolverine |
| Suzuki Mirage | Yamaha Rapier, Thundercloud Contrail |
| Chrysler-Nissan Jackrabbit | Peugeot 112, Opel Luna |
| Honda Spirit | Wuxing Breezer, Toyota Gazelle |
| Hyundai Shin-Hyung | BMW 400GT, GMC Commodore |
| Eurocar Westwind 3000 | Porsche Aguilar, Ferrari Diabolus |
| Ford Americar | Mercury Comet, Honda Citizen |
| S-K Bentley Concordat | GMC Cadillac Nocturne, BMW X89 |
| Mitsubishi Nightsky | Rolls Royce Phaeton |
| Toyota Gopher | Gaz P-179, Wuxing Peng You 4x4 |
| GMC Bulldog Step-Van | Renault-Fiat Eurovan, Aztechnology Governor |
| Rover Model 2072 | Ares Humvee, Toyota Coaster |
| Ares Roadmaster | Esprit Industries Sororita, Renraku Kamekichi |
| Samuvani-Criscraft Otter | GMC Outrider, Celebrian Nymph |
| Yongkang-Gala Trinity | Zemlya-Poltava Crest, Celebrian Dart |
| Morgan Cutlass | Surfstar Marine Seacop, Messerschmidt-Kawasaki Harbor Sentry |
| Proteus Lamprey | Kalmaar Seefuchs, Toyota TLM-2 |
| Vulkan Electronaut | Proteus Explorer, Aztechnology Jade Diver |
| Artemis Industries Nightwing / Northrup Nightwing | IFMU Spatz, Suzuki Wingman |
| Cessna C750 | Lear-Cessna Rover |
| Federated-Boeing Tundra-9 | Airbus JPFB-03, Toyota TX13 |
| Ares Dragon | Hughes Stallion |
| Ares Wasp / Northrup Wasp | Lockheed Kestrel, Renraku Dragonfly |
| Ares Venture | Cascade Skraacha, Zhejiang Shenying Industries Raptor |
| GMC Banshee | Aztechnology Lobo |
| Federated-Boeing Commuter | Hughes-Aerospace Daytrader |
""".strip()

header = """# Vehicles

Agent reference (SR5). Compact; full mechanical detail; no flavor.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `rigger5.pdf` · `stolensouls.pdf`
**Books:** Core · R5 · SS · HT* (compiled stats only; no local Hard Targets PDF)
**Printed:** Core Vehicles and Drones 461-466 (vehicle half); R5 World of Wheels / Ruling the Waves / Air Superiority 41-109; R5 compiled tables 184-188; SS extractor vehicle lines ~187
**See also:** `Encyclopedia/Drones.md` · `Encyclopedia/Vehicle and Drone Modifications.md` · `Encyclopedia/Rigger Gear.md` · `Mechanics/Vehicles.md` · `Mechanics/Rigging.md`

**In scope:** metahuman-crewed ground / water / air vehicles with buy stats (bikes, cars, trucks/vans/RVs/limos, buses, tractor-trailers, hovercraft, boats/subs, security/military vehicles, aircraft).
**Out of scope:** drones (→ Drones.md); vehicle mods / weapon mounts as upgrade SKUs (→ Vehicle and Drone Modifications); RCC / autosofts (→ Rigger Gear); chase action list detail (→ Mechanics/Vehicles.md).

## Schema

| Col | Meaning |
| --- | --- |
| Src | Core / R5 / SS / HT* |
| Sub | Compiled subsection under parent table (VANS, RVS, LIMOS, COMMERCIAL) or `-` |
| Handl | Handling; `A/B` = on-road / off-road (or mode pair as printed) |
| Speed | Speed; letter suffixes in other books (G/J/R) are movement modes for chase mixing; `A/B` = dual-mode |
| Accel | Acceleration; dual-mode when paired with dual Speed |
| Body | Body attribute |
| Armor | Armor |
| Pilot | Pilot program Rating (= Device Rating / Matrix attrs when applicable) |
| Sens | Sensor array Rating |
| Seats | Passenger seats; `A/B` = config options (e.g. cab/cargo) |
| Avail / Cost | Street Availability / nuyen; `-` = none |
| Ref | Printed page from R5 compiled tables (source of buy line) |
| Rules | Factory Standard Equipment / Notes when printed; else `-` |

## Common rules

### Skills and power

- Ground craft (bikes, cars, trucks, vans, buses, most security ground): **Pilot Ground Craft**.
- Watercraft: **Pilot Watercraft** (hovercraft use watercraft or as printed).
- Aircraft (fixed-wing, rotor, LAV/LTAV, zeppelins): appropriate **Pilot Aircraft** / specialty as GM.
- Core note: most ground vehicles available with electric or hybrid biofuel engines.

### Attributes (Core / R5)

- **Handling:** limit for vehicle tests; `on-road/off-road` when two numbers.
- **Speed / Acceleration:** chase and movement (see Mechanics/Vehicles.md; R5 Maximum Pursuit for advanced).
- **Body / Armor:** physical Condition Monitor and resist; treat damage as vehicles.
- **Pilot:** dog-brain Rating; Device Rating = Pilot; Matrix attributes = Pilot unless modified.
- **Sensor:** sensor array Rating (Perception / Sensor tests).
- Vehicles do **not** ship with rigger interface unless listed (Std Equip / Notes) or installed via Vehicle Modifications. Drones do.

### Weapon mounts (Core Street Gear)

- Vehicles/drones: unaugmented Body ÷ 3 (round down) mounts.
- Standard mount: assault rifle or smaller + 250 rounds.
- Heavy mount: costs 2 mounts; any weapon + 500 belt or Body rockets/missiles.
- Mounts remote-operated; 90° arc H/V. Manual operation: vehicles only, extra cost (not drones).

### Similar models (Core)

Same stats as listed SKU; branding / year only unless GM adjusts one attribute or price slightly.

"""

# catalog
parts = [header, "## Similar models (Core)\n\n", SIMILAR, "\n\n## Catalog\n\n"]

for cat in CAT_ORDER:
    rows = [v for v in vehicles if v["cat"] == cat]
    if not rows:
        continue
    title = {
        "SECURITY/POLICE/MILITARY": "Security / Police / Military",
        "TRACTOR/TRAILERS": "Tractor / Trailers",
    }.get(cat, cat.title())
    parts.append(f"### {title}\n\n")
    parts.append(
        "| Name | Sub | Src | Handl | Speed | Accel | Body | Armor | Pilot | Sens | Seats | Avail | Cost | Ref | Rules |\n"
    )
    parts.append(
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
    )
    for v in rows:
        rules = (v.get("rules") or "").replace("|", "/").strip() or "-"
        sub = v.get("sub") or "-"
        parts.append(
            f"| {v['name']} | {sub} | {v['src']} | {v['handl']} | {v['speed']} | {v['accel']} | {v['body']} | {v['armor']} | {v['pilot']} | {v['sens']} | {v['seats']} | {v['avail']} | {v['cost']} | {v['ref']} | {rules} |\n"
        )
    parts.append("\n")

# SS extractor note
parts.append(
    """### Stolen Souls extractor chassis note (SS)

SS lists factory chassis commonly counterfeited as emergency/gov vehicles. Stats are the buy lines above. Disguise mods (lights, siren, chameleon, spoof, smuggling): Vehicle Modifications / SS tables, not duplicated here.

| Factory vehicle | Typical fake role |
| --- | --- |
| Ares Roadmaster | Counterfeit SWAT / Urban Command |
| Chrysler-Nissan Journey | Counterfeit Lone Star patrol |
| Conestoga Trailblazer | Counterfeit moving truck |
| Dodge Ram Industrial | Garbage truck |
| Esprit Industries Watcher | Counterfeit CAS government |
| GMC Endurance | Counterfeit DocWagon ambulance |
| GMC Sidewinder | Counterfeit UCAS government |
| Honda Artemis | Counterfeit Knight Errant patrol |
| S-K LT-21 | Counterfeit CrashCart ambulance |

"""
)

# index
parts.append("## Item index\n\n")
for cat in CAT_ORDER:
    rows = [v for v in vehicles if v["cat"] == cat]
    if not rows:
        continue
    parts.append(f"**{cat.title()} ({len(rows)}):** " + "; ".join(v["name"] for v in rows) + "\n\n")

parts.append(f"**Total vehicle SKUs:** {len(vehicles)}\n")

text = "".join(parts)
# no em dashes
text = text.replace("\u2014", "-").replace("—", "-")
ENC.write_text(text, encoding="utf-8")
print("wrote", ENC, "chars", len(text), "vehicles", len(vehicles))

