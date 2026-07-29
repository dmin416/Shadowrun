"""Generate Ch.08 stat blocks and Ch.17 index inserts for Encyclopedia/Critters.md."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COND = ROOT / "Source Texts/Howling Shadows/Howling Shadows Condensed.md"
CH17 = ROOT / "Source Texts/Howling Shadows/17 - Critter Tables.md"
OUT08 = ROOT / "Encyclopedia/_ch08_insert.md"
OUT17 = ROOT / "Encyclopedia/_ch17_insert.md"


def gen_ch08() -> str:
    text = COND.read_text(encoding="utf-8")
    m = re.search(r"## 08 - Paranormal Animals(.*?)## 08b", text, re.S)
    if not m:
        raise SystemExit("Ch.08 section not found")
    parts = re.split(r"\n### ", m.group(1))
    blocks = ["## Paranormal animals (*Howling Shadows* Ch. 08)", ""]
    for part in parts[1:]:
        lines = part.strip().split("\n")
        name = lines[0].strip()
        body = "\n".join(lines[1:])
        if name.startswith("**Story"):
            continue
        header_line = re.search(r"(\| B \|[^\n]+\n\|[-| ]+\n\|[^\n]+)", body)
        if not header_line:
            continue
        table = header_line.group(1)
        has_m = "| M |" in table.split("\n")[0]
        init = re.search(r"\*\*Init:\*\*\s*([^|\n]+)", body)
        move = re.search(r"\*\*Move:\*\*\s*([^|\n]+)", body)
        cm = re.search(r"\*\*CM:\*\*\s*([^|\n]+)", body)
        lim = re.search(r"\*\*Limits:\*\*\s*([^|\n]+)", body)
        arm = re.search(r"\*\*Armor:\*\*\s*([^|\n]+)", body)
        skills = re.search(r"\*\*Skills:\*\*\s*([^\n]+)", body)
        powers = re.search(r"\*\*Powers:\*\*\s*([^\n]+)", body)
        weak = re.search(r"\*\*Weaknesses:\*\*\s*([^\n]+)", body)
        note = re.search(r"\*\*Note[s]?:\*\*\s*([^\n]+)", body)
        qual = re.search(r"\*\*Qualities:\*\*\s*([^\n]+)", body)
        blocks.append(f"### {name}")
        blocks.append("")
        blocks.append(table)
        blocks.append("")
        summary = " | ".join(
            x
            for x in [
                f"Init {init.group(1).strip()}" if init else None,
                f"Move {move.group(1).strip()}" if move else None,
                f"CM {cm.group(1).strip()}" if cm else None,
                f"Limits {lim.group(1).strip()}" if lim else None,
                f"Armor {arm.group(1).strip()}" if arm else None,
            ]
            if x
        )
        blocks.append(summary)
        if skills:
            blocks.append(f"Skills: {skills.group(1).strip()}")
        if qual:
            blocks.append(f"Qualities: {qual.group(1).strip()}")
        if powers:
            blocks.append(f"Powers: {powers.group(1).strip()}")
        if weak:
            blocks.append(f"Weaknesses: {weak.group(1).strip()}")
        if note:
            blocks.append(f"Notes: {note.group(1).strip()}")
        blocks.append("")
    return "\n".join(blocks)


def gen_ch17() -> str:
    hab_data = {
        "Coastal regions": [("Roc, lesser", "71")],
        "Desert": [
            ("Deathrattle", "57"),
            ("Juggernaut", "65"),
            ("Nova scorpion", "69"),
        ],
        "Forest": [
            ("Agropelter", "53"),
            ("Angel squirrel", "93"),
            ("Bandit", "54"),
            ("Basilisk", "403, SR5"),
            ("Black annis", "55"),
            ("Centaur", "55"),
            ("Cerberus hound", "56"),
            ("Deathspiral butterfly", "58"),
            ("Drop bear", "60"),
            ("Fenrir wolf", "61"),
            ("Flatworm viper", "95"),
            ("Harpy", "62"),
            ("Hell hound", "405, SR5"),
            ("Horned bear", "64"),
            ("Iridescent owl", "97"),
            ("Juggernaut", "65"),
            ("Killdeer", "97"),
            ("Martichoras", "65"),
            ("Montauk", "99"),
            ("Pandamonium", "100"),
            ("Phoenician birds", "70"),
            ("Peryton", "71"),
            ("Piasma", "71"),
            ("Razorcat", "102"),
            ("Shadowhound", "72"),
            ("Shardik", "103"),
            ("Snow snake", "72"),
            ("Spider beast", "73"),
            ("Spidermoose", "105"),
            ("Unicorn", "76"),
            ("Volleying porcupines", "76"),
            ("Wolverine, greater", "77"),
        ],
        "Freshwater": [
            ("Devil jack diamond", "59"),
            ("Souleater leech", "105"),
            ("Spark salmon", "104"),
        ],
        "Grasslands / plains / prairie": [
            ("Centaur", "55"),
            ("Cockatrice", "404, SR5"),
            ("Conway's cheetah", "94"),
            ("Hellcow", "96"),
            ("Juggernaut", "65"),
            ("Killdeer", "97"),
            ("Ozian baboon", "69"),
            ("Phoenician birds", "70"),
            ("Pegasus", "70"),
            ("Peryton", "71"),
            ("Unicorn", "76"),
        ],
        "Jungle": [
            ("Blink sloth", "93"),
            ("Blood monkey", "55"),
            ("Chupacabra (Havana variant)", "132, Hard Targets"),
            ("Chupacabra mk. II", "111"),
            ("Gomatia", "62"),
            ("Kokoro cobra", "98"),
            ("Naga", "68"),
            ("Ozian baboon", "69"),
            ("Phoenician birds", "70"),
            ("Spider beast", "73"),
            ("Void wasp", "106"),
        ],
        "Mountains": [
            ("Cerberus hound", "56"),
            ("Gargoyle", "61"),
            ("Sasquatch", "406, SR5"),
            ("Thunderbird, greater", "73"),
        ],
        "Saltwater": [
            ("Abrams lobster", "52"),
            ("Magui", "133, Hard Targets"),
            ("Meistersinger", "66"),
            ("Merrow", "68"),
            ("Night Manta", "134, Hard Targets"),
            ("Sea leech", "102"),
            ("Spark salmon", "104"),
        ],
        "Swamp": [("Afanc", "53"), ("Behemoth", "54")],
        "Tundra": [("Snow snake", "72")],
        "Underground": [("Black annis", "55"), ("Troglodyte", "75")],
        "Urban": [
            ("Agropelter", "53"),
            ("Amphora mite", "92"),
            ("Bandit", "54"),
            ("Barghest", "403, SR5"),
            ("Deathspiral butterfly", "58"),
            ("Demon rat", "58"),
            ("Devil rat", "404, SR5"),
            ("Flatworm viper", "95"),
            ("Gargoyle", "61"),
            ("Ghoul", "404, SR5"),
            ("Glow rat", "95"),
            ("Harpy", "62"),
            ("Horned bear", "64"),
            ("Montauk", "99"),
            ("Neogargoyle", "99"),
            ("Phoenician birds", "70"),
            ("Radhound", "100"),
            ("Razorcat", "102"),
            ("Shadowhound", "72"),
            ("Snow snake", "72"),
        ],
    }
    raw = CH17.read_text(encoding="utf-8")
    idx = raw.split("MASTER CRITTER INDEX", 1)[1]
    idx = re.sub(r"\s+", " ", idx.replace("\n", " ")).strip()
    idx = re.sub(
        r"p\.\s+((?:\d\s*){2,})(?=\s+[A-Za-z])",
        lambda m: "p. " + re.sub(r"\s", "", m.group(1)),
        idx,
    )
    master = []
    for m in re.finditer(
        r"([A-Za-z][A-Za-z,' \-\(\)/]+?)\s+p\.\s*"
        r"(\d+(?:,\s*(?:SR5|Hard Targets|Aetherology))?(?:,\s*[A-Za-z][^,]+(?:,\s*SR5)?)?)",
        idx,
    ):
        name = m.group(1).strip()
        page = m.group(2).strip()
        page = re.sub(r",Hard Targets", ", Hard Targets", page)
        page = re.sub(r",Aetherology", ", Aetherology", page)
        page = re.sub(r",SR5", ", SR5", page)
        master.append((name, page))
    seen = set()
    uniq = []
    for name, page in master:
        key = name.lower()
        if key not in seen:
            seen.add(key)
            uniq.append((name, page))

    lines = [
        "## Critters by habitat (*Howling Shadows* Ch. 17)",
        "",
        "Mundane critters, protosapients, extraplanar travelers, technocritters, and most Infected omitted (chapter note). Page refs are *Howling Shadows* unless noted.",
        "",
    ]
    for hab, items in hab_data.items():
        lines += [f"### {hab}", "", "| Critter | Page |", "| --- | --- |"]
        for n, p in items:
            lines.append(f"| {n} | {p} |")
        lines.append("")
    lines += [
        "## Master critter index (Ch. 17)",
        "",
        "Alphabetical index from *Howling Shadows* Ch. 17. Cross-book refs preserved.",
        "",
        "| Critter | Page |",
        "| --- | --- |",
    ]
    for n, p in uniq:
        lines.append(f"| {n} | {p} |")
    lines.append("")
    return "\n".join(lines)


def merge_critters():
    critters = ROOT / "Encyclopedia/Critters.md"
    text = critters.read_text(encoding="utf-8")
    ch08 = OUT08.read_text(encoding="utf-8")
    ch17 = OUT17.read_text(encoding="utf-8")

    text = re.sub(
        r"\*\*Verified from:\*\*[^\n]+",
        "**Verified from:** `Howling Shadows Condensed.md` (Ch. 08-10) · `17 - Critter Tables.md` · `Hard Targets Condensed.md`",
        text,
        count=1,
    )
    text = re.sub(
        r"Agent reference \(SR5\)\. Condensed[^\n]+",
        "Agent reference (SR5). Paranormal animals (Ch. 08), mutants/toxic (Ch. 09), extraplanar (Ch. 10), habitat/index (Ch. 17), plus *Hard Targets* Caribbean blocks.",
        text,
        count=1,
    )

    if "## Paranormal animals" not in text:
        text = text.replace(
            "\n---\n\n## Mutants and toxic critters",
            f"\n---\n\n{ch08}\n---\n\n## Mutants and toxic critters",
        )
    else:
        text = re.sub(
            r"## Paranormal animals \(.*?Ch\. 08\).*?(?=\n---\n\n## Mutants and toxic critters)",
            ch08.rstrip() + "\n",
            text,
            flags=re.S,
        )

    text = re.sub(
        r"\n---\n\n## Critters by habitat.*",
        f"\n---\n\n{ch17.rstrip()}\n",
        text,
        flags=re.S,
    )

    critters.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    OUT08.write_text(gen_ch08(), encoding="utf-8")
    OUT17.write_text(gen_ch17(), encoding="utf-8")
    merge_critters()
    print("Wrote", OUT08, OUT17, "and merged Critters.md")
