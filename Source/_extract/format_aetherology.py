# -*- coding: utf-8 -*-
"""Formatting pass for Aetherology Source Texts chapters."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Aetherology")
SKIP = {"INDEX.md"}

DASHES = (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"))

JUNK = re.compile(
    r"^(>>\s*SHADOWRUN\s*<<|<<\s*AETHEROLOGY\s*>>.*|AETHEROLOGY\s+\d+)\s*$",
    re.I,
)

SECTION_H2: dict[str, str] = {
    "posted by: magister": "Posted by: Magister",
    "posted by: arete": "Posted by: Arete",
    "astral sea": "Astral Sea",
    "metaplanes": "Metaplanes",
    "excerpted from dr. gordon's writings": "Excerpted from Dr. Gordon's Writings",
    "astral navigation": "Astral Navigation",
    "the plane of faerie": "The Plane of Faerie",
    "dr. gordon's metaplanar terminology": "Dr. Gordon's Metaplanar Terminology",
    "interpreted by magister": "Interpreted by Magister",
    "fractured metaplane": "Fractured Metaplane",
    "hyper-metaplane": "Hyper-Metaplane",
    "bubble metaplane": "Bubble Metaplane",
    "brocéliande": "Brocéliande",
    "broceliande": "Brocéliande",
    "seelie and unseelie court": "Seelie and Unseelie Court",
    "the northern islands": "The Northern Islands",
    "the plane of beasts": "The Plane of Beasts",
    "astral phenomena": "Astral Phenomena",
    "astral shallow": "Astral Shallow",
    "astral rift": "Astral Rift",
    "astral shallows": "Astral Shallows",
    "aerie": "Aerie",
    "island of tandora": "Island of Tandora",
    "metaplane of man": "Metaplane of Man",
    "more astral phenomena": "More Astral Phenomena",
    "background count": "Background Count",
    "daoineann draoidheil": "Daoineann Draoidheil",
    "mana storm": "Mana Storm",
    "celephaïs": "Celephaïs",
    "celephais": "Celephaïs",
    "hudson valley": "Hudson Valley",
    "mr. darke": "Mr. Darke",
    "miggon": "Miggon",
    "carcean": "Carcean",
    "kadath": "Kadath",
    "metaplane of plants": "Metaplane of Plants",
    "tranquil gardens": "Tranquil Gardens",
    "umbrage": "Umbrage",
    "the elemental plane of water": "The Elemental Plane of Water",
    "still more astral phenomena": "Still More Astral Phenomena",
    "the mist": "The Mist",
    "elemental pole of water": "Elemental Pole of Water",
    "metaplane of earth": "Metaplane of Earth",
    "country of kaol": "Country of Kaol",
    "country of midden and drumlin": "Country of Midden and Drumlin",
    "argillaceous lands of the east": "Argillaceous Lands of the East",
    "city of amphibolite": "City of Amphibolite",
    "southern pole of earth": "Southern Pole of Earth",
    "metaplane of fire": "Metaplane of Fire",
    "the ash wastes": "The Ash Wastes",
    "the grove of kindling": "The Grove of Kindling",
    "muspellheim": "Muspellheim",
    "one more astral phenomena": "One More Astral Phenomena",
    "the veil": "The Veil",
    "the ancients should have used warning labels": (
        "The Ancients Should Have Used Warning Labels"
    ),
    "metaplane of air": "Metaplane of Air",
    "the octahedron": "The Octahedron",
    "the southern pole of air": "The Southern Pole of Air",
    "the eastern pole of air": "The Eastern Pole of Air",
    "the northern pole of air": "The Northern Pole of Air",
    "coriolis": "Coriolis",
    "plane of death": "Plane of Death",
    "well of souls": "Well of Souls",
    "metaplane of shadows": "Metaplane of Shadows",
    "moons over the shadow metaplane": "Moons over the Shadow Metaplane",
    "black moon": "Black Moon",
    "one more astral phenomena just came to mind": (
        "One More Astral Phenomena Just Came to Mind"
    ),
    "foveae": "Foveae",
    "blood moon": "Blood Moon",
    "pale moon": "Pale Moon",
    "wild moon": "Wild Moon",
    "desh'veroi, land of demons": "Desh'veroi, Land of Demons",
    "roggoth'shoth, land beyond death": "Roggoth'shoth, Land Beyond Death",
    "the tower": "The Tower",
    "the vault": "The Vault",
    "the books of shadow": "The Books of Shadow",
    "ancient wizard penticlese": "Ancient Wizard Penticlese",
    "azzorloth, the bridge between worlds": "Azzorloth, the Bridge Between Worlds",
    "vhortas (the hive)": "Vhortas (The Hive)",
    "metabeles (the web)": "Metabeles (The Web)",
    "the warrior plains": "The Warrior Plains",
    "another cool astral phenomena": "Another Cool Astral Phenomena",
    "voids": "Voids",
    "void": "Void",
    "remembering carlos": "Remembering Carlos",
    "the palace of whispers": "The Palace of Whispers",
    "the house arachne": "The House Arachne",
    "the twisted web": "The Twisted Web",
    "dweller on the threshold": "Dweller on the Threshold",
    "the hungry void": "The Hungry Void",
    "the violet gas": "The Violet Gas",
    "deep metaplanes": "Deep Metaplanes",
    "we just remembered another astral phenomena": (
        "We Just Remembered Another Astral Phenomena"
    ),
    "maya cloud": "Maya Cloud",
    "new spirits": "New Spirits",
    "free spirits": "Free Spirits",
    "movement": "Movement",
    "spirit powers": "Spirit Powers",
    "shift": "Shift",
    "skill": "Skill",
    "transfer energy (essence)": "Transfer Energy (Essence)",
    "vanishing": "Vanishing",
    "korrigan pact": "Korrigan Pact",
    "the inner circle": "The Inner Circle",
    "henry's old coat": "Henry's Old Coat",
}

ITEM_PARENTS = {"new spirits", "spirit powers", "free spirits"}

KNOWN_ITEMS: dict[str, str] = {
    "gum toad (demon)": "Gum Toad (Demon)",
    "crawler (demon)": "Crawler (Demon)",
    "ghasts (demon)": "Ghasts (Demon)",
    "vrygoths": "Vrygoths",
    "gremlin": "Gremlin",
    "anansi": "Anansi",
    "tsuchigumo warrior": "Tsuchigumo Warrior",
}

HANDLES = {
    "magister",
    "elijah",
    "winterhawk",
    "slamm-0!",
    "slamm-0",
    "mika",
    "bull",
    "arete",
    "glitch",
    "kane",
    "clockwork",
    "netcat",
    "pebble",
    "lyran",
    "axis mundi",
    "man-of-many-names",
    "hurricane",
    "ether",
    "frosty",
    "snopes",
    "beaker",
    "kat o' nine tales",
    "turbo bunny",
    "red",
    "stone",
    "jimmy no",
    "goat foot",
    "sounder",
    "hard exit",
    "aufheben",
    "plan 9",
    "the smiling bandit",
    "fianchetto",
}


def clean_dashes(text: str) -> str:
    for a, b in DASHES:
        text = text.replace(a, b)
    return text


def norm_key(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("'", "'").replace("'", "'")
    s = re.sub(r"\s+", " ", s)
    return s


def title_case_fallback(s: str) -> str:
    small = {"of", "the", "and", "in", "on", "a", "an", "or", "to", "for"}
    words = s.strip().split()
    out = []
    for i, w in enumerate(words):
        low = w.lower()
        if i > 0 and low in small:
            out.append(low)
        else:
            out.append(low[:1].upper() + low[1:] if low else w)
    return " ".join(out)


def fix_soft_hyphens(text: str) -> str:
    text = re.sub(r"([A-Za-z]{2,})-\s*\n\s*([A-Za-z]{2,})", r"\1\2", text)
    text = re.sub(r"([A-Za-z]{2,})-\s+([a-z]{2,})", r"\1\2", text)
    return text


def is_all_caps_candidate(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 90:
        return False
    if s.startswith("#") or s.startswith(">") or s.startswith("**") or s.startswith("|"):
        return False
    if re.match(r"^\d", s):
        return False
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return False
    upper = sum(1 for c in letters if c.isupper())
    return upper / len(letters) >= 0.85


def is_handle(line: str) -> bool:
    s = line.strip().lstrip(">").strip()
    if not s or len(s) > 40:
        return False
    key = s.lower()
    if key in HANDLES:
        return True
    # short Name / Name-Name patterns
    if re.match(r"^[A-Za-z][A-Za-z0-9'!. -]{0,30}$", s) and s[0].isupper():
        words = re.split(r"[\s-]+", s)
        if 1 <= len(words) <= 4 and all(w[:1].isupper() for w in words if w):
            return True
    return False


_DANGLING = re.compile(
    r"\b(I|A|An|The|We|He|She|They|I'm|I'd|I've|It's|Its)$", re.I
)


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
        # Stat labels / short all-caps cells: keep separate
        if len(s) <= 12 and s.isupper() and s.isalpha():
            if buf:
                paras.append(buf)
            buf = s
            continue
        # Dangling article/pronoun at end of line: always continue
        if _DANGLING.search(buf) and s[0].islower():
            buf = buf + " " + s
            continue
        if re.search(r'[.!?]"?$', buf) and (s[0].isupper() or s[0] in "\"'>"):
            paras.append(buf)
            buf = s
            continue
        buf = buf + " " + s
    if buf:
        paras.append(buf)
    # Merge paras split on dangling pronouns across blank lines
    merged: list[str] = []
    for p in paras:
        if merged and _DANGLING.search(merged[-1]) and p and p[0].islower():
            merged[-1] = merged[-1] + " " + p
        else:
            merged.append(p)
    return "\n\n".join(merged)


def format_body(body: str, fname: str) -> str:
    body = clean_dashes(body)
    body = fix_soft_hyphens(body)

    raw = [ln.rstrip() for ln in body.splitlines()]
    blocks: list[str] = []
    prose: list[str] = []
    current_parent = ""

    def flush_prose() -> None:
        nonlocal prose
        if prose:
            blocks.append(reflow_prose(prose))
            prose = []

    i = 0
    while i < len(raw):
        s = raw[i].strip()
        if not s:
            flush_prose()
            i += 1
            continue
        if JUNK.match(s):
            i += 1
            continue

        # JackPoint: > \n comment \n > \n Handle
        if s == ">" or (s.startswith(">") and len(s) <= 2):
            flush_prose()
            i += 1
            chunk: list[str] = []
            while i < len(raw) and raw[i].strip() != ">":
                t = raw[i].strip()
                if t.startswith("##") or is_all_caps_candidate(t):
                    key = norm_key(t)
                    if key in SECTION_H2 or key in KNOWN_ITEMS:
                        break
                if t:
                    chunk.append(t)
                i += 1
            if i < len(raw) and raw[i].strip() == ">":
                i += 1
            while i < len(raw) and not raw[i].strip():
                i += 1
            handle = ""
            if i < len(raw) and is_handle(raw[i]):
                handle = raw[i].strip().lstrip(">").strip()
                i += 1
            body_c = " ".join(chunk)
            # soft-hyphen leftovers inside comment
            body_c = re.sub(r"([A-Za-z]{2,})-\s+([a-z]{2,})", r"\1\2", body_c)
            if body_c:
                blocks.append("> " + body_c)
            if handle:
                blocks.append("> **" + handle + "**")
            continue

        if is_all_caps_candidate(s):
            key = norm_key(s)
            if key in SECTION_H2:
                flush_prose()
                blocks.append(f"## {SECTION_H2[key]}")
                current_parent = key
                i += 1
                continue
            if key in KNOWN_ITEMS and (
                current_parent in ITEM_PARENTS or "rules" in fname.lower()
            ):
                flush_prose()
                blocks.append(f"### {KNOWN_ITEMS[key]}")
                current_parent = key if key in ITEM_PARENTS else current_parent
                i += 1
                continue
            # Promote other short ALL-CAPS titles as ## when they look like headings
            promote = (len(s) <= 60 and not re.search(r"\d", s) and (" " in s or len(s) <= 28))
            if promote and key not in {
                "sr4a",
                "sr5",
                "init",
                "edg",
                "ess",
                "acc",
                "dam",
                "ammo",
                "avail",
                "cost",
                "mode",
                "powers",
                "skills",
                "weaknesses",
                "attacks",
            }:
                nxt = ""
                j = i + 1
                while j < len(raw) and not raw[j].strip():
                    j += 1
                if j < len(raw):
                    nxt = raw[j].strip()
                if nxt and not is_all_caps_candidate(nxt) and not nxt.startswith(">"):
                    flush_prose()
                    display = SECTION_H2.get(key) or title_case_fallback(s)
                    blocks.append(f"## {display}")
                    current_parent = key
                    i += 1
                    continue

        prose.append(s)
        i += 1

    flush_prose()
    text = "\n\n".join(blocks)
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
        formatted = format_body(body, path.name)
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
