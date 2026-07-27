"""Careful Street Gear + Index rebuild. Footers only when page-numbered."""
from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

PDF = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source Texts\Shadowrun Fifth Edition Core Rulebook")

# ONLY strip running headers/footers that include page numbers
FOOTER = re.compile(
    r"(?<![A-Za-z])\d{2,3}\s+"
    r"(?:GEAR RATINGS|BUYING GEAR|STREET GEAR|GEAR LISTING|ELECTRONICS|"
    r"AUGMENTATION|SHADOWRUN,? FIFTH EDITION|MASTER INDEX|IMPORTANT TABLES|"
    r"COMBAT|THE MATRIX|MAGIC|SKILLS|CREATING A SHADOWRUNNER|"
    r"HELPS AND HINDRANCES|GAMEMASTER ADVICE|LIFE IN THE SIXTH WORLD|"
    r"SHADOWRUN CONCEPTS|VEHICLES AND DRONES|FIREARMS|MELEE WEAPONS|"
    r"CLOTHING AND ARMOR|AMMUNITION|INDUSTRIAL CHEMICALS|SURVIVAL GEAR|"
    r"BIOTECH|WIRELESS FUNCTIONALITY|CONCEALING GEAR|CARRYING GEAR|"
    r"SIZE COSTS|FENCING GEAR|COMMUNICATIONS AND COUNTERMEASURES|"
    r"BREAKING AND ENTERING|OPTICAL AND IMAGING DEVICES|SECURITY DEVICES|"
    r"SENSORS|HEADWARE|EYEWARE|EARWARE|BODYWARE|CYBERLIMBS|BIOWARE|"
    r"CULTURED BIOWARE|MAGICAL EQUIPMENT|PROJECTILE AND THROWING WEAPONS|"
    r"GRENA DES, ROCKETS,? AND MISSILES|GRENADES, ROCKETS,? AND MISSILES|"
    r"DOCWAGON CONTRACT|SLAP PATCHES|RFID TAGS|SOFTWARE|SKILLSOFTS|"
    r"ID AND CREDIT|TOOLS|AUDIO DEVICES|AUDIO ENHANCEMENTS|"
    r"VISION ENHANCEMENTS|OPTICAL DEVICES|COMMLINKS|CYBERDECKS|"
    r"BIKES|CARS|TRUCKS AND VANS|BOATS|SUBMARINES|FIXED-WING AIRCRAFT|"
    r"ROTORCRAFT|VTOL/VSTOL|MICRODRONES|MINIDRONES|SMALL DRONES|"
    r"MEDIUM DRONES|LARGE DRONES|STANDARD GOODS|BLACK MARKET GOODS|"
    r"\(IL\)LEGALITY|JURISDICTION|NOTICING HIDDEN GEAR|"
    r"CARRYING CAPACITY|ENCUMBRANCE|USING UNADAPTED GEAR|"
    r"WIRELESS BONUSES|TURNING IT OFF|INCOMPATIBILITY|"
    r"FIREARM ACCESSORIES|EXPLOSIVES)"
    r"(?:\s*(?:>>|<<))?(?:\s*\d{2,3})?(?![A-Za-z0-9])",
    re.I,
)
# Trailing form: SECTION 420
FOOTER2 = re.compile(
    r"(?<![A-Za-z])(?:"
    r"GEAR RATINGS|BUYING GEAR|STREET GEAR|GEAR LISTING|ELECTRONICS|"
    r"AUGMENTATION|MASTER INDEX|FIREARMS|MELEE WEAPONS|CLOTHING AND ARMOR|"
    r"VEHICLES AND DRONES|AMMUNITION|BIOTECH|HEADWARE|WIRELESS FUNCTIONALITY"
    r")\s+\d{2,3}(?![A-Za-z0-9])",
    re.I,
)
SIDEBAR = re.compile(r"(?:<<|>>).{0,60}")
PAGE_ONLY = re.compile(r"^\d{1,3}$")

