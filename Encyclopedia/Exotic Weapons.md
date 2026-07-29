# Exotic Weapons

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `runandgun.pdf` · `streetlethal.pdf`
**Books:** Core · RnG · SL. CT has no separate exotic SKU list (no CT PDF in repo; INDEX cross-check only).
**See also:** `Encyclopedia/Melee Weapons.md` (shares exotic melee rows) · `Encyclopedia/Projectile Weapons.md` (Archery / Throwing skill gear) · `Encyclopedia/Firearms.md` · `Encyclopedia/Weapon Accessories.md` · `Encyclopedia/Ammunition.md` · `Encyclopedia/Drugs Toxins and Chemicals.md`
**Out of scope:** Archery skill weapons (harpoon gun, pistol crossbow, slingshot, bows, Krime Trollbow archery mode); Throwing skill weapons (boomerang, javelin, tomahawk) except when a SKU explicitly requires Exotic Ranged for a mode; tasers (Pistols skill); grenade/missile/torpedo launchers using Heavy Weapons (e.g. ArmTech PTL-02); cyber implant weapons; Narcoject Dazzler and Krime Stun-O-Net (Weapon Accessories, not Exotic skill weapons); flavor-only net variants without SKU rows (Terra Cotta ShredNet); gyrojet alternate munitions without SKU rows (jelly rockets).

## Schema

| Field | Meaning |
| --- | --- |
| Cat | Melee / Ranged / Laser / Flame / Ammo / Power / Accessory |
| Src | Book + page |
| Skill | Exact Exotic Melee / Exotic Ranged specialization required |
| Acc | Attack limit; `Phys` = Physical limit; `N(M)` wireless |
| Reach | Melee Reach only; `-` if ranged |
| DV / AP | Damage / Armor Penetration; `-` none |
| Mode / RC / Ammo | Fire mode / Recoil Comp / capacity (`PU` = power unit) |
| Avail / Cost | Street Availability / nuyen |
| Rules | Full mechanical notes |

## Common rules

### Skills

- Exotic Melee Weapon and Exotic Ranged Weapon are separate Active skills; each weapon subtype is a specialization / required specialty (Core Skills).
- Subtype must match the weapon (Monofilament Whip != Garrote != Blowgun).
- Core Special Weapons: use Exotic Ranged Weapon skill (Core p.429).

### Shock / electricity melee

- Unless a row overrides: 10 charges; wall recharge 1 / 10 seconds; wireless induction 1 / hour (Core stun baton family).

### Peak-discharge power (RnG p.52)

- Used by lasers, Screech, PEP, Thunderstruck (not exotic), etc.
- Power clip 10 PU Avail 14F 400¥; satchel 20 PU 16F 900¥; backpack 30 PU 20F 2,500¥.
- Recharge 1 PU / 30 minutes. Cord attach to satchel/backpack = Simple Action.
- Not usable as improvised explosives.

### Laser stack penalties (RnG p.47)

- No recoil.
- Range DV: Medium -1, Long -2, Extreme -3 (per category past Short).
- Visibility DV: Light -1, Moderate -2, Heavy -3 (Environmental Visibility Conditions, Core p.175).
- Range and Visibility modifiers stack.
- Top + underbarrel accessories only; cannot be modified otherwise.
- Require Exotic Ranged Weapon (Laser Weapons).

### Flamethrower basics (RnG p.49)

- Pilot light ready: Complex / Wireless Simple / DNI Free.
- Area Complex: up to 2 additional targets within 2 m of another; one Attack Test, separate Defense; DV -2 per additional target.
- Suppressive Fire consumes 4 shots; may use Flechette Suppressive Fire rules (RnG p.120).
- Fire damage (Core p.171); ignites items (GM).
- Taser ranges but only -1 at Extreme; no penalty at Long or closer.
- Exotic Ranged Weapon (Flamethrowers). No accessories except biometric/advanced safety.

### Cross-file exotic melee

- Full exotic melee SKUs are duplicated here for a single exotic lookup and also live in Melee Weapons.md.

## Catalog

