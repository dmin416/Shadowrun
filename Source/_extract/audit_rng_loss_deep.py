# -*- coding: utf-8 -*-
"""Deep loss audit: TOC headings + significant PDF phrases vs RnG markdown."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\rng_loss_report.md")

SECTIONS = [
    ("01 - Contents and Credits.md", 1, 5),
    ("02 - Catspaw.md", 5, 9),
    ("03 - Fight for Your Life.md", 9, 10),
    ("04 - What You Don't Know Kills You.md", 10, 17),
    ("05 - Arsenal.md", 17, 55),
    ("06 - Armor and Protection.md", 55, 87),
    ("07 - Tactics and Tools.md", 87, 105),
    ("08 - Killshots and More.md", 105, 127),
    ("09 - Martial Arts.md", 127, 142),
    ("10 - Fixin All the Broken Drek.md", 142, 143),
    ("11 - Staying Alive.md", 143, 169),
    ("12 - Blow Up Good.md", 169, 197),
    ("13 - Hostile Extraction.md", 197, 201),
    ("14 - Run and Gun Tables.md", 201, 213),
]

# Print page -> which chapter owns it (from TOC major sections)
TOC_CHECKS = [
    # (needle, expected chapter file substring or None for any)
    ("Highland Forge Claymore", "05"),
    ("Horizon-Flynn Rapier", "05"),
    ("Victorinox Memory Blade", "05"),
    ("Ares \"One\" Monosword", "05"),
    ("Cougar Fineblade", "05"),
    ("Nemesis Arms Maul", "05"),
    ("Queen of Hearts", "05"),
    ("Ash Arms Combat Chainsaw", "05"),
    ("Ash Arms Monofilament Chainsaw", "05"),
    ("Aquadyne Shark-XS", "05"),
    ("Ranger Sliver", "05"),
    ("Giantslayer Slingshot", "05"),
    ("Hammerhead", "05"),
    ("Urban Tribe Tomahawk", "05"),
    ("Ares Screech", "05"),
    ("Suruchin", "05"),
    ("FN-AAL Gyrojet", "05"),
    ("Trafalger", "05"),
    ("Retiarus", "05"),
    ("Tiffani", "05"),
    ("Cavalier SafeGuard", "05"),
    ("Self-Defender 2075", "05"),
    ("Fichetti Executive Action", "05"),
    ("Shiawase Arms Puzzler", "05"),
    ("Nitama Sporter", "05"),
    ("Cavalier Deputy", "05"),
    ("PSK-3", "05"),
    ("Savalette Guardian", "05"),
    ("Onotari Arms Violator", "05"),
    ("PPSK-4", "05"),
    ("Ultimax 70", "05"),
    ("Ares Executioner", "05"),
    ("HK Urban Combat", "05"),
    ("AK-98", "05"),
    ("Ares HVAR", "05"),
    ("HK XM30", "05"),
    ("Nitama Optimum", "05"),
    ("Terracotta Arms AM-47", "05"),
    ("JP-K50", "05"),
    ("Pioneer 60", "05"),
    ("Barret Model 122", "05"),
    ("Auto-Assault 16", "05"),
    ("Mossberg AM-CMDT", "05"),
    ("Franchi SPAS-24", "05"),
    ("Remington 990", "05"),
    ("GE Vindicator", "05"),
    ("SA Nemesis", "05"),
    ("FN MAG-5", "05"),
    ("Ultimax MMG", "05"),
    ("Ruhrmetall SF-20", "05"),
    ("Ultimax HMG-2", "05"),
    ("Thunderstruck", "05"),
    ("Ogre Hammer", "05"),
    ("Ares Vigorous", "05"),
    ("Ballista", "05"),
    ("Yakusoku", "05"),
    ("Ares Redline", "05"),
    ("Ares Lancer", "05"),
    ("Ares Archon", "05"),
    ("Shiawase Blazer", "05"),
    ("EX-Explosive", "05"),
    ("Frangible", "05"),
    ("Armanté", "05"),
    ("Mortimer of London", "06"),
    ("Vashon Island", "06"),
    ("Form-Fitting Body Armor", "06"),
    ("Hardened Mil-Spec", "06"),
    ("SecureTech PPP", "06"),
    ("Ruthenium Polymer", "06"),
    ("Gel Packs", "06"),
    ("Responsive Interface Gear", "06"),
    ("Bounding Overwatch", "07"),
    ("Chuck and Charge", "07"),
    ("Slicing the Pie", "07"),
    ("Personal Integrated Tactical", "07"),
    ("RG1", "08"),
    ("RG6", "08"),
    ("Bellringer", "08"),
    ("Through and Through", "08"),
    ("Acrobatic Defender", "08"),
    ("Combat Junkie", "08"),
    ("52 Blocks", "09"),
    ("Carromeleg", "09"),
    ("Gun Kata", "09"),
    ("Wudang Sword", "09"),
    ("Dim Mak", "09"),
    ("Fixin", "10"),
    ("Broken Weapons", "10"),
    ("Killing Frost", "11"),
    ("Radiation Sponge", "11"),
    ("Spacesuit", "11"),
    ("ANFO", "12"),
    ("Linear Cutting Charge", "12"),
    ("Optical Detonator", "12"),
    ("Hostile Extraction", "13"),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("—", "-").replace("–", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = re.sub(r"\s+", " ", s)
    return s.lower()


def significant_phrases(page_text: str, min_len: int = 28) -> list[str]:
    """Pull prose-ish lines long enough to be distinctive."""
    phrases: list[str] = []
    for raw in page_text.splitlines():
        line = raw.strip()
        if len(line) < min_len:
            continue
        if re.match(r"^>>|^<<|RUN\s*&\s*GUN|CONTENTS", line, re.I):
            continue
        if re.match(r"^\d+\s+.+\s*>>\s*$", line):
            continue
        # skip pure table header rows
        if line.upper() in {
            "ACC",
            "REACH",
            "DV",
            "AP",
            "AVAIL",
            "COST",
            "ITEM",
            "MODE",
            "AMMO",
            "RC",
            "NAME",
            "PAGE",
        }:
            continue
        # de-hyphenate soft breaks already joined in page text rarely; take as-is
        phrases.append(line)
    return phrases


def main() -> None:
    doc = fitz.open(str(PDF))
    chapters = {
        fname: norm((OUT / fname).read_text(encoding="utf-8")) for fname, _, _ in SECTIONS
    }
    all_md = "\n".join(chapters.values())

    lines: list[str] = ["# Run & Gun loss audit", ""]

    # TOC/key presence
    lines.append("## TOC / landmark presence")
    lines.append("")
    missing_toc: list[str] = []
    for needle, chap in TOC_CHECKS:
        n = norm(needle)
        hit_files = [f for f, body in chapters.items() if n in body]
        ok = any(f.startswith(chap) for f in hit_files) if chap else bool(hit_files)
        if not hit_files:
            missing_toc.append(needle)
            lines.append(f"- MISSING: `{needle}`")
        elif not ok:
            lines.append(f"- WRONG CHAPTER: `{needle}` in {hit_files} (expected {chap})")
        else:
            pass
    if not missing_toc:
        lines.append("- All landmark needles present in expected chapters.")
    lines.append("")

    # Per-page phrase sampling
    lines.append("## Per-page phrase hits (sample)")
    lines.append("")
    weak_pages: list[tuple[int, str, float, list[str]]] = []
    for fname, start, end in SECTIONS:
        md = chapters[fname]
        for i in range(start, end):
            raw = doc[i].get_text("text") or ""
            phrases = significant_phrases(raw)
            if not phrases:
                continue
            # sample up to 8 longest phrases
            sample = sorted(phrases, key=len, reverse=True)[:8]
            hits = 0
            misses: list[str] = []
            for p in sample:
                # tolerate hyphenation: remove spaces/hyphens for fuzzy
                pn = norm(p)
                pn_compact = re.sub(r"[-\s]", "", pn)
                md_compact = re.sub(r"[-\s]", "", md)
                # also try first 40 chars
                chunk = pn[:40]
                if chunk in md or pn_compact[:35] in md_compact:
                    hits += 1
                else:
                    misses.append(p[:80])
            rate = hits / len(sample)
            if rate < 0.75:
                weak_pages.append((i + 1, fname, rate, misses[:3]))

    if not weak_pages:
        lines.append("- No weak pages (all sampled phrases >= 75% hit rate).")
    else:
        lines.append(f"- Weak pages: {len(weak_pages)}")
        for page, fname, rate, misses in weak_pages[:40]:
            lines.append(f"  - PDF p{page} / `{fname}` hit={rate:.0%}")
            for m in misses:
                lines.append(f"    - miss: {m}")
    lines.append("")

    # Size ratios
    lines.append("## Size ratios")
    lines.append("")
    for fname, start, end in SECTIONS:
        pdf_t = "".join((doc[i].get_text("text") or "") for i in range(start, end))
        md = (OUT / fname).read_text(encoding="utf-8")
        body = md.split("**Source:**", 1)[-1]
        if "\n" in body:
            body = body.split("\n", 1)[1]
        ratio = len(body) / max(1, len(pdf_t))
        flag = " WEAK" if ratio < 0.90 else ""
        lines.append(f"- `{fname}` ratio={ratio:.2f}{flag}")
    lines.append("")

    # Credits / byline checks
    lines.append("## Special checks")
    lines.append("")
    for needle in [
        "Raymond Croteau",
        "Robyn",
        "Jason M. Hardy",
        "Combat Options Cheat Sheet",
        "Gyro mount",
        "YNT SoftWeave",
        "Pulse Weave",
        "Fresnel Fabric",
        "Auto-Injector",
    ]:
        lines.append(f"- `{needle}`: {'YES' if norm(needle) in all_md else 'MISSING'}")

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