SOFT = [
    (r"\bfavor ites\b", "favorites"),
    (r"\bpur chase\b", "purchase"),
    (r"\bpur chased\b", "purchased"),
    (r"\bchar acters\b", "characters"),
    (r"\bchar acter\b", "character"),
    (r"\bmar ket\b", "market"),
    (r"\bspir its\b", "spirits"),
    (r"\bequip ment\b", "equipment"),
    (r"\bammu nition\b", "ammunition"),
    (r"\bammuni tion\b", "ammunition"),
    (r"\bavail ability\b", "availability"),
    (r"\bcyber ware\b", "cyberware"),
    (r"\bbio ware\b", "bioware"),
    (r"\bcom mlink\b", "commlink"),
    (r"\bfire arms\b", "firearms"),
    (r"\bpro jectile\b", "projectile"),
    (r"\bgren ades\b", "grenades"),
    (r"\bexplo sives\b", "explosives"),
    (r"\baug mentation\b", "augmentation"),
    (r"\bmag ical\b", "magical"),
    (r"\bvehi cles\b", "vehicles"),
    (r"\belec tronics\b", "electronics"),
    (r"\bsoft ware\b", "software"),
    (r"\bskill softs\b", "skillsofts"),
    (r"\benhan cements\b", "enhancements"),
    (r"\bsecur ity\b", "security"),
    (r"\bindus trial\b", "industrial"),
    (r"\bchem icals\b", "chemicals"),
    (r"\bsur vival\b", "survival"),
    (r"\bgrap ple\b", "grapple"),
    (r"\bbio tech\b", "biotech"),
    (r"\bhead ware\b", "headware"),
    (r"\beye ware\b", "eyeware"),
    (r"\bear ware\b", "earware"),
    (r"\bbody ware\b", "bodyware"),
    (r"\bcyber limbs\b", "cyberlimbs"),
    (r"\bcul tured\b", "cultured"),
    (r"\brun ners\b", "runners"),
    (r"\bmetro plex\b", "metroplex"),
    (r"\bhard cases\b", "hardcases"),
    (r"\bdata trail\b", "datatrail"),
    (r"\bentrap ment\b", "entrapment"),
    (r"\bdeal ings\b", "dealings"),
    (r"\bconnec tions\b", "connections"),
    (r"\bprac tically\b", "practically"),
    (r"\bpracti cally\b", "practically"),
    (r"\bdiffi cult\b", "difficult"),
    (r"\bneces sarily\b", "necessarily"),
    (r"\bneces sary\b", "necessary"),
    (r"\bespe cially\b", "especially"),
    (r"\bpartic ularly\b", "particularly"),
    (r"\bpartic ular\b", "particular"),
    (r"\bgener ally\b", "generally"),
    (r"\btypi cally\b", "typically"),
    (r"\bbasi cally\b", "basically"),
    (r"\bactu ally\b", "actually"),
    (r"\bvirtu ally\b", "virtually"),
    (r"\bliter ally\b", "literally"),
    (r"\bulti mately\b", "ultimately"),
    (r"\bimme diately\b", "immediately"),
    (r"\bauto matically\b", "automatically"),
    (r"\baddi tional\b", "additional"),
    (r"\bpoten tial\b", "potential"),
    (r"\bpoten tially\b", "potentially"),
    (r"\bstatis tics\b", "statistics"),
    (r"\bmodi fiers\b", "modifiers"),
    (r"\bmodi fier\b", "modifier"),
    (r"\boppo sed\b", "opposed"),
    (r"\bresis tance\b", "resistance"),
    (r"\bpenetra tion\b", "penetration"),
    (r"\bcapa city\b", "capacity"),
    (r"\bconceala bility\b", "concealability"),
    (r"\bfunc tionality\b", "functionality"),
    (r"\bincom patibility\b", "incompatibility"),
    (r"\bwire less\b", "wireless"),
    (r"\bacces sories\b", "accessories"),
    (r"\bprotec tive\b", "protective"),
    (r"\bcloth ing\b", "clothing"),
    (r"\bover all\b", "overall"),
    (r"\brepre sentative\b", "representative"),
    (r"\bexhaus tive\b", "exhaustive"),
    (r"\bselec tion\b", "selection"),
    (r"\bgad gets\b", "gadgets"),
    (r"\bcus tomizations\b", "customizations"),
    (r"\bprag matic\b", "pragmatic"),
    (r"\bstimu lant\b", "stimulant"),
    (r"\bdis guise\b", "disguise"),
    (r"\bdiffer ence\b", "difference"),
    (r"\bbusi ness\b", "business"),
    (r"\bcom municate\b", "communicate"),
    (r"\bweap onry\b", "weaponry"),
    (r"\bpre cautions\b", "precautions"),
    (r"\bcom pletely\b", "completely"),
    (r"\bimpres sive\b", "impressive"),
    (r"\bpimp ing\b", "pimping"),
    (r"\bcyber deck\b", "cyberdeck"),
    (r"\bfetish ism\b", "fetishism"),
    (r"\btool box\b", "toolbox"),
    (r"\bspecial ized\b", "specialized"),
    (r"\bintro duces\b", "introduces"),
    (r"\bdescri bed\b", "described"),
    (r"\binclu des\b", "includes"),
    (r"\bnumer ical\b", "numerical"),
    (r"\bamalga mation\b", "amalgamation"),
    (r"\bfac tors\b", "factors"),
    (r"\brar ity\b", "rarity"),
    (r"\blegal ity\b", "legality"),
    (r"\bdistri bution\b", "distribution"),
    (r"\bsitua tions\b", "situations"),
    (r"\brestrict ed\b", "restricted"),
    (r"\becon omy\b", "economy"),
    (r"\bfluctua tions\b", "fluctuations"),
    (r"\bextenu ating\b", "extenuating"),
    (r"\bcircum stances\b", "circumstances"),
    (r"\bappro priate\b", "appropriate"),
    (r"\bemi nently\b", "eminently"),
    (r"\btrace able\b", "traceable"),
    (r"\bcross indexed\b", "cross-indexed"),
    (r"\bliabil ity\b", "liability"),
    (r"\bmarket ing\b", "marketing"),
    (r"\badver tisements\b", "advertisements"),
    (r"\bremem bers\b", "remembers"),
    (r"\bsneak ers\b", "sneakers"),
    (r"\bperva sive\b", "pervasive"),
    (r"\bdata mining\b", "data-mining"),
    (r"\baccu mulate\b", "accumulate"),
    (r"\bpro files\b", "profiles"),
    (r"\blong term\b", "long-term"),
    (r"\bsome one\b", "someone"),
    (r"\bpara noia\b", "paranoia"),
    (r"\bsur charge\b", "surcharge"),
    (r"\bdigi tal\b", "digital"),
    (r"\bnum bers\b", "numbers"),
    (r"\bNegotia tion\b", "Negotiation"),
    (r"\bdeliv ery\b", "delivery"),
    (r"\bdeliv ered\b", "delivered"),
    (r"\bsell er\b", "seller"),
    (r"\bper cent\b", "percent"),
    (r"\bcriti cal\b", "critical"),
    (r"\binqui ries\b", "inquiries"),
    (r"\batten tion\b", "attention"),
    (r"\bunder cover\b", "undercover"),
    (r"\bsting opera tion\b", "sting operation"),
    (r"\btwig ging\b", "twigging"),
    (r"\bconse quences\b", "consequences"),
    (r"\bitera tion\b", "iteration"),
    (r"\bacquir ing\b", "acquiring"),
    (r"\binfor mation\b", "information"),
    (r"\bgold plated\b", "gold-plated"),
]


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
    s = FOOTER2.sub("", s)
    s = s.replace("\u2014", " - ").replace("\u2013", "-")
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fix_soft(text: str) -> str:
    for pat, rep in SOFT:
        text = re.sub(pat, rep, text, flags=re.I)
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


