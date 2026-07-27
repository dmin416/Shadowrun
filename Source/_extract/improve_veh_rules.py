# -*- coding: utf-8 -*-
"""Improve vehicle Rules via printed page refs; fix names; rebuild catalog MD."""
import fitz
import json
import re
from pathlib import Path

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

NAME_FIX = {
    "KVP�28": "Mostrans KVP-28",
    "KVP-28": "Mostrans KVP-28",
    "St�rmwagon": "BMW Stormwagon",
    "Stormwagon": "BMW Stormwagon",
    "Commercial G�series": "Commercial G-series",
    "Stallion": None,  # context-dependent
}


def fix_name(v):
    n = v["name"]
    if "�" in n or "\ufffd" in n:
        if "KVP" in n:
            n = "Mostrans KVP-28"
        elif "wagon" in n.lower() or "St" in n:
            n = "BMW Stormwagon"
        elif "series" in n.lower():
            n = "Commercial G-series"
    # Disambiguate Stallion
    if n == "Stallion":
        if v["cat"] == "AIRCRAFT":
            n = "Hughes Stallion WK-4"
        elif v["cat"] == "SECURITY/POLICE/MILITARY":
            n = "Dodge Stallion"
    # Prefix well-known brands from common short names when helpful
    brand = {
        "Scoot": "Dodge Scoot",
        "Scorpion": "Harley-Davidson Scorpion",
        "Growler": "Yamaha Growler",
        "Mirage": "Suzuki Mirage",
        "Jackrabbit": "Chrysler-Nissan Jackrabbit",
        "Spirit": "Honda Spirit",
        "Shin-Hyung": "Hyundai Shin-Hyung",
        "Westwind 3000": "Eurocar Westwind 3000",
        "Americar": "Ford Americar",
        "Concordat": "S-K Bentley Concordat",
        "Nightsky": "Mitsubishi Nightsky",
        "Gopher": "Toyota Gopher",
        "Bulldog": "GMC Bulldog Step-Van",
        "Roadmaster": "Ares Roadmaster",
        "Rover Model 2072": "Rover Model 2072",
        "Otter": "Samuvani-Criscraft Otter",
        "Trinity": "Yongkang-Gala Trinity",
        "Cutlass": "Morgan Cutlass",
        "Lamprey": "Proteus Lamprey",
        "Waveskipper": "Aztechnology Nightrunner",  # NO - Waveskipper is Core jetski
        "Electronaut": "GMC Riverine",  # NO wrong
        "Banshee": "Ares Dragon",  # NO
    }
    # Only apply safe Core full names
    core_full = {
        "Scoot": "Dodge Scoot",
        "Scorpion": "Harley-Davidson Scorpion",
        "Growler": "Yamaha Growler",
        "Mirage": "Suzuki Mirage",
        "Jackrabbit": "Chrysler-Nissan Jackrabbit",
        "Spirit": "Honda Spirit",
        "Shin-Hyung": "Hyundai Shin-Hyung",
        "Westwind 3000": "Eurocar Westwind 3000",
        "Americar": "Ford Americar",
        "Concordat": "S-K Bentley Concordat",
        "Nightsky": "Mitsubishi Nightsky",
        "Gopher": "Toyota Gopher",
        "Bulldog": "GMC Bulldog Step-Van",
        "Roadmaster": "Ares Roadmaster",
        "Otter": "Samuvani-Criscraft Otter",
        "Trinity": "Yongkang-Gala Trinity",
        "Cutlass": "Morgan Cutlass",
        "Lamprey": "Proteus Lamprey",
        "Waveskipper": "Yamaha Waveskipper",
        "Tundra-9": "Federated-Boeing Tundra-9",
        "Commuter": "Ares Venture",  # WRONG - Commuter is separate
        "Wasp": "Ares Dragon",  # WRONG
        "Dragon": "Ares Dragon",
        "Banshee": "GMC Banshee",
        "Nightwing": "Northrup Nightwing",
        "Venture": "Ares Venture",
        "Cessna C750": "Cessna C750",
        "Hound": "Ares Roadmaster",  # WRONG - aircraft hound
    }
    safe_core = {
        "Scoot": "Dodge Scoot",
        "Scorpion": "Harley-Davidson Scorpion",
        "Growler": "Yamaha Growler",
        "Mirage": "Suzuki Mirage",
        "Jackrabbit": "Chrysler-Nissan Jackrabbit",
        "Spirit": "Honda Spirit",
        "Shin-Hyung": "Hyundai Shin-Hyung",
        "Westwind 3000": "Eurocar Westwind 3000",
        "Americar": "Ford Americar",
        "Concordat": "S-K Bentley Concordat",
        "Nightsky": "Mitsubishi Nightsky",
        "Gopher": "Toyota Gopher",
        "Bulldog": "GMC Bulldog Step-Van",
        "Roadmaster": "Ares Roadmaster",
        "Otter": "Samuvani-Criscraft Otter",
        "Trinity": "Yongkang-Gala Trinity",
        "Cutlass": "Morgan Cutlass",
        "Lamprey": "Proteus Lamprey",
        "Waveskipper": "Yamaha Waveskipper",
        "Dragon": "Ares Dragon",
        "Banshee": "GMC Banshee",
        "Nightwing": "Northrup Nightwing",
        "Venture": "Ares Venture",
        "Wasp": "Ares Wasp",
        "Tundra-9": "Federated-Boeing Tundra-9",
        "Artemis": "Honda Artemis",
        "Journey": "Chrysler-Nissan Journey",
        "Phaeton": "Rolls-Royce Phaeton",
        "Comet": "Mercury Comet",
        "Watcher": "Esprit Industries Watcher",
        "Sidewinder": "GMC Sidewinder",
        "Endurance": "GMC Endurance",
        "S-K LT-21": "S-K LT-21",
        "Cocotaxi HT": "Cocotaxi (Hard Targets)",
        "Camellos HT": "Camellos (Hard Targets)",
    }
    if n in safe_core:
        n = safe_core[n]
    v["name"] = n
    return v


