# -*- coding: utf-8 -*-
"""Generate Encyclopedia/Projectile Weapons.md"""
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Encyclopedia\Projectile Weapons.md")

def E(**kw):
    return kw

ITEMS = []

# ========== BOWS ==========
ITEMS += [
E(name="Bow (generic)", cat="Bow", src="Core p.423-424 Street Gear; combat p.181-183; range table p.185; RnG tables p.203",
  skill="Archery",
  acc="6", reach="-", dv="(Rating + 2)P", ap="-(Rating / 4)", mode="SS", rc="-", ammo="1 arrow (reload Simple)",
  avail="Rating", cost="Rating x 100¥",
  rules="Traditional longbow or modern compound. Max Rating 10 (Street Gear). Min Strength = Rating; if STR < Rating: -3 dice per point below. Range and damage use lowest of: character Strength, bow Rating, arrow Rating. Reload = Simple Action (Ready Weapon). Hacker-proof. Fire arrows (match Rating) / Injection Arrows / RnG heads."),
E(name="Krime Trollbow (bow mode)", cat="Bow", src="SL p.24-25; summary table p.48",
  skill="Archery",
  acc="4", reach="-", dv="(Rating + 2)P", ap="-(Rating / 4)", mode="SS", rc="-", ammo="1 arrow",
  avail="(Rating)R", cost="Rating x 150¥ (same SKU as blade mode)",
  rules="Composite bow with blade troll-horn limbs. Ratings 6-12 only. Requires Strength equal to Rating to use properly. Blade melee: Acc 3 Reach 1 DV (STR+1)P AP -1 (Melee Weapons.md). SL summary Avail Rating(R) Cost Rating x 150¥ for bow row."),
E(name="Winchester Airbow", cat="Bow", src="SL p.25 / summary table p.49",
  skill="Archery (or Longarms at -3)",
  acc="5", reach="-", dv="10P", ap="-2", mode="SS", rc="-", ammo="1(ml); air tank 5 shots",
  avail="10R", cost="800¥",
  rules="Compressed-air launcher firing specially built arrow-length bolts at ~140 m/s. Medium Crossbow ranges. Only arrows of Rating 6 or higher. Air tank: 5 shots then refill (included automatic pump = 3 Combat Turns; hand pump = 3 minutes). Table Ammo 1(ml) = one projectile loaded; tank is separate. Mounts: top, under, side, internal, stock. May use Longarms at -3 dice. Not silent (loud hiss). Does not play well with water. Roughly bullpup-rifle size."),
]

# ========== CROSSBOWS ==========
ITEMS += [
E(name="Light Crossbow", cat="Crossbow", src="Core p.423-424; RnG tables p.203",
  skill="Archery",
  acc="7", reach="-", dv="5P", ap="-1", mode="SS", rc="-", ammo="4(m)",
  avail="2", cost="300¥",
  rules="Modern auto-reload: Ready Weapon not required to reload unless museum piece. Internal magazine up to 4 bolts. Light Crossbow ranges. Bolts / Injection Bolts / RnG heads."),
E(name="Medium Crossbow", cat="Crossbow", src="Core p.423-424; RnG tables p.203",
  skill="Archery",
  acc="6", reach="-", dv="7P", ap="-2", mode="SS", rc="-", ammo="4(m)",
  avail="4R", cost="500¥",
  rules="Same crossbow reload/magazine rules as Light. Medium Crossbow ranges."),
E(name="Heavy Crossbow", cat="Crossbow", src="Core p.423-424; RnG tables p.203",
  skill="Archery",
  acc="5", reach="-", dv="10P", ap="-3", mode="SS", rc="-", ammo="4(m)",
  avail="8R", cost="1,000¥",
  rules="Same crossbow reload/magazine rules as Light. Heavy Crossbow ranges."),
E(name="Ranger Sliver Pistol Crossbow", cat="Crossbow", src="RnG p.22-23 / tables p.203 (label: Pistol crossbow)",
  skill="Archery",
  acc="7", reach="-", dv="4P", ap="-", mode="SS", rc="-", ammo="-",
  avail="6R", cost="300¥",
  rules="Stealth-oriented pistol crossbow. Heavy Pistol ranges. Often used with injection bolts (flavor name Ranger Puncture Injection Bolts = Core Injection Bolt stats, no separate SKU). Interchangeable RnG heads apply."),
]