GLOSSARY_TERMS = [
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
]


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

    heading_keys = []
    for depth, title in headings:
        key = re.sub(r"[^a-z0-9]+", "", title.lower())
        heading_keys.append((key, depth, title))
    heading_keys.sort(key=lambda x: -len(x[0]))

    lines = join_hyphen_breaks(extract_pages(420, 472))
    paras: list[str] = []
    buf = ""
    used: set[str] = set()
    in_glossary = False

    def flush():
        nonlocal buf
        if buf:
            paras.append(fix_soft(buf.strip()))
            buf = ""

    def emit(depth: int, title: str, key: str):
        nonlocal in_glossary
        if key in used:
            return False
        used.add(key)
        flush()
        if paras and paras[-1].startswith("#") and paras[-1].lstrip("# ").lower() == title.lower():
            return False
        paras.append("#" * min(depth + 1, 4) + f" {title}")
        in_glossary = title.lower() == "glossary"
        return True

    for line in lines:
        upper = line.upper().strip()

        # Skip chapter title lines
        if re.sub(r"[^a-z0-9]+", "", line.lower()) == "streetgear":
            continue

        # Glossary box
        if "GLOSSARY" in upper and (
            upper.startswith("SECTION") or upper == "GLOSSARY" or upper.startswith("GLOSSARY")
        ):
            emit(2, "Glossary", "glossary")
            rest = re.sub(r"^SECTION\.?\s*\d+\s*", "", line, flags=re.I)
            rest = re.sub(r"^GLOSSARY\s*", "", rest, flags=re.I).strip(" :.-")
            if rest:
                buf = rest
            continue

        # Starting Gear / Contacts and Availability as ALL CAPS jammed or alone
        for needle, nice, depth in [
            ("STARTING GEAR", "Starting Gear", 2),
            ("CONTACTS AND AVAILABILITY", "Contacts and Availability", 2),
            ("DELIVERY TIMES", "Delivery Times", 2),
        ]:
            if upper == needle or upper.startswith(needle + " "):
                key = re.sub(r"[^a-z0-9]+", "", nice.lower())
                rest = line[len(needle) :].lstrip(" :.-")
                if rest and rest[0].islower():
                    # mid-sentence mention; don't promote
                    pass
                else:
                    emit(depth, nice, key)
                    if rest:
                        buf = rest
                    break
        else:
            # Outline headings, first occurrence only
            matched = False
            for key, depth, title in heading_keys:
                if key in used:
                    continue
                tu = title.upper()
                if not upper.startswith(tu):
                    continue
                if len(upper) > len(tu) and upper[len(tu)].isalnum():
                    continue
                rest = line[len(title) :].lstrip(" :.-")
                if rest and rest[0].islower():
                    continue
                title_span_upper = line[: len(title)].isupper() or upper == tu
                exact = re.sub(r"[^a-z0-9]+", "", line.lower()) == key
                if not (title_span_upper or exact):
                    continue
                # Avoid matching short words inside longer ALL CAPS lines poorly
                if emit(depth, title, key):
                    if rest:
                        buf = rest
                    matched = True
                    break
            if matched:
                continue

            # Glossary terms
            if in_glossary:
                hit = False
                for term in GLOSSARY_TERMS:
                    if line.startswith(term + ":"):
                        flush()
                        paras.append(f"#### {term}")
                        buf = line[len(term) + 1 :].strip()
                        hit = True
                        break
                if hit:
                    continue

            # FENCING GEAR jammed mid-paragraph without having been emitted
            jam = re.match(r"^(FENCING GEAR)\s+(.+)$", line, re.I)
            if jam:
                emit(1, "Fencing Gear", "fencinggear")
                buf = jam.group(2)
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
            continue

        # if for-else broke via break, continue loop
        continue

    flush()

    # Fix Delivery Times mid-sentence split
    body = "\n\n".join(paras)
    body = re.sub(
        r"given on the\n\n#{1,4} Delivery Times\n\ntable",
        "given on the Delivery Times table",
        body,
    )
    body = fix_soft(body)
    body = re.sub(r" {2,}", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)

    # Ensure major parent headings exist even if PDF text missed ALL CAPS
    # (already emitted from outline matches when present)

    md = "# Street Gear\n\n" + body.strip() + "\n"
    path = OUT / "21 - Street Gear.md"
    path.write_text(md, encoding="utf-8")

    # Report which outline headings were missed
    missed = [t for _, t in headings if re.sub(r"[^a-z0-9]+", "", t.lower()) not in used]
    print("Street Gear", path.stat().st_size, "heads used", len(used), "missed", len(missed))
    if missed:
        print("  missed:", ", ".join(missed[:20]), ("..." if len(missed) > 20 else ""))