## EXOTIC MELEE
### Monofilament whip
- Cat: Melee
- Src: Core p.423 / Street Gear melee table; RnG tables p.202
- Skill: Exotic Melee Weapon (Monofilament Whip)
- Acc: 5(7) | Reach: 2 | DV: 12P | AP: -8
- Mode: - | RC: - | Ammo: -
- Avail: 12F | Cost: 10,000¥
- Rules: Line extends to 2 m; retracts into handle. Glitch: weighted tip snags; disentangle before another proper attack. Crit glitch: hit self for base DV (resist normally). Wireless: Ready Weapon = Free; built-in safety auto-retracts on glitch (no snag); Acc +2 (5->7). Also in Melee Weapons.md.
### Garrote (standard)
- Cat: Melee
- Src: RnG p.20 / tables p.202
- Skill: Exotic Melee Weapon (Garrote)
- Acc: 5 | Reach: 0 | DV: (STR+4)S | AP: -6
- Mode: - | RC: - | Ammo: -
- Avail: - | Cost: 50¥
- Rules: Wire/cord + handles (or improvised). PLACE: attack with Called Shot Location; need >=1 net hit (like subduing). After placed, later Action Phase: deal weapon DV and/or improve hold with another Attack Test and/or knock down. Break free: Agility + Unarmed Combat [Physical], threshold = attacker net hits on all attacks so far; or Knock Out of Hands / grip-breaking attack. Also in Melee Weapons.md. Nunchaku choke may substitute Clubs for Exotic(Garrote) at -2 (SL; Clubs SKU).
### Ares "Queen of Hearts" Monofilament Garrote
- Cat: Melee
- Src: RnG p.20 / tables p.202
- Skill: Exotic Melee Weapon (Garrote)
- Acc: 5 | Reach: 0 | DV: (STR+6)P | AP: -8
- Mode: - | RC: - | Ammo: -
- Avail: 18F | Cost: 2,000¥
- Rules: Same Garrote placement/break procedures as standard. Dangerous to untrained users on mistakes. Also in Melee Weapons.md.
### Bullwhip
- Cat: Melee
- Src: RnG p.20-21 / tables p.202
- Skill: Exotic Melee Weapon (Whip)
- Acc: 6 | Reach: 2 | DV: (STR+1)P | AP: +3
- Mode: - | RC: - | Ammo: -
- Avail: 6 | Cost: 100¥
- Rules: Within 2 m: Blast Out of Hands called shot + Opposed Strength to yank item toward attacker instead of away (+2 dice to that Strength Test); or Knockdown called shot to trip. Attacker must be within 2 m. Also in Melee Weapons.md.
### Ash Arms Combat Chainsaw
- Cat: Melee
- Src: RnG p.21 / tables p.202
- Skill: Exotic Melee Weapon (Chainsaw)
- Acc: 5 | Reach: 1 | DV: 8P | AP: -4
- Mode: - | RC: - | Ammo: -
- Avail: 6R | Cost: 2,000¥
- Rules: Weaponized (safeties stripped for swinging). Also in Melee Weapons.md. See civilian/tool sibling entry.
### Ash Arms Combat Chainsaw (civilian/tool)
- Cat: Melee
- Src: RnG p.21
- Skill: Exotic Melee Weapon (Chainsaw)
- Acc: 3 | Reach: 1 | DV: 6P | AP: -4
- Mode: - | RC: - | Ammo: -
- Avail: 2 | Cost: 150¥
- Rules: Non-combat tool version of Combat Chainsaw: Acc reduced to 3; DV reduced by 2 (8P->6P); Avail 2; Cost 150¥. Same Reach/AP as combat model unless GM rules otherwise.
### Ash Arms Monofilament Chainsaw
- Cat: Melee
- Src: RnG p.21 / tables p.202
- Skill: Exotic Melee Weapon (Chainsaw)
- Acc: 5 | Reach: 1 | DV: 12P | AP: -8
- Mode: - | RC: - | Ammo: -
- Avail: 8R | Cost: 7,500¥
- Rules: Weaponized monofilament chainsaw. Also in Melee Weapons.md. See civilian/tool sibling entry.
### Ash Arms Monofilament Chainsaw (civilian/tool)
- Cat: Melee
- Src: RnG p.21
- Skill: Exotic Melee Weapon (Chainsaw)
- Acc: 3 | Reach: 1 | DV: 10P | AP: -8
- Mode: - | RC: - | Ammo: -
- Avail: 6R | Cost: 1,500¥
- Rules: Non-combat tool version: Acc 3; DV -2 (12P->10P); Avail 6R; Cost 1,500¥. Flavor: cutting concrete / sculpting stone.
### Krime Stun Lance
- Cat: Melee
- Src: SL p.24-25
- Skill: Exotic Melee Weapon (Stun Lance)
- Acc: 4 | Reach: 2 | DV: 10S(e) | AP: -5
- Mode: - | RC: - | Ammo: charges (stun baton rules)
- Avail: 9R | Cost: 900¥
- Rules: ~3 m stun baton/lance. Troll sizes only (Using Unadapted Gear, Core p.420). Charge rules as stun baton (10 charges; wall 1/10 sec; wireless induction 1/hour); SL table does not override recharge. Also in Melee Weapons.md.
## EXOTIC RANGED
### Ares S-III Super Squirt
- Cat: Ranged
- Src: Core p.429-430 Special Weapons
- Skill: Exotic Ranged Weapon (Special Weapons / Super Squirt)
- Acc: 3 | Reach: - | DV: Chemical (no weapon DV) | AP: -
- Mode: SA | RC: - | Ammo: 20(c)
- Avail: 7R | Cost: 950¥
- Rules: Fires DMSO gel packs. DMSO forces skin to absorb carried chemical as Contact-vector toxin into bloodstream (Core Toxins p.408); the attack itself causes no damage. Buy chemical/toxin separately. Light Pistol ranges. Top + underbarrel accessories. DMSO gel packs are not a separate ammo SKU in Core ammo table.
### Fichetti Pain Inducer
- Cat: Ranged
- Src: Core p.429-430
- Skill: Exotic Ranged Weapon (Special Weapons / Pain Inducer)
- Acc: 3 | Reach: - | DV: Special (toxin-like) | AP: -
- Mode: SS | RC: - | Ammo: Special (10 charges)
- Avail: 11R | Cost: 5,000¥
- Rules: Microwave-like pain. Toxin attack Power 8, Immediate; resist Body + Willpower. If modified Power > Mental limit: next Action Phase must flee the pain. Attacker may hold beam with Complex Action (until GM says target dodged/covered). If trapped in beam: incapacitated; dice pool modifier equal to modified Power on all tests while held. SMG ranges; top + underbarrel accessories. 10 charges; wall recharge 1 charge / 10 seconds. Wireless: induction recharge 1 charge / hour.
### Parashield Dart Pistol
- Cat: Ranged
- Src: Core p.429-430
- Skill: Exotic Ranged Weapon (Special Weapons / Dart Gun)
- Acc: 5 | Reach: - | DV: as Drug/Toxin | AP: -
- Mode: SA | RC: - | Ammo: 5(c)
- Avail: 4R | Cost: 600¥
- Rules: Fires Injection Darts (Core p.433-434) with Narcoject or other payload (sold separate). Heavy Pistol ranges; top-mounted accessories only. Wireless: dart reports hit/inject success; may report gross tissue anomalies (Device Rating 1). See Injection Darts ammo entry.
### Parashield Dart Rifle
- Cat: Ranged
- Src: Core p.429-430
- Skill: Exotic Ranged Weapon (Special Weapons / Dart Gun)
- Acc: 6 | Reach: - | DV: as Drug/Toxin | AP: -
- Mode: SA | RC: - | Ammo: 6(m)
- Avail: 6R | Cost: 1,200¥
- Rules: Compressed-air Injection Darts. Includes top-mounted imaging scope. Sporting rifle ranges; top + underbarrel accessories. Same wireless dart reporting as pistol. See Injection Darts ammo entry.
### Ares Screech Sonic Rifle
- Cat: Ranged
- Src: RnG p.26 / tables p.204
- Skill: Exotic Ranged Weapon (Sonic Rifle)
- Acc: 6 | Reach: - | DV: 7S | AP: *
- Mode: SS | RC: - | Ammo: 10(c) peak-discharge (1 PU/shot)
- Avail: 16R | Cost: 8,000¥
- Rules: Variable beam uses shotgun rules (Core p.180) for targets affected, DV modifier, ranges. Damage Resistance: Willpower (not Body); ignores standard armor. Damper earware +2 to resist. Hush/Silence spell: -1 DV per Spellcasting hit. Hit: Disorientation + Nausea (Core p.409; use Damage Resistance in place of Toxin Resistance). Immune spirits (no standard biology). Peak-discharge packs; 1 PU/shot.
### Blowgun
- Cat: Ranged
- Src: RnG p.26 / tables p.204
- Skill: Exotic Ranged Weapon (Blowgun)
- Acc: 8 | Reach: - | DV: 1P | AP: -
- Mode: SS | RC: - | Ammo: 1(ml)
- Avail: 4 | Cost: 15¥
- Rules: Almost always toxin/drug on needle (sold separate). Deliver toxin via Called Shot Location to unarmored area; success delivers poison. Crit glitch: may inhale own dart; some modern mouthpieces have cross-guard safeguard. Taser ranges.
### Bolas (standard)
- Cat: Ranged
- Src: RnG p.26-27 / tables p.204
- Skill: Exotic Ranged Weapon (Bolas)
- Acc: Phys | Reach: - | DV: (STR+3)S | AP: +4
- Mode: thrown | RC: - | Ammo: -
- Avail: 6 | Cost: 75¥
- Rules: HIT for damage: Exotic Ranged (Bolas) Attack Test with listed DV/AP. WRAP Called Shot Location: target Agility + Gymnastics [Physical] vs attacker net hits or fall prone. Remove wrap: Agility + Escape Artist [Physical] (6, 1 Action Phase) Extended, or Complex Action with sharp knife. Shuriken ranges. Boom-bolas (grenade improvisation, no separate SKU): -2 Acc; miss scatter max distance direction 7; success = grenades at 0 distance (Multiple Simultaneous Blast Core p.183).
### Nemesis Arms Suruchin Monofilament Bolas
- Cat: Ranged
- Src: RnG p.26-27 / tables p.204
- Skill: Exotic Ranged Weapon (Bolas)
- Acc: Phys | Reach: - | DV: (STR+3)S / 12P | AP: +4 / -8
- Mode: thrown | RC: - | Ammo: -
- Avail: 18F | Cost: 4,000¥
- Rules: Hit use left slash stats; wrap also forces immediate Damage Resistance with right slash stats + Gymnastics test. While wrapped, Escape Artist or movement attempts each require another Damage Resistance Test. Shuriken ranges.
### FN-AAL Gyrojet Pistol
- Cat: Ranged
- Src: RnG p.26-27 / tables p.204
- Skill: Exotic Ranged Weapon (Gyrojet)
- Acc: 5 | Reach: - | DV: 10P | AP: -2
- Mode: SA | RC: - | Ammo: 10(c)
- Avail: 12F | Cost: 2,000¥
- Rules: 6mm mini-rockets explode on impact. Heavy pistol accessories + Heavy Pistol ranges. Underwater: +2 DV to standard munitions (plus other mods). Commentary: alternate munitions (jelly rockets etc.) exist; no separate SKU stats in RnG.
### Mortimer of London "Trafalger" Gun Cane
- Cat: Ranged
- Src: RnG p.27 / tables p.204
- Skill: Exotic Ranged Weapon (Gun Cane)
- Acc: 6 | Reach: - | DV: 7P | AP: -
- Mode: SS | RC: - | Ammo: 1(b)
- Avail: 9R | Cost: 750¥
- Rules: Caseless only; no accessories. Taser ranges. Concealability: +0 whole cane; -6 to detect true nature (Core p.419).
### Knockoff Gun Cane
- Cat: Ranged
- Src: RnG p.27 / tables p.204
- Skill: Exotic Ranged Weapon (Gun Cane)
- Acc: 5 | Reach: - | DV: 9P | AP: -
- Mode: SS | RC: - | Ammo: 1 (destroyed after fire)
- Avail: 6R | Cost: 150¥
- Rules: Same cane rules as Trafalger. Destroyed after firing. Table Ammo column is blank for knockoff.
### SA Retiarus Net Gun (Basic)
- Cat: Ranged
- Src: RnG p.28 / tables p.204
- Skill: Exotic Ranged Weapon (Net Gun)
- Acc: 5 | Reach: - | DV: - | AP: -
- Mode: SS | RC: - | Ammo: 4(b)
- Avail: 9 | Cost: 750¥ gun (ammo load separate)
- Rules: On hit: apply thrown Net subduing rules (RnG p.25). Light Pistol ranges; no accessories. Large net vs normal target: -2 Agility on break tests; large target vs normal net: +2 Agility. Full ammo load: see Net Gun ammo (Basic).
### SA Retiarus Net Gun (XL)
- Cat: Ranged
- Src: RnG p.28 / tables p.204
- Skill: Exotic Ranged Weapon (Net Gun)
- Acc: 5 | Reach: - | DV: - | AP: -
- Mode: SS | RC: - | Ammo: 2(b)
- Avail: 9 | Cost: 1,000¥ gun (ammo load separate)
- Rules: For trolls / larger creatures. Same net-gun procedures as Basic. Full ammo load: see Net Gun ammo (XL).
### Tiffani "Elegance" Shooting Bracer
- Cat: Ranged
- Src: RnG p.28 / tables p.204
- Skill: Exotic Ranged Weapon (Shooting Bracer)
- Acc: 5(6) | Reach: - | DV: 7P | AP: -
- Mode: SS | RC: - | Ammo: 1(b)
- Avail: 10R | Cost: 1,250¥
- Rules: Caseless only; no accessories. Taser ranges. Acc 6 with laser sight on newest model. Concealability -5 to hide true function (Core p.419).
### Net (thrown)
- Cat: Ranged
- Src: RnG p.24-25 / tables p.204
- Skill: Exotic Ranged Weapon (Net)
- Acc: Phys-2 | Reach: - | DV: - | AP: -
- Mode: thrown | RC: - | Ammo: -
- Avail: 6 | Cost: 350¥
- Rules: Grazing Hit success: target in subduing combat (Core p.195). Attacker must move to target for Subduing actions. Break free: Agility + Unarmed Combat or Agility + Escape Artist Complex Action vs attacker net hits (Agility not Strength). Half Thrown Knife ranges (round up). Flavor variants without separate SKU rows: Terra Cotta ShredNet (barbed); Ares ShockNet (electrical) -> use ShockNet ammo when firing from Net Gun.
### Narcoject Gas Gun
- Cat: Ranged
- Src: SL p.43-45
- Skill: Exotic Ranged Weapon (Gas Gun)
- Acc: 5 | Reach: - | DV: As toxin | AP: -
- Mode: SS | RC: - | Ammo: 5x2(c)
- Avail: 8R | Cost: 1,500¥
- Rules: Inhalation-vector toxin stream via compressed air mixing with separate toxin doses. Armor useless; respiratory protection helps (Core Toxin Protection table p.408). Single target or Complex Action vs up to 3 targets in 4 m spread (one Attack, separate Defense); multi consumes 2 toxin rounds. Cloud ~2 Combat Turns (GM: wind/confined). Enclosed space dangerous to everyone. Air tank refill with included electric pump: 3 minutes. Toxin doses separate. Taser ranges.
### Narcoject PEP
- Cat: Ranged
- Src: SL p.44-45
- Skill: Exotic Ranged Weapon (PEP)
- Acc: 6 | Reach: - | DV: 10S | AP: - / -5*
- Mode: SS | RC: - | Ammo: 2x10(c); 2 PU/shot
- Avail: 12R | Cost: 7,500¥
- Rules: Pulsed Energy Projectile: short intense laser pulses vaporize surface -> plasma flash/bang/stun (non-lethal design). *AP none if armor can Chemical Seal; AP -5 if clothing/armor with gaps. Heavy Pistol ranges; top + underbarrel only. Peak-discharge packs (RnG p.52); typically 2 clips of 10 charges.
### Narcoject Trackstopper
- Cat: Ranged
- Src: SL p.44-46
- Skill: Exotic Ranged Weapon (Trackstopper / foam projector)
- Acc: 5 | Reach: - | DV: - | AP: -
- Mode: SS | RC: - | Ammo: 6
- Avail: 15R | Cost: 8,500¥
- Rules: Backpack foam stream (adapted from discontinued Ares Fogger Glop Cannon). Hardens in 1 Combat Round (not instant). Per net hit: -1 Agility; at Agility 0 cannot move or take limb actions. Hardened foam Structure 4, Armor 6; formulated to allow breathing. Dissolves in 1 hour or instantly with Narcoject solvent (free with foam refills). Light Pistol ranges. See Foam Refills ammo.
### Gunstock War Club (thrown mode)
- Cat: Ranged
- Src: SL p.22
- Skill: Exotic Ranged Weapon (when thrown); Clubs in melee
- Acc: Phys | Reach: 0 thrown | DV: (STR+2)P thrown | AP: -1
- Mode: thrown | RC: - | Ammo: -
- Avail: 10 (melee SKU) | Cost: 200¥ (same SKU)
- Rules: Melee profile is Clubs Acc 5 Reach 1 DV (STR+3)P AP -1 (see Melee Weapons.md). Thrown requires Exotic Ranged Weapon skill (no Clubs).
### Shiawase/Nemesis Arms Man-Catcher
- Cat: Ranged
- Src: SL p.133 CorpSec Arsenal
- Skill: Exotic Ranged Weapon (Man-Catcher)
- Acc: 4 | Reach: - | DV: Ammo | AP: -
- Mode: SS | RC: - | Ammo: 10(m)
- Avail: 18F | Cost: 6,000¥
- Rules: ~50 cm tube launcher; ~30 cm warhead of expanding rubber compound. Pre-program detonate: timer, proximity, or impact. Impact: 50% chance compound works (1D6, success on 4+; no Edge rerolls). Range table not listed in SL. See Man-Catcher ammo.
## LASER WEAPONS (Exotic Ranged: Laser Weapons)
### Ares Redline
- Cat: Laser
- Src: RnG p.47-48 / tables p.208
- Skill: Exotic Ranged Weapon (Laser Weapons)
- Acc: 9 | Reach: - | DV: 5P | AP: -10
- Mode: SA | RC: - | Ammo: 10(c) power clip or external; 1 PU/shot
- Avail: 14F | Cost: 7,500¥
- Rules: Laser basics (Common rules). Detachable power clip or external (usually satchel). SMG ranges. Top + underbarrel only; cannot otherwise modify.
### Ares Lancer MP Laser
- Cat: Laser
- Src: RnG p.48 / tables p.208
- Skill: Exotic Ranged Weapon (Laser Weapons)
- Acc: 7 | Reach: - | DV: 7P | AP: -10
- Mode: SA | RC: - | Ammo: 2x10(c) or external; 2 PU/shot
- Avail: 18F | Cost: 16,000¥
- Rules: Laser basics. Twin power clips or satchel/backpack. Assault Rifle ranges. Note: RnG Lancer body text mislabels power line as Archon; table + Archon entry confirm Lancer = 2 PU, Archon = 4 PU.
### Ares Archon Heavy MP Laser
- Cat: Laser
- Src: RnG p.49 / tables p.208
- Skill: Exotic Ranged Weapon (Laser Weapons)
- Acc: 7 | Reach: - | DV: 10P | AP: -10
- Mode: SA | RC: - | Ammo: External only; 4 PU/shot
- Avail: 24F | Cost: 35,000¥
- Rules: Laser basics. Std upgrades: bipod; tripod or gyro stabilization mount; sound suppressor. Sniper rifle ranges. External pack (almost always backpack) or emplacement power link (unlimited while powered).
## FLAMETHROWERS (Exotic Ranged: Flamethrowers)
### Shiawase Blazer
- Cat: Flame
- Src: RnG p.49-50 / tables p.208
- Skill: Exotic Ranged Weapon (Flamethrowers)
- Acc: 6 | Reach: - | DV: 10P | AP: -6
- Mode: SA/BF/FA | RC: - | Ammo: 4(c)
- Avail: 16F | Cost: 2,200¥
- Rules: See Flamethrower basics. Handheld modern package (fuel in weapon, not backpack tank). No accessories except biometric/advanced safety. Replace fuel tank: full Combat Turn.
## EXOTIC AMMO / PAYLOADS
### Injection Darts
- Cat: Ammo
- Src: Core p.433-434 ammo table
- Skill: as dart gun
- Acc: - | Reach: - | DV: as Drug/Toxin | AP: -
- Mode: - | RC: - | Ammo: 1 dose capacity each
- Avail: 4R | Cost: 75¥
- Rules: For dart guns (Parashield pistol/rifle, etc.). Each dart carries +1 dose drug/toxin (sold separate). Deliver payload on >=1 net hit vs unarmored, or >=3 net hits vs armored. Injection-vector toxin attack. Also listed in Ammunition.md.
### Net Gun ammo load (Basic)
- Cat: Ammo
- Src: RnG p.28
- Skill: as Net Gun Basic
- Acc: as gun | Reach: - | DV: - | AP: -
- Mode: as gun | RC: - | Ammo: fills 4(b)
- Avail: 9 | Cost: 350¥ (full load)
- Rules: Full ammunition load for SA Retiarus Net Gun Basic. Cost is the right side of the 750/350¥ slash in RnG.
### Net Gun ammo load (XL)
- Cat: Ammo
- Src: RnG p.28
- Skill: as Net Gun XL
- Acc: as gun | Reach: - | DV: - | AP: -
- Mode: as gun | RC: - | Ammo: fills 2(b)
- Avail: 9 | Cost: 400¥ (full load)
- Rules: Full ammunition load for SA Retiarus Net Gun XL. Cost is the right side of the 1,000/400¥ slash in RnG.
### ShockNet (net-gun ammo)
- Cat: Ammo
- Src: RnG p.28 / tables p.204
- Skill: as Net Gun
- Acc: as gun | Reach: - | DV: 8S(e) | AP: -5
- Mode: as gun | RC: - | Ammo: as gun
- Avail: 10R | Cost: +250¥
- Rules: Electrical net ammo for Net Gun. Two charges: one on contact, second at start of next Combat Turn. Otherwise as Net Gun hit/subdue rules (RnG p.25).
### Narcoject Foam Refills
- Cat: Ammo
- Src: SL p.46
- Skill: as Trackstopper
- Acc: - | Reach: - | DV: - | AP: -
- Mode: - | RC: - | Ammo: 6 charges
- Avail: 15R | Cost: 500¥ (6 charges)
- Rules: Refills for Trackstopper. Purchase includes Narcoject solvent (free) that instantly dissolves hardened foam; foam otherwise dissolves in 1 hour.
### Man-Catcher ammo compound
- Cat: Ammo
- Src: SL p.133
- Skill: as Man-Catcher
- Acc: - | Reach: - | DV: - | AP: -
- Mode: - | RC: - | Ammo: 10 shots per pack
- Avail: 18 | Cost: 200¥ (10 shots)
- Rules: Blast 10 m. Anyone/thing in blast: opposed grapple vs dice pool 12 or trapped/immobile as compound hardens and expands +1 m.
## PEAK-DISCHARGE POWER PACKS
### Peak-discharge Power Clip
- Cat: Power
- Src: RnG p.52 / accessories table p.54
- Skill: n/a
- Acc: - | Reach: - | DV: - | AP: -
- Mode: - | RC: - | Ammo: 10 power units
- Avail: 14F | Cost: 400¥
- Rules: Fits like a clip. Charge 1 PU / 30 min. Not slot-using accessory. Not usable as IED.
### Peak-discharge Satchel Power Pack
- Cat: Power
- Src: RnG p.52
- Skill: n/a
- Acc: - | Reach: - | DV: - | AP: -
- Mode: - | RC: - | Ammo: 20 power units
- Avail: 16F | Cost: 900¥
- Rules: Canteen-sized belt pack. Cord attach Simple Action. Charge 1 PU / 30 min.
### Peak-discharge Power Backpack
- Cat: Power
- Src: RnG p.52
- Skill: n/a
- Acc: - | Reach: - | DV: - | AP: -
- Mode: - | RC: - | Ammo: 30 power units
- Avail: 20F | Cost: 2,500¥
- Rules: Backpack. Cord attach Simple Action. Charge 1 PU / 30 min.
## RELATED UNDERBARREL EXOTIC ACCESSORIES
### Underbarrel Bola Launcher
- Cat: Accessory
- Src: RnG p.53 / tables p.209
- Skill: Exotic Ranged Weapon (Bola)
- Acc: as bola | Reach: - | DV: as bola STR 5 | AP: as bola
- Mode: - | RC: - | Ammo: bola
- Avail: 8R | Cost: 350¥
- Rules: Underneath slot; rifle-sized+. Launched bola as thrown bola with Strength 5. Heavy Pistol ranges. Full accessory install rules in Weapon Accessories.md.
### Underbarrel Chainsaw
- Cat: Accessory
- Src: RnG p.53 / tables p.209
- Skill: Exotic Melee Weapon (Chainsaw)
- Acc: as chainsaw | Reach: - | DV: as chainsaw (x2 DV vs barriers) | AP: as chainsaw
- Mode: - | RC: - | Ammo: -
- Avail: 10R | Cost: as chainsaw + 500¥
- Rules: Underneath; rifle+. Barrier: double DV. See Weapon Accessories.md.
### Underbarrel Flamethrower
- Cat: Accessory
- Src: RnG p.53 / tables p.209
- Skill: Exotic Ranged Weapon (Flamethrowers)
- Acc: as Blazer / FT rules | Reach: - | DV: as flamethrower | AP: as flamethrower
- Mode: - | RC: - | Ammo: as FT
- Avail: as flamethrower +2 | Cost: as flamethrower + 200¥
- Rules: Underneath; rifle+. Use flamethrower rules RnG p.49. See Weapon Accessories.md.
## Inventory checklist
Total entries: 45

