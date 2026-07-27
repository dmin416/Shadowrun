# -*- coding: utf-8 -*-
"""Parse R5 compiled vehicle tables + extract special rules into Vehicles.md blocks."""
import fitz
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

KNOWN_CATS = {
    "MOTORCYCLES",
    "CARS",
    "TRUCKS AND VANS",
    "BUSES",
    "CONSTRUCTION AND MUNICIPAL",
    "CORPSEC AND POLICE",
    "MILITARY AND RESTRICTED",
    "BOATS",
    "SUBMARINES",
    "HOVERCRAFT",
    "FIXED-WING AIRCRAFT",
    "ROTORCRAFT",
    "LTAVS",
    "LAVS",
    "VTOL/VSTOL",
    "AIRSHIPS",
    "ZEPPELINS",
}

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


def is_numish(s: str) -> bool:
    if s in ("ù", "-", "—", "", "*", "ù*"):
        return True
    if re.match(r"^\d+[RF]?$", s):
        return True
    if re.match(r"^\d+[RF]?\*$", s):
        return True
    s2 = s.replace("Ñ", "").replace("¥", "").replace(",", "").replace("ù", "")
    if re.match(r"^\d+(\.\d+)?$", s2):
        return True
    if "/" in s:
        parts = s.split("/")
        if all(re.match(r"^\d+(\.\d+)?$", p) or p == "" for p in parts):
            return True
    if re.match(r"^\d+\(\d+\)$", s):
        return True
    if re.match(r"^\d+/\d+$", s):
        return True
    return False


def normalize_yen(s: str) -> str:
    s = s.replace("Ñ", "¥").replace("�", "¥")
    if s and not s.endswith("¥") and re.match(r"^[\d,]+$", s):
        s = s + "¥"
    if s in ("ù", "-", "—"):
        return "-"
    return s


def normalize_avail(s: str) -> str:
    if s in ("ù", "-", "—", ""):
        return "-"
    return s.replace("ù", "-")


def parse_compiled():
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    text = ""
    for i in range(184, 190):
        text += "\n" + r5.load_page(i).get_text("text")
    # cut at drones
    for marker in ("MICRODRONES", "\nDRONES\n"):
        j = text.find(marker)
        if j >= 0:
            text = text[:j]
            break
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
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
        if (
            ln in SKIP
            or ln.startswith(">>")
            or ln.startswith("<<")
            or ("RIGGER" in ln and "<<" in ln)
            or ln.startswith("p.")
            or ln.startswith("pp.")
        ):
            i += 1
            continue
        if cur is None:
            i += 1
            continue
        name = ln
        if name.upper() in SKIP:
            i += 1
            continue
        fields = []
        j = i + 1
        while j < len(lines) and len(fields) < 14:
            lj = lines[j]
            if lj.upper() in KNOWN_CATS:
                break
            if lj.startswith(">>") or lj.startswith("<<") or lj in SKIP:
                j += 1
                continue
            fields.append(lj)
            j += 1
            if lj.startswith("p.") or lj.startswith("pp."):
                break
            if len(fields) >= 10 and (
                "Ñ" in lj
                or "¥" in lj
                or re.match(r"^[\d,]+$", lj)
                or lj.startswith("p.")
            ):
                if j < len(lines) and (
                    lines[j].startswith("p.") or lines[j].startswith("pp.")
                ):
                    fields.append(lines[j])
                    j += 1
                    break
                if lj.startswith("p."):
                    break
        if len(fields) >= 10:
            ref = ""
            cost = ""
            data = fields[:]
            if data and (data[-1].startswith("p.") or data[-1].startswith("pp.")):
                ref = data.pop()
            if data:
                cost = data.pop()
            while len(data) > 9 and not is_numish(data[0]):
                name = name + " " + data.pop(0)
            if len(data) == 9:
                handl, speed, accel, body, armor, pilot, sens, seats, avail = data
                out.append(
                    {
                        "cat": cur,
                        "name": name,
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
                    }
                )
                i = j
                continue
        i += 1
    return out


