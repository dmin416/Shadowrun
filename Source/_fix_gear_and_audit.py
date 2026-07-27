"""Improved Street Gear rebuild + full Core chapter quality audit."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source Texts\Shadowrun Fifth Edition Core Rulebook")
AUDIT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_chapter_audit.md")

FOOTER = re.compile(
    r"(?:\d{2,3}\s+)?"
    r"(?:GEAR RATINGS|BUYING GEAR|STREET GEAR|GEAR LISTING|ELECTRONICS|"
    r"AUGMENTATION|SHADOWRUN,? FIFTH EDITION|MASTER INDEX|TABLES|"
    r"IMPORTANT TABLES|COMBAT|THE MATRIX|MAGIC|SKILLS|CREATING A SHADOWRUNNER|"
    r"HELPS AND HINDRANCES|GAMEMASTER ADVICE|LIFE IN THE SIXTH WORLD|"
    r"SHADOWRUN CONCEPTS|VEHICLES AND DRONES)"
    r"(?:\s*(?:>>|<<))?(?:\s*\d{2,3})?",
    re.I,
)
SIDEBAR = re.compile(r"(?:<<|>>).{0,60}")
PAGE_ONLY = re.compile(r"^\d{1,3}$")

# Common OCR soft-hyphen leftovers (space inside word)
SOFT_WORD = re.compile(
    r"\b("
    r"favor ites|pur chased|char acters|mar ket|spir its|tech nology|"
    r"equip ment|ammu nition|avail ability|cyber ware|bio ware|"
    r"com mlink|fire arms|pro jectile|gren ades|explo sives|"
    r"aug mentation|mag ical|vehi cles|elec tronics|soft ware|"
    r"skill softs|imag ing|enhan cements|secur ity|indus trial|"
    r"chem icals|sur vival|grap ple|bio tech|head ware|eye ware|"
    r"ear ware|body ware|cyber limbs|cul tured|drone s|"
    r"infor mation|orga nization|corpo ration|corpo rations|"
    r"char acter|char acter's|run ners|shadow runners|"
    r"metro plex|hard cases|play ground|data trail|"
    r"entrap ment|deal ings|connec tions|acquiring|"
    r"prac tically|practi cally|diffi cult|diffi culty|"
    r"nec essary|neces sary|espe cially|partic ular|"
    r"partic ularly|gener ally|typi cally|basi cally|"
    r"actu ally|virtu ally|liter ally|ulti mately|"
    r"imme diately|auto matically|addi tional|addi tionally|"
    r"origi nal|origi nally|poten tial|poten tially|"
    r"statis tics|statis tic|modi fier|modi fiers|"
    r"oppo nent|oppo nents|oppo sed|resis tance|"
    r"penetra tion|capa city|conceala bility|conceala bility|"
    r"func tion|func tionality|incom patibility|"
    r"wire less|acces sories|ammuni tion|explo sion|"
    r"protec tive|cloth ing|over all|over all|"
    r"repre sentative|exhaus tive|selec tion|"
    r"gad gets|cus tomizations|prag matic|"
    r"stimu lant|dis guise|differ ence|leg end|"
    r"fad ing|pavement|busi ness|com municate|"
    r"weap onry|pre cautions|com pletely|"
    r"instal ling|flashy|impres sive|gold plated|"
    r"pimp ing|cyber deck|fetish ism|tool box|"
    r"get ting|around|fact that|special ized|"
    r"intro duces|descri bed|inclu des|statis tics|"
    r"numer ical|amalga mation|fac tors|rar ity|"
    r"legal ity|distri bution|sup ply|de mand|"
    r"situa tions|war rant|war zone|restrict ed|"
    r"econ omy|adjust ments|fluctua tions|"
    r"extenu ating|circum stances|appro priate|"
    r"emi nently|trace able|records|cross indexed|"
    r"data trail|fake SIN|liabil ity|market ing|"
    r"adver tisements|tailored|Com merce|"
    r"remem bers|sneak ers|neces sarily|secure|"
    r"shield|perva sive|data mining|accu mulate|"
    r"pro files|long term|chance|some one|"
    r"para noia|sur charge|digi tal|serial|"
    r"num bers|filed off|"
    r"char acter creation|Avail ability Rating|"
    r"Op posed Test|Negotia tion|deliv ery|"
    r"deliv ered|addi tional|willing|sell er|"
    r"per cent|extra dice|glitch|criti cal|"
    r"inqui ries|unwanted|atten tion|under cover|"
    r"Lone Star|sting opera tion|spell entrapment|"
    r"Yakuza|rival|enemies|twig ging|conse quences|"
    r"smoothly|extreme|itera tion|stand no|"
    r"chance of|actu ally|acquir ing|"
    r")\b",
    re.I,
)

SOFT_FIX = {
    "favor ites": "favorites",
    "pur chased": "purchased",
    "char acters": "characters",
    "char acter": "character",
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
    "fire arms": "firearms",
    "pro jectile": "projectile",
    "gren ades": "grenades",
    "explo sives": "explosives",
    "explo sion": "explosion",
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
    "drone s": "drones",
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
    "statis tic": "statistic",
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
    "Op posed Test": "Opposed Test",
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
    "Avail ability Rating": "Availability Rating",
    "char acter creation": "character creation",
    "gold plated": "gold-plated",
    "infor mation": "information",
    "orga nization": "organization",
    "corpo ration": "corporation",
    "corpo rations": "corporations",
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
            acc.append((depth, title, page, it))
    return acc


def clean_line(s: str) -> str:
    s = SIDEBAR.sub("", s)
    s = FOOTER.sub("", s)
    s = s.replace("\u2014", " - ").replace("\u2013", "-")
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fix_soft_hyphens(text: str) -> str:
    # generic: letter-space-letter inside words from bad hyphen joins
    def repl(m: re.Match) -> str:
        key = m.group(0)
        low = key.lower()
        for bad, good in SOFT_FIX.items():
            if low == bad.lower():
                # preserve capitalization of first letter roughly
                if key[0].isupper():
                    return good[0].upper() + good[1:]
                return good
        return key

    text = SOFT_WORD.sub(repl, text)
    # generic pattern: lowercase letter, space, 2-4 lowercase letters that form a word fragment
    # Only fix when previous token ends mid-word-ish (short second part)
    text = re.sub(
        r"([a-z]{2,}) ([a-z]{2,4})\b",
        lambda m: m.group(1) + m.group(2)
        if (m.group(1) + m.group(2)).lower()
        in {
            "favorites",
            "purchased",
            "characters",
            "character",
            "market",
            "spirits",
            "technology",
            "equipment",
            "ammunition",
            "availability",
            "cyberware",
            "bioware",
            "commlink",
            "firearms",
            "projectile",
            "grenades",
            "explosives",
            "augmentation",
            "magical",
            "vehicles",
            "electronics",
            "software",
            "skillsofts",
            "imaging",
            "enhancements",
            "security",
            "industrial",
            "chemicals",
            "survival",
            "grapple",
            "biotech",
            "headware",
            "eyeware",
            "earware",
            "bodyware",
            "cyberlimbs",
            "cultured",
            "runners",
            "shadowrunners",
            "metroplex",
            "hardcases",
            "datatrail",
            "entrapment",
            "dealings",
            "connections",
            "practically",
            "difficult",
            "difficulty",
            "necessary",
            "necessarily",
            "especially",
            "particular",
            "particularly",
            "generally",
            "typically",
            "basically",
            "actually",
            "virtually",
            "literally",
            "ultimately",
            "immediately",
            "automatically",
            "additional",
            "additionally",
            "original",
            "originally",
            "potential",
            "potentially",
            "statistics",
            "statistic",
            "modifier",
            "modifiers",
            "opponent",
            "opponents",
            "opposed",
            "resistance",
            "penetration",
            "capacity",
            "concealability",
            "function",
            "functionality",
            "incompatibility",
            "wireless",
            "accessories",
            "protective",
            "clothing",
            "overall",
            "representative",
            "exhaustive",
            "selection",
            "gadgets",
            "customizations",
            "pragmatic",
            "stimulant",
            "disguise",
            "difference",
            "legend",
            "fading",
            "business",
            "communicate",
            "weaponry",
            "precautions",
            "completely",
            "installing",
            "impressive",
            "pimping",
            "cyberdeck",
            "fetishism",
            "toolbox",
            "getting",
            "specialized",
            "introduces",
            "described",
            "includes",
            "numerical",
            "amalgamation",
            "factors",
            "rarity",
            "legality",
            "distribution",
            "supply",
            "demand",
            "situations",
            "warrant",
            "restricted",
            "economy",
            "adjustments",
            "fluctuations",
            "extenuating",
            "circumstances",
            "appropriate",
            "eminently",
            "traceable",
            "liability",
            "marketing",
            "advertisements",
            "remembers",
            "sneakers",
            "pervasive",
            "accumulate",
            "profiles",
            "someone",
            "paranoia",
            "surcharge",
            "digital",
            "numbers",
            "negotiation",
            "delivery",
            "delivered",
            "seller",
            "percent",
            "critical",
            "inquiries",
            "attention",
            "undercover",
            "twigging",
            "consequences",
            "iteration",
            "acquiring",
            "information",
            "organization",
            "corporation",
            "corporations",
            "creation",
            "rating",
            "ratings",
            "glossary",
            "accuracy",
            "reloading",
            "magazine",
            "cylinder",
            "beltfed",
            "penetration",
            "restricted",
            "forbidden",
            "brackets",
            "subsystem",
            "standalone",
            "perception",
            "intuition",
            "concealing",
            "flechette",
            "electrical",
            "effectiveness",
            "stimulant",
            "reduction",
            "implanted",
            "underbarrel",
            "holdouts",
            "pistols",
            "machine",
            "rifles",
            "projectile",
            "designed",
            "specifically",
            "abstract",
            "advantage",
            "enemies",
            "compensation",
            "modifiers",
            "integral",
            "accessories",
            "deployed",
            "folding",
            "detachable",
            "stocks",
            "permanent",
            "qualities",
            "borrow",
            "grubby",
            "hands",
            "certainly",
            "talismonger",
            "deckmeister",
            "specialize",
            "specializes",
            "maintaining",
            "shooting",
            "banishing",
            "hacking",
            "hone",
            "abilities",
            "connection",
            "serving",
            "bonus",
            "social",
            "limit",
        }
        else m.group(0),
        text,
    )
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
            nxt = lines[i + 1]
            cur = cur[:-1] + nxt
            i += 1
        out.append(cur)
        i += 1
    return out


KNOWN_INLINE_HEADS = [
    ("SECTION.11 GLOSSARY", "Glossary"),
    ("SECTION 11 GLOSSARY", "Glossary"),
    ("GLOSSARY", "Glossary"),
    ("STARTING GEAR", "Starting Gear"),
    ("CONTACTS AND AVAILABILITY", "Contacts and Availability"),
    ("DELIVERY TIMES", "Delivery Times"),
    ("FENCING GEAR", "Fencing Gear"),
    ("BLACK MARKET GOODS", "Black Market Goods"),
    ("STANDARD GOODS", "Standard Goods"),
    ("WIRELESS FUNCTIONALITY", "Wireless Functionality"),
    ("GEAR LISTING", "Gear Listing"),
]


def build_street_gear():
    flat = walk(reader.outline)
    headings = []
    capturing = False
    base = 0
    for d, t, p, _ in flat:
        if t == "Street Gear":
            capturing = True
            base = d
            continue
        if capturing:
            if d <= base:
                break
            headings.append((d - base, t))

    # Map normalized keys; prefer longer matches
    heading_keys = []
    for depth, title in headings:
        key = re.sub(r"[^a-z0-9]+", "", title.lower())
        heading_keys.append((key, depth, title))
    heading_keys.sort(key=lambda x: -len(x[0]))

    lines = join_hyphen_breaks(extract_pages(420, 472))
    paras: list[str] = []
    buf = ""
    seen_titles = set()

    def flush():
        nonlocal buf
        if buf:
            paras.append(fix_soft_hyphens(buf.strip()))
            buf = ""

    def emit_heading(depth: int, title: str):
        # avoid immediate duplicates
        marker = f"{depth}:{title.lower()}"
        if paras and paras[-1].lstrip("# ").lower() == title.lower():
            return
        if marker in seen_titles and title.lower() in {
            "glossary",
            "starting gear",
            "contacts and availability",
        }:
            # allow only once for these
            return
        seen_titles.add(marker)
        paras.append("#" * min(depth + 1, 4) + f" {title}")

    for line in lines:
        upper = line.upper()
        matched = None

        # Explicit inline glossary/starting heads
        for needle, nice in KNOWN_INLINE_HEADS:
            if upper.startswith(needle):
                rest = line[len(needle) :].lstrip(" :.-")
                # Glossary terms often follow immediately
                depth = 2 if nice == "Glossary" else 2
                if nice in {"Black Market Goods", "Standard Goods", "Fencing Gear", "Wireless Functionality", "Gear Listing"}:
                    # prefer outline depth if known
                    key = re.sub(r"[^a-z0-9]+", "", nice.lower())
                    for hk, hd, ht in heading_keys:
                        if hk == key:
                            depth = hd
                            nice = ht
                            break
                matched = (depth, nice, rest)
                break

        if matched is None:
            for key, depth, title in heading_keys:
                tu = title.upper()
                # line starts with heading in ALL CAPS
                if upper.startswith(tu) and (
                    line[: len(title)].replace(" ", "").isupper()
                    or upper == tu
                    or re.sub(r"[^a-z0-9]+", "", line.lower()) == key
                ):
                    # Avoid matching short substrings of longer words
                    if len(tu) < 4:
                        continue
                    # Require either exact or ALL-CAPS prefix ending at boundary
                    if upper != tu:
                        after = upper[len(tu) : len(tu) + 1]
                        if after and after.isalnum():
                            continue
                    rest = line[len(title) :].lstrip(" :.-")
                    matched = (depth, title, rest)
                    break

        if matched:
            flush()
            depth, title, rest = matched
            emit_heading(depth, title)
            if rest:
                # Glossary: split term definitions if present
                if title == "Glossary" and ":" in rest:
                    # Accuracy: def...
                    buf = rest
                else:
                    buf = rest
            continue

        # Glossary-style TERM: definition as ### if ALL CAPS term
        m = re.match(r"^([A-Z][A-Za-z0-9 /()'+\-]{2,40}):\s+(.*)$", line)
        if m and paras and any(p.lower().endswith("glossary") or p == "## Glossary" or p == "### Glossary" for p in paras[-5:]):
            term, defin = m.group(1), m.group(2)
            # Only treat as glossary entry if term looks like a heading word(s)
            if term.isupper() or term in {
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
            }:
                flush()
                paras.append(f"#### {term}")
                buf = defin
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
    flush()

    # Drop leading Street Gear duplicate title lines
    while paras and re.sub(r"[^a-z0-9]+", "", paras[0].lower().lstrip("# ")) in {
        "streetgear",
        "1streetgear",
    }:
        paras = paras[1:]

    body = "\n\n".join(paras)
    body = re.sub(r" {2,}", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = fix_soft_hyphens(body)
    # empty page refs: see Foo, ). -> see Foo.
    body = re.sub(r"\(see ([^)]+),\s*\)", r"(see \1)", body)
    body = re.sub(r"see ([A-Za-z][^,]{0,40}),\s*\)", r"see \1)", body)
    body = re.sub(r"\(\s*\)", "", body)
    body = re.sub(r"\s+\)", ")", body)

    md = "# Street Gear\n\n" + body.strip() + "\n"
    path = OUT / "21 - Street Gear.md"
    path.write_text(md, encoding="utf-8")
    print(
        "Street Gear",
        path.stat().st_size,
        "heads",
        sum(1 for p in paras if p.startswith("#")),
    )


def score_chapter(path: Path) -> dict:
    t = path.read_text(encoding="utf-8", errors="replace")
    lines = t.splitlines()
    footer = len(
        re.findall(
            r"\d{2,3}\s+(?:COMBAT|MATRIX|MAGIC|SKILLS|STREET GEAR|GEAR|SHADOW|"
            r"CREATING|THE MATRIX|RUNNING|SOCIAL|VEHICLE|MASTER INDEX)",
            t,
            re.I,
        )
    )
    allcaps = sum(1 for l in lines if len(l) > 12 and l.isupper() and not l.startswith("#"))
    tables = t.count("|---")
    heads = sum(1 for l in lines if l.startswith("##"))
    soft = len(re.findall(r"\b[a-z]{3,} [a-z]{2,4}\b", t))  # rough
    empty_refs = len(re.findall(r"see [^,]{1,40},\s*\)|\(\s*\)", t))
    jammed = len(re.findall(r"[A-Z]{6,} [a-z]", t))  # ALLCAPS then lowercase midstream
    stub = path.stat().st_size < 200
    rating = "GOOD"
    reasons = []
    if stub:
        rating = "STUB"
        reasons.append("image/art stub or empty")
    elif footer > 5 or allcaps > 8 or jammed > 15 or empty_refs > 20:
        rating = "POOR"
    elif footer > 0 or allcaps > 2 or jammed > 5 or tables == 0 and heads < 5 and path.stat().st_size > 50000:
        rating = "FAIR"
    if footer:
        reasons.append(f"{footer} footer artifacts")
    if allcaps:
        reasons.append(f"{allcaps} ALL-CAPS lines")
    if jammed:
        reasons.append(f"{jammed} jammed headers")
    if empty_refs:
        reasons.append(f"{empty_refs} empty page refs")
    if tables == 0 and "Gear" in path.name or "Combat" in path.name or "Tables" in path.name:
        if tables == 0 and path.stat().st_size > 10000 and "Tables" in path.name:
            reasons.append("no markdown tables")
            rating = "POOR" if rating == "GOOD" else rating
    return {
        "file": path.name,
        "kb": path.stat().st_size // 1024,
        "lines": len(lines),
        "heads": heads,
        "tables": tables,
        "footer": footer,
        "allcaps": allcaps,
        "jammed": jammed,
        "empty_refs": empty_refs,
        "rating": rating,
        "reasons": reasons,
    }


def audit_all():
    files = sorted(
        f for f in OUT.glob("*.md") if f.name != "INDEX.md" and re.match(r"^\d+", f.name)
    )
    rows = [score_chapter(f) for f in files]
    # completeness vs outline
    flat = walk(reader.outline)
    chapters = []
    for d, t, p, _ in flat:
        if d == 0 and p is not None:
            chapters.append((t, p))
    # expected page spans
    spans = []
    for i, (t, p) in enumerate(chapters):
        end = chapters[i + 1][1] if i + 1 < len(chapters) else len(reader.pages)
        spans.append((t, p, end, end - p))

    lines = ["# Core Rulebook Chapter Audit", "", f"PDF pages: {len(reader.pages)}", ""]
    lines.append("## Quality scores")
    lines.append("")
    lines.append("| File | KB | Lines | ## | Tables | Rating | Issues |")
    lines.append("|------|----|-------|----|--------|--------|--------|")
    for r in rows:
        issues = "; ".join(r["reasons"]) if r["reasons"] else "-"
        lines.append(
            f"| {r['file']} | {r['kb']} | {r['lines']} | {r['heads']} | {r['tables']} | **{r['rating']}** | {issues} |"
        )

    lines.append("")
    lines.append("## PDF outline top-level spans")
    lines.append("")
    lines.append("| Outline title | Start page (0-based) | Pages |")
    lines.append("|---------------|----------------------|-------|")
    for t, p, end, n in spans:
        lines.append(f"| {t} | {p} | {n} |")

    counts = defaultdict(int)
    for r in rows:
        counts[r["rating"]] += 1
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for k in ("GOOD", "FAIR", "POOR", "STUB"):
        lines.append(f"- **{k}**: {counts[k]}")

    AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Audit written", AUDIT)
    for r in rows:
        print(f"{r['rating']:5} {r['file']}")


reader = PdfReader(str(PDF))
build_street_gear()
audit_all()