Core Special Weapons (4): Super Squirt, Pain Inducer, Dart Pistol, Dart Rifle.

Core exotic melee (1): Monofilament whip.

Core ammo (1): Injection Darts.

RnG exotic melee (7): Garrote, Mono Garrote, Bullwhip, Combat Chainsaw, Combat Chainsaw civilian, Mono Chainsaw, Mono Chainsaw civilian.

RnG exotic ranged (11): Screech, Blowgun, Bolas, Mono Bolas, Gyrojet, Trafalger cane, Knockoff cane, Net Gun Basic/XL, Shooting Bracer, thrown Net.

RnG lasers (3): Redline, Lancer, Archon.

RnG flamethrower (1): Blazer.

RnG net ammo (3): Net Gun load Basic, Net Gun load XL, ShockNet.

RnG power packs (3): clip, satchel, backpack.

RnG underbarrel exotic accessories (3): bola, chainsaw, flamethrower.

SL exotic melee (1): Krime Stun Lance.

SL exotic ranged (5): Gas Gun, PEP, Trackstopper, Gunstock thrown mode, Man-Catcher.

SL ammo (2): Foam Refills, Man-Catcher ammo.

## Hard Targets / Cutting Aces / Lockdown exotic

**Verified from:** HT Wetwork Toolkit; CA Gats and Glad Rags; Lockdown Game Information.