def build_index():
    lines = join_hyphen_breaks(extract_pages(472, 494))
    entries: list[str] = []
    buf = ""
    for line in lines:
        line = FOOTER.sub("", line)
        line = FOOTER2.sub("", line)
        line = SIDEBAR.sub("", line)
        line = re.sub(r"\s+", " ", line).strip()
        if not line or PAGE_ONLY.fullmatch(line):
            continue
        if re.match(r"^(?:SHADOWRUN|MASTER INDEX|INDEX)\b", line, re.I):
            continue
        if re.fullmatch(r"[A-Z]", line):
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
        e = FOOTER2.sub("", e)
        e = re.sub(r"\s+", " ", e).strip()
        if len(e) < 2:
            continue
        letter = e[0].upper() if e[0].isalpha() else "#"
        by_letter.setdefault(letter, []).append(e)

    parts = [
        "# Index",
        "",
        "Alphabetical master index from the Core Rulebook PDF. "
        "Many entries cite other Fifth Edition books (codes such as SG, RF, CF, DT, RG, R5) "
        "as well as SR5.",
        "",
    ]
    for letter in sorted(k for k in by_letter if k != "#") + (["#"] if "#" in by_letter else []):
        parts.append(f"## {letter}")
        parts.append("")
        for e in by_letter[letter]:
            parts.append(f"- {e}")
        parts.append("")

    path = OUT / "22 - Book Index.md"
    path.write_text("\n".join(parts), encoding="utf-8")
    print("Index", path.stat().st_size, "entries", sum(len(v) for v in by_letter.values()))


reader = PdfReader(str(PDF))
build_street_gear()
build_index()
