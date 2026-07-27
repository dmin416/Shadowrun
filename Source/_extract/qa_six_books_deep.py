# -*- coding: utf-8 -*-
"""Deeper loss spot-check: end pages + TOC major starts present in right chapters."""
from pathlib import Path
import pypdf
import re

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")

CHECKS = [
    # (folder, pdf, chapter_file, phrases_that_must_be_in_that_file)
    ("Rigger 5", "rigger5.pdf", "15 - Tables.md", ["Cocotaxi", "Armadillo", "Escalade"]),
    ("Rigger 5", "rigger5.pdf", "08 - Demolition Derby.md", ["Mack Hellhound", "Harley-Davidson Nightmare"]),
    ("Rigger 5", "rigger5.pdf", "14 - Maximum Pursuit.md", ["Bootleg Turn", "Crazy Ivan", "PIT"]),
    ("Street Grimoire", "streetgrimoire.pdf", "09 - Expanded Grimoire.md", ["Napalm", "Shapechange", "Spirit Barrier"]),
    ("Street Grimoire", "streetgrimoire.pdf", "12 - Physical Magic.md", ["Adepts in the", "Elemental Strike"]),
    ("Street Grimoire", "streetgrimoire.pdf", "14 - Turning Lead into Nuyen.md", ["reagent", "alchemy"]),
    ("Forbidden Arcana", "forbiddenarcana.pdf", "05 - Magic Mastery.md", ["Adept Healer", "Blood Necromancer"]),
    ("Forbidden Arcana", "forbiddenarcana.pdf", "11 - Advanced Alchemy.md", ["Ghost Orchid", "reagent"]),
    ("Forbidden Arcana", "forbiddenarcana.pdf", "08 - Blood Magic.md", ["blood magic", "Pulse of Magic"]),
    ("Run Faster", "runfaster.pdf", "08 - Construction Kits.md", ["Sum to Ten", "Point Buy"]),
    ("Run Faster", "runfaster.pdf", "10 - Into the Night.md", ["HMHVV", "Vampire"]),
    ("Run Faster", "runfaster.pdf", "15 - Pack Your Kit.md", ["PACK", "Basic"]),
    ("Street Lethal", "streetlethal.pdf", "04 - Expanded Arsenal.md", ["Narcoject", "Krime Bill"]),
    ("Street Lethal", "streetlethal.pdf", "06 - Opposition Report CorpSec.md", ["CorpSec", "Corporate Security"]),
    ("Street Lethal", "streetlethal.pdf", "10 - Adventure Hooks.md", ["Adventure", "Narcoject"]),
    ("Howling Shadows", "howlingshadows.pdf", "08 - Paranormal Animals.md", ["Abrams Lobster", "Behemoth"]),
    ("Howling Shadows", "howlingshadows.pdf", "14 - Drakes.md", ["Drake", "Eastern"]),
    ("Howling Shadows", "howlingshadows.pdf", "17 - Critter Tables.md", ["CRITTERS", "HABITAT"]),
]

fail = 0
for folder, pdf, fname, phrases in CHECKS:
    path = ROOT / "Source Texts" / folder / fname
    text = path.read_text(encoding="utf-8")
    low = text.lower()
    missing = [p for p in phrases if p.lower() not in low]
    status = "OK" if not missing else "MISS"
    if missing:
        fail += 1
        print(f"{status} {folder}/{fname}: missing {missing}")
    else:
        print(f"{status} {folder}/{fname}")

# Page-span continuity: last chapter should include near-final PDF text samples
print("\n--- End-page continuity ---")
ENDS = [
    ("Rigger 5", "rigger5.pdf", 190, "15 - Tables.md"),
    ("Street Grimoire", "streetgrimoire.pdf", 230, "14 - Turning Lead into Nuyen.md"),
    ("Forbidden Arcana", "forbiddenarcana.pdf", 214, "12 - Index.md"),
    ("Run Faster", "runfaster.pdf", 250, "15 - Pack Your Kit.md"),
    ("Street Lethal", "streetlethal.pdf", 198, "10 - Adventure Hooks.md"),
    ("Howling Shadows", "howlingshadows.pdf", 199, "17 - Critter Tables.md"),
]
for folder, pdf_name, page_idx, fname in ENDS:
    pdf = pypdf.PdfReader(str(ROOT / "Source" / "PDF" / pdf_name))
    if page_idx >= len(pdf.pages):
        page_idx = len(pdf.pages) - 2
    pt = pdf.pages[page_idx].extract_text() or ""
    words = re.findall(r"[A-Za-z]{5,}", pt)
    uniq = []
    for w in words:
        if w.lower() not in uniq:
            uniq.append(w.lower())
        if len(uniq) >= 6:
            break
    body = (ROOT / "Source Texts" / folder / fname).read_text(encoding="utf-8").lower()
    hits = sum(1 for w in uniq if w in body)
    ok = hits >= 2 or len(pt.strip()) < 50
    print(f"{'OK' if ok else 'FAIL'} {folder} PDF[{page_idx}] tokens={uniq} hits={hits}/{len(uniq)}")
    if not ok:
        fail += 1

print(f"\nDeep spot-check failures: {fail}")
