# -*- coding: utf-8 -*-
"""Formatting pass for Bullets & Bandages Source Texts chapters.

Conservative: only promote known section/item titles to headings.
Re-run extract before this if chapter bodies were previously over-formatted.
"""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Bullets and Bandages")
SKIP = {"INDEX.md"}

DASHES = (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"))

# key -> display heading
SECTION_H2: dict[str, str] = {
    "docwagon at a glance": "DocWagon at a Glance",
    "introduction": "Introduction",
    "high threat response": "High Threat Response",
    "medical training": "Medical Training",
    "tactical operations": "Tactical Operations",
    "physical training": "Physical Training",
    "conclusion": "Conclusion",
    "building a medic character": "Building a Medic Character",
    "metatype and attributes": "Metatype and Attributes",
    "skills": "Skills",
    "qualities": "Qualities",
    "gear and other resources": "Gear and Other Resources",
    "new qualities": "New Qualities",
    "positive quality": "Positive Quality",
    "negative qualities": "Negative Qualities",
    "biotech, knowledge skills, and data search (optional rule)": (
        "Biotech, Knowledge Skills, and Data Search (Optional Rule)"
    ),
    "biotech actions": "Biotech Actions",
    "free actions": "Free Actions",
    "simple actions": "Simple Actions",
    "complex actions": "Complex Actions",
    "care under fire (optional rules)": "Care Under Fire (Optional Rules)",
    "damage progression": "Damage Progression",
    "stabilization tests": "Stabilization Tests",
    "stabilization and magic": "Stabilization and Magic",
    "using trauma patches and crash": "Using Trauma Patches and Crash",
    "diagnosis tests": "Diagnosis Tests",
    "diagnosis and magic": "Diagnosis and Magic",
    "treatment tests": "Treatment Tests",
    "treatment and magic": "Treatment and Magic",
    "pregnancy quality": "Pregnancy Quality",
    "illness quality": "Illness Quality",
    "glossary": "Glossary",
    "advanced medkit and autodoc rules": "Advanced Medkit and Autodoc Rules",
    "medical expert systems": "Medical Expert Systems",
    "components and capabilities": "Components and Capabilities",
    "using medkits and autodocs": "Using Medkits and Autodocs",
    "expending medkit supplies": "Expending Medkit Supplies",
    "upgrading medkits": "Upgrading Medkits",
    "improvised medical supplies": "Improvised Medical Supplies",
    "new drugs, toxins, and pathogens": "New Drugs, Toxins, and Pathogens",
    "drugs": "Drugs",
    "toxins": "Toxins",
    "pathogens": "Pathogens",
    "new spells and powers": "New Spells and Powers",
    "spells": "Spells",
    "adept powers": "Adept Powers",
    "new gear": "New Gear",
    "biotech gear": "Biotech Gear",
    "armor and armor modifications": "Armor and Armor Modifications",
    "drones": "Drones",
    "biotech skill ratings (sr4a)": "Biotech Skill Ratings (SR4A)",
    "biotech skill ratings (sr5)": "Biotech Skill Ratings (SR5)",
}

ITEM_PARENTS = {
    "new qualities",
    "positive quality",
    "negative qualities",
    "drugs",
    "toxins",
    "pathogens",
    "spells",
    "adept powers",
    "biotech gear",
    "armor and armor modifications",
    "drones",
    "new gear",
}

# Strict whitelist for ### item headings
KNOWN_ITEMS: dict[str, str] = {
    "gifted healer": "Gifted Healer",
    "aged": "Aged",
    "harrowed": "Harrowed",
    "illness": "Illness",
    "crash": "Crash",
    "cryo": "Cryo",
    "hemosynth": "Hemosynth",
    "nanoscan": "Nanoscan",
    "neostigmine": "Neostigmine",
    "ondansetron": "Ondansetron",
    "dread": "Dread",
    "picrotoxin": "Picrotoxin",
    "retro": "Retro",
    "rocuronium": "Rocuronium",
    "cryptococcus metaformans": "Cryptococcus Metaformans",
    "cypher": "Cypher",
    "red masque": "Red Masque",
    "death replay": "Death Replay",
    "incision (manipulation/physical)": "Incision (Manipulation/Physical)",
    "incision": "Incision",
    "feign illness": "Feign Illness",
    "feign death": "Feign Death",
    "transmit damage": "Transmit Damage",
    "vasotech autoinjection gun": "Vasotech Autoinjection Gun",
    "vasotech rapid infuser": "Vasotech Rapid Infuser",
    "docwagon hemostatix dressing": "DocWagon HemostatiX Dressing",
    "ge statscan": "GE STATscan",
    "pneumatic anti-shock garments": "Pneumatic Anti-Shock Garments",
    "drag handle": "Drag Handle",
    'aeroquip m.e.d.-1 "dustoff"': 'Aeroquip M.E.D.-1 "Dustoff"',
    'shiawase caduceus "cad" 7': 'Shiawase Caduceus "CAD" 7',
}

JUNK = re.compile(
    r"^(?:"
    r">>\s*SHADOWRUN\s*<<"
    r"|<<\s*BULLETS\s*&\s*BANDAGES\s+\d+"
    r"|BULLETS\s*&\s*BANDAGES\s+\d+"
    r"|PRIMUM NON NOCERE"
    r"|COLLATERAL NUYEN"
    r"|COMBAT MEDICINE 101"
    r"|GAME INFORMATION"
    r"|ADVANCED BIOTECH RULES"
    r"|JACKPOINT"
    r"|AUTHOR:.*UPLOAD"
    r")$",
    re.I,
)

# Multi-line title joins applied before classification
JOIN_TITLES = [
    (r"(?im)^BUILDING A\s*\nMEDIC CHARACTER\s*$", "BUILDING A MEDIC CHARACTER"),
    (r"(?im)^USING TRAUMA PATCHES\s*\nAND CRASH\s*$", "USING TRAUMA PATCHES AND CRASH"),
    (r"(?im)^ADVANCED MEDKIT\s*\nAND AUTODOC RULES\s*$", "ADVANCED MEDKIT AND AUTODOC RULES"),
    (r"(?im)^NEW DRUGS, TOXINS,\s*\nAND PATHOGENS\s*$", "NEW DRUGS, TOXINS, AND PATHOGENS"),
    (r"(?im)^ILLNESS/\s*\nINTOXICATION\s*$", "ILLNESS/INTOXICATION"),
    (r"(?im)^THRESHOLD\s*\nINJURIES\s*$", "THRESHOLD INJURIES"),
    (r"(?im)^AEROQUIP M\.E\.D\.-1\s*\n\"DUSTOFF\"\s*\nMEDICAL EVACUATION DRONE\s*$",
     'AEROQUIP M.E.D.-1 "DUSTOFF" MEDICAL EVACUATION DRONE'),
    (r"(?im)^AEROQUIP M\.E\.D\.-1\s*\n\"DUSTOFF\"\s*$", 'AEROQUIP M.E.D.-1 "DUSTOFF"'),
    (r"(?im)^SHIAWASE CADUCEUS\s*\n\"CAD\" 7\s*$", 'SHIAWASE CADUCEUS "CAD" 7'),
    (r"(?im)^PNEUMATIC ANTI-SHOCK\s*\nGARMENTS\s*$", "PNEUMATIC ANTI-SHOCK GARMENTS"),
    (r"(?im)^DOCWAGON HEMOSTATIX\s*\nDRESSING\s*$", "DOCWAGON HEMOSTATIX DRESSING"),
    (r"(?im)^VASOTECH AUTOINJECTION\s*\nGUN\s*$", "VASOTECH AUTOINJECTION GUN"),
    (r"(?im)^CRYPTOCOCCUS\s*\nMETAFORMANS\s*$", "CRYPTOCOCCUS METAFORMANS"),
    (r"(?im)^INCISION\s*\n\(MANIPULATION/PHYSICAL\):\s*$", "INCISION (MANIPULATION/PHYSICAL)"),
    (r"(?im)^BIOTECH SKILL RATINGS\s*\n\(SR4A\)\s*$", "BIOTECH SKILL RATINGS (SR4A)"),
    (r"(?im)^BIOTECH SKILL RATINGS\s*\n\(SR5\)\s*$", "BIOTECH SKILL RATINGS (SR5)"),
]


def clean_dashes(s: str) -> str:
    for a, b in DASHES:
        s = s.replace(a, b)
    return s


def norm_key(s: str) -> str:
    s = s.lower().strip().strip(":")
    s = s.replace(""", '"').replace(""", '"')
    s = re.sub(r"\s+", " ", s)
    return s


def title_case(s: str) -> str:
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "vs", "at", "with"}
    keep_upper = {
        "HTR", "CRT", "BP", "SR4A", "SR5", "PAG", "DMSO", "IV", "CPR", "EMT",
        "CAD", "GE", "AA", "AAA", "CAS",
    }
    words = s.split()
    out: list[str] = []
    for i, w in enumerate(words):
        bare = w.strip('()"\'.,:')
        up = bare.upper()
        if up in keep_upper:
            fixed = up
            if w.startswith('"'):
                fixed = '"' + fixed
            if w.endswith('"'):
                fixed = fixed + '"'
            if w.endswith(":"):
                fixed += ":"
            out.append(fixed)
            continue
        lw = bare.lower()
        if i > 0 and lw in small:
            out.append(lw)
        else:
            fixed = bare[:1].upper() + bare[1:].lower() if bare else bare
            if w.startswith("(") and w.endswith(")"):
                out.append(f"({fixed})")
            elif w.endswith(":"):
                out.append(fixed + ":")
            elif w.startswith('"') and w.endswith('"'):
                out.append(f'"{fixed}"')
            else:
                out.append(fixed)
    return " ".join(out)