# ========== HARPOON GUNS / SLINGSHOT ==========
ITEMS += [
E(name="Standard Harpoon Gun", cat="ArcheryOther", src="RnG p.22-23 / tables p.203",
  skill="Archery",
  acc="5", reach="-", dv="9P", ap="-2", mode="SS", rc="-", ammo="1",
  avail="6R", cost="200¥",
  rules="Light Crossbow ranges underwater; Heavy Pistol ranges above water."),
E(name="Aquadyne Shark-XS Harpoon Gun", cat="ArcheryOther", src="RnG p.22-23 / tables p.203; Core index alias Shark-X5",
  skill="Archery",
  acc="5", reach="-", dv="9P", ap="-2", mode="SS", rc="-", ammo="5(m)",
  avail="8R", cost="800¥",
  rules="CO2-powered; internal magazine. QuickClip line system. Same range rules as Standard (LC underwater / HP above water). Commentary: enough force for heavier line (spidersilk etc.). Core master index lists as Shark-X5."),
E(name="Ares Giantslayer Slingshot", cat="ArcheryOther", src="RnG p.23 / tables p.203",
  skill="Archery",
  acc="7", reach="-", dv="2P (hard) / chem only (soft)", ap="-", mode="SS", rc="-", ammo="-",
  avail="-", cost="50¥",
  rules="Hard projectiles (ball bearings, marbles, etc.): listed DV 2P. Soft projectiles (capsule rounds with contact toxin/drug): no weapon DV; effect from substance only (Core Toxins p.408). Shuriken ranges. See Capsule Rounds ammo entry. Flavor creative loads (RFID trackers, sticky explosive) have no separate SKU stats."),
]

# ========== THROWING ==========
ITEMS += [
E(name="Throwing knife / shuriken", cat="Thrown", src="Core p.424; RnG tables p.204",
  skill="Throwing Weapons",
  acc="Phys", reach="-", dv="(STR + 1)P", ap="-1", mode="thrown", rc="-", ammo="-",
  avail="4R", cost="25¥ each",
  rules="Includes throwing spikes, darts, kunai, shuriken, etc. Ready floor(Agility / 2) knives with one Ready Weapon action. Thrown Knife ranges (shuriken may use Shuriken ranges when using shuriken form; Core table lists both). Wireless + smartlink: if all knives thrown in one Combat Turn are wireless and aimed at the same current target, +1 dice per prior knife that Turn (0 first, +1 second, +2 third, ...)."),
E(name="Boomerang", cat="Thrown", src="RnG p.24-25 / tables p.204",
  skill="Throwing Weapons",
  acc="Phys - 1", reach="-", dv="(STR + 2)P", ap="-", mode="thrown", rc="-", ammo="-",
  avail="4", cost="50¥",
  rules="Returning throw needs two tests over two Combat Turns: (1) Throwing Weapons + Agility [Physical] (2) to throw properly; (2) Agility + Reaction (4) to catch on return. A boomerang that hits a target does not return. Aerodynamic Grenade ranges."),
E(name="Horizon BoomerEye", cat="Thrown", src="RnG p.24-25 (variant under Boomerang; also called Renraku Australia in jackpoint)",
  skill="Throwing Weapons",
  acc="as boomerang", reach="-", dv="as boomerang if used as weapon", ap="-", mode="thrown", rc="-", ammo="-",
  avail="no separate row", cost="no separate SKU cost in RnG",
  rules="Lightweight sport boomerang with underside video camera for bird's-eye recon. Download footage: Complex Action on return. Wireless: live-feed video while in flight. No separate Avail/Cost table row."),
E(name="Harpoon / Javelin (thrown)", cat="Thrown", src="RnG p.24-25 / tables p.204",
  skill="Throwing Weapons (ranged); Blades (melee)",
  acc="Phys", reach="2 melee", dv="(STR + 3)P", ap="-1", mode="thrown or melee", rc="-", ammo="-",
  avail="6", cost="125¥",
  rules="Thrown: Throwing Weapons; Aerodynamic Grenade ranges. Melee: Blades skill, same DV/AP, Reach 2."),
E(name="Cavalier Arms Urban Tribe Tomahawk", cat="Thrown", src="RnG p.25 / tables p.204",
  skill="Throwing Weapons (ranged); Blades (melee)",
  acc="Phys + 1", reach="-", dv="(STR + 2)P", ap="-1", mode="thrown or melee", rc="-", ammo="-",
  avail="4", cost="200¥",
  rules="Modern composite throwing tomahawk. Thrown: Throwing Weapons, Thrown Knife ranges. Melee: Blades, same DV as thrown."),
E(name="Net (thrown) [cross-ref]", cat="Thrown", src="RnG p.24-25 / tables p.204; full entry Exotic Weapons.md",
  skill="Exotic Ranged Weapon (Net)",
  acc="Phys - 2", reach="-", dv="-", ap="-", mode="thrown", rc="-", ammo="-",
  avail="6", cost="350¥",
  rules="On RnG Throwing Weapons table but uses Exotic Ranged (Net), not Throwing Weapons. Grazing Hit -> subduing; half Thrown Knife ranges. Full procedures, ShockNet, Net Guns: see Exotic Weapons.md. Listed here so the RnG throwing inventory is complete."),
]

