# Projectile Weapons

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

## BOWS
### Bow (generic)
- Cat: Bow
- Src: Core p.423-424 Street Gear; combat p.181-183; range table p.185; RnG tables p.203
- Skill: Archery
- Acc: 6 | Reach: - | DV: (Rating + 2)P | AP: -(Rating / 4)
- Mode: SS | RC: - | Ammo: 1 arrow (reload Simple)
- Avail: Rating | Cost: Rating x 100¥
- Rules: Traditional longbow or modern compound. Max Rating 10 (Street Gear). Min Strength = Rating; if STR < Rating: -3 dice per point below. Range and damage use lowest of: character Strength, bow Rating, arrow Rating. Reload = Simple Action (Ready Weapon). Hacker-proof. Fire arrows (match Rating) / Injection Arrows / RnG heads.
### Krime Trollbow (bow mode)
- Cat: Bow
- Src: SL p.24-25; summary table p.48
- Skill: Archery
- Acc: 4 | Reach: - | DV: (Rating + 2)P | AP: -(Rating / 4)
- Mode: SS | RC: - | Ammo: 1 arrow
- Avail: (Rating)R | Cost: Rating x 150¥ (same SKU as blade mode)
- Rules: Composite bow with blade troll-horn limbs. Ratings 6-12 only. Requires Strength equal to Rating to use properly. Blade melee: Acc 3 Reach 1 DV (STR+1)P AP -1 (Melee Weapons.md). SL summary Avail Rating(R) Cost Rating x 150¥ for bow row.
### Winchester Airbow
- Cat: Bow
- Src: SL p.25 / summary table p.49
- Skill: Archery (or Longarms at -3)
- Acc: 5 | Reach: - | DV: 10P | AP: -2
- Mode: SS | RC: - | Ammo: 1(ml); air tank 5 shots
- Avail: 10R | Cost: 800¥
- Rules: Compressed-air launcher firing specially built arrow-length bolts at ~140 m/s. Medium Crossbow ranges. Only arrows of Rating 6 or higher. Air tank: 5 shots then refill (included automatic pump = 3 Combat Turns; hand pump = 3 minutes). Table Ammo 1(ml) = one projectile loaded; tank is separate. Mounts: top, under, side, internal, stock. May use Longarms at -3 dice. Not silent (loud hiss). Does not play well with water. Roughly bullpup-rifle size.
## CROSSBOWS
### Light Crossbow
- Cat: Crossbow
- Src: Core p.423-424; RnG tables p.203
- Skill: Archery
- Acc: 7 | Reach: - | DV: 5P | AP: -1
- Mode: SS | RC: - | Ammo: 4(m)
- Avail: 2 | Cost: 300¥
- Rules: Modern auto-reload: Ready Weapon not required to reload unless museum piece. Internal magazine up to 4 bolts. Light Crossbow ranges. Bolts / Injection Bolts / RnG heads.
### Medium Crossbow
- Cat: Crossbow
- Src: Core p.423-424; RnG tables p.203
- Skill: Archery
- Acc: 6 | Reach: - | DV: 7P | AP: -2
- Mode: SS | RC: - | Ammo: 4(m)
- Avail: 4R | Cost: 500¥
- Rules: Same crossbow reload/magazine rules as Light. Medium Crossbow ranges.
### Heavy Crossbow
- Cat: Crossbow
- Src: Core p.423-424; RnG tables p.203
- Skill: Archery
- Acc: 5 | Reach: - | DV: 10P | AP: -3
- Mode: SS | RC: - | Ammo: 4(m)
- Avail: 8R | Cost: 1,000¥
- Rules: Same crossbow reload/magazine rules as Light. Heavy Crossbow ranges.
### Ranger Sliver Pistol Crossbow
- Cat: Crossbow
- Src: RnG p.22-23 / tables p.203 (label: Pistol crossbow)
- Skill: Archery
- Acc: 7 | Reach: - | DV: 4P | AP: -
- Mode: SS | RC: - | Ammo: -
- Avail: 6R | Cost: 300¥
- Rules: Stealth-oriented pistol crossbow. Heavy Pistol ranges. Often used with injection bolts (flavor name Ranger Puncture Injection Bolts = Core Injection Bolt stats, no separate SKU). Interchangeable RnG heads apply.
## OTHER ARCHERY (harpoon guns, slingshot)
### Standard Harpoon Gun
- Cat: ArcheryOther
- Src: RnG p.22-23 / tables p.203
- Skill: Archery
- Acc: 5 | Reach: - | DV: 9P | AP: -2
- Mode: SS | RC: - | Ammo: 1
- Avail: 6R | Cost: 200¥
- Rules: Light Crossbow ranges underwater; Heavy Pistol ranges above water.
### Aquadyne Shark-XS Harpoon Gun
- Cat: ArcheryOther
- Src: RnG p.22-23 / tables p.203; Core index alias Shark-X5
- Skill: Archery
- Acc: 5 | Reach: - | DV: 9P | AP: -2
- Mode: SS | RC: - | Ammo: 5(m)
- Avail: 8R | Cost: 800¥
- Rules: CO2-powered; internal magazine. QuickClip line system. Same range rules as Standard (LC underwater / HP above water). Commentary: enough force for heavier line (spidersilk etc.). Core master index lists as Shark-X5.
### Ares Giantslayer Slingshot
- Cat: ArcheryOther
- Src: RnG p.23 / tables p.203
- Skill: Archery
- Acc: 7 | Reach: - | DV: 2P (hard) / chem only (soft) | AP: -
- Mode: SS | RC: - | Ammo: -
- Avail: - | Cost: 50¥
- Rules: Hard projectiles (ball bearings, marbles, etc.): listed DV 2P. Soft projectiles (capsule rounds with contact toxin/drug): no weapon DV; effect from substance only (Core Toxins p.408). Shuriken ranges. See Capsule Rounds ammo entry. Flavor creative loads (RFID trackers, sticky explosive) have no separate SKU stats.
## THROWING WEAPONS
### Throwing knife / shuriken
- Cat: Thrown
- Src: Core p.424; RnG tables p.204
- Skill: Throwing Weapons
- Acc: Phys | Reach: - | DV: (STR + 1)P | AP: -1
- Mode: thrown | RC: - | Ammo: -
- Avail: 4R | Cost: 25¥ each
- Rules: Includes throwing spikes, darts, kunai, shuriken, etc. Ready floor(Agility / 2) knives with one Ready Weapon action. Thrown Knife ranges (shuriken may use Shuriken ranges when using shuriken form; Core table lists both). Wireless + smartlink: if all knives thrown in one Combat Turn are wireless and aimed at the same current target, +1 dice per prior knife that Turn (0 first, +1 second, +2 third, ...).
### Boomerang
- Cat: Thrown
- Src: RnG p.24-25 / tables p.204
- Skill: Throwing Weapons
- Acc: Phys - 1 | Reach: - | DV: (STR + 2)P | AP: -
- Mode: thrown | RC: - | Ammo: -
- Avail: 4 | Cost: 50¥
- Rules: Returning throw needs two tests over two Combat Turns: (1) Throwing Weapons + Agility [Physical] (2) to throw properly; (2) Agility + Reaction (4) to catch on return. A boomerang that hits a target does not return. Aerodynamic Grenade ranges.
### Horizon BoomerEye
- Cat: Thrown
- Src: RnG p.24-25 (variant under Boomerang; also called Renraku Australia in jackpoint)
- Skill: Throwing Weapons
- Acc: as boomerang | Reach: - | DV: as boomerang if used as weapon | AP: -
- Mode: thrown | RC: - | Ammo: -
- Avail: no separate row | Cost: no separate SKU cost in RnG
- Rules: Lightweight sport boomerang with underside video camera for bird's-eye recon. Download footage: Complex Action on return. Wireless: live-feed video while in flight. No separate Avail/Cost table row.
### Harpoon / Javelin (thrown)
- Cat: Thrown
- Src: RnG p.24-25 / tables p.204
- Skill: Throwing Weapons (ranged); Blades (melee)
- Acc: Phys | Reach: 2 melee | DV: (STR + 3)P | AP: -1
- Mode: thrown or melee | RC: - | Ammo: -
- Avail: 6 | Cost: 125¥
- Rules: Thrown: Throwing Weapons; Aerodynamic Grenade ranges. Melee: Blades skill, same DV/AP, Reach 2.
### Cavalier Arms Urban Tribe Tomahawk
- Cat: Thrown
- Src: RnG p.25 / tables p.204
- Skill: Throwing Weapons (ranged); Blades (melee)
- Acc: Phys + 1 | Reach: - | DV: (STR + 2)P | AP: -1
- Mode: thrown or melee | RC: - | Ammo: -
- Avail: 4 | Cost: 200¥
- Rules: Modern composite throwing tomahawk. Thrown: Throwing Weapons, Thrown Knife ranges. Melee: Blades, same DV as thrown.
### Net (thrown) [cross-ref]
- Cat: Thrown
- Src: RnG p.24-25 / tables p.204; full entry Exotic Weapons.md
- Skill: Exotic Ranged Weapon (Net)
- Acc: Phys - 2 | Reach: - | DV: - | AP: -
- Mode: thrown | RC: - | Ammo: -
- Avail: 6 | Cost: 350¥
- Rules: On RnG Throwing Weapons table but uses Exotic Ranged (Net), not Throwing Weapons. Grazing Hit -> subduing; half Thrown Knife ranges. Full procedures, ShockNet, Net Guns: see Exotic Weapons.md. Listed here so the RnG throwing inventory is complete.
## SHAFTS / BOLTS / SLINGSHOT AMMO
### Arrow
- Cat: Ammo
- Src: Core p.424; RnG tables p.203
- Skill: n/a
- Acc: - | Reach: - | DV: as bow (limited by arrow Rating) | AP: as bow
- Mode: - | RC: - | Ammo: shaft
- Avail: Rating | Cost: Rating x 2¥
- Rules: Match bow Rating. With RnG head: complete cost ≈ (Rating x 2¥) + head. Damage/range limited by lowest of STR / bow Rating / arrow Rating.
### Injection Arrow
- Cat: Ammo
- Src: Core p.424
- Skill: n/a
- Acc: - | Reach: - | DV: as arrow + toxin | AP: as arrow
- Mode: - | RC: - | Ammo: 1 dose
- Avail: (Rating + 2)R | Cost: Rating x 20¥
- Rules: Same damage as regular arrow of that Rating + 1 dose drug/toxin (sold separate). Payload delivers only if attack deals >=1 box after Damage Resistance. Injection-vector toxin. Also in Ammunition.md.
### Bolt
- Cat: Ammo
- Src: Core p.424; RnG tables p.203
- Skill: n/a
- Acc: - | Reach: - | DV: as crossbow | AP: as crossbow
- Mode: - | RC: - | Ammo: shaft
- Avail: 2 | Cost: 5¥
- Rules: Standard crossbow bolt. With RnG head: bolt + head cost.
### Injection Bolt
- Cat: Ammo
- Src: Core p.424
- Skill: n/a
- Acc: - | Reach: - | DV: as bolt + toxin | AP: as bolt
- Mode: - | RC: - | Ammo: 1 dose
- Avail: 8R | Cost: 50¥
- Rules: Same damage as regular bolt + 1 dose drug/toxin. Deliver if >=1 box after Damage Resistance. Injection vector. Flavor: Ranger Puncture Injection Bolts (RnG) use these stats.
### Capsule Rounds (slingshot soft ammo)
- Cat: Ammo
- Src: Core/RnG ammo; slingshot use RnG p.23; Ammunition.md
- Skill: n/a (fired with slingshot Archery)
- Acc: firearm table -4 (guns); slingshot uses weapon Acc 7 | Reach: - | DV: firearm -4; slingshot soft = chem only | AP: firearm +4; slingshot soft n/a
- Mode: - | RC: - | Ammo: empty shell
- Avail: 2 | Cost: 5¥ (per 10 typical ammo pack; see Ammunition.md)
- Rules: Empty chem shells. Fill: Logic + Armorer [Mental] (12, 1 minute) Extended per round; 1 chem dose fills 5 capsules. Hit/graze ruptures capsule. In Giantslayer soft mode: substance effect only (no 2P). Firearm use always Light Pistol ranges (Ammunition.md). Also in Ammunition.md.
## ARROWHEADS / SPECIAL SHAFTS (RnG)
### Barbed Head
- Cat: Head
- Src: RnG p.23 / tables p.203
- Skill: n/a
- Acc: - | Reach: - | DV: +1 | AP: -
- Mode: - | RC: - | Ammo: head
- Avail: 5R | Cost: 10¥
- Rules: Adds to shaft. Safe removal: First Aid + Logic [Mental] (3). Failure: (3 - hits) boxes Physical, unresisted.
### Explosive Head
- Cat: Head
- Src: RnG p.23 / tables p.203
- Skill: n/a
- Acc: -1 | Reach: - | DV: +2 | AP: -1
- Mode: - | RC: - | Ammo: head
- Avail: 9F | Cost: 15¥
- Rules: Small shaped-charge tip. Acc/DV/AP mods stack onto the attack.
### Hammerhead
- Cat: Head
- Src: RnG p.23-24 / tables p.203
- Skill: n/a
- Acc: -1 | Reach: - | DV: +1S | AP: +2
- Mode: - | RC: - | Ammo: head
- Avail: 5 | Cost: 5¥
- Rules: Stun-leaning impact head (small-game / live-capture intent).
### Incendiary Head
- Cat: Head
- Src: RnG p.24 / tables p.203
- Skill: n/a
- Acc: -1 | Reach: - | DV: special (WP fire) | AP: special
- Mode: - | RC: - | Ammo: head
- Avail: 12F | Cost: 100¥
- Rules: On successful hit (even Grazing Hit): white phosphorous DV 8P AP -6; burns 3 Combat Turns at 6P AP -4 each turn (Fire Damage Core p.171); may ignite items (GM). Wireless: detonate before impact and split between two targets within 1 m; both defend separately; neither takes initial 8P, only 6P AP -4 for 4 Combat Turns including current.
### Screamer Head
- Cat: Head
- Src: RnG p.24 / tables p.203
- Skill: n/a
- Acc: -2 | Reach: - | DV: -2S (weapon DV as Stun, then -2) | AP: +6
- Mode: - | RC: - | Ammo: head
- Avail: 2 | Cost: 5¥
- Rules: Signaling / stun head. Table DV -2S = convert attack to Stun and apply -2 DV. Reset sound pattern: Simple Action + Logic + Intuition (1). Wireless: reset Free, even in flight.
### Stick-n-Shock Head
- Cat: Head
- Src: RnG p.24 / tables p.203
- Skill: n/a
- Acc: -1 | Reach: - | DV: 8S(e) | AP: -5
- Mode: - | RC: - | Ammo: head
- Avail: 6R | Cost: 25¥
- Rules: Electrical head (absolute DV/AP on table, not a small mod). Pair with Static Shaft for charged flight: Static Shaft adds +4S(e) (table). Commentary: jostling Static Shafts can discharge carelessly.
### Static Shaft
- Cat: Head
- Src: RnG p.24 / tables p.203
- Skill: n/a
- Acc: - | Reach: - | DV: +4S(e) | AP: -
- Mode: - | RC: - | Ammo: shaft (Ares)
- Avail: 6R | Cost: Rating x 25¥
- Rules: Shaft with powder that builds charge during flight. Used with Stick-n-Shock heads for full potential. Rating-priced. Replaces normal shaft (not a tip).
## HARD TARGETS (UNVERIFIED - no local PDF)
### Ares Mono Tip [UNVERIFIED HT]
- Cat: Unverified
- Src: Hard Targets (no local PDF); recorded in Ammunition.md
- Skill: n/a
- Acc: - | Reach: - | DV: - | AP: -2
- Mode: - | RC: - | Ammo: head
- Avail: 8R | Cost: Rating x 30¥
- Rules: UNVERIFIED without Hard Targets PDF. Molecular-edge broadhead. Stats as previously recorded in Ammunition.md only.
### Seeker Shafts [UNVERIFIED HT]
- Cat: Unverified
- Src: Hard Targets (no local PDF); recorded in Ammunition.md
- Skill: n/a
- Acc: - | Reach: - | DV: - | AP: -
- Mode: - | RC: - | Ammo: shaft
- Avail: 12F | Cost: 45¥
- Rules: UNVERIFIED without Hard Targets PDF. Needs smartlinked bow. Lock-on Simple Action (+1 attack, ignore up to 2 situational penalties). Wireless: lock-on Free. Works with head-only arrow types. From Ammunition.md secondary record.
### Throwing Syringe [UNVERIFIED HT]
- Cat: Unverified
- Src: Hard Targets (no local PDF); recorded in Ammunition.md
- Skill: Throwing Weapons or Exotic (confirm in HT when PDF available)
- Acc: - | Reach: - | DV: as injection | AP: -
- Mode: thrown | RC: - | Ammo: 1 dose
- Avail: 6F | Cost: 40¥ each
- Rules: UNVERIFIED without Hard Targets PDF. Thrown exotic ammo/weapon; injection delivery. From Ammunition.md secondary record.
## Inventory checklist
Total entries: 31

Core weapons (5): Bow, Light/Medium/Heavy Crossbow, Throwing knife/shuriken.

Core shafts (4): Arrow, Injection Arrow, Bolt, Injection Bolt.

RnG Archery (4): Standard Harpoon Gun, Shark-XS Harpoon Gun, Pistol Crossbow (Ranger Sliver), Giantslayer Slingshot.

RnG throwing (5): Boomerang, BoomerEye variant, Harpoon/Javelin, Urban Tribe Tomahawk, Net cross-ref.

RnG arrowheads/shafts (7): Barbed, Explosive, Hammerhead, Incendiary, Screamer, Stick-n-Shock, Static Shaft.

Slingshot ammo (1): Capsule Rounds (soft mode).

SL (2): Krime Trollbow (bow mode), Winchester Airbow.

HT unverified (3): Mono Tip, Seeker Shafts, Throwing Syringe.

Cross-refs: Trollbow blade -> Melee Weapons; Net full rules -> Exotic Weapons.
