# -*- coding: utf-8 -*-
"""Parse R5 compiled vehicle tables (no drones) into JSON + markdown body."""
import fitz
import json
import re
from pathlib import Path
from collections import Counter

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

TOP_CATS = {
    "MOTORCYCLES",
    "CARS",
    "TRUCKS",
    "TRACTOR/TRAILERS",
    "HOVERCRAFT",
    "BUSES",
    "WATERCRAFT",
    "SECURITY/POLICE/MILITARY",
    "AIRCRAFT",
}

SUB_CATS = {"VANS", "RVS", "LIMOS", "COMMERCIAL"}

STOP_CATS = {"DRONES", "DRONES, CONT.", "DRONES, CONT"}

SKIP = {
    "NAME",
    "HANDL",
    "SPEED",
    "ACCEL",
    "BODY",
    "ARMOR",
    "PILOT",
    "SENS",
    "SEATS",
    "AVAIL",
    "COST",
    "REF",
    "SEATS AVAIL",
}

HEADER_RE = re.compile(
    r"^(\d+\s+)?>>\s*COMPILED TABLES|^>>\s*RIGGER|^<<\s*COMPILED|^\d+\s+>>"
)


def is_numish(s: str) -> bool:
    if s in ("ù", "-", "—", "", "*", "ù*", "—*", "-*"):
        return True
    if re.match(r"^\d+[RF]?\*?$", s):
        return True
    s2 = (
        s.replace("Ñ", "")
        .replace("¥", "")
        .replace(",", "")
        .replace("ù", "")
        .replace("—", "")
        .replace("*", "")
    )
    if re.match(r"^\d+(\.\d+)?$", s2):
        return True
    if "/" in s:
        parts = s.replace("*", "").split("/")
        if all(re.match(r"^\d+(\.\d+)?$", p) or p == "" for p in parts):
            return True
    if re.match(r"^\d+\(\d+\)$", s):
        return True
    return False


def normalize_yen(s: str) -> str:
    s = s.replace("Ñ", "¥").replace("�", "¥").strip()
    if s in ("ù", "-", "—"):
        return "-"
    if s and "¥" not in s and re.match(r"^[\d,]+$", s):
        s = s + "¥"
    return s


def normalize_avail(s: str) -> str:
    if s in ("ù", "-", "—", ""):
        return "-"
    return s.replace("ù", "-").replace("—", "-")


def map_src(ref: str) -> str:
    r = (ref or "").lower()
    if "sr5" in r:
        return "Core"
    if "stolen" in r:
        return "SS"
    if "hard targets" in r:
        return "HT*"
    return "R5"


def clean_name(name: str) -> str:
    name = name.replace("�", "-").replace("“", '"').replace("”", '"')
    name = name.replace("\u00ad", "")  # soft hyphen
    name = re.sub(r"\s+", " ", name).strip()
    # fix known OCR/encoding
    repl = {
        "KVP-28": "KVP-28",
        "KVP�28": "KVP-28",
        "St�rmwagon": "Stormwagon",
        "Commercial G�series": "Commercial G-series",
        "Ram Industrail Narrow": "Ram Industrial Narrow",
        '"Lift-Ticket" ALS-669': '"Lift-Ticket" ALS-699',
    }
    return repl.get(name, name)


def parse_compiled():
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    text = ""
    for i in range(184, 190):
        text += "\n" + r5.load_page(i).get_text("text")

    lines = []
    for ln in text.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if HEADER_RE.search(ln):
            continue
        lines.append(ln)

    cur = None
    sub = ""
    out = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        up = ln.upper().rstrip(".")
        # stop at drones
        if ln.upper().startswith("DRONES"):
            break
        if ln.upper() in TOP_CATS or up in TOP_CATS:
            cur = ln.upper()
            sub = ""
            i += 1
            continue
        if ln.upper() in SUB_CATS:
            sub = ln.upper()
            i += 1
            continue
        if ln in SKIP or ln.startswith("p.") or ln.startswith("pp."):
            i += 1
            continue
        if cur is None:
            i += 1
            continue
        if "COMPILED" in ln.upper():
            i += 1
            continue

        name = ln
        fields = []
        j = i + 1
        while j < len(lines) and len(fields) < 14:
            lj = lines[j]
            lju = lj.upper()
            if lju.startswith("DRONES"):
                break
            if lju in TOP_CATS or lju in SUB_CATS:
                break
            if lj in SKIP:
                j += 1
                continue
            fields.append(lj)
            j += 1
            if lj.startswith("p.") or lj.startswith("pp."):
                break
            if len(fields) >= 10:
                if j < len(lines) and (
                    lines[j].startswith("p.") or lines[j].startswith("pp.")
                ):
                    fields.append(lines[j])
                    j += 1
                    break
                if "¥" in lj or "Ñ" in lj or re.match(r"^[\d,]+$", lj):
                    if j < len(lines) and lines[j].startswith("p."):
                        fields.append(lines[j])
                        j += 1
                    break

        if len(fields) >= 10:
            data = fields[:]
            ref = ""
            if data and (data[-1].startswith("p.") or data[-1].startswith("pp.")):
                ref = data.pop()
            cost = data.pop() if data else ""
            while len(data) > 9 and not is_numish(data[0]):
                name = name + " " + data.pop(0)
            if len(data) == 9:
                handl, speed, accel, body, armor, pilot, sens, seats, avail = data
                # skip if name is clearly a header fragment
                if name.upper() in TOP_CATS | SUB_CATS | SKIP:
                    i = j
                    continue
                out.append(
                    {
                        "cat": cur,
                        "sub": sub,
                        "name": clean_name(name),
                        "handl": handl.replace("—", "-").replace("ù", "-"),
                        "speed": speed.replace("—", "-").replace("ù", "-"),
                        "accel": accel.replace("—", "-").replace("ù", "-"),
                        "body": body.replace("—", "-").replace("ù", "-"),
                        "armor": armor.replace("—", "-").replace("ù", "-"),
                        "pilot": pilot.replace("—", "-").replace("ù", "-"),
                        "sens": sens.replace("—", "-").replace("ù", "-"),
                        "seats": seats.replace("—", "-").replace("ù", "-"),
                        "avail": normalize_avail(avail),
                        "cost": normalize_yen(cost),
                        "ref": ref,
                        "src": map_src(ref),
                    }
                )
                i = j
                continue
        i += 1
    return out


