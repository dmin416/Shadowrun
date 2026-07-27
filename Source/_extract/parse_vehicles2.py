# -*- coding: utf-8 -*-
"""Parse R5 compiled vehicle tables into clean JSON + markdown catalog."""
import fitz
import json
import re
from pathlib import Path
from collections import Counter

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

KNOWN_CATS = [
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


def parse_compiled():
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    text = ""
    for i in range(184, 190):
        text += "\n" + r5.load_page(i).get_text("text")
    # cut drones
    for marker in ("MICRODRONES",):
        j = text.find(marker)
        if j >= 0:
            text = text[:j]
            break

    lines = []
    for ln in text.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if HEADER_RE.search(ln):
            continue
        if ln in (">> RIGGER 5.0 <<",):
            continue
        lines.append(ln)

    cur = None
    out = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        up = ln.upper()
        if up in KNOWN_CATS:
            cur = up
            i += 1
            continue
        if ln in SKIP or ln.startswith("p.") or ln.startswith("pp."):
            i += 1
            continue
        if cur is None:
            i += 1
            continue

        name = ln
        # skip garbage names
        if name.upper() in SKIP or "COMPILED" in name.upper():
            i += 1
            continue

        fields = []
        j = i + 1
        while j < len(lines) and len(fields) < 14:
            lj = lines[j]
            if lj.upper() in KNOWN_CATS:
                break
            if lj in SKIP:
                j += 1
                continue
            fields.append(lj)
            j += 1
            if lj.startswith("p.") or lj.startswith("pp."):
                break
            if len(fields) >= 10:
                # cost then maybe ref
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
                out.append(
                    {
                        "cat": cur,
                        "name": clean_name(name),
                        "handl": handl,
                        "speed": speed,
                        "accel": accel,
                        "body": body,
                        "armor": armor,
                        "pilot": pilot,
                        "sens": sens,
                        "seats": seats,
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


def clean_name(name: str) -> str:
    name = name.replace("�", '"').replace("“", '"').replace("”", '"')
    name = re.sub(r"\s+", " ", name).strip()
    return name


def mine_rules(vehicles):
    """Attach short Rules strings from chapter text by matching vehicle name fragments."""
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    chapter = ""
    for i in range(40, 110):
        chapter += "\n" + r5.load_page(i).get_text("text")
    core = fitz.open(PDF_DIR / "shadowrunfiftheditioncorerulebook_V2.pdf")
    for i in range(466, 472):
        chapter += "\n" + core.load_page(i).get_text("text")
    ss = fitz.open(PDF_DIR / "stolensouls.pdf")
    for i in range(186, 201):
        chapter += "\n" + ss.load_page(i).get_text("text")

    # Normalize chapter for search
    chapter_n = chapter.replace("\u2014", "-").replace("Ñ", "¥")

    # Standard equipment lines often follow "Standard Upgrades:" or similar
    std_re = re.compile(
        r"(Standard (?:Upgrades|Equipment|Features|Features/Upgrades)\s*[:：]\s*[^\n]+(?:\n(?![A-Z][A-Z].{0,40}$)[^\n]+)*)",
        re.I,
    )

    # For each vehicle, find nearest mention and pull nearby mechanical sentences
    for v in vehicles:
        key = v["name"].split()[-1] if v["name"] else ""
        # Prefer longer distinctive tokens
        tokens = [t for t in re.split(r"[\s/\-\"']+", v["name"]) if len(t) >= 4]
        tokens = sorted(set(tokens), key=len, reverse=True)
        blob = ""
        for tok in tokens[:3]:
            # find case-insensitive
            m = re.search(re.escape(tok), chapter_n, re.I)
            if not m:
                continue
            start = max(0, m.start() - 200)
            end = min(len(chapter_n), m.end() + 1200)
            blob = chapter_n[start:end]
            break
        rules_bits = []
        if blob:
            for pat in (
                r"Standard Upgrades?:\s*[^\n]+",
                r"Standard Equipment:\s*[^\n]+",
                r"Weapon Mount[^\n]{0,120}",
                r"Rigger Interface[^\n]{0,80}",
                r"Mod Points[^\n]{0,80}",
            ):
                mm = re.search(pat, blob, re.I)
                if mm:
                    bit = re.sub(r"\s+", " ", mm.group(0)).strip()
                    if bit not in rules_bits:
                        rules_bits.append(bit)
        v["rules_auto"] = "; ".join(rules_bits)[:400]
    return vehicles


def to_markdown(vehicles):
    cat_order = KNOWN_CATS
    by = {c: [] for c in cat_order}
    for v in vehicles:
        by.setdefault(v["cat"], []).append(v)

    lines = []
    for cat in cat_order:
        rows = by.get(cat) or []
        if not rows:
            continue
        lines.append(f"### {cat.title()}")
        lines.append("")
        lines.append(
            "| Name | Src | Handl | Speed | Accel | Body | Armor | Pilot | Sens | Seats | Avail | Cost | Ref | Rules |"
        )
        lines.append(
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
        )
        for v in rows:
            rules = (v.get("rules_auto") or "").replace("|", "/")
            lines.append(
                "| {name} | {src} | {handl} | {speed} | {accel} | {body} | {armor} | {pilot} | {sens} | {seats} | {avail} | {cost} | {ref} | {rules} |".format(
                    **{**v, "rules": rules or "-"}
                )
            )
        lines.append("")
    return "\n".join(lines)


def main():
    vehicles = parse_compiled()
    print("parsed", len(vehicles), Counter(v["cat"] for v in vehicles))
    # list any suspicious
    for v in vehicles:
        if "COMPILED" in v["name"] or len(v["name"]) > 45:
            print("SUSPECT", v)
    vehicles = mine_rules(vehicles)
    OUT.joinpath("veh_parsed.json").write_text(
        json.dumps(vehicles, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    OUT.joinpath("veh_catalog_body.md").write_text(
        to_markdown(vehicles), encoding="utf-8"
    )
    print("wrote catalog body", len(vehicles))
    for c in KNOWN_CATS:
        n = sum(1 for v in vehicles if v["cat"] == c)
        if n:
            print(f"  {c}: {n}")


if __name__ == "__main__":
    main()