# ========== AMMO / SHAFTS ==========
ITEMS += [
E(name="Arrow", cat="Ammo", src="Core p.424; RnG tables p.203",
  skill="n/a",
  acc="-", reach="-", dv="as bow (limited by arrow Rating)", ap="as bow", mode="-", rc="-", ammo="shaft",
  avail="Rating", cost="Rating x 2¥",
  rules="Match bow Rating. With RnG head: complete cost ≈ (Rating x 2¥) + head. Damage/range limited by lowest of STR / bow Rating / arrow Rating."),
E(name="Injection Arrow", cat="Ammo", src="Core p.424",
  skill="n/a",
  acc="-", reach="-", dv="as arrow + toxin", ap="as arrow", mode="-", rc="-", ammo="1 dose",
  avail="(Rating + 2)R", cost="Rating x 20¥",
  rules="Same damage as regular arrow of that Rating + 1 dose drug/toxin (sold separate). Payload delivers only if attack deals >=1 box after Damage Resistance. Injection-vector toxin. Also in Ammunition.md."),
E(name="Bolt", cat="Ammo", src="Core p.424; RnG tables p.203",
  skill="n/a",
  acc="-", reach="-", dv="as crossbow", ap="as crossbow", mode="-", rc="-", ammo="shaft",
  avail="2", cost="5¥",
  rules="Standard crossbow bolt. With RnG head: bolt + head cost."),
E(name="Injection Bolt", cat="Ammo", src="Core p.424",
  skill="n/a",
  acc="-", reach="-", dv="as bolt + toxin", ap="as bolt", mode="-", rc="-", ammo="1 dose",
  avail="8R", cost="50¥",
  rules="Same damage as regular bolt + 1 dose drug/toxin. Deliver if >=1 box after Damage Resistance. Injection vector. Flavor: Ranger Puncture Injection Bolts (RnG) use these stats."),
E(name="Capsule Rounds (slingshot soft ammo)", cat="Ammo", src="Core/RnG ammo; slingshot use RnG p.23; Ammunition.md",
  skill="n/a (fired with slingshot Archery)",
  acc="firearm table -4 (guns); slingshot uses weapon Acc 7", reach="-", dv="firearm -4; slingshot soft = chem only", ap="firearm +4; slingshot soft n/a", mode="-", rc="-", ammo="empty shell",
  avail="2", cost="5¥ (per 10 typical ammo pack; see Ammunition.md)",
  rules="Empty chem shells. Fill: Logic + Armorer [Mental] (12, 1 minute) Extended per round; 1 chem dose fills 5 capsules. Hit/graze ruptures capsule. In Giantslayer soft mode: substance effect only (no 2P). Firearm use always Light Pistol ranges (Ammunition.md). Also in Ammunition.md."),
]