| Name | Src | Skill | Acc | DV | AP | Mode | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Flame Bracer | HT | Exotic Ranged (Flame Bracer) | 4 | 6P(fire) | −6 | SS | 2(c) | 8F | 775¥ | Crit glitch hits wielder. |
| Ares Armatus | HT | Exotic Ranged (Laser Weapons) | 6 | 6P | −5 | SA | 10(c)/ext | 20F | 19,000¥ | Laser shotgun; RnG laser rules + shotgun spreads. |
| Shiawase Simoom | HT | Exotic Ranged (Simoom) | 5 | 6P | - | SA/FA | 6(ml) | 14R | 1,500¥ | Forearm guards +1 Armor; FA −2 recoil; Conceal −4; Complex fire (wireless Simple). |
| Throwing Syringe | HT | Exotic Ranged / Thrown | Phys | (STR−2)P | −2 | - | - | 6F | 40¥ | Injection on penetrate. |
| Tactical Grapple Gun | HT | Exotic Ranged (Grapple Gun) | 4(6) | 9S | −2 | SS | 1(b) | 15F | 10,000¥ | Heavy crossbow ranges; smartlink; RC 1; arachnofibre 600 kg rope. Heads: Harpoon 300¥ (9P AP −4); Articulated grapnel 1,000¥; Sticky grapnel 150¥; Grenade reel 750¥+grenade. |
| Injector Pen | CA | Exotic Melee | 4 | as drug/toxin | −2 | - | 1 | 9F | 220¥ | One-dose hypodermic in pen/stylus. |
| Pepper Punch Pen | CA | Exotic Ranged | 3 | as pepper punch | - | SS | 1(c) | 3 | 45¥ | Range 2 m; any inhalation toxin OK. |
| Modified Spray Pen | CA | Exotic Ranged | 3 | as drug/toxin | - | SS | 1(c) | 4F | 60¥+payload | Payload sold separately. |
| Briefcase Shield (melee) | CA | Exotic Melee | 3 | (STR+2)P | - | - | - | - | - | Melee use when deployed as shield (armor row separate). |
| Microwave Gun (high/low) | Lockdown | Exotic Ranged | see Firearms | see Firearms | see Firearms | SS | packs | 20R | N/A | Prototype; full rows in Firearms.md. |
| Repeating Laser | Lockdown | Exotic Ranged (Laser) | see Firearms | see Firearms | see Firearms | SA/BF/FA | packs | 16F | N/A | Prototype; full row in Firearms.md. |

