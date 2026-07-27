"""Rebuild Street Gear cleanly; clean all Core chapters; re-audit."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source Texts\Shadowrun Fifth Edition Core Rulebook")
AUDIT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_chapter_audit.md")

FOOTER = re.compile(
    r"(?<![A-Za-z])(?:\d{2,3}\s+)?"
    r"(?:GEAR RATINGS|BUYING GEAR|STREET GEAR|GEAR LISTING|ELECTRONICS|"
    r"AUGMENTATION|SHADOWRUN,? FIFTH EDITION|MASTER INDEX|"
    r"IMPORTANT TABLES|COMBAT|THE MATRIX|MAGIC|SKILLS|"
    r"CREATING A SHADOWRUNNER|HELPS AND HINDRANCES|GAMEMASTER ADVICE|"
    r"LIFE IN THE SIXTH WORLD|SHADOWRUN CONCEPTS|VEHICLES AND DRONES|"
    r"FIREARMS|MELEE WEAPONS|CLOTHING AND ARMOR|AMMUNITION|"
    r"PROJECTILE AND THROWING WEAPONS|GRENA DES|ROCKETS AND MISSILES|"
    r"INDUSTRIAL CHEMICALS|SURVIVAL GEAR|BIOTECH|DOCWAGON CONTRACT|"
    r"SLAP PATCHES|MAGICAL EQUIPMENT|WIRELESS FUNCTIONALITY|"
    r"CONCEALING GEAR|CARRYING GEAR|SIZE COSTS|FENCING GEAR|"
    r"\(IL\)LEGALITY|BLACK MARKET GOODS|STANDARD GOODS|"
    r"COMMUNICATIONS AND COUNTERMEASURES|BREAKING AND ENTERING|"
    r"OPTICAL AND IMAGING DEVICES|SECURITY DEVICES|SENSORS|"
    r"HEADWARE|EYEWARE|EARWARE|BODYWARE|CYBERLIMBS|BIOWARE|"
    r"CULTURED BIOWARE|BIKES|CARS|TRUCKS AND VANS|BOATS|"
    r"SUBMARINES|FIXED-WING AIRCRAFT|ROTORCRAFT|VTOL/VSTOL|"
    r"MICRODRONES|MINIDRONES|SMALL DRONES|MEDIUM DRONES|LARGE DRONES|"
    r"RIGGERS|WHERE THERE.?S SMOKE|ROOFTOPS AND RAINBOWS|"
    r"THE DANGERS OF SIDE JOBS|A LITTLE SHADOW MAGIC|ALL THE ANGLES|"
    r"GIRLS WITH GUNS|ANOTHER NIGHT,? ANOTHER RUN|THE BATTLE FOUGHT|"
    r"INTRODUCTION|TABLE OF CONTENTS|CREDITS)"
    r"(?:\s*(?:>>|<<))?(?:\s*\d{2,3})?(?![A-Za-z])",
    re.I,
)
SIDEBAR = re.compile(r"(?:<<|>>).{0,60}")
PAGE_ONLY = re.compile(r"^\d{1,3}$")

SOFT_PAIRS = {
    "favor ites": "favorites",
    "pur chase": "purchase",
    "pur chased": "purchased",
    "char acter": "character",
    "char acters": "characters",
    "char acter's": "character's",
    "mar ket": "market",
    "spir its": "spirits",
    "tech nology": "technology",
    "equip ment": "equipment",
    "ammu nition": "ammunition",
    "ammuni tion": "ammunition",
    "avail ability": "availability",
    "cyber ware": "cyberware",
    "bio ware": "bioware",
    "com mlink": "commlink",
    "com mlinks": "commlinks",
    "fire arms": "firearms",
    "pro jectile": "projectile",
    "gren ades": "grenades",
    "explo sives": "explosives",
    "aug mentation": "augmentation",
    "mag ical": "magical",
    "vehi cles": "vehicles",
    "elec tronics": "electronics",
    "soft ware": "software",
    "skill softs": "skillsofts",
    "imag ing": "imaging",
    "enhan cements": "enhancements",
    "secur ity": "security",
    "indus trial": "industrial",
    "chem icals": "chemicals",
    "sur vival": "survival",
    "grap ple": "grapple",
    "bio tech": "biotech",
    "head ware": "headware",
    "eye ware": "eyeware",
    "ear ware": "earware",
    "body ware": "bodyware",
    "cyber limbs": "cyberlimbs",
    "cul tured": "cultured",
    "run ners": "runners",
    "shadow runners": "shadowrunners",
    "metro plex": "metroplex",
    "hard cases": "hardcases",
    "data trail": "datatrail",
    "entrap ment": "entrapment",
    "deal ings": "dealings",
    "connec tions": "connections",
    "prac tically": "practically",
    "practi cally": "practically",
    "diffi cult": "difficult",
    "diffi culty": "difficulty",
    "nec essary": "necessary",
    "neces sary": "necessary",
    "neces sarily": "necessarily",
    "espe cially": "especially",
    "partic ular": "particular",
    "partic ularly": "particularly",
    "gener ally": "generally",
    "typi cally": "typically",
    "basi cally": "basically",
    "actu ally": "actually",
    "virtu ally": "virtually",
    "liter ally": "literally",
    "ulti mately": "ultimately",
    "imme diately": "immediately",
    "auto matically": "automatically",
    "addi tional": "additional",
    "addi tionally": "additionally",
    "origi nal": "original",
    "origi nally": "originally",
    "poten tial": "potential",
    "poten tially": "potentially",
    "statis tics": "statistics",
    "modi fier": "modifier",
    "modi fiers": "modifiers",
    "oppo nent": "opponent",
    "oppo nents": "opponents",
    "oppo sed": "opposed",
    "resis tance": "resistance",
    "penetra tion": "penetration",
    "capa city": "capacity",
    "conceala bility": "concealability",
    "func tion": "function",
    "func tionality": "functionality",
    "incom patibility": "incompatibility",
    "wire less": "wireless",
    "acces sories": "accessories",
    "protec tive": "protective",
    "cloth ing": "clothing",
    "over all": "overall",
    "repre sentative": "representative",
    "exhaus tive": "exhaustive",
    "selec tion": "selection",
    "gad gets": "gadgets",
    "cus tomizations": "customizations",
    "prag matic": "pragmatic",
    "stimu lant": "stimulant",
    "dis guise": "disguise",
    "differ ence": "difference",
    "leg end": "legend",
    "fad ing": "fading",
    "busi ness": "business",
    "com municate": "communicate",
    "weap onry": "weaponry",
    "pre cautions": "precautions",
    "com pletely": "completely",
    "instal ling": "installing",
    "impres sive": "impressive",
    "pimp ing": "pimping",
    "cyber deck": "cyberdeck",
    "fetish ism": "fetishism",
    "tool box": "toolbox",
    "get ting": "getting",
    "special ized": "specialized",
    "intro duces": "introduces",
    "descri bed": "described",
    "inclu des": "includes",
    "numer ical": "numerical",
    "amalga mation": "amalgamation",
    "fac tors": "factors",
    "rar ity": "rarity",
    "legal ity": "legality",
    "distri bution": "distribution",
    "sup ply": "supply",
    "de mand": "demand",
    "situa tions": "situations",
    "war rant": "warrant",
    "restrict ed": "restricted",
    "econ omy": "economy",
    "adjust ments": "adjustments",
    "fluctua tions": "fluctuations",
    "extenu ating": "extenuating",
    "circum stances": "circumstances",
    "appro priate": "appropriate",
    "emi nently": "eminently",
    "trace able": "traceable",
    "cross indexed": "cross-indexed",
    "liabil ity": "liability",
    "market ing": "marketing",
    "adver tisements": "advertisements",
    "Com merce": "Commerce",
    "remem bers": "remembers",
    "sneak ers": "sneakers",
    "perva sive": "pervasive",
    "data mining": "data-mining",
    "accu mulate": "accumulate",
    "pro files": "profiles",
    "long term": "long-term",
    "some one": "someone",
    "para noia": "paranoia",
    "sur charge": "surcharge",
    "digi tal": "digital",
    "num bers": "numbers",
    "Negotia tion": "Negotiation",
    "deliv ery": "delivery",
    "deliv ered": "delivered",
    "sell er": "seller",
    "per cent": "percent",
    "criti cal": "critical",
    "inqui ries": "inquiries",
    "atten tion": "attention",
    "under cover": "undercover",
    "sting opera tion": "sting operation",
    "twig ging": "twigging",
    "conse quences": "consequences",
    "itera tion": "iteration",
    "acquir ing": "acquiring",
    "infor mation": "information",
    "orga nization": "organization",
    "corpo ration": "corporation",
    "corpo rations": "corporations",
    "attrib ute": "attribute",
    "attrib utes": "attributes",
    "meta type": "metatype",
    "initia tive": "initiative",
    "thresh old": "threshold",
    "thresh olds": "thresholds",
    "dice pool": "dice pool",
    "gamemas ter": "gamemaster",
    "game master": "gamemaster",
}


def walk(items, depth=0, acc=None):
    if acc is None:
        acc = []
    for it in items:
        if isinstance(it, list):
            walk(it, depth + 1, acc)
        else:
            title = (getattr(it, "title", None) or str(it)).strip()
            try:
                page = reader.get_destination_page_number(it)
            except Exception:
                page = None
            acc.append((depth, title, page))
    return acc


def clean_line(s: str) -> str:
    s = SIDEBAR.sub("", s)
    s = FOOTER.sub("", s)
    s = s.replace("\u2014", " - ").replace("\u2013", "-")
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fix_soft(text: str) -> str:
    for bad, good in sorted(SOFT_PAIRS.items(), key=lambda x: -len(x[0])):
        text = re.sub(re.escape(bad), good, text, flags=re.I)
    return text


def extract_pages(start: int, end: int) -> list[str]:
    lines = []
    for i in range(start, end):
        t = reader.pages[i].extract_text() or ""
        for line in t.splitlines():
            c = clean_line(line)
            if not c or PAGE_ONLY.fullmatch(c):
                continue
            lines.append(c)
    return lines


def join_hyphen_breaks(lines: list[str]) -> list[str]:
    out = []
    i = 0
    while i < len(lines):
        cur = lines[i]
        while cur.endswith("-") and i + 1 < len(lines):
            cur = cur[:-1] + lines[i + 1]
            i += 1
        out.append(cur)
        i += 1
    return out


GLOSSARY_TERMS = {
    "Accuracy",
    "Ammo",
    "Armor",
    "Armor Penetration",
    "Availability",
    "Blast",
    "Capacity",
    "Concealability Modifier",
    "Cost",
    "Damage Value (DV)",
    "Device Rating",
    "Essence Cost",
    "Mode",
    "Mounts",
    "Reach",
    "Recoil Compensation (RC)",
}


def build_street_gear():
    flat = walk(reader.outline)
    headings = []
    capturing = False
    base = 0
    for d, t, p in flat:
        if t == "Street Gear":
            capturing = True
            base = d
            continue
        if capturing:
            if d <= base:
                break
            headings.append((d - base, t))

    # longest key first
    heading_keys = []
    for depth, title in headings:
        key = re.sub(r"[^a-z0-9]+", "", title.lower())
        heading_keys.append((key, depth, title))
    heading_keys.sort(key=lambda x: -len(x[0]))

    lines = join_hyphen_breaks(extract_pages(420, 472))
    paras: list[str] = []
    buf = ""
    used_keys: set[str] = set()
    in_glossary = False

    def flush():
        nonlocal buf
        if buf:
            paras.append(fix_soft(buf.strip()))
            buf = ""

    def emit_heading(depth: int, title: str, key: str | None = None):
        nonlocal in_glossary
        if key and key in used_keys:
            return False
        if key:
            used_keys.add(key)
        # skip if last heading is same title
        if paras:
            last = paras[-1]
            if last.startswith("#") and last.lstrip("# ").lower() == title.lower():
                return False
        flush()
        paras.append("#" * min(depth + 1, 4) + f" {title}")
        in_glossary = title.lower() == "glossary"
        return True

    i = 0
    while i < len(lines):
        line = lines[i]
        upper = line.upper().strip()

        # Skip pure noise
        if upper in {"SECTION.11", "SECTION 11", "SECTION.11 GLOSSARY"} or upper.startswith(
            "SECTION.11"
        ):
            if "GLOSSARY" in upper:
                emit_heading(2, "Glossary", "glossary")
                rest = re.sub(r"^SECTION\.?\s*11\s*GLOSSARY\s*", "", line, flags=re.I).strip()
                if rest:
                    buf = rest
            i += 1
            continue

        if upper == "GLOSSARY":
            emit_heading(2, "Glossary", "glossary")
            i += 1
            continue

        # Outline heading: only first time, and only if line is mostly the heading
        matched = False
        for key, depth, title in heading_keys:
            if key in used_keys:
                continue
            tu = title.upper()
            if not upper.startswith(tu):
                continue
            # boundary after title
            if len(upper) > len(tu):
                after = upper[len(tu) : len(tu) + 1]
                if after.isalnum():
                    continue
            rest = line[len(title) :].lstrip(" :.-")
            # Reject mid-sentence matches: rest starts lowercase (continuation)
            if rest and rest[0].islower():
                continue
            # Reject weak matches where heading is buried in long prose
            if rest and len(rest) > 80 and not line[: len(title)].isupper():
                continue
            # Prefer ALL-CAPS or exact (ignoring case) short lines
            title_span = line[: len(title)]
            is_allcaps = title_span.isupper() or upper == tu
            is_exact = re.sub(r"[^a-z0-9]+", "", line.lower()) == key
            if not (is_allcaps or is_exact or (rest == "" and len(line) <= len(title) + 5)):
                continue
            if emit_heading(depth, title, key):
                if rest:
                    buf = rest
                matched = True
                break
        if matched:
            i += 1
            continue

        # Inline jammed headers: WORD WORD rest...
        jam = re.match(
            r"^((?:FENCING GEAR|STARTING GEAR|CONTACTS AND AVAILABILITY|"
            r"DELIVERY TIMES|WIRELESS FUNCTIONALITY|GEAR LISTING|"
            r"BLACK MARKET GOODS|STANDARD GOODS|"
            r"CONTACTS AND FENCING))\s+(.+)$",
            line,
            re.I,
        )
        if jam:
            title = jam.group(1).title().replace("And", "and")
            # normalize known titles
            fixes = {
                "Fencing Gear": "Fencing Gear",
                "Starting Gear": "Starting Gear",
                "Contacts And Availability": "Contacts and Availability",
                "Contacts and Availability": "Contacts and Availability",
                "Delivery Times": "Delivery Times",
                "Wireless Functionality": "Wireless Functionality",
                "Gear Listing": "Gear Listing",
                "Black Market Goods": "Black Market Goods",
                "Standard Goods": "Standard Goods",
                "Contacts And Fencing": "Contacts and Fencing",
                "Contacts and Fencing": "Contacts and Fencing",
            }
            title = fixes.get(title, title)
            key = re.sub(r"[^a-z0-9]+", "", title.lower())
            depth = 2
            for hk, hd, ht in heading_keys:
                if hk == key:
                    depth = hd
                    title = ht
                    break
            if key == "startinggear" or key == "deliverytimes":
                depth = 2
            if key not in used_keys or key in {"deliverytimes"}:
                # Delivery Times table caption can appear twice; allow caption once as heading
                if key == "deliverytimes" and key in used_keys:
                    pass
                else:
                    emit_heading(depth, title, key)
                    buf = jam.group(2)
                    i += 1
                    continue

        # Glossary term lines
        if in_glossary:
            m = re.match(r"^([A-Za-z][A-Za-z0-9 /()'+\-]{1,40}):\s+(.*)$", line)
            if m and m.group(1) in GLOSSARY_TERMS:
                flush()
                paras.append(f"#### {m.group(1)}")
                buf = m.group(2)
                i += 1
                continue

        if not buf:
            buf = line
        else:
            if line.startswith('"') or (
                buf.endswith((".", "!", "?", '"')) and re.match(r"^[A-Z\"]", line)
            ):
                flush()
                buf = line
            else:
                buf += " " + line
        i += 1
    flush()

    while paras and re.sub(r"[^a-z0-9]+", "", paras[0].lower().lstrip("# ")) in {
        "streetgear",
    }:
        paras = paras[1:]

    # Deduplicate consecutive identical headings
    cleaned = []
    for p in paras:
        if cleaned and p.startswith("#") and cleaned[-1] == p:
            continue
        cleaned.append(p)
    paras = cleaned

    body = "\n\n".join(paras)
    body = fix_soft(body)
    body = re.sub(r" {2,}", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = re.sub(r"\(see ([^)]+),\s*\)", r"(see \1)", body)
    body = re.sub(r"see ,\s*p\.", "see p.", body)
    body = re.sub(r"\(\s*\)", "", body)
    # Fix split "Delivery Times" mid sentence remnants
    body = body.replace(
        "the amount of time given on the\n\n### Delivery Times\n\ntable",
        "the amount of time given on the Delivery Times table",
    )
    body = body.replace(
        "the amount of time given on the\n\n## Delivery Times\n\ntable",
        "the amount of time given on the Delivery Times table",
    )

    md = "# Street Gear\n\n" + body.strip() + "\n"
    path = OUT / "21 - Street Gear.md"
    path.write_text(md, encoding="utf-8")
    print("Street Gear", path.stat().st_size, "heads", sum(1 for p in paras if p.startswith("#")))


def build_index():
    lines = join_hyphen_breaks(extract_pages(472, 494))
    entries: list[str] = []
    buf = ""
    for line in lines:
        line = FOOTER.sub("", line).strip()
        line = SIDEBAR.sub("", line).strip()
        line = re.sub(r"\s+", " ", line)
        if not line or PAGE_ONLY.fullmatch(line):
            continue
        if re.match(r"^(?:SHADOWRUN|MASTER INDEX|INDEX)\b", line, re.I):
            continue
        if re.fullmatch(r"[A-Z]", line):
            # letter section header from PDF
            if buf:
                entries.append(buf.strip())
                buf = ""
            continue
        if buf and re.match(r"^[A-Z]", line) and re.search(r"\d\s*$", buf):
            entries.append(buf.strip())
            buf = line
        elif not buf:
            buf = line
        else:
            buf += " " + line
    if buf:
        entries.append(buf.strip())

    by_letter: dict[str, list[str]] = {}
    for e in entries:
        e = FOOTER.sub("", e)
        e = re.sub(r"\s+", " ", e).strip()
        if len(e) < 2:
            continue
        letter = e[0].upper() if e[0].isalpha() else "#"
        by_letter.setdefault(letter, []).append(e)

    parts = [
        "# Index",
        "",
        "Alphabetical master index from the Core Rulebook PDF. "
        "Many entries cite other Fifth Edition books (book codes such as SG, RF, CF, DT, RG, R5) "
        "in addition to SR5.",
        "",
    ]
    for letter in sorted(by_letter.keys()):
        parts.append(f"## {letter}")
        parts.append("")
        for e in by_letter[letter]:
            parts.append(f"- {e}")
        parts.append("")

    path = OUT / "22 - Book Index.md"
    path.write_text("\n".join(parts), encoding="utf-8")
    print(
        "Index",
        path.stat().st_size,
        "letters",
        len(by_letter),
        "entries",
        sum(len(v) for v in by_letter.values()),
    )


JAMMED_HEAD = re.compile(
    r"(?<![#\w])("
    r"CHARACTER CREATION|METATYPE|PRIORITY TABLE|QUALITY|QUALITIES|"
    r"POSITIVE QUALITIES|NEGATIVE QUALITIES|SKILL GROUPS|ACTIVE SKILLS|"
    r"KNOWLEDGE SKILLS|LANGUAGE SKILLS|COMBAT TURN|INITIATIVE|"
    r"DECLARE ACTIONS|RESOLVE ACTIONS|MOVEMENT|ATTACKER|"
    r"DEFENDER|DAMAGE|ARMOR|HEALING|MATRIX ACTIONS|"
    r"SPELLCASTING|SUMMONING|ADEPT POWERS|MENTORS|"
    r"CONTACTS|LIFESTYLES|MAGIC TRADITIONS|SPIRITS|"
    r"FENCING GEAR|STARTING GEAR|WIRELESS FUNCTIONALITY|"
    r"GEAR LISTING|BLACK MARKET GOODS|STANDARD GOODS|"
    r"DELIVERY TIMES|CONTACTS AND AVAILABILITY|"
    r"USING EDGE|GLITCHES|CRITICAL GLITCHES|"
    r"SUCCESS TESTS|OPPOSED TESTS|EXTENDED TESTS|"
    r"TEAMWORK TESTS|LIMITS|ATTRIBUTES|"
    r"PHYSICAL ATTRIBUTES|MENTAL ATTRIBUTES|SPECIAL ATTRIBUTES|"
    r"CONDITION MONITOR|OVERFLOW|WOUNDS|"
    r"RANGED COMBAT|MELEE COMBAT|FIREARMS|"
    r"FULL DEFENSE|INTERRUPT ACTIONS|CALLED SHOTS|"
    r"AREA EFFECT|BLAST|GRENADES|"
    r"VEHICLE COMBAT|CHASE COMBAT|"
    r"BUILDING A SHADOWRUNNER|FINISHING TOUCHES|"
    r"KARMA|NUYEN|RESOURCES|AUGMENTATIONS|"
    r"POSITIVE QUALITIES|NEGATIVE QUALITIES"
    r")\s+([A-Z]?[a-z].{10,})"
)


def clean_existing_chapter(path: Path) -> dict:
    """Strip footers, split jammed headers, fix soft hyphens, dedupe heads."""
    if path.name.startswith(("26 ", "27 ", "28 ")):
        return {"file": path.name, "changed": False, "note": "stub"}
    if path.name.startswith(("23 ", "24 ", "25 ", "01 ", "02 ", "03 ", "04 ")):
        # already curated; light cleanup only
        text = path.read_text(encoding="utf-8", errors="replace")
        new = FOOTER.sub("", text)
        new = fix_soft(new)
        new = re.sub(r" {2,}", " ", new)
        new = re.sub(r"\n{3,}", "\n\n", new)
        changed = new != text
        if changed:
            path.write_text(new, encoding="utf-8")
        return {"file": path.name, "changed": changed, "note": "light"}

    text = path.read_text(encoding="utf-8", errors="replace")
    original = text
    text = FOOTER.sub("", text)
    text = SIDEBAR.sub("", text)
    text = fix_soft(text)

    # Split jammed ALL-CAPS headers embedded in paragraphs
    def jam_repl(m: re.Match) -> str:
        title = m.group(1).title()
        # fix And/Of/The casing lightly
        title = re.sub(
            r"\b(And|Or|Of|The|A|An|In|On|For|To|With)\b",
            lambda x: x.group(0).lower(),
            title,
        )
        title = title[0].upper() + title[1:]
        rest = m.group(2)
        return f"\n\n## {title}\n\n{rest}"

    text = JAMMED_HEAD.sub(jam_repl, text)

    # Remove empty leftover lines from footer strip
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" {2,}", " ", text)
    # Deduplicate consecutive identical headings
    lines = text.splitlines()
    out_lines = []
    prev_head = None
    for line in lines:
        if line.startswith("#"):
            if line == prev_head:
                continue
            prev_head = line
        else:
            if line.strip():
                prev_head = None
        out_lines.append(line)
    text = "\n".join(out_lines)
    if not text.endswith("\n"):
        text += "\n"

    changed = text != original
    if changed:
        path.write_text(text, encoding="utf-8")
    return {"file": path.name, "changed": changed, "note": "full"}


def completeness_check() -> list[str]:
    """Compare PDF extract size vs markdown size per top-level chapter."""
    flat = walk(reader.outline)
    tops = [(t, p) for d, t, p in flat if d == 0 and p is not None]
    # Map outline titles to files via INDEX order
    index = (OUT / "INDEX.md").read_text(encoding="utf-8")
    files = sorted(
        f for f in OUT.glob("*.md") if f.name != "INDEX.md" and re.match(r"^\d+ - ", f.name)
    )
    # Build expected spans from outline matching INDEX names loosely
    report = []
    for f in files:
        title = re.sub(r"^\d+ - ", "", f.stem)
        # find matching outline entry
        match = None
        for i, (t, p) in enumerate(tops):
            tn = re.sub(r"[^a-z0-9]+", "", t.lower())
            fn = re.sub(r"[^a-z0-9]+", "", title.lower())
            if tn == fn or tn in fn or fn in tn:
                end = tops[i + 1][1] if i + 1 < len(tops) else len(reader.pages)
                match = (t, p, end)
                break
        if not match:
            report.append(f"- {f.name}: no PDF outline match")
            continue
        t, p, end = match
        pdf_chars = 0
        for i in range(p, end):
            pdf_chars += len(reader.pages[i].extract_text() or "")
        md_chars = len(f.read_text(encoding="utf-8", errors="replace"))
        ratio = md_chars / pdf_chars if pdf_chars else 0
        flag = ""
        if f.name.startswith(("26 ", "27 ", "28 ")):
            flag = " (image stub OK)"
        elif ratio < 0.35:
            flag = " **THIN vs PDF**"
        elif ratio > 2.5 and "Index" not in f.name:
            flag = " **bloated?**"
        report.append(
            f"- {f.name}: PDF p.{p+1}-{end} (~{pdf_chars} chars) -> MD {md_chars} chars "
            f"(ratio {ratio:.2f}){flag}"
        )
    return report


def score_chapter(path: Path) -> dict:
    t = path.read_text(encoding="utf-8", errors="replace")
    lines = t.splitlines()
    footer = len(
        re.findall(
            r"\d{2,3}\s+(?:COMBAT|MATRIX|MAGIC|SKILLS|STREET GEAR|MASTER INDEX|"
            r"CREATING|HELPS AND HINDRANCES)",
            t,
            re.I,
        )
    )
    allcaps = sum(1 for l in lines if len(l) > 12 and l.isupper() and not l.startswith("#"))
    jammed = len(re.findall(r"[A-Z]{8,} [a-z]", t))
    tables = t.count("|---")
    heads = sum(1 for l in lines if l.startswith("##"))
    stub = path.stat().st_size < 200
    rating = "GOOD"
    reasons = []
    if stub:
        rating = "STUB"
        reasons.append("image/art stub")
    elif footer > 5 or allcaps > 10 or jammed > 20:
        rating = "POOR"
    elif footer > 0 or allcaps > 3 or jammed > 8:
        rating = "FAIR"
    if footer:
        reasons.append(f"{footer} footers")
    if allcaps:
        reasons.append(f"{allcaps} ALL-CAPS")
    if jammed:
        reasons.append(f"{jammed} jammed")
    return {
        "file": path.name,
        "kb": path.stat().st_size // 1024,
        "lines": len(lines),
        "heads": heads,
        "tables": tables,
        "rating": rating,
        "reasons": reasons,
    }


def audit_all():
    files = sorted(
        f for f in OUT.glob("*.md") if f.name != "INDEX.md" and re.match(r"^\d+", f.name)
    )
    rows = [score_chapter(f) for f in files]
    comp = completeness_check()
    lines = ["# Core Rulebook Chapter Audit", "", "## Quality scores", ""]
    lines.append("| File | KB | Lines | ## | Tables | Rating | Issues |")
    lines.append("|------|----|-------|----|--------|--------|--------|")
    for r in rows:
        issues = "; ".join(r["reasons"]) if r["reasons"] else "-"
        lines.append(
            f"| {r['file']} | {r['kb']} | {r['lines']} | {r['heads']} | {r['tables']} | **{r['rating']}** | {issues} |"
        )
    lines.append("")
    lines.append("## Completeness vs PDF text")
    lines.append("")
    lines.extend(comp)
    counts = defaultdict(int)
    for r in rows:
        counts[r["rating"]] += 1
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for k in ("GOOD", "FAIR", "POOR", "STUB"):
        lines.append(f"- **{k}**: {counts[k]}")
    AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Audit written")
    for r in rows:
        print(f"{r['rating']:5} {r['file']}")


reader = PdfReader(str(PDF))
build_street_gear()
build_index()
print("--- cleaning chapters ---")
for f in sorted(OUT.glob("*.md")):
    if f.name == "INDEX.md" or not re.match(r"^\d+", f.name):
        continue
    # skip freshly rebuilt 21/22 from second clean that might re-jam
    if f.name.startswith(("21 ", "22 ")):
        r = clean_existing_chapter(f)  # light soft-fix only path? use full carefully
        # For 21/22 only soft + footer, not jammed splitter (already structured)
        continue
    r = clean_existing_chapter(f)
    if r["changed"]:
        print("cleaned", r["file"])
# soft-fix only for 21/22
for name in ("21 - Street Gear.md", "22 - Book Index.md"):
    p = OUT / name
    t = p.read_text(encoding="utf-8")
    n = fix_soft(FOOTER.sub("", t))
    n = re.sub(r"\n{3,}", "\n\n", n)
    if n != t:
        p.write_text(n if n.endswith("\n") else n + "\n", encoding="utf-8")
        print("polished", name)

audit_all()