# ========== ARROWHEADS ==========
ITEMS += [
E(name="Barbed Head", cat="Head", src="RnG p.23 / tables p.203",
  skill="n/a",
  acc="-", reach="-", dv="+1", ap="-", mode="-", rc="-", ammo="head",
  avail="5R", cost="10¥",
  rules="Adds to shaft. Safe removal: First Aid + Logic [Mental] (3). Failure: (3 - hits) boxes Physical, unresisted."),
E(name="Explosive Head", cat="Head", src="RnG p.23 / tables p.203",
  skill="n/a",
  acc="-1", reach="-", dv="+2", ap="-1", mode="-", rc="-", ammo="head",
  avail="9F", cost="15¥",
  rules="Small shaped-charge tip. Acc/DV/AP mods stack onto the attack."),
E(name="Hammerhead", cat="Head", src="RnG p.23-24 / tables p.203",
  skill="n/a",
  acc="-1", reach="-", dv="+1S", ap="+2", mode="-", rc="-", ammo="head",
  avail="5", cost="5¥",
  rules="Stun-leaning impact head (small-game / live-capture intent)."),
E(name="Incendiary Head", cat="Head", src="RnG p.24 / tables p.203",
  skill="n/a",
  acc="-1", reach="-", dv="special (WP fire)", ap="special", mode="-", rc="-", ammo="head",
  avail="12F", cost="100¥",
  rules="On successful hit (even Grazing Hit): white phosphorous DV 8P AP -6; burns 3 Combat Turns at 6P AP -4 each turn (Fire Damage Core p.171); may ignite items (GM). Wireless: detonate before impact and split between two targets within 1 m; both defend separately; neither takes initial 8P, only 6P AP -4 for 4 Combat Turns including current."),
E(name="Screamer Head", cat="Head", src="RnG p.24 / tables p.203",
  skill="n/a",
  acc="-2", reach="-", dv="-2S (weapon DV as Stun, then -2)", ap="+6", mode="-", rc="-", ammo="head",
  avail="2", cost="5¥",
  rules="Signaling / stun head. Table DV -2S = convert attack to Stun and apply -2 DV. Reset sound pattern: Simple Action + Logic + Intuition (1). Wireless: reset Free, even in flight."),
E(name="Stick-n-Shock Head", cat="Head", src="RnG p.24 / tables p.203",
  skill="n/a",
  acc="-1", reach="-", dv="8S(e)", ap="-5", mode="-", rc="-", ammo="head",
  avail="6R", cost="25¥",
  rules="Electrical head (absolute DV/AP on table, not a small mod). Pair with Static Shaft for charged flight: Static Shaft adds +4S(e) (table). Commentary: jostling Static Shafts can discharge carelessly."),
E(name="Static Shaft", cat="Head", src="RnG p.24 / tables p.203",
  skill="n/a",
  acc="-", reach="-", dv="+4S(e)", ap="-", mode="-", rc="-", ammo="shaft (Ares)",
  avail="6R", cost="Rating x 25¥",
  rules="Shaft with powder that builds charge during flight. Used with Stick-n-Shock heads for full potential. Rating-priced. Replaces normal shaft (not a tip)."),
]

# ========== HT UNVERIFIED (from Ammo secondary records; no local PDF) ==========
ITEMS += [
E(name="Ares Mono Tip [UNVERIFIED HT]", cat="Unverified", src="Hard Targets (no local PDF); recorded in Ammunition.md",
  skill="n/a",
  acc="-", reach="-", dv="-", ap="-2", mode="-", rc="-", ammo="head",
  avail="8R", cost="Rating x 30¥",
  rules="UNVERIFIED without Hard Targets PDF. Molecular-edge broadhead. Stats as previously recorded in Ammunition.md only."),
E(name="Seeker Shafts [UNVERIFIED HT]", cat="Unverified", src="Hard Targets (no local PDF); recorded in Ammunition.md",
  skill="n/a",
  acc="-", reach="-", dv="-", ap="-", mode="-", rc="-", ammo="shaft",
  avail="12F", cost="45¥",
  rules="UNVERIFIED without Hard Targets PDF. Needs smartlinked bow. Lock-on Simple Action (+1 attack, ignore up to 2 situational penalties). Wireless: lock-on Free. Works with head-only arrow types. From Ammunition.md secondary record."),
E(name="Throwing Syringe [UNVERIFIED HT]", cat="Unverified", src="Hard Targets (no local PDF); recorded in Ammunition.md",
  skill="Throwing Weapons or Exotic (confirm in HT when PDF available)",
  acc="-", reach="-", dv="as injection", ap="-", mode="thrown", rc="-", ammo="1 dose",
  avail="6F", cost="40¥ each",
  rules="UNVERIFIED without Hard Targets PDF. Thrown exotic ammo/weapon; injection delivery. From Ammunition.md secondary record."),
]

