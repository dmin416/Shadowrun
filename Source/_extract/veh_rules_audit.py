# -*- coding: utf-8 -*-
"""
Rebuild vehicle Rules correctly:
- For each R5 vehicle with a chapter page ref (p. N without SR5/Stolen/Hard),
  load PDF pages N and N+1 (print page ~= PDF page for World of Wheels offset:
  print P -> PDF index P, i.e. load_page(P) which is PDF P+1... verify).
- Extract Standard Equipment + Notes belonging to THAT vehicle only.
- Fix wrong cross-copied rules.
Also emit a special-rules appendix for long Notes.
"""
import fitz
import json
import re
from pathlib import Path

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")
ENC = Path(r"C:\Users\admin\Desktop\Shadowrun\Encyclopedia\Vehicles.md")

# Known TOC list (complete from R5 TOC)
TOC = [
    # Motorcycles
    ("Daihatsu-Caterpillar Horseman", 41),
    ("Ares-Segway Terrier", 42),
    ("Horizon-Doble Revolution", 42),
    ("Evo Falcon-EX", 43),
    ("Entertainment Systems Cyclops", 43),
    ("Echo Motors Zip", 44),
    ("Yamaha Kaburaya", 44),
    ("Buell Spartan", 44),
    ("Harley-Davidson Nightmare", 45),
    ("Yamaha Nodachi", 45),
    ("Thundercloud Mustang", 46),
    # Cars / light
    ("Renault-Fiat FunOne", 47),
    ("Dodge Xenon", 47),
    ("Echo Motors MetaWay", 47),
    ("GMC 442 Chameleon", 48),
    ("Mercury Comet", 49),
    ("Saab Gladius 998 ti", 49),
    ("GMC Phoenix", 50),
    ("Hyundai Equus", 51),
    ("Chevrolet Longboard", 52),
    ("Rolls-Royce Phaeton", 52),
    ("Thundercloud Morgan", 52),
    ("Tata Hotspur", 53),
    ("GMC Armadillo", 54),
    ("Ford Percheron", 54),
    ("Jeep Trailblazer", 54),
    ("Toyota Talon", 55),
    ("Nissan Hauler", 56),
    ("Eurocar Northstar", 56),
    ("GMC Escalade", 57),
    ("Ford Econovan", 58),
    ("Dodge Caravaner", 58),
    ("GMC Universe", 59),
    ("Ares Chuck Wagon", 59),
    ("Airstream Traveler Line Motorhomes", 59),
    ("Mack Hellhound", 60),
    ("Omni Motors Omnibus", 62),
    ("GMC Commercial G-series", 62),
    ("GMC Commercial D-series", 63),
    ("Saeder-Krupp Konstructors", 64),
    ("Mostrans KVP-28", 64),
    ("Universal Hovercraft Minnesota", 65),
    ("Vodyanoy Assault Hovercraft", 65),
    ("BMW Blitzkrieg", 66),
    ("Dodge Charger", 67),
    ("BMW i8 Interceptor", 68),
    ("Dodge Goliath", 70),
    ("BMW Teufelkatze", 71),
    ("Dodge Stallion", 71),
    ("BMW Luxus", 73),
    ("Dodge General", 74),
    ("BMW Stormwagon", 75),
    ("Dodge Rhino", 77),
    ("Ruhrmetall Wolf II", 77),
    # Water - from earlier TOC
    ("Evo Waterking", 79),
    ("Sea Ray Cottonmouth", 80),
    ("Kawasaki Stingray/Manta Ray", 81),
    ("Aztech Nightrunner", 81),
    ("Zodiac Scorpio", 82),
    ("Mitsubishi Waterbug", 83),
    ("Evo Water Strider", 84),
    ("Corsair Elysium", 85),
    ("Corsair Panther", 85),
    ("Corsair Trident", 87),
    ("Blohm & Voss Classic 111", 88),
    ("Lurssen Mobius", 89),
    ("Sun Tracker Lake King", 90),
    ("Evo Aquavida", 90),
    ("UltraMarine Kingfisher", 92),
    ("American Airboat AirRanger", 92),
    ("GMC Riverine", 92),
    # Air
    ("Hughes Stallion WK-4", 95),
    ("Aztechnology Agular GX-2 and GX-3AT", 97),
    ("S-K Aerospace SKA-008", 98),
    ("Dassault Sea Sprite", 99),
    ("Federated-Boeing PBY-70 Catalina II", 100),
    ("Airbus Lift-Ticket ALS-699", 102),
    ("GMC Gryphon", 103),
    ("Evo-Krime Krime Wing", 105),
    ("Luftschiffbau Personal Zeppelin LZP-2070", 106),
    ("Renegade Works Mothership LAvH", 108),
]