def extract_std_upgrades():
    """Map approximate Standard Upgrades text by scanning R5 chapters."""
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    text = ""
    for i in range(40, 110):
        text += "\n" + r5.load_page(i).get_text("text")
    core = fitz.open(PDF_DIR / "shadowrunfiftheditioncorerulebook_V2.pdf")
    for i in range(466, 472):
        text += "\n" + core.load_page(i).get_text("text")
    ss = fitz.open(PDF_DIR / "stolensouls.pdf")
    for i in range(186, 201):
        text += "\n" + ss.load_page(i).get_text("text")

    text = text.replace("\u2014", "-").replace("Ñ", "¥").replace("�", "-")

    # Find all "Standard Upgrades:" occurrences with preceding ~80 chars for name hint
    hits = []
    for m in re.finditer(r"Standard Upgrades?:\s*([^\n]+)", text, re.I):
        pre = text[max(0, m.start() - 300) : m.start()]
        upgrades = re.sub(r"\s+", " ", m.group(1)).strip()
        hits.append((pre, upgrades))
    return hits, text


def attach_rules(vehicles, hits, chapter_text):
    for v in vehicles:
        tokens = [
            t
            for t in re.split(r'[\s/\-"\']+', v["name"])
            if len(t) >= 4 and t.lower() not in ("model", "series")
        ]
        tokens = sorted(set(tokens), key=len, reverse=True)
        rules = []
        for pre, upg in hits:
            if any(tok.lower() in pre.lower() for tok in tokens[:2]):
                rules.append("Std: " + upg)
                break
        # Extra mechanical lines near name
        for tok in tokens[:2]:
            m = re.search(re.escape(tok), chapter_text, re.I)
            if not m:
                continue
            blob = chapter_text[m.start() : m.start() + 1500]
            for pat in (
                r"Weapon mounts?:[^\n]+",
                r"comes (?:armed|standard)[^\n]{0,160}",
                r"Rigger [Ii]nterface[^\n]{0,100}",
                r"GridGuide[^\n]{0,100}",
                r"amphibious[^\n]{0,120}",
                r"Mod Points[^\n]{0,80}",
            ):
                mm = re.search(pat, blob, re.I)
                if mm:
                    bit = re.sub(r"\s+", " ", mm.group(0)).strip()
                    if bit not in rules and len(bit) < 220:
                        rules.append(bit)
            break
        v["rules"] = "; ".join(rules)[:500] if rules else ""
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


def to_markdown(vehicles):
    lines = []
    for cat in CAT_ORDER:
        rows = [v for v in vehicles if v["cat"] == cat]
        if not rows:
            continue
        title = cat.title().replace("Security/Police/Military", "Security / Police / Military")
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
            sub = v.get("sub") or "-"
            lines.append(
                f"| {v['name']} | {sub} | {v['src']} | {v['handl']} | {v['speed']} | {v['accel']} | {v['body']} | {v['armor']} | {v['pilot']} | {v['sens']} | {v['seats']} | {v['avail']} | {v['cost']} | {v['ref']} | {rules} |"
            )
        lines.append("")
    return "\n".join(lines)


def main():
    vehicles = parse_compiled()
    print("parsed", len(vehicles), Counter(v["cat"] for v in vehicles))
    hits, chapter = extract_std_upgrades()
    print("std upgrade hits", len(hits))
    vehicles = attach_rules(vehicles, hits, chapter)
    OUT.joinpath("veh_parsed.json").write_text(
        json.dumps(vehicles, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    OUT.joinpath("veh_catalog_body.md").write_text(
        to_markdown(vehicles), encoding="utf-8"
    )
    for c in CAT_ORDER:
        names = [v["name"] for v in vehicles if v["cat"] == c]
        print(c, len(names), names)
    # duplicates
    from collections import Counter as C

    d = C(v["name"] for v in vehicles)
    print("dups", [x for x in d.items() if x[1] > 1])


if __name__ == "__main__":
    main()