header = """# Projectile Weapons

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `runandgun.pdf` · `streetlethal.pdf`
**Books:** Core · RnG · SL. Hard Targets archery extras included only as **UNVERIFIED** (no HT PDF in repo; stats from Ammunition.md secondary record).
**See also:** `Encyclopedia/Ammunition.md` · `Encyclopedia/Melee Weapons.md` (Trollbow blade; harpoon/javelin/tomahawk melee) · `Encyclopedia/Exotic Weapons.md` (Net full rules; bolas) · `Encyclopedia/Firearms.md` · `Encyclopedia/Weapon Accessories.md` · `Encyclopedia/Tools Kits and Survival.md` (grapple gun standalone)
**Out of scope as primary SKUs here:** bolas / gunstock thrown mode (Exotic) · grenades/rockets · firearms · micro flare launcher · grapple gun (Exotic Ranged / survival; underbarrel in Weapon Accessories).

## Schema

| Field | Meaning |
| --- | --- |
| Cat | Bow / Crossbow / ArcheryOther / Thrown / Ammo / Head / Unverified |
| Src | Book + page |
| Skill | Archery · Throwing Weapons · Blades (melee modes) · Exotic where noted |
| Acc | Attack limit; `Phys` = Physical limit |
| Reach | Melee Reach when applicable; `-` if ranged-only |
| DV / AP | Damage / Armor Penetration |
| Mode / RC / Ammo | Fire mode / Recoil Comp / capacity |
| Avail / Cost | Street Availability / nuyen |
| Rules | Full mechanical notes |

## Common rules

### Skills

- Archery: bows, crossbows, pistol crossbow, harpoon guns, slingshot, Airbow.
- Throwing Weapons: knives/shuriken, boomerang, harpoon/javelin (thrown), tomahawk (thrown).
- Blades: harpoon/javelin melee; tomahawk melee; Trollbow blade mode (Melee Weapons.md).
- Exotic Ranged (Net): thrown Net on RnG throwing table (full entry Exotic Weapons.md).

### Bow Rating / Strength (Core Street Gear p.423 + combat p.181)

- Bow Rating = minimum Strength and feeds DV/AP/range formulas.
- Max Rating 10 for generic Core bow; Trollbow 6-12.
- If STR < Rating: -3 dice pool per point below minimum.
- Attack range and damage use the **lowest** of: Strength, bow Rating, arrow Rating.

### Crossbows (Core p.424)

- Modern: auto-reload; no Ready Weapon to reload (unless museum piece).
- Internal magazine (m) up to 4 bolts (Light/Medium/Heavy).

### Injection shafts (Core p.424)

- Injection arrow/bolt: normal shaft damage + 1 dose chem (sold separate).
- Payload delivers only if attack deals >=1 box after Damage Resistance (injection vector).

### Arrowheads (RnG)

- Mount on arrow/bolt shafts. Complete projectile cost ≈ shaft + head (Static Shaft is a shaft, not a tip).
- Acc/DV/AP columns are modifiers unless a head sets absolute DV (Stick-n-Shock 8S(e), Incendiary special).

### Range table meters (Core p.185)

Dice pool by category: Short +0 / Medium -1 / Long -3 / Extreme -6.

**Ballistic projectiles**

| Weapon | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| Bow | 0-STR | to STR x 10 | to STR x 30 | to STR x 60 |
| Light Crossbow | 0-6 | 7-24 | 25-60 | 61-120 |
| Medium Crossbow | 0-9 | 10-36 | 37-90 | 91-150 |
| Heavy Crossbow | 0-15 | 16-45 | 46-120 | 121-180 |

**Impact projectiles**

| Weapon | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| Thrown Knife | 0-STR | to STR x 2 | to STR x 3 | to STR x 5 |
| Shuriken | 0-STR | to STR x 2 | to STR x 5 | to STR x 7 |

**Thrown grenades (also used by some thrown weapons)**

| Type | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| Aerodynamic | 0-STR x 2 | to STR x 4 | to STR x 8 | to STR x 15 |

**Mapped ranges for RnG/SL extras**

- Pistol crossbow: Heavy Pistol 0-5 / 6-20 / 21-40 / 41-60
- Harpoon guns: Light Crossbow underwater; Heavy Pistol above water
- Slingshot: Shuriken ranges
- Airbow: Medium Crossbow ranges
- Tomahawk thrown: Thrown Knife ranges
- Boomerang / harpoon-javelin thrown: Aerodynamic Grenade ranges
- Thrown Net: half Thrown Knife ranges (round up); see Exotic Weapons.md

## Catalog

"""

