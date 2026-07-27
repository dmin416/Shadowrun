# -*- coding: utf-8 -*-
"""Attach Standard Equipment / Notes rules to parsed vehicles; emit catalog MD."""
import fitz
import json
import re
from pathlib import Path

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")


def load_chapter_text():
    text = ""
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    for i in range(40, 110):
        text += "\n" + r5.load_page(i).get_text("text")
    core = fitz.open(PDF_DIR / "shadowrunfiftheditioncorerulebook_V2.pdf")
    for i in range(466, 472):
        text += "\n" + core.load_page(i).get_text("text")
    ss = fitz.open(PDF_DIR / "stolensouls.pdf")
    for i in range(186, 201):
        text += "\n" + ss.load_page(i).get_text("text")
    return text.replace("\u2014", "-").replace("Ñ", "¥").replace("�", "-")


def extract_std_blocks(text):
    hits = []
    for m in re.finditer(r"Standard\s*\n?\s*Equipment\s*\n?", text, re.I):
        after = text[m.end() : m.end() + 500]
        lines = []
        notes = []
        mode = "equip"
        for ln in after.splitlines():
            raw = ln
            ln = ln.strip()
            if not ln:
                if lines and mode == "equip":
                    # blank after equipment may start Notes or next vehicle
                    continue
                if notes:
                    break
                continue
            if ln.startswith(">>") or ln.startswith("<<"):
                break
            if re.match(r"^Notes?\s*$", ln, re.I):
                mode = "notes"
                continue
            if mode == "notes":
                if re.match(r"^[A-Z][A-Za-z].{0,50}$", ln) and len(ln) < 40 and notes:
                    # possible next vehicle title
                    if not any(
                        k in ln.lower()
                        for k in (
                            "mount",
                            "decrease",
                            "increase",
                            "adds",
                            "passenger",
                            "cargo",
                            "drone",
                            "security",
                            "handling",
                            "speed",
                            "accel",
                            "seats",
                        )
                    ):
                        break
                notes.append(ln)
                continue
            # equipment mode
            if re.match(r"^[A-Z][A-Za-z0-9].{0,40}$", ln) and lines and len(ln) < 35:
                # next vehicle name likely
                break
            lines.append(ln)
        upg = re.sub(r"\s+", " ", " ".join(lines)).strip(" ,;")
        note = re.sub(r"\s+", " ", " ".join(notes)).strip()
        pre = text[max(0, m.start() - 500) : m.start()]
        hits.append({"pre": pre, "equip": upg, "notes": note})
    return hits


def tokens(name):
    parts = re.split(r'[\s/\-"\']+', name)
    return sorted(
        {p for p in parts if len(p) >= 3 and p.lower() not in ("the", "and", "model")},
        key=len,
        reverse=True,
    )


def attach(vehicles, hits):
    for v in vehicles:
        toks = tokens(v["name"])
        best = None
        for h in hits:
            pre_l = h["pre"].lower()
            score = sum(1 for t in toks[:4] if t.lower() in pre_l)
            if score and (best is None or score > best[0]):
                best = (score, h)
        bits = []
        if best:
            h = best[1]
            if h["equip"]:
                bits.append("Std Equip: " + h["equip"])
            if h["notes"]:
                bits.append("Notes: " + h["notes"])
        v["rules"] = "; ".join(bits)[:600]
    return vehicles


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


def fix_names(vehicles):
    for v in vehicles:
        v["name"] = (
            v["name"]
            .replace("KVP-28", "KVP-28")
            .replace("KVP�28", "KVP-28")
            .replace("St�rmwagon", "Stormwagon")
            .replace("Stormwagon", "Stormwagon")
            .replace("Commercial G�series", "Commercial G-series")
            .replace("Commercial G-series", "Commercial G-series")
        )
        # encoding fix via unicode replace of replacement char
        if "\ufffd" in v["name"] or "�" in v["name"]:
            n = v["name"]
            if "KVP" in n:
                v["name"] = "KVP-28"
            elif "rmwagon" in n or "Storm" in n or "St" in n and "wagon" in n:
                v["name"] = "Stormwagon"
            elif "G" in n and "series" in n:
                v["name"] = "Commercial G-series"
    return vehicles


def to_markdown(vehicles):
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
    return "\n".join(lines)


def main():
    vehicles = json.loads(OUT.joinpath("veh_parsed.json").read_text(encoding="utf-8"))
    # Re-parse to get clean list without drone contamination - use parse_vehicles3 output already
    vehicles = fix_names(vehicles)
    # Drop any drone leftovers if present
    vehicles = [v for v in vehicles if not v["name"].upper().startswith("DRONES")]
    text = load_chapter_text()
    hits = extract_std_blocks(text)
    print("std blocks", len(hits))
    vehicles = attach(vehicles, hits)
    matched = sum(1 for v in vehicles if v.get("rules"))
    print("matched", matched, "/", len(vehicles))
    print("unmatched", [v["name"] for v in vehicles if not v.get("rules")])
    OUT.joinpath("veh_parsed.json").write_text(
        json.dumps(vehicles, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    OUT.joinpath("veh_catalog_body.md").write_text(
        to_markdown(vehicles), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