def find_vehicle_block(text: str, name: str) -> str:
    """Find text from vehicle name heading to next major heading or Standard Equip of next vehicle."""
    # Build search patterns from distinctive tokens
    tokens = [t for t in re.split(r"[\s/\-\"\']+", name) if len(t) >= 4]
    tokens = sorted(set(tokens), key=len, reverse=True)
    idx = -1
    used = None
    for tok in tokens[:4]:
        # Prefer ALL CAPS heading style
        for m in re.finditer(re.escape(tok), text, re.I):
            # check nearby for uppercase name-ish
            window = text[max(0, m.start() - 40) : m.start() + len(tok) + 40]
            if tok.lower() in ("series", "general", "model", "line"):
                continue
            idx = m.start()
            used = tok
            break
        if idx >= 0:
            break
    if idx < 0:
        return ""
    # take until next ALL-CAPS vehicle title (heuristic) or 2500 chars
    chunk = text[idx : idx + 2800]
    return chunk


def extract_equip_notes(chunk: str) -> tuple[str, str]:
    equip, notes = "", ""
    m = re.search(r"Standard\s*\n?\s*Equipment\s*\n(.*?)(?=\nNotes\b|\n>>|\Z)", chunk, re.S | re.I)
    if m:
        equip = re.sub(r"\s+", " ", m.group(1)).strip(" ,;")
        # cut if another vehicle name starts (all caps line)
        equip = re.split(r"\s(?=[A-Z]{2,}[A-Z\- ]{6,}$)", equip)[0][:300]
    m2 = re.search(r"\nNotes?\s*\n(.*?)(?=\nStandard\s*\n?\s*Equipment|\n>>|\n[A-Z][A-Z].{8,40}\n[A-Za-z]|\Z)", chunk, re.S | re.I)
    if m2:
        notes = re.sub(r"\s+", " ", m2.group(1)).strip()[:400]
        # drop shadowtalk
        if notes.startswith(">"):
            notes = ""
    return equip, notes


def load_pages(print_page: int) -> str:
    r5 = fitz.open(PDF / "rigger5.pdf")
    # Empirically: Cyclops print 43 -> PDF 44 -> index 43
    # Horseman print 41 -> PDF 42 -> index 41
    idxs = [print_page, print_page + 1, print_page - 1]
    parts = []
    for i in idxs:
        if 0 <= i < len(r5):
            parts.append(r5.load_page(i).get_text("text"))
    return "\n".join(parts).replace("\u2014", "-").replace("Ñ", "¥")


def main():
    results = {}
    for name, page in TOC:
        text = load_pages(page)
        chunk = find_vehicle_block(text, name)
        equip, notes = extract_equip_notes(chunk) if chunk else ("", "")
        # Also try whole text if chunk empty equip
        if not equip and not notes:
            # try searching Standard Equipment occurrences and score by name tokens nearby
            tokens = [t for t in re.split(r"[\s/\-\"\']+", name) if len(t) >= 4]
            best = None
            for m in re.finditer(r"Standard\s*\n?\s*Equipment\s*\n?", text, re.I):
                pre = text[max(0, m.start() - 400) : m.start()]
                score = sum(1 for t in tokens if t.lower() in pre.lower())
                if score and (best is None or score > best[0]):
                    after = text[m.end() : m.end() + 400]
                    lines = []
                    note_lines = []
                    mode = "e"
                    for ln in after.splitlines():
                        ln = ln.strip()
                        if not ln:
                            continue
                        if re.match(r"^Notes?$", ln, re.I):
                            mode = "n"
                            continue
                        if ln.startswith(">>"):
                            break
                        if mode == "e":
                            if re.match(r"^[A-Z][A-Za-z0-9].{0,35}$", ln) and lines and len(ln) < 40:
                                break
                            lines.append(ln)
                        else:
                            if re.match(r"^[A-Z][A-Za-z].{0,35}$", ln) and note_lines and len(ln) < 40:
                                break
                            note_lines.append(ln)
                    best = (
                        score,
                        re.sub(r"\s+", " ", " ".join(lines)).strip()[:300],
                        re.sub(r"\s+", " ", " ".join(note_lines)).strip()[:400],
                    )
            if best:
                equip, notes = best[1], best[2]
        results[name] = {"page": page, "equip": equip, "notes": notes, "ok": bool(equip or notes)}

    matched = sum(1 for v in results.values() if v["ok"])
    print(f"TOC entries with equip/notes: {matched}/{len(TOC)}")
    for name, v in results.items():
        if not v["ok"]:
            print(" NO RULES:", name, "p.", v["page"])
        else:
            print(" OK:", name)
            if v["equip"]:
                print("   E:", v["equip"][:120])
            if v["notes"]:
                print("   N:", v["notes"][:120])

    OUT.joinpath("veh_rules_by_toc.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Compare TOC to encyclopedia
    md = ENC.read_text(encoding="utf-8")
    print("\n=== Missing from Vehicles.md ===")
    for name, page in TOC:
        tokens = sorted(
            [t for t in re.split(r"[\s/\-\"\']+", name) if len(t) >= 5],
            key=len,
            reverse=True,
        )
        found = any(t.lower() in md.lower() for t in tokens[:2]) if tokens else False
        if not found:
            # try shorter
            tokens = [t for t in re.split(r"[\s/\-\"\']+", name) if len(t) >= 4]
            found = any(t.lower() in md.lower() for t in tokens[:3])
        if not found:
            print(" MISS", name, page)


if __name__ == "__main__":
    main()