def fix_soft_hyphens(text: str) -> str:
    text = re.sub(r"([A-Za-z]{2,})-\s*\n\s*([A-Za-z]{2,})", r"\1\2", text)
    text = re.sub(r"([A-Za-z]{2,})-\s+([a-z]{2,})", r"\1\2", text)
    return text


def join_titles(text: str) -> str:
    for pat, repl in JOIN_TITLES:
        text = re.sub(pat, repl, text)
    return text


def is_all_caps_candidate(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 80:
        return False
    if s.startswith("#") or s.startswith(">") or s.startswith("**") or s.startswith("|"):
        return False
    if re.match(r"^\d", s):
        return False
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return False
    # mostly uppercase letters
    upper = sum(1 for c in letters if c.isupper())
    return upper / len(letters) >= 0.85


def reflow_prose(lines: list[str]) -> str:
    if not lines:
        return ""
    paras: list[str] = []
    buf = lines[0].strip()
    for line in lines[1:]:
        s = line.strip()
        if not s:
            continue
        if buf.endswith("-") and s and s[0].isalpha():
            buf = buf[:-1] + s
            continue
        if s.startswith("*") or re.match(r"^[A-Za-z][\w /-]+:\s+\S", s):
            if buf:
                paras.append(buf)
            buf = s
            continue
        if re.search(r'[.!?]"?$', buf) and (s[0].isupper() or s[0] in "\"'>"):
            paras.append(buf)
            buf = s
            continue
        buf = buf + " " + s
    if buf:
        paras.append(buf)
    return "\n\n".join(paras)


def format_jp_blocks(lines: list[str]) -> list[str]:
    """Turn orphan '>' separators into markdown blockquotes with handles."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s == ">":
            chunk: list[str] = []
            i += 1
            while i < len(lines):
                t = lines[i].strip()
                if not t:
                    i += 1
                    continue
                if t == ">":
                    break
                if re.match(r"^>\s*[A-Za-z0-9]", t) and len(t) < 50:
                    break
                if t.startswith("##") or t.startswith("###"):
                    break
                chunk.append(t)
                i += 1
            body = " ".join(c for c in chunk if c)
            handle = ""
            if i < len(lines) and re.match(r"^>\s*[A-Za-z0-9]", lines[i].strip()):
                handle = lines[i].strip()
                if not handle.startswith(">"):
                    handle = "> " + handle
                i += 1
            if body:
                out.append("> " + body)
            if handle:
                out.append(handle)
            continue
        out.append(lines[i])
        i += 1
    return out


def format_body(body: str) -> str:
    body = clean_dashes(body)
    body = fix_soft_hyphens(body)
    body = join_titles(body)

    raw_lines = [ln.rstrip() for ln in body.splitlines()]
    blocks: list[str] = []
    prose_buf: list[str] = []
    current_parent = ""

    def flush() -> None:
        nonlocal prose_buf
        if prose_buf:
            blocks.append(reflow_prose(prose_buf))
            prose_buf = []

    for ln in raw_lines:
        s = ln.strip()
        if not s:
            flush()
            continue
        if JUNK.match(s):
            continue

        if s.startswith(">") or s == ">":
            flush()
            blocks.append(s)
            continue

        if is_all_caps_candidate(s):
            key = norm_key(s)
            if key in SECTION_H2:
                flush()
                blocks.append(f"## {SECTION_H2[key]}")
                current_parent = key
                continue
            if key in KNOWN_ITEMS and (
                current_parent in ITEM_PARENTS or current_parent in {"", "new qualities", "new gear"}
            ):
                flush()
                blocks.append(f"### {KNOWN_ITEMS[key]}")
                continue
            # leave as prose (table cells, DV lines, subtype tags, etc.)
            prose_buf.append(s)
            continue

        prose_buf.append(s)

    flush()

    # second pass: fix JP orphan >
    expanded: list[str] = []
    for b in blocks:
        expanded.extend(b.splitlines() if b else [])
        expanded.append("")
    fixed_lines = format_jp_blocks([ln for ln in expanded])
    text = "\n".join(fixed_lines)
    text = re.sub(
        r"(Apex Pharmaceuticals)\s+(Founded in)",
        r"\1\n\n\2",
        text,
    )
    text = re.sub(r"subscriptionbased", "subscription-based", text, flags=re.I)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return clean_dashes(text)


def split_header(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines:
        return "", ""
    header_lines: list[str] = []
    i = 0
    if lines[0].startswith("# "):
        header_lines.append(lines[0])
        i = 1
        while i < len(lines) and not lines[i].strip():
            header_lines.append(lines[i])
            i += 1
        if i < len(lines) and lines[i].startswith("**Source:**"):
            header_lines.append(lines[i])
            i += 1
            while i < len(lines) and not lines[i].strip():
                header_lines.append(lines[i])
                i += 1
    header = "\n".join(header_lines).rstrip() + "\n\n"
    body = "\n".join(lines[i:])
    return header, body


def main() -> None:
    for path in sorted(OUT.glob("*.md")):
        if path.name in SKIP:
            continue
        raw = path.read_text(encoding="utf-8")
        header, body = split_header(raw)
        # If already formatted (has ##), still ok - extract should be re-run first
        formatted = format_body(body)
        out = clean_dashes(header + formatted)
        path.write_text(out, encoding="utf-8")
        print("formatted", path.name, "bytes", path.stat().st_size)

    idx = OUT / "INDEX.md"
    if idx.exists():
        t = idx.read_text(encoding="utf-8")
        t = t.replace("- [ ] Format", "- [x] Format")
        idx.write_text(clean_dashes(t), encoding="utf-8")


if __name__ == "__main__":
    main()