def render(d):
    return "\n".join([
        f"### {d['name']}",
        f"- Cat: {d['cat']}",
        f"- Src: {d['src']}",
        f"- Skill: {d['skill']}",
        f"- Acc: {d['acc']} | Reach: {d['reach']} | DV: {d['dv']} | AP: {d['ap']}",
        f"- Mode: {d['mode']} | RC: {d['rc']} | Ammo: {d['ammo']}",
        f"- Avail: {d['avail']} | Cost: {d['cost']}",
        f"- Rules: {d['rules']}",
        "",
    ])

CAT_ORDER = ["Bow", "Crossbow", "ArcheryOther", "Thrown", "Ammo", "Head", "Unverified"]
CAT_HEAD = {
    "Bow": "BOWS",
    "Crossbow": "CROSSBOWS",
    "ArcheryOther": "OTHER ARCHERY (harpoon guns, slingshot)",
    "Thrown": "THROWING WEAPONS",
    "Ammo": "SHAFTS / BOLTS / SLINGSHOT AMMO",
    "Head": "ARROWHEADS / SPECIAL SHAFTS (RnG)",
    "Unverified": "HARD TARGETS (UNVERIFIED - no local PDF)",
}

parts = [header]
for cat in CAT_ORDER:
    group = [i for i in ITEMS if i["cat"] == cat]
    if not group:
        continue
    parts.append(f"## {CAT_HEAD[cat]}\n")
    for i in group:
        parts.append(render(i))

parts.append("## Inventory checklist\n")
parts.append(f"Total entries: {len(ITEMS)}\n\n")
parts.append("""Core weapons (5): Bow, Light/Medium/Heavy Crossbow, Throwing knife/shuriken.

Core shafts (4): Arrow, Injection Arrow, Bolt, Injection Bolt.

RnG Archery (4): Standard Harpoon Gun, Shark-XS Harpoon Gun, Pistol Crossbow (Ranger Sliver), Giantslayer Slingshot.

RnG throwing (5): Boomerang, BoomerEye variant, Harpoon/Javelin, Urban Tribe Tomahawk, Net cross-ref.

RnG arrowheads/shafts (7): Barbed, Explosive, Hammerhead, Incendiary, Screamer, Stick-n-Shock, Static Shaft.

Slingshot ammo (1): Capsule Rounds (soft mode).

SL (2): Krime Trollbow (bow mode), Winchester Airbow.

HT unverified (3): Mono Tip, Seeker Shafts, Throwing Syringe.

Cross-refs: Trollbow blade -> Melee Weapons; Net full rules -> Exotic Weapons.
""")

text = "".join(parts)
for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"')):
    text = text.replace(a, b)
OUT.write_text(text, encoding="utf-8")
print("Wrote", OUT, "entries", len(ITEMS), "bytes", OUT.stat().st_size)