def extract_core_table():
    """Core Street Gear vehicle buy table pages."""
    core = fitz.open(PDF_DIR / "shadowrunfiftheditioncorerulebook_V2.pdf")
    # tables are on PDF 470-471 typically
    text = ""
    for i in range(468, 472):
        text += "\n" + core.load_page(i).get_text("text")
    return text


def extract_special_rules():
    """Pull RULES-like mechanical notes from R5 vehicle chapters (PDF 41-110)."""
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    rules = {}
    # Also Core vehicle descriptions for mechanical bits
    # Pattern: lines after vehicle name headers that contain mechanical keywords
    mech_kw = re.compile(
        r"(Weapon Mount|weapon mount|rigger interface|Standard Equipment|"
        r"Standard Upgrades|Rules:|Mod Points|amphibious|hover|"
        r"\+\d |-\d |dice|limit|Armor |Body |Pilot |Sensor |"
        r"Avail|¥|nuyen|hot-sim|cold-sim|ECM|drone rack|"
        r"takes off|landing|submerge|depth|GridGuide|manual)",
        re.I,
    )
    for i in range(40, 110):
        t = r5.load_page(i).get_text("text")
        # split on ALL-CAPS-ish vehicle name lines is hard; store page blobs keyed later
        rules[f"r5_p{i+1}"] = t
    return rules


def map_src(ref: str) -> str:
    if not ref:
        return "R5"
    r = ref.lower()
    if "sr5" in r or "core" in r:
        return "Core"
    if "stolen" in r:
        return "SS"
    if "hard targets" in r:
        return "HT"
    if "rigger" in r:
        return "R5"
    # default chapter refs are R5
    if re.match(r"^p\.\s*\d+", ref):
        return "R5"
    return "R5"


def main():
    vehicles = parse_compiled()
    print("parsed", len(vehicles))
    print(Counter(v["cat"] for v in vehicles))
    # sanity: list names
    names = [v["name"] for v in vehicles]
    print("sample", names[:20])
    print("last", names[-10:])
    OUT.joinpath("veh_parsed.json").write_text(
        json.dumps(vehicles, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Dump chapter text for rule mining
    r5 = fitz.open(PDF_DIR / "rigger5.pdf")
    chunks = []
    for i in range(40, 110):
        chunks.append(f"\n===== R5 PDF {i+1} =====\n" + r5.load_page(i).get_text("text"))
    OUT.joinpath("veh_r5_chapters.txt").write_text("".join(chunks), encoding="utf-8")

    core = fitz.open(PDF_DIR / "shadowrunfiftheditioncorerulebook_V2.pdf")
    core_chunks = []
    for i in range(466, 472):
        core_chunks.append(
            f"\n===== CORE PDF {i+1} =====\n" + core.load_page(i).get_text("text")
        )
    OUT.joinpath("veh_core_chapters.txt").write_text(
        "".join(core_chunks), encoding="utf-8"
    )

    # Stolen Souls vehicle stats
    ss = fitz.open(PDF_DIR / "stolensouls.pdf")
    ss_chunks = []
    for i in range(186, 201):
        t = ss.load_page(i).get_text("text")
        if "HANDL" in t or "Artemis" in t or "Journey" in t or "VEHICLE" in t:
            ss_chunks.append(f"\n===== SS PDF {i+1} =====\n" + t)
    OUT.joinpath("veh_ss.txt").write_text("".join(ss_chunks), encoding="utf-8")

    # Street Lethal / Complete Trog
    for pdfn, start, end, outn in [
        ("streetlethal.pdf", 50, 60, "veh_sl.txt"),
        ("completetrog.pdf", 140, 150, "veh_ct.txt"),
    ]:
        doc = fitz.open(PDF_DIR / pdfn)
        parts = []
        for i in range(start, min(end, len(doc))):
            t = doc.load_page(i).get_text("text")
            if "HANDL" in t or "Seats" in t or "vehicle" in t.lower():
                parts.append(f"\n===== {pdfn} PDF {i+1} =====\n" + t)
        OUT.joinpath(outn).write_text("".join(parts), encoding="utf-8")

    print("dumps done")


if __name__ == "__main__":
    main()