def page_text_r5(page_num_print: int) -> str:
    """R5 PDF page index is print-1 for many pages; TOC says p.41 = PDF 41? Check: Horseman p.41 -> load 40."""
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    # Try print page as 1-indexed PDF page (common for Catalyst)
    idx = page_num_print - 1
    if 0 <= idx < len(r5):
        return r5.load_page(idx).get_text("text")
    return ""


def rules_from_page(text: str) -> str:
    text = text.replace("\u2014", "-").replace("Ñ", "¥")
    bits = []
    # Standard Equipment block
    m = re.search(r"Standard\s*\n?\s*Equipment\s*\n?(.*?)(?:\nNotes|\n>>|\n[A-Z]{3,} [A-Z]|$)", text, re.S | re.I)
    if m:
        equip = re.sub(r"\s+", " ", m.group(1)).strip(" ,;\n")
        # cut at next vehicle-looking ALL CAPS header if long
        equip = equip[:250]
        if equip:
            bits.append("Std Equip: " + equip)
    m2 = re.search(r"\nNotes?\s*\n(.*?)(?:\n>>|\nStandard|\n[A-Z][A-Za-z].{0,30}\n[a-z]|$)", text, re.S | re.I)
    if m2:
        notes = re.sub(r"\s+", " ", m2.group(1)).strip()[:300]
        if notes and not notes.startswith(">"):
            bits.append("Notes: " + notes)
    return "; ".join(bits)


def main():
    vehicles = json.loads(OUT.joinpath("veh_parsed.json").read_text(encoding="utf-8"))
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    core = fitz.open(PDF_DIR / "shadowrunfiftheditioncorerulebook_V2.pdf")

    for v in vehicles:
        fix_name(v)
        ref = v.get("ref") or ""
        # page number from "p. 43" or "p. 462, SR5"
        m = re.search(r"p\.\s*(\d+)", ref)
        if not m:
            continue
        page = int(m.group(1))
        if v.get("rules"):
            continue
        if "SR5" in ref or "sr5" in ref.lower():
            # Core print pages ~462-465 -> PDF often same-ish; try 467-471 area
            # Core vehicle table is PDF 470; descriptions 467-469
            blob = ""
            for i in range(466, 472):
                blob += core.load_page(i).get_text("text")
            # find name fragment
            for tok in re.split(r"[\s\-]+", v["name"])[-2:]:
                if len(tok) < 4:
                    continue
                idx = blob.lower().find(tok.lower())
                if idx >= 0:
                    snippet = blob[idx : idx + 800]
                    # Core rarely has Std Equip; pull mechanical sentences
                    mech = []
                    if "weapon mount" in snippet.lower():
                        mech.append(re.search(r".{0,40}weapon mount.{0,80}", snippet, re.I).group(0))
                    if mech:
                        v["rules"] = re.sub(r"\s+", " ", "; ".join(mech))[:400]
                    break
            continue
        if "Stolen" in ref:
            continue
        if "Hard Targets" in ref:
            v["rules"] = "Hard Targets SKU (no local PDF); stats from R5 compiled table only."
            continue
        # R5 chapter page
        idx = page - 1
        if 0 <= idx < len(r5):
            t = r5.load_page(idx).get_text("text")
            # also next page (entries span)
            if idx + 1 < len(r5):
                t += "\n" + r5.load_page(idx + 1).get_text("text")
            got = rules_from_page(t)
            if got:
                v["rules"] = got

    matched = sum(1 for v in vehicles if v.get("rules"))
    print("matched", matched, "/", len(vehicles))
    print("still unmatched", [v["name"] for v in vehicles if not v.get("rules")])

    OUT.joinpath("veh_parsed.json").write_text(
        json.dumps(vehicles, indent=2, ensure_ascii=False), encoding="utf-8"
    )
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
    lines = []
    for cat in CAT_ORDER:
        rows = [v for v in vehicles if v["cat"] == cat]
        if not rows:
            continue
        title = {
            "SECURITY/POLICE/MILITARY": "Security / Police / Military",
            "TRACTOR/TRAILERS": "Tractor / Trailers",
        }.get(cat, cat.title())
        lines.append(f"### {title}")
        lines.append("")
        lines.append(
            "| Name | Sub | Src | Handl | Speed | Accel | Body | Armor | Pilot | Sens | Seats | Avail | Cost | Ref | Rules |"
        )
        lines.append(
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
        )
        for v in rows:
            rules = (v.get("rules") or "-").replace("|", "/")
            if not rules.strip():
                rules = "-"
            sub = v.get("sub") or "-"
            lines.append(
                f"| {v['name']} | {sub} | {v['src']} | {v['handl']} | {v['speed']} | {v['accel']} | {v['body']} | {v['armor']} | {v['pilot']} | {v['sens']} | {v['seats']} | {v['avail']} | {v['cost']} | {v['ref']} | {rules} |"
            )
        lines.append("")
    OUT.joinpath("veh_catalog_body.md").write_text("\n".join(lines), encoding="utf-8")
    print("catalog lines", len(lines))


if __name__ == "__main__":
    main()
