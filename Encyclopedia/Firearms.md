# Firearms

Agent reference (SR5). Compact layout; full mechanical detail for slug-throwing firearms (tasers through cannons, launchers, lasers, and flamethrowers).

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` (chapter extract: `Source Texts/Shadowrun Fifth Edition Core Rulebook/21 - Street Gear.md`) - `runandgun.pdf` (extracts: `Source/_extract/rng_firearms.txt`, `Source/_extract/rng_tables.txt`) - `streetlethal.pdf` (extracts: `Source/_extract/sl_firearms.txt`, `Source/_extract/sl_tables.txt`, `Source/_extract/sl_corpsec_arsenal.txt`)
**Books:** Core - RnG (+ official RnG errata E-CAT27002E) - SL (Expanded Arsenal) - SL-CorpSec - **GH3** (Gun Heaven 3) - **HT** (Hard Targets) - **CA** (Cutting Aces) - **AP** (Assassin's Primer) - Lockdown prototypes (no street cost).
**See also:** `Encyclopedia/Ammunition.md` (ammo types, flechette/shot, APDS, etc.) - `Encyclopedia/Weapon Accessories.md` (sights, silencers, gyros, gas-vent, underbarrel mounts, smartgun) - `Encyclopedia/Exotic Weapons.md` (net guns, shooting bracers, gyrojet pistol, gun canes, sonic rifle, blowgun) - `Encyclopedia/Projectile Weapons.md` (bows, crossbows, Winchester Airbow) - `Encyclopedia/Grenades and Explosives.md` (minigrenades, rockets, missiles, plastic explosive) - `Encyclopedia/Melee Weapons.md` (Krime Whammy club mode, bayonet accessory stats, Krime Reaver/Gloves packages) - `Mechanics/Combat/Ranged Combat.md` (range tables, recoil, fire modes, suppression).

**Out of scope:** RnG exotic ranged weapons that precede Tasers in the RnG chapter (Retiarus net gun, Tiffani Elegance shooting bracer, FN-AAL gyrojet pistol, Trafalger/knockoff gun canes, Ares Screech sonic rifle, blowgun, bolas) - projectile/throwing weapons (bows, crossbows, harpoon guns, Winchester Airbow; see Projectile Weapons) - firearm accessories and modifications as standalone items (Additional Clip, Krime Pack, Stun-O-Net, Narcoject Dazzler, Red Dot Sight, etc.; see Weapon Accessories) - melee weapons, including bayonets and Krime Whammy's club mode (see Melee Weapons) - SL's speculative "Military and Future Weapons" chapter (Ares DPC-002A "Slam Dancer" vehicle particle cannon, Aztechnology-Dassault Blood Hawk aircraft weapons) - armor, vehicles, and non-firearm CorpSec gear (Bug Stomper armor, Rampart emplacement, Wavecutter MPAC, Renraku Red Samurai katana, Aztechnology Blood Drinker axe) - Complete Trog gear (no firearm SKUs; Troll Roarer is an implant).

## Schema

| Col | Meaning |
| --- | --- |
| Src | Core / RnG / SL / SL-CorpSec / GH3 / HT / CA / AP / Lockdown |
| Skill | Active skill used to fire the weapon (Pistols, Automatics, Longarms, Heavy Weapons, Exotic Ranged Weapon (subtype)) |
| Acc | Attack limit. `N(M)` = base N, wireless-on (or accessory) M |
| DV | Damage Value. `P`/`S` = Physical/Stun; `(e)` = Electricity; `(f)` = flechette-factored; non-numeric entries (`Grenade`, `Missile`, `Torpedo`, `Chemical`, `as Drug/Toxin`, `as toxin`) mean damage is determined by the loaded munition |
| AP | Armor penetration. `-` = none |
| Mode | SS (single-shot) / SA (semi-auto) / BF (burst fire) / FA (full auto); `/` separates available modes |
| RC | Recoil Compensation. Positive integer = built-in compensation; `N(M)` = base N, M with standard/wireless accessories active. `-` = none |
| Ammo | Capacity `(type)`: c = clip, m = magazine, cy = cylinder, b = break-action/internal, d = drum, belt = belt-fed, ml = missile/rocket launcher tube |
| Avail / Cost | Street Availability / nuyen. `-` = none, included in a parent SKU, or not sold |
| Rules | All per-item mechanical notes (no flavor): integral accessories, wireless bonuses, concealability, special modes, size/Strength restrictions, range-table overrides |

## Common rules

- **Wireless ammo counter (Core):** All firearms include wireless capability and a digital ammo counter as standard. While wireless, the weapon displays an ARO with ammo level and type. With a DNI, ejecting a clip/magazine is a Free Action (instead of Simple) and changing fire modes is a Free Action (instead of Simple). This base bonus applies to every row below in addition to any model-specific wireless bonus called out in Rules.
- **Accessory mounts by class:** Tasers = top only. Hold-outs = none. Light/Heavy/Machine Pistols and SMGs = top and barrel. Assault Rifles, Carbines, Sniper Rifles, Shotguns, Machine Guns = top, barrel, and underbarrel. Assault Cannons and Launchers = top and underbarrel. Laser Weapons = top and underbarrel only, and cannot otherwise be modified. Flamethrowers cannot mount any accessory except biometric/advanced safety systems.
- **Skills by class:** Pistols (Tasers, Hold-outs, Light/Heavy Pistols; Machine Pistols may also use Pistols in SA-only mode). Automatics (Machine Pistols, SMGs, Carbines, Assault Rifles). Longarms (Sniper Rifles, Shotguns). Heavy Weapons (Machine Guns, Assault Cannons, Grenade/Missile/Torpedo Launchers). Exotic Ranged Weapon (subtype) for Special Weapons, Laser Weapons, and Flamethrowers - the subtype is named per weapon (e.g. Laser Weapons, Flamethrowers, Man-Catcher).
- **Ranges:** See `Mechanics/Combat/Ranged Combat.md` for the range-category tables (Short/Medium/Long/Extreme) by weapon class. Several rows below explicitly borrow another class's range table (noted in Rules); use that table instead of the class the row is filed under.
- **Machine Guns and Cannons/Launchers suffer double dice-pool modifiers for uncompensated recoil** (Core, Recoil rules) instead of the normal single modifier other classes use.
- **Shotgun slug vs. flechette:** All shotgun catalog stats below are for standard slug rounds. Loading shot/flechette ammo instead uses the separate shotgun spread, choke, and flechette rules (see Ranged Combat and Ammunition) rather than the printed DV/AP; only rows where the source explicitly prints an alternate flechette/shot profile (e.g. Remington Roomsweeper) get a secondary catalog row.
- **RC notation normalization:** Core and this file print RC as a positive integer meaning points of compensation, with `N(M)` showing base vs. with-accessories totals (e.g. `2(3)`). RnG and SL sometimes print RC as a negative number or with a slash (e.g. `-2`, `-1/-6`, `-2(-8)`) to mean the same thing. This file normalizes all such prints to the positive Core style (`-2` -> `2`; `-1/-6` -> `1(6)`; `-2(-8)` -> `2(8)`). No mechanical difference is intended, only notation.
- **Empty AP/RC cells are printed as `-`.**
- **Known stat conflicts (chapter text preferred per file policy; see individual Rules cells too):**
  - *Nitama Sporter* (RnG): chapter page 31 stat block reads Acc 6(7), 6P, SA, RC "-", 18(c), Avail 10R, Cost 300¥, and a chapter footnote says it uses Heavy Pistol ranges. The RnG summary table (p. 205) instead prints RC 1, Ammo 5(m), Avail 4R, Cost 270¥. This file uses the chapter values.
  - *Onotari Arms Violator* (RnG): chapter page 33 prints Acc 5(7); the RnG summary table prints Acc 5 (no wireless bonus shown). This file uses the chapter value, 5(7).
  - *Ares Light Fire 70* (Core/RnG): Core chapter and table both print Ammo 16(c); the RnG summary reprint (p. 425) misprints it as 18(c). This file uses 16(c).
  - *Krime Whammy* (SL): chapter page 42 prints Cost 2,000¥; the SL summary table (p. 50) misprints Cost as 4,000¥. This file uses the chapter value, 2,000¥ (matches `Encyclopedia/Melee Weapons.md`).
  - *Ares Antioch-2* (Core): chapter and table agree at Avail 8F; used as printed.
  - *Onotari HL-13 (Sniper Support)* (SL): this fourth configuration (Acc 6(8), 11P, AP -2, SA/BF, 30(c)) appears only in the SL summary table; the extracted chapter prose only describes the base rifle, Personal Defense Weapon, and Urban Assault configs. Stat is sourced from the summary table, not invented, but is flagged since chapter confirmation was not found in the available extract.
  - *Ares Lancer MP Laser* (RnG): the chapter's power-unit/range sentence for the Lancer is printed under an "Archon" label ("The Archon uses 2 power units per shot... It uses Assault Rifle ranges") immediately after the Lancer's stat block, and is a chapter typo. Cross-referencing the Redline (SMG ranges, 1 unit/shot) and the real Archon entry (4 units/shot, sniper ranges, its own paragraph) confirms this sentence belongs to the Lancer. This file assigns 2 power units/shot and Assault Rifle ranges to the Lancer.
- **RnG official errata applied (E-CAT27002E, 2014):** Fichetti Executive Action and Savalette Guardian: ignore printed BF* Complex Action notes; BF is a Simple Action as normal. PPSK-4 collapsed Concealability Modifier -6. Barret Model 122 includes sound suppressor as a standard upgrade. GE Vindicator includes smartgun (already in chapter). Ares Thunderstruck Avail is 24F (not 12F). Minus-signed RC listings are compensation (already normalized in this file).

## Shared procedures

### XM30 / HL-13 modular weapon systems (RnG HK XM30; SL Onotari HL-13)

1. Each kit/frame ships with several drop-in configurations (barrel, feed, and furniture changes) built around one receiver.
2. Refit to a different configuration: Automatics + Agility (5, 1 minute) Extended Test for the XM30 (RnG chapter; no limit printed), or Firearms + Logic [Mental] (5, 1 minute) Extended Test for the HL-13.
3. Skill and range table follow the current configuration's weapon class (e.g. the XM30's Carbine config uses the SMG range table; its LMG config functionally plays as a light machine gun). Treat each configuration's Skill/Acc/DV/etc. as printed on its own catalog row.
4. Avail/Cost are only listed on the base (first) configuration row; secondary configuration rows are included in that purchase.

### Concealable component pistols (RnG Shiawase Puzzler; SL WW Infiltrator)

1. Disassembled, the weapon looks like ordinary items (jewelry/commlink parts for the Puzzler; toiletries/luggage parts for the Infiltrator).
2. Recognizing the disassembled parts as a firearm: Armorer + Logic [Mental] (3) or Perception + Intuition [Mental] (4) Test.
3. Assembling or disassembling: Armorer + Logic [Mental] (6, 1 minute) Extended Test.
4. A glitch on the assembly test means starting over; a critical glitch breaks a piece, which must be repaired before the weapon can be used again.

### Laser weapon basics (RnG)

- No recoil (RC always `-`).
- DV falls off with range: -1 at Medium, -2 at Long, -3 at Extreme (relative to Short).
- DV also falls off with Environmental Visibility modifiers: -1 per Light level, -2 per Moderate level, -3 per Heavy level. Range and visibility penalties stack.
- Powered by peak-discharge battery packs (power clip = 10 units, satchel = 20 units, backpack = 30 units); each weapon's power-unit-per-shot cost is in its Rules cell.
- Skill: Exotic Ranged Weapon (Laser Weapons). Mounts: top and underbarrel only; cannot otherwise be modified.

### Flamethrower basics (RnG)

- Igniting the flame to ready the weapon: Complex Action normally, Simple Action if wirelessly linked to the user's PAN, Free Action with a wireless DNI connection.
- Single-target attack as normal, or a Complex Action area attack hitting up to two additional targets within 2 meters of the primary target (one Attack Test, separate Defense Tests); DV is reduced by 2 per additional target engulfed.
- Can lay down Suppressive Fire (4 shots), using the Flechette Suppressive Fire rules.
- Deals fire damage and can ignite flammable objects in the area (GM discretion on duration).
- Uses Taser ranges, but only -1 at Extreme and no penalty at Long or closer.
- Skill: Exotic Ranged Weapon (Flamethrowers). Cannot mount any accessory except biometric/advanced safety systems. Refueling takes a full Combat Turn (Shiawase Blazer).

### Onotari Ballista MML reload (RnG)

- Backpack-and-launcher system holding 4 spare missiles that auto-reload after each shot.
- Handheld laser designator is hardwired to the backpack via fiber-optic cable (hack-resistant); can also receive wireless orders from other designators on the user's PAN.
- Manual magazine swap (if the auto-loader is out of missiles or broken): remove backpack (Complex Action), replace magazine (3 Complex Actions, or 3 Complex Actions by a second person), re-don backpack (2 Complex Actions).

### Mitsubishi Yakusoku MRL split pool (RnG)

- Dual-tube launcher; can hold up to 4 missile/rocket types total (2 per tube).
- Selecting which loaded munition(s) to fire is a Free Action via the integrated wireless smartgun link.
- Firing both tubes at once (SA/BF listed in Mode) requires splitting the attacker's dice pool between the two targets/munitions, unless one tube holds a self-guided munition (which does not need to share the pool).

### Carbines (SL)

Carbines are fired with the Automatics skill, use the SMG range table, and have a flat Concealability Modifier of +4 regardless of the individual model.

### Gatling gun enhanced suppression (SL)

Any Gatling-pattern weapon (Krime Triple series below, plus the RnG Ares HVAR and GE Vindicator Mini-Gun) can suppress one additional adjacent zone per the Enhanced Suppression rules (RnG p. 120) with a single test, at a cost of 20 additional rounds of ammunition per extra zone.

### Krime Whammy (SL)

Troll-sized combination shotgun/warhammer. See `Encyclopedia/Melee Weapons.md` -> Shared procedures -> Krime Whammy package for the club-mode row, purchase bundling, and the vs.-barriers test. The shotgun profile is catalogued below under Shotguns.

### Nemesis Arms Man-Catcher (SL-CorpSec)

- Fires a warhead that bursts into a rubberizing compound on detonation; anything in the blast must win an opposed grapple test (dice pool 12) or become trapped, and the compound expands another meter around them.
- Detonation can be set to timer, proximity, or impact; impact detonation only has a 50% chance (1D6, no Edge rerolls; works on 4+) of triggering the compound properly.
- Requires Exotic Ranged Weapon (Man-Catcher).

### ArmTech PTL-02 torpedo types (SL-CorpSec)

Underwater grenade launcher analog firing two torpedo-grenade types (separate catalog rows below): HEAP (impact, armor-piercing) and Depth Charge (area-effect concussive). Standard Environment modification 2 (underwater) is pre-installed.

## Catalog

### Tasers

Electrical weapons; flat AP -5 and Electricity (e) damage is standard across the class. Skill: Pistols. Mounts: top only.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Defiance EX Shocker | Core | Pistols | 4 | 9S(e) | -5 | SS | - | 4(m) | - | 250¥ | Fires up to 4 wired darts (wire runs to 20 m); wired connection gives a more powerful shock than wireless models. Contacts allow melee use (Acc 3, DV 8S(e), Reach 0). Wireless: a successful hit reports target's basic health/Condition Monitor status |
| Yamaha Pulsar | Core | Pistols | 5 | 7S(e) | -5 | SA | - | 4(m) | - | 180¥ | Wireless dart capacitors (no trailing wires), trading some power for faster fire and no melee contacts. Wireless: a successful hit reports target's basic health/Condition Monitor status |
| Cavalier Safeguard | RnG | Pistols | 5(6) | 6S(e) | -5 | SA | - | 6(m) | - | 275¥ | Larger dart capacity, lower power per dart. Standard upgrades: laser sight |
| Tiffani-Defiance Protector | RnG | Pistols | 5(6) | 7S(e) | -5 | SA | - | 3(m) | 2 | 300¥ | Geckogrip mounting; fashion-styled. Standard upgrades: laser sight |
| Krime Tingler | SL | Pistols | 3 | 10S(e) | -5 | SS | - | 2(m) | 6 | 240¥ | Fires shotgun-shell-style stun darts via compressed air (quieter than a gunshot, not silent). Concealability Modifier 0 (heavy pistol-sized) |
| Defense-Com Taser | SL-CorpSec | Pistols | 5 | 6S(e) | -4 | SS | - | 4(b) | 10 | 300¥ | Horizon-Flynn concealed weapon disguised as a non-functional commlink |

### Hold-Outs

Very concealable, weak, inaccurate. Skill: Pistols. Mounts: none.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fichetti Tiffani Needler | Core | Pistols | 5 | 8P(f) | +5 | SA | - | 4(c) | 5R | 1,000¥ | Flechette-only (factored into DV). Color-changing coating. Wireless: change color as a Simple Action |
| Streetline Special | Core | Pistols | 4 | 6P | - | SA | - | 6(c) | 4R | 120¥ | Composite construction gives MAD scanners a -2 dice pool modifier to detect it |
| Walther Palm Pistol | Core | Pistols | 4 | 7P | - | SS/BF | - | 2(b) | 4R | 180¥ | Over-under double-barrel derringer; both barrels can fire at once as a short burst (Not Enough Bullets rule) |
| Fichetti-Tiffani Self-Defender 2075 | RnG | Pistols | 4 | 6P | - | SS | - | 4(c) | 3R | 350¥ | Color-change coating fashion pistol; poor choice as a primary/secondary weapon |
| Narcoject One | SL | Pistols | 5 | as Narcoject | - | SA | - | 6(c) | 6R | 1,200¥ | Printed as a Light Pistol type but uses Hold-out Pistol ranges (chapter note). Only fires Narcoject-brand darts, no other toxin loads |
| Raecor Sting | SL | Pistols | 4 | 8P(f) | +5 | SS | - | 4(m) | 6R | 350¥ | "Lemon-squeezer" design fired by grip pressure; flechette-only. Non-metallic, invisible to MAD scanners (ammunition is not). Concealability Modifier +2. Standard Accessories: Ceramic Components (Rating 6) |
| Terracotta Arms Pup | SL | Pistols | 4(6) | 6P | - | SA | - | 5(c) | 4R/6F | 500¥/900¥ | Higher Avail/Cost pair includes an included custom silencer + internal smartlink; civilian version omits the silencer (non-standard thread, can't retrofit an aftermarket one) |
| Defense-Com Hold-Out Pistol | SL-CorpSec | Pistols | 5 | 5P | - | SS | - | 2(b) | 10 | 400¥ | Horizon-Flynn concealed weapon disguised as a non-functional commlink; often loaded with capsule rounds |

### Light Pistols

Accurate, fairly concealable. Skill: Pistols. Mounts: top and barrel.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares Light Fire 75 | Core | Pistols | 6(8) | 6P | - | SA | - | 16(c) | 6F | 1,250¥ | Integral barrel-mounted silencer exclusive to this model gives an extra -1 dice pool modifier (stacks with the normal silencer penalty). Includes smartgun system |
| Ares Light Fire 70 | Core | Pistols | 7 | 6P | - | SA | - | 16(c) | 3R | 200¥ | Optional model-exclusive silencer (750¥) adds a further -1 to the usual -4, for -5 total. Ammo is 16(c) per Core chapter/table; see Common rules conflict note |
| Beretta 201T | Core | Pistols | 6 | 6P | - | SA/BF | (1) | 21(c) | 7R | 210¥ | Semi-auto bursts require a Simple Action. Includes detachable shoulder stock |
| Colt America L36 | Core | Pistols | 7 | 7P | - | SA | - | 11(c) | 4R | 320¥ | Cheap, common throwaway pistol |
| Fichetti Security 600 | Core | Pistols | 6(7) | 7P | - | SA | (1) | 30(c) | 6R | 350¥ | 30-round magazine; detachable folding stock and laser sight included |
| Taurus Omni-6 | Core | Pistols | 5(6) | 6P/7P | 0/-1 | SA/SS | - | 6(cy) | 3R | 300¥ | Interchangeable cylinders: SA/6P/AP 0 on light pistol ammo, SS/7P/AP -1 on heavy pistol ammo. Includes integral laser sight |
| Fichetti Executive Action | RnG | Pistols | 6 | 7P | - | SA/BF | - | 18(c) | 10R | 300¥ | Burst-fire option as standard. Printed BF* Complex Action note is removed by RnG errata; BF is a Simple Action |
| Shiawase Armaments Puzzler | RnG | Pistols | 4 | 6P | - | SA | - | 12(c) | 14R | 900¥ | Disassembles into ~20 MAD-defeating everyday-looking components. See Shared procedures -> Concealable component pistols |
| Nitama Sporter | RnG | Pistols | 6(7) | 6P | - | SA | - | 18(c) | 10R | 300¥ | Chapter stats used (see Common rules conflict note). Uses Heavy Pistol ranges. Integral laser sight, low felt recoil, small internal magazine |
| Browning Ghost | SL | Pistols | 5(7) | 6P | - | SA | 1 | 10(c) | 10R | 1,250¥ | SmartSteel body flexes to conform to the body; cannot fire while flexible. Changing states: Complex Action (Simple Action wirelessly). Concealability Modifier -3 while flexible. Cannot accept further modifications. Standard Accessories: Electronic Firing, Personalized Grip, Smartgun System |
| Colt Coral Snake | SL | Pistols | 5(6) | 7P | -1 | SS | - | 5(cy) | 3R | 320¥ | Uses Heavy Pistol ranges and ammunition. Standard Accessories: Laser Sight (top) |

### Heavy Pistols

Powerful sidearms, compromise between concealability and firepower. Skill: Pistols. Mounts: top and barrel.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares Predator V | Core | Pistols | 5(7) | 8P | -1 | SA | - | 15(c) | 5R | 725¥ | Includes smartgun system |
| Ares Viper Slivergun | Core | Pistols | 4 | 9P(f) | +4 | SA/BF | - | 30(c) | 8F | 380¥ | Fires flechette-equivalent slivers (factored into DV). Integral silencer |
| Browning Ultra-Power | Core | Pistols | 5(6) | 8P | -1 | SA | - | 10(c) | 4R | 640¥ | Built-in top-mounted laser sight |
| Colt Government 2066 | Core | Pistols | 6 | 7P | -1 | SA | - | 14(c) | 7R | 425¥ | Electrically-induced spark ignition; fewer moving parts, high reliability |
| Remington Roomsweeper | Core | Pistols | 4 | 7P | -1 | SA | - | 8(m) | 6R | 250¥ | Short-barreled shotgun in pistol form. Slug profile shown here; see flechette secondary row |
| Remington Roomsweeper (flechette) | Core | Pistols | - | 9P(f) | +4 | - | - | - | - | - | Alternate profile of the Roomsweeper loaded with shot rounds: uses Heavy Pistol ranges but shotgun rules (see Common rules) |
| Ruger Super Warhawk | Core | Pistols | 5 | 9P | -2 | SS | - | 6(cy) | 4R | 400¥ | Loud, powerful revolver; cased-ammo variant popular for manual reload theatrics |
| Cavalier Deputy | RnG | Pistols | 6 | 7P | -1 | SA | - | 7(cy) | 3R | 225¥ | Seven-chamber cylinder revolver, Western styling |
| PSK-3 Collapsible Heavy Pistol | RnG | Pistols | 4 | 8P | -1 | SA | - | 10(c) | 16F | 1,050¥ | Folds into a wallet-sized box with clip removed; single-button flip to combat mode. Requires a custom silencer (bought separately, 700¥) |
| Savalette Guardian | RnG | Pistols | 5(7) | 8P | -1 | SA/BF | 1 | 12(c) | 6R | 870¥ | Integrated smartgun link and micro-gyro recoil absorption (1 RC). Printed BF* Complex Action note is removed by RnG errata; BF is a Simple Action. Standard upgrades: Smartlink |
| Onotari Arms Violator | RnG | Pistols | 5(7) | 7P | -1 | SA | 1 | 10(c) | 7R | 550¥ | Chapter Acc 5(7) used (see Common rules conflict note). Delayed-recoil operation, caseless ammo. Standard upgrades: Advanced safety system, internal smartgun, safe target system base |
| Ares Striker | SL | Pistols | 5 | 8P | -1 | SA | - | 12(c) | 4R | 400¥ | No electronics (immune to hacking/malware); striker-fired, no external hammer. Throwback. Ships with a legal RFID presence chip; possessing the gun without the chip is treated as a contractual/jurisdictional violation in most areas. Standard Accessories: Red Dot Sight (top) |
| Barrens Special | SL | Pistols | 4 | 8P | -1 | SS | - | 5(cy) | 2F | 150¥ | Cobbled-together improvised heavy pistol; glitches are treated as critical glitches due to shoddy construction. Standard Accessories: integral bayonet (Blades, Acc 4, DV (STR+1)P, AP -1, fixed or detached) |
| Browning Phantom | SL | Pistols | 4(6) | 8P | -1 | SA | 1 | 12(c) | 12R | 1,500¥ | SmartSteel flexible-state pistol (see Browning Ghost); cannot fire while flexible, Complex Action to change states (Simple Action wirelessly). Concealability Modifier -2 while flexible. Cannot accept further modifications. Standard Accessories: Electronic Firing, Personalized Grip, Smartgun System |
| Cavalier Champion | SL | Pistols | 6 | 10P | -2 | SS | - | 1(b) | 8R | 650¥ | Break-action single-shot; uses the SMG range table and fires Sporting Rifle ammunition. Reloading a round is a Simple Action. Standard Accessories: Longbarrel (barrel) |
| Cavalier Thunderstruck | SL | Pistols | 5(7) | 8P | -1 | BF | 3 | 12(c) | 12F | 1,150¥ | Suffers double modifiers for uncompensated recoil (treated as a heavier-class weapon). Can accept two side-slot accessories/modifications. Restricted to authorized security forces in most jurisdictions. Standard Accessories: Gas Vent (Rating 2, barrel), Smartgun System (internal) |
| Hammerli Gemini | SL | Pistols | 5 | 7P | -3 | Special* | - | 8x2(c) | 10R | 700¥ | Dual parallel barrels/clips. *Only fires Double Tap (+1 DV, 2 rounds, no defense penalty, Simple Action) or Brain Blaster (+2 DV, 6 rounds, no defense penalty, Complex Action); no other firing actions available. Barrel mods/clips cost double. Concealability Modifier +1. Standard Accessories: Custom Look |
| HK Urban Fighter | SL | Pistols | 5 | 8P | -1 | SA | 1 | 10(c) | 15F | 1,950¥ | Ceramic/plastic construction defeats MAD scanners; hermetically-sealed clips mask ammo from chemsniffers. Only accepts a Personalized Grip modification. Spare clips: 100¥, Avail 10F, standard size only. Standard Accessories: Ceramic Components (Rating 6), Silencer (barrel) |
| Morrissey Alta | SL | Pistols | 5(6) | 8P | -1 | SA | - | 12(c) | 7F | 800¥ | Carrying it does not trigger a "wrong attire" Etiquette penalty in upscale settings (weapon bans still apply). Standard Accessories: Laser Sight (top) |
| Morrissey Elite | SL | Pistols | 4(5) | 8P | -1 | SA | - | 5(c) | 6R | 500¥ | Uses Light Pistol ranges; Concealability Modifier -1. Standard Accessories: Laser Sight (top) |
| Nemesis Arms Praetorian | SL | Pistols | 4(6) | 8P | -1 | SA | 1 | 12(c) | 7R | 750¥ | Reinforced frame reduces barrel rise. Cannot accept barrel accessories/modifications (bayonet is permanently affixed). Standard Accessories: Bayonet (barrel, Blades, Acc 5, DV (STR+1)P, AP -1, fixed), Melee Hardening, Smartgun System (internal) |
| Onotari Arms Vagabond | SL | Pistols | 5 | 8P | -2 | SA | 1 | 6(cy) | 6R | 375¥ | Bottom-of-cylinder firing gives a more stable platform with less felt recoil (built-in RC 1) |
| WW Infiltrator | SL | Pistols | 5 | 7P | -1 | SA | - | 15(c) | 14R | 1,200¥ | Breaks down into toiletry/luggage-shaped components. See Shared procedures -> Concealable component pistols. Cannot accept accessories or modifications |

### Machine Pistols

High rate of fire in a compact package. Skill: Automatics (Pistols usable in SA mode only). Mounts: top and barrel.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares Crusader II | Core | Automatics | 5(7) | 7P | - | SA/BF | 2 | 40(c) | 9R | 830¥ | Integral barrel-mounted gas-vent 2 and smartgun system |
| Ceska Black Scorpion | Core | Automatics | 5 | 6P | - | SA/BF | (1) | 35(c) | 6R | 270¥ | Integral folding stock |
| Steyr TMP | Core | Automatics | 4 | 7P | - | SA/BF/FA | - | 30(c) | 8R | 350¥ | Light polymer frame, hard to control on full auto. Built-in top-mounted laser sight |
| PPSK-4 Collapsible Machine Pistol | RnG | Automatics | 5(6) | 6P | - | SA/BF | (1) | 30(c) | 17F | 2,800¥ | Folds into an innocuous box with clip removed and stock collapsed; no other accessories can be added. Collapsed Concealability Modifier -6 (RnG errata). Standard upgrades: Folding stock, laser sight |
| Onotari Arms Equalizer | RnG | Automatics | 4(5) | 7P | - | BF/FA | (1) | 12(c) | 7R | 750¥ | Cased ammo only, no iron sights (snag-free draw). Ejects shells up-and-right (awkward for left-handed users). Standard upgrades: Folding stock, laser sight |
| Ultimax 70 | RnG | Automatics | 5(6) | 6P | - | BF/FA | 2 | 15(c) | 7R | 800¥ | No wireless systems from the factory (popular for clandestine carry). Standard upgrades: Gas-vent 2, laser sight |
| Cavalier Flash | SL | Automatics | 4(6) | 7P | - | SA/BF | - | 24(c) | 8R | 1,850¥ | Folds to fit a hidden arm slide, but is still visibly a weapon when collapsed (clip stays seated). Collapsing takes two Complex Actions; unfolding without the slide is a Standard Action that does not count as Ready Weapon. Concealability Modifier -2 collapsed in slide. Cannot accept accessories/modifications. Wireless: unfolds automatically as part of drawing it from the hidden arm slide. Standard Accessories: Smartgun system (internal) |

### Submachine Guns

Skill: Automatics. Mounts: top and barrel.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Colt Cobra TZ-120 | Core | Automatics | 4(5) | 7P | - | SA/BF/FA | 2(3) | 32(c) | 5R | 660¥ | Folding stock, top-mounted laser sight, barrel-mounted gas-vent 2 |
| FN P93 Praetor | Core | Automatics | 6 | 8P | - | SA/BF/FA | 1(2) | 50(c) | 11F | 900¥ | Special chamber gives 1 RC; integral rigid stock; flashlight reduces darkness penalty by one step. Possession outside a Corporate Court force is illegal in most jurisdictions |
| HK-227 | Core | Automatics | 5(7) | 7P | - | SA/BF/FA | (1) | 28(c) | 8R | 730¥ | Retractable stock, smartgun system, integral sound suppressor |
| Ingram Smartgun X | Core | Automatics | 4(6) | 8P | - | BF/FA | 2 | 32(c) | 6R | 800¥ | Gas-vent 2, smartgun system, integral sound suppressor |
| SCK Model 100 | Core | Automatics | 5(7) | 8P | - | SA/BF | (1) | 30(c) | 6R | 875¥ | Internal smartgun system, folding stock |
| Uzi IV | Core | Automatics | 4(5) | 7P | - | BF | (1) | 24(c) | 4R | 450¥ | Integral folding stock, built-in top-mounted laser sight |
| Ares Executioner | RnG | Automatics | 4(6) | 7P | - | SA/BF/FA | (1) | 30(c) | 14F | 1,000¥ | Fits into a briefcase (extra cases +400¥ each); fireable through the case via concealed stud or PAN with a smartlinked version (+500¥). Recoil penalties double when fired from the case. Simple Action to remove from case; removal required to reload caseless ammo. Standard upgrades: Folding stock, sound suppressor |
| HK Urban Combat | RnG | Automatics | 7(9) | 8P | - | SA/BF/FA | 2 | 36(c) | 16F | 2,300¥ | Non-metallic construction defeats MAD scanners. Cannot accept further modifications. Standard upgrades: Smartlink, sound suppressor |
| Esprit Tsunami | SL | Automatics | 4(6) | 7P | - | BF/FA | - | 40(c) | 8R | 750¥ | Friend-or-foe safe target system. Wireless: Tsunamis on the same PAN share safe-target profiles; system can invert to authorize firing only at shared (friendly) profiles. Standard Accessories: Safe target system (top), smartgun system (internal) |
| Onotari Arms S-3K | SL | Automatics | 4(6) | 7P | - | BF/FA | (1) | 30(c) | 8R | 725¥ | Folds in half; folded Concealability Modifier +0. Folding/unfolding is a Standard Action, not a Ready Weapon action. Standard Accessories: Folding stock (stock), smartgun system (internal) |
| Ingram Supermach 200 | SL-CorpSec | Automatics | 6 | 5P | -6 | BF/FA | 2 | 40(c) | 18F | 5,000¥ | Proprietary ammo only (gameplay: treat price as standard ammo, Avail 16F). RC normalized from printed -2. Chapter table header may say "2000"; SKU is Supermach 200. Standard Upgrades: Internal smartgun system, shock pad |

### Carbines

SL-introduced class between SMG and Assault Rifle. Skill: Automatics; uses SMG ranges; flat Concealability Modifier +4 (see Shared procedures -> Carbines). Mounts as Assault Rifles (top, barrel, underbarrel).

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares Stalwart | SL | Automatics | 5 | 9P | -2 | SA/BF/FA | (1) | 36(c) | 6R | 750¥ | Bare-bones budget carbine; groups shots at distance even with only fixed sights. Standard Accessories: Folding stock |
| Colt M23A2 | SL | Automatics | 5(7) | 9P | -2 | SA/BF/FA | 1 | 40(c) | 10R | 3,150¥ | Chamber design gives 1 RC. Standard Accessories: Improved rangefinder (top), low-light flashlight (side), slide mount (under), smartgun system (internal) |
| Izom Artemis | SL | Automatics | 5(6) | 9P | -2 | BF/FA | - | 30(c) | 8F | 1,800¥ | Smaller frame/shorter barrel than an assault rifle for close quarters. Standard Accessories: Laser sight, underbarrel grenade launcher |
| Izom Artemis (grenade launcher) | SL | Heavy Weapons | 3(4) | Grenade | Grenade | SS | - | 1(m) | - | - | Underbarrel secondary profile; shorter barrel than a standalone launcher, reduced Acc |

### Assault Rifles

Skill: Automatics. Mounts: top, barrel, underbarrel.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AK-97 | Core | Automatics | 5 | 10P | -2 | SA/BF/FA | - | 38(c) | 4R | 950¥ | Legendary reliability, functions after long neglect/burial |
| Ares Alpha | Core | Automatics | 5(7) | 11P | -2 | SA/BF/FA | 2 | 42(c) | 11F | 2,650¥ | Underbarrel grenade launcher (secondary row below), smartgun system, expensive chamber gives 2 RC |
| Ares Alpha (grenade launcher) | Core | Heavy Weapons | 4(6) | Grenade | - | SS | - | 6(c) | - | - | Underbarrel secondary profile of the Ares Alpha |
| Colt M23 | Core | Automatics | 4 | 9P | -2 | SA/BF/FA | - | 40(c) | 4R | 550¥ | Cheap, mass-produced, popular base for modification |
| FN HAR | Core | Automatics | 5(6) | 10P | -2 | SA/BF/FA | 2 | 35(c) | 8R | 1,500¥ | Laser sight and gas-vent 2 system included |
| Yamaha Raiden | Core | Automatics | 6(8) | 11P | -2 | BF/FA | 1 | 60(c) | 14F | 2,600¥ | Electronic firing mechanism gives 1 RC. Integral sound suppressor and smartgun system |
| AK-98 | RnG | Automatics | 5 | 10P | -2 | SA/BF/FA | - | 38(c) | 8F | 1,250¥ | AK-97 with an integral underbarrel grenade launcher (secondary row below); grenade launcher accuracy is considered too inaccurate for serious room-clearing by some users |
| AK-98 (grenade launcher) | RnG | Heavy Weapons | 3 | Grenade | Grenade | SS | - | 6(m) | - | - | Underbarrel secondary profile of the AK-98 |
| Ares HVAR | RnG | Automatics | 5(7) | 8P | - | SA/BF/FA | 3(4) | 50(c) | 11F | 2,400¥ | Integral smartlink, rigid stock with shock pad, custom recoil reduction optimized for high rate of fire. Barrel cannot accept further additions. Gatling-pattern weapon for Enhanced Suppression (see Shared procedures). Standard upgrades: Shock pad, smartlink |
| HK XM30 (assault rifle) | RnG | Automatics | 6(8) | 9P | -2 | SA/BF/FA | (1) | 30(c) | 15F | 4,500¥ | Base config of a 6-config modular system: shock-pad stock, smartgun system, imaging scope, two underbarrel secondaries, secondary feed mechanism, four barrels, bipod for heavy options. See Shared procedures -> XM30/HL-13 modular systems. Standard upgrades: Imaging scope, shock pad, smartlink |
| HK XM30 (carbine) | RnG | Automatics | 6(8) | 9P | -2 | SA/BF/FA | (1) | 30(c) | - | - | Uses the SMG range table (see Shared procedures) |
| HK XM30 (sniper) | RnG | Longarms | 7(9) | 9P | -2 | SA | 2(3) | 10(c) | - | - | Sniper configuration of the modular system |
| HK XM30 (LMG) | RnG | Heavy Weapons | 6(8) | 9P | -2 | BF/FA | 2(3) | 100(belt) | - | - | Light machine gun configuration; suffers double uncompensated-recoil modifiers as a Heavy Weapons-class weapon |
| HK XM30 (shotgun) | RnG | Longarms | 3(5) | 10P | -1 | SA | (1) | 10(c) | - | - | Shotgun configuration; slug stats shown, see Common rules for shot/flechette |
| HK XM30 (grenade launcher) | RnG | Heavy Weapons | 4 | Grenade | Grenade | SS | - | 6(c) | - | - | Underbarrel grenade launcher secondary of the modular system |
| Nitama Optimum II | RnG | Automatics | 5(7) | 9P | -2 | SA/BF/FA | 1 | 30(c) | 10F | 2,300¥ | Standard weapon of the Imperial Japanese military. Recoil-absorbing shock pad, smartgun system. Standard upgrades: Shock pad, smartlink |
| Nitama Optimum II (shotgun) | RnG | Longarms | 4(6) | 10P | -1 | SA | 1 | 5(m) | - | - | Underbarrel shotgun secondary profile; slug stats shown, see Common rules for shot/flechette |
| Cavalier Frontier | SL | Automatics | 5 | 10P | -2 | SA/BF/FA | - | 30(c) | 6R | 1,750¥ | Corrosion-resistant, built to take (and inflict) a beating; go-anywhere merc/militia rifle. Standard Accessories: Extreme environment adaptation (level 1), melee hardening |
| Krime Happiness | SL | Automatics | 3 | 9P | -2 | FA | - | 100(belt) | 6F | 500¥ | Belt-fed assault rifle. On a glitch, suffers a runaway-fire malfunction (fires continuously until ammo runs out or the weapon is disabled); critical glitch is similar but worse |
| Onotari HL-13 (assault rifle) | SL | Automatics | 5(7) | 10P | -2 | SA/BF/FA | - | 30(c) | 15F | 3,500¥ | Base config of Saeder-Krupp's modular system (see Shared procedures -> XM30/HL-13). Barrel mods must be bought per-configuration; refit is a Firearms + Logic [Mental] (5, 1 minute) Extended Test. Standard Accessories: Slide mount (under), smartgun system (internal) |
| Onotari HL-13 (Personal Defense Weapon) | SL | Automatics | 4(6) | 7P | - | SA/BF/FA | - | 30(c) | - | - | SMG-role configuration; cannot use the under-barrel slide mount |
| Onotari HL-13 (Urban Assault) | SL | Automatics | 3(5) | 9P | -2 | SA/BF/FA | - | 30(c) | - | - | Carbine-role configuration: Automatics skill, SMG ranges, Concealability Modifier +4 (see Shared procedures -> Carbines) |
| Onotari HL-13 (Sniper Support) | SL | Longarms | 6(8) | 11P | -2 | SA/BF | - | 30(c) | - | - | Designated-marksman configuration. Sourced from SL summary table only (chapter prose lists AR/PDW/Urban Assault only); see Common rules conflict note |

### Sniper Rifles

Skill: Longarms. Mounts: top, barrel, underbarrel (unless noted).

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares Desert Strike | Core | Longarms | 7 | 13P | -4 | SA | (1) | 14(c) | 10F | 17,500¥ | Hardened for harsh environments. Rigid stock with shock pad, detachable imaging scope |
| Cavalier Arms Crockett EBR | Core | Longarms | 6 | 12P | -3 | SA/BF | (1) | 20(c) | 12F | 10,300¥ | Straddles assault-rifle/sniper-rifle roles; burst fire mode. Rigid stock with shock pad, detachable imaging scope |
| Ranger Arms SM-5 | Core | Longarms | 8 | 14P | -5 | SA | (1) | 15(c) | 16F | 28,000¥ | Disassembles into a standard briefcase; assembly/breakdown is an Extended Firearms + Logic [Mental] (6, Complex Action) Test. Fragile: Acc drops by 1 (min 3) at the end of any Combat Turn used in a running firefight, or by 2 (min 3) if used or defended against as a melee weapon; a one-hour recalibration restores normal Acc. Silencer and imaging scope included |
| Remington 950 | Core | Longarms | 7 | 12P | -4 | SS | - | 5(m) | 4R | 2,100¥ | Bolt-action hunting rifle; top-mounted imaging scope. Cannot mount underbarrel accessories |
| Ruger 100 | Core | Longarms | 6 | 11P | -3 | SA | (1) | 8(m) | 4R | 1,300¥ | Gas-operated sporting rifle. Built-in imaging scope, rigid stock with shock pad |
| Terracotta Arms AM-47 | RnG | Longarms | 7(9) | 15P | -4 | SA | 1(3) | 18(c) | 14F | 35,000¥ | Sized for larger metahumans (troll-scale). Extended barrel for extra range. Includes underbarrel weight and safe target system. Standard upgrades: Bipod, commlink (Device Rating 5), imaging scope (low-light vision, image link, vision magnification), smartgun |
| Onotari JP-K50 | RnG | Longarms | 7 | 12P | -3 | SA/BF | 1 | 25(c) | 13F | 12,500¥ | Anti-dragon-scale designated rifle; can switch between long-range single fire and bursts against clusters. Standard upgrades: Shock pad |
| Pioneer 60 | RnG | Longarms | 5 | 10P | -1 | SS | - | 5(m) | 2R | 500¥ | Simple, rugged hunting rifle |
| Barret Model 122 | RnG | Longarms | 7(9) | 14P | -6 | SA | (2) | 14(c) | 20F | 38,500¥ | Definitive anti-materiel rifle. Standard upgrades: Bipod, smartgun, sound suppressor (sound suppressor confirmed by RnG errata) |
| PSG Enforcer | SL | Longarms | 6 | 12P | -4 | SA | - | 2x12(c) | 12F | 11,000¥ | Dual-clip design for quickly answering multiple threats; a counter-terrorism/DM rifle, not a true long-range sniper piece. Ejects brass 8+ meters from the shooter's position. Standard Accessories: Additional Clip (side), Imaging Scope (top) |

### Shotguns

Catalog stats are for slug rounds; see Common rules for flechette/shot. Skill: Longarms. Mounts: top, barrel, underbarrel.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Defiance T-250 | Core | Longarms | 4 | 10P | -1 | SS/SA | - | 5(m) | 4R | 450¥ | Full-length version. Gas-operated with a secondary pump action to reduce jams. Same SKU also sold short-barreled (see next row) |
| Defiance T-250 (short barrel) | Core | Longarms | 4 | 9P | -1 | SS/SA | - | 5(m) | 4R | 450¥ | Short-barreled variant of the T-250: Concealability +4, uses Heavy Pistol ranges, DV 9P (other stats as full-length) |
| Enfield AS-7 | Core | Longarms | 4(5) | 13P | -1 | SA/BF | - | 10(c) or 24(d) | 12F | 1,100¥ | Military assault shotgun. Built-in top-mounted laser sight |
| PJSS Model 55 | Core | Longarms | 6 | 11P | -1 | SS | (1) | 2(b) | 9R | 1,000¥ | Double-barrel break-action; both barrels can fire at once as a short burst (Not Enough Bullets). Integrated shock pad on rigid stock |
| Auto-Assault 16 | RnG | Longarms | 4 | 13P | -1 | SA/BF/FA | 2 | 10(c) or 32(d) | 18F | 1,800¥ | Full-auto assault shotgun ("The Warhammer"). Internal mechanisms absorb most recoil (RC normalized from printed -2; see Common rules) |
| Mossberg AM-CMDT | RnG | Longarms | 5(7) | 12P | -1 | SA/BF/FA | - | 10(c) | 12F | 1,400¥ | Accurate but low ammo capacity limits full-auto use in practice. Standard upgrades: Smartlink |
| Franchi SPAS-24 | RnG | Longarms | 4(6) | 12P | -1 | SA/BF | 1 | 10(c) | 12F | 1,050¥ | Pump-action with rigid stock and shock pad, integrated weapon light in the fore-stock (RC normalized from printed -1). Standard upgrades: Shock pad, smartgun system |
| Remington 990 | RnG | Longarms | 4 | 11P | -1 | SA | - | 8(c) | 6R | 950¥ | Budget, no-frills, widely available. Top rail and smaller fore-stock mount. Standard upgrades: Slide mounts (top and bottom) |
| Beretta Northstar | SL | Longarms | 4(6) | 11P | -1 | SA | - | 6(m)x2 | 12R | 2,000¥ | Dual-magazine bullpup; toggles between two loaded ammo types (extra bin +250¥). Standard Accessories: Additional magazine (side), smartgun system (internal) |
| Krime Boom | SL | Longarms | 4 | 10P | -1 | FA | - | 20(m) | 15F | 750¥ | Also called Krime Broom in chapter prose. Troll-sized only. Full-auto Roomsweeper-derivative with a 20-round integrated magazine; marketed as house-scale suppression vs. room-scale |
| Krime Whammy | SL | Longarms | 3 | 12P | -1 | SS | 1 | 5(m) | 12F | 2,000¥ | Troll-sized only. Chapter cost used (see Common rules conflict note). All range penalties doubled; fired rounds are not penetrating weapons vs. barriers. See Shared procedures -> Krime Whammy for the club-mode row. Standard Accessories: Melee hardening, shock pad |
| Remington 995 "Buzzsaw" | SL-CorpSec | Longarms | 4 | 11P | -1 | SA | - | 8(c) | 6R | 1,000¥ | Pistol-grip door-breaching shotgun. Barrel-mounted titanium "teeth" give +2 Accuracy when the barrel is seated against the target (door lock/hinge, or a person). Standard Upgrades: Breaching teeth, foregrip, modified pump handle, side mount (top and bottom) |

### Special / Exotic Ranged Weapons

Skill: Exotic Ranged Weapon (subtype per weapon).

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares S-III Super Squirt | Core | Exotic Ranged Weapon | 3 | Chemical | - | SA | - | 20(c) | 7R | 950¥ | Fires DMSO gel packs; the hit itself deals no damage, but delivers a Contact-vector toxin payload chosen by the operator. Uses Light Pistol ranges. Mounts: top and underbarrel |
| Fichetti Pain Inducer | Core | Exotic Ranged Weapon | 3 | Special | - | SS | - | Special | 11R | 5,000¥ | Toxin-style attack, Power 8, Speed Immediate, resisted with Body + Willpower; if modified Power exceeds Mental limit the target must flee next Action Phase. Attacker can hold the beam with a Complex Action; sustained exposure incapacitates with a dice pool modifier equal to modified Power. 10 charges, 1 charge/10 sec on a power point. Uses SMG ranges. Mounts: top and underbarrel. Wireless: recharges by induction at 1 charge/hour |
| Parashield Dart Pistol | Core | Exotic Ranged Weapon | 5 | as Drug/Toxin | - | SA | - | 5(c) | 4R | 600¥ | Fires injection darts (narcoject or other payload). Uses Heavy Pistol ranges. Mounts: top only. Wireless: dart reports hit/injection success and gross tissue anomalies (Device Rating 1 sensor) |
| Parashield Dart Rifle | Core | Exotic Ranged Weapon | 6 | as Drug/Toxin | - | SA | - | 6(m) | 6R | 1,200¥ | Compressed-air injection dart rifle with top-mounted imaging scope. Uses Sporting Rifle ranges. Mounts: top and underbarrel. Wireless: same dart-report bonus as the Dart Pistol |
| Narcoject Gas Gun | SL | Exotic Ranged Weapon | 5 | as toxin | - | SS | - | 5x2(c) | 8R | 1,500¥ | Sprays inhalation-vector toxin gas; armor is useless against it, respiratory protection helps. Complex Action to hit up to 3 targets in a 4 m spread (uses 2 "rounds" of toxin, one Attack Test, separate Defense Tests). Cloud lasts ~2 Combat Turns (GM adjusts for wind/confinement). Uses Taser ranges. Electric-pump refill (included) takes 3 minutes |
| Narcoject PEP | SL | Exotic Ranged Weapon | 6 | 10S | -/-5* | SS | - | 2x10(c) | 12R | 7,500¥ | Pulsed Energy Projectile: vaporizes surface tissue into plasma for a stun-focused flash/bang/pulse effect. *No AP if target's armor supports a Chemical Seal; AP -5 if clothing/armor has gaps. Uses Heavy Pistol ranges. Mounts: top and underbarrel only. Powered by peak-discharge battery packs, 2 power units/shot (typically 2 packs of 10 charges each) |
| Narcoject Trackstopper | SL | Exotic Ranged Weapon | 5 | - | - | SS | - | 6 | 15R | 8,500¥ | Backpack-fed firehose-style sprayer; foam hardens in 1 Combat Round, -1 Agility per net hit (immobile at Agility 0). Hardened foam: Structure 4, Armor 6; dissolves in 1 hour or with Narcoject solvent (free with refills). Uses Light Pistol ranges. Foam refills: 500¥/6 charges, Avail 15R |
| Nemesis Arms Man-Catcher | SL-CorpSec | Exotic Ranged Weapon (Man-Catcher) | 4 | Ammo | - | SS | - | 10(m) | 18F | 6,000¥ | Rocket launcher firing a rubberizing-compound warhead. See Shared procedures -> Nemesis Arms Man-Catcher |
| Man-Catcher ammo compound | SL-CorpSec | - | - | Special (grapple, see Rules) | - | - | - | 10 shots/pack | 18 | 200¥ | Blast radius 10 m; anyone caught must win an opposed grapple test (dice pool 12) or become trapped as the compound hardens/expands another meter |

### Machine Guns

Light/medium/heavy variants determined by ranges; all suffer double uncompensated-recoil modifiers. Skill: Heavy Weapons. Mounts: top, barrel, underbarrel.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ingram Valiant | Core | Heavy Weapons | 5(6) | 9P | -2 | BF/FA | 2(3) | 50(c) or 100(belt) | 12F | 5,800¥ | LMG. Rigid stock with shock pad, laser sight, barrel-mounted gas-vent 2 |
| Stoner-Ares M202 | Core | Heavy Weapons | 5 | 10P | -3 | FA | - | 50(c) or 100(belt) | 12F | 7,000¥ | MMG. Lightweight extra-durable frame; popular vehicle secondary weapon, occasionally trolls carry it personally |
| RPK HMG | Core | Heavy Weapons | 5 | 12P | -4 | FA | (6) | 50(c) or 100(belt) | 16F | 16,300¥ | HMG. Detachable tripod; usually fired prone/sitting/kneeling when unmounted |
| GE Vindicator Mini-Gun | RnG | Heavy Weapons | 4(6) | 9P | -4 | FA | 2 | 100 or 200(belt) | 24F | 6,000¥ | LMG (six-barreled rotary). RC normalized from printed -2. Barrels need a Simple Action to spin up before firing (FA only). Custom 200-round GE belt costs 100¥, incompatible with other weapons. Gatling-pattern weapon for Enhanced Suppression (see Shared procedures). Standard upgrades: Slide mounts (top and bottom), smartgun system |
| SA Nemesis | RnG | Heavy Weapons | 5(7) | 9P | -2 | BF/FA | 2 | 50(c) or 100(belt) | 16F | 6,500¥ | LMG. RC normalized from printed -2. Standard upgrades: Gas-vent 2, Safe Target System (20 RFID data sets, 20 image profiles), smartgun system |
| FN MAG-5 | RnG | Heavy Weapons | 4(5) | 11P | -3 | FA | 2(8) | 50(c) or 100(belt) | 18F | 8,500¥ | MMG. RC normalized from printed -2(-8). Ergonomics widely disliked; most users modify the grip. Standard upgrades: Gas-vent 2, laser sight, tripod |
| Ultimax MMG | RnG | Heavy Weapons | 5(6) | 10P | -2 | FA | 1(6) | 50(c) or 100(belt) | 16F | 7,600¥ | MMG. RC normalized from printed -1/-6. Standard upgrades: Foregrip, Laser Sight, Under-barrel Tripod |
| Ruhrmetall SF-20 | RnG | Heavy Weapons | 5(6) | 12P | -4 | FA | 1(4) | 50(c) or 100(belt) | 18F | 19,600¥ | HMG. RC normalized from printed -1(-4). Standard upgrades: Gas-vent 3, hip pad bracing system, laser sight |
| Ultimax HMG-2 | RnG | Heavy Weapons | 4(5) | 11P | -4 | FA | 6 | 50(c) or 100(belt) | 16F | 16,000¥ | HMG. RC normalized from printed -6. Underpowered/inaccurate for its class unless heavily modified. Standard upgrades: Laser sight, tripod |
| Krime Triple-Troll Minigun | SL | Heavy Weapons | 3(5) | 10P | -4 | FA | - | 100(belt) | 18F | 2,000¥ | LMG-class Gatling gun firing LMG rounds; sized for trolls only. Gatling-pattern weapon for Enhanced Suppression (see Shared procedures). Standard Accessories: Personalized grip, smartgun link (internal, DR 1) |
| Krime Triple-Ork Microgun | SL | Heavy Weapons | 3(5) | 8P | -2 | FA | - | 100(belt) | 16F | 1,400¥ | LMG-class Gatling gun firing Assault Rifle rounds; sized for orks only. Gatling-pattern weapon for Enhanced Suppression. Standard Accessories: Personalized grip, smartgun link (internal, DR 1) |
| Krime Triple-Dwarf Nanogun | SL | Heavy Weapons | 3(5) | 7P | - | FA | - | 100(belt) | 14F | 1,000¥ | LMG-class Gatling gun firing SMG rounds; sized for dwarves only. Gatling-pattern weapon for Enhanced Suppression. Standard Accessories: Personalized grip, smartgun link (internal, DR 1) |
| Stoner-Ares M-22A1 (vehicle-mounted HMG) | SL-CorpSec | Heavy Weapons | 4 | 18P | -6 | FA | 6 | 200(belt) | 24F | 29,000¥ | Modernized Browning M-2 .50-cal; recoil is too severe for effective unmounted use, vehicle/heavy-drone mount only. RC printed as +6 (kept positive as printed). Standard Equipment: Smartgun Targeting System |

### Cannons & Launchers

Assault cannons and grenade/missile/torpedo launchers; all suffer double uncompensated-recoil modifiers. Skill: Heavy Weapons. Mounts: top and underbarrel.

MCT/Winchester-Howe Hornet direct-fire mini-grenade (SL-CorpSec, DV 12P, AP -2, Blast Special, Avail 16F, Cost 400¥) is ammunition fired from any standard grenade launcher below, not a separate weapon; treat as a six-projectile burst-fire effect (loses AP and becomes base DV -2 on a glitch, no burst separation).

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares Antioch-2 | Core | Heavy Weapons | 4(6) | Grenade | - | SS | - | 8(m) | 8F | 3,200¥ | Integral smartlink system. Wireless: can use the wireless link trigger for grenades even without DNI |
| ArmTech MGL-12 | Core | Heavy Weapons | 4 | Grenade | - | SA | - | 12(c) | 10F | 5,000¥ | Bullpup, semi-auto, larger minigrenade capacity than most competitors. Wireless: link-trigger works without DNI |
| Aztechnology Striker | Core | Heavy Weapons | 5 | Missile | - | SS | - | 1(ml) | 10F | 1,200¥ | Extremely light, disposable single-shot launcher. Wireless: link-trigger works without DNI |
| Krime Cannon | Core | Heavy Weapons | 4 | 16P | -6 | SA | (1) | 6(m) | 20F | 21,000¥ | Standard troll modification; first assault cannon intended for larger customers |
| Onotari Interceptor | Core | Heavy Weapons | 4(6) | Missile | - | SS | - | 2(ml) | 18F | 14,000¥ | Two separate barrels/chambers, can load two different missile types at once; cannot fire both barrels together (backblast). Integral smartgun system. Wireless: link-trigger works without DNI |
| Panther XXL | Core | Heavy Weapons | 5(7) | 17P | -6 | SS | - | 15(c) | 20F | 43,000¥ | Small-tank-caliber assault cannon. Built-in smartgun system |
| Ares Thunderstruck Gauss Rifle | RnG | Heavy Weapons | 7(8) | 15P | -8 | SA | (1) | 10(c) + Energy | 24F | 26,000¥ | Uses both ammunition and energy per shot: 1 power unit/shot from peak-discharge battery packs (power clip, satchel pack, power backpack, or vehicle power if mounted). Standard upgrades: Laser sight, shock pad |
| Ogre Hammer SWS Assault Cannon | RnG | Heavy Weapons | 6 | 16P | -4 | SA | - | 6(c) | 20F | 32,000¥ | Improved recoil handling/cycle speed for slightly faster fire than peers. Standard upgrades: Advanced safety, integrated commlink (Device Rating 4), imaging scope (night vision, flare compensation, image link, magnification) |
| Ares Vigorous Assault Cannon | RnG | Heavy Weapons | 4 | 16P | -6 | SS | - | 12(c) | 18F | 24,500¥ | Panther XXL competitor with no smartlink; single-shot only by design |
| Onotari Arms Ballista MML | RnG | Heavy Weapons | Missile | Missile | Missile | SS | - | 4(m) | 19F | 7,500¥ | Backpack-and-launcher missile system. See Shared procedures -> Onotari Ballista MML reload |
| Mitsubishi Yakusoku MRL | RnG | Heavy Weapons | Missile | Missile | Missile | SA/BF* | - | 4x2(m) | 20F | 14,000¥ | Dual-tube missile/rocket launcher. See Shared procedures -> Mitsubishi Yakusoku MRL split pool |
| HK 82A1 | SL | Heavy Weapons | 3 | Grenade | Grenade | SS | (1) | 1(b) | 6F | 1,500¥ | Compact 2.5 kg grenade launcher; -1 dice pool at Long range, -2 at Extreme range. Concealability Modifier +4 with folding stock retracted |
| M79B1 LAW Rocket | SL | Heavy Weapons | 4 | Missile | Missile | SS | - | 1(ml) | 9F | 750¥ | Single-shot disposable anti-vehicle rocket launcher; can only fire anti-vehicular missiles/rockets. Housing forms a watertight seal until opened, then cannot be resealed. Wireless: link-trigger works without DNI |
| Phalanx Systems Vogeljager II | SL | Heavy Weapons | 5 | Missile | Missile | SS | - | 1(ml) | 20F | 2,600¥ | MANPADS. +1 dice pool vs. airborne targets, -3 vs. other target types; sensor-equipped missiles get +2 vs. airborne targets. Standard Accessories: Imaging scope (top, thermographic + low-light). Wireless: IFF allows rerolling missile scatter direction once per missile (must use the second roll) |
| Terracotta X-6 MGL | SL | Heavy Weapons | 4 | Grenade | Grenade | SS | 1 | 6(cy) | 8F | 2,000¥ | 6-round rotating-cylinder grenade launcher; lower rate of fire than competitors but minimal recoil issues. Standard Accessories: Foregrip (under) |
| ArmTech PTL-02 | SL-CorpSec | Heavy Weapons | 5 | Torpedo | - | SS | - | 6(cy) | 18F | 5,000¥ | Underwater torpedo-grenade launcher. See Shared procedures -> ArmTech PTL-02 torpedo types. Standard Upgrades: Environment modification 2 (underwater) |
| HEAP Torpedo | SL-CorpSec | - | - | 14P | -4 | - | - | - | 14F | 300¥ | Impact-detonating armor-piercing torpedo-grenade for the PTL-02. Blast -2/m |
| Depth Charge Torpedo | SL-CorpSec | - | - | 12S | -4 | - | - | - | 12F | 175¥ | Area-effect concussive torpedo-grenade for the PTL-02. Blast 10m |

### Laser Weapons

RnG-introduced class. Skill: Exotic Ranged Weapon (Laser Weapons). Mounts: top and underbarrel only; no other modification. See Shared procedures -> Laser weapon basics for range/environment DV falloff.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ares Redline | RnG | Exotic Ranged Weapon | 9 | 5P | -10 | SA | - | 10(c) or external source | 14F | 7,500¥ | Uses SMG ranges. 1 power unit/shot; power clip or external source (usually a satchel pack) |
| Ares Lancer MP Laser | RnG | Exotic Ranged Weapon | 7 | 7P | -10 | SA | - | 2x10(c) or external source | 18F | 16,000¥ | Uses Assault Rifle ranges. 2 power units/shot; twin power clips or an external satchel/backpack pack. (Chapter prints this power/range sentence under an "Archon" label; it belongs here - see Common rules conflict note) |
| Ares Archon Heavy MP Laser | RnG | Exotic Ranged Weapon | 7 | 10P | -10 | SA | - | External source | 24F | 35,000¥ | Uses Sniper Rifle ranges. 4 power units/shot; external battery pack (usually a power backpack) or direct link to a local energy source when emplaced (unlimited ammo while that supply is online). Standard upgrades: Bipod, tripod mount or gyro stabilization unit mount, sound suppressor |

### Flamethrowers

RnG-introduced class. Skill: Exotic Ranged Weapon (Flamethrowers). See Shared procedures -> Flamethrower basics for ignition, area attack, and range rules.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shiawase Blazer | RnG | Exotic Ranged Weapon | 6 | 10P | -6 | SA/BF/FA | - | 4(c) | 16F | 2,200¥ | Handheld, portable flamethrower; used widely in the Az-Am War. Replacing the fuel tank requires a full Combat Turn |

## Gun Heaven 3 firearms

**Verified from:** `Source/PDF/Shadowrun_5E_Gun_H(e)aven_3.pdf` (`Source Texts/Gun Heaven 3/`). Summary table ~p.37; traits Vintage / Cap & Ball in front matter.

**Traits:** **Vintage** — no modern electronics; physical upgrades cost **2×**. **Cap & Ball** — hand-load each round (**3 Complex Actions**); ammo marked `(cb)`; restart if interrupted.

Factory-installed accessories are listed in Rules (detail in Weapon Accessories / RnG).

### Hold-outs / Light / Heavy (GH3)

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Colt New Model Revolver | GH3 | Pistols | 6 | 5P | - | SA | - | 5(cy) | 4R | 180¥ | Hold-out. No stock upgrades. |
| Colt Agent Special | GH3 | Pistols | 5 | 8P | - | SA | - | 8(c) | 5R | 250¥ | Light pistol. Uses **taser ranges**; fires **heavy pistol** ammo. |
| Colt Future Frontier | GH3 | Pistols | 5 | 8P | -1 | SS | - | 7(cy) | 6R | 500¥ | Heavy pistol. Stock: Melee Hardening. |

### Machine Pistols (GH3)

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fianchetti Military 100 | GH3 | Automatics | 5(7) | 6P | - | SA/BF/FA | - | 20(c) | 8R | 850¥ | Stock: Smartlink. |
| Cavalier Evanator | GH3 | Automatics | 5(6) | 6P | - | BF/FA | 1(2) | 20(c) | 8R | 775¥ | Stock: Electronic Firing, Laser Sight, Folding Stock. |
| Remington Suppressor | GH3 | Automatics | 6 | 7P | -1 | SA/BF | - | 15(c) | 6R | 700¥ | Stock: Sound Suppressor. |

### Submachine Guns (GH3)

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Krime Spree | GH3 | Automatics | 4 | 7P | - | FA | 1 | 30(c) | 6R | 425¥ | Stock: Metahuman Adaptation. |
| Ares Sigma-3 | GH3 | Automatics | 4(6) | 8P | - | SA/BF/FA | (2) | 50(d) | 7R | 1,000¥ | Stock: Collapsible Stock, Foregrip, Powered Slide Mount (2), Smartlink. |
| Cavalier Arms Gladius | GH3 | Automatics | 3(4) | 7P | - | BF/FA | 1(2) | 32(c) | 6R | 400¥ | Stock: Collapsible Stock, Laser Sight. |

### Assault Rifles (GH3)

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shiawase Arms Monsoon | GH3 | Automatics | 5 | 10P | -1 | SA/FA | 1 | 20(ml)×6 | 10F | 1,900¥ | Magazine-barrel; reload = swap barrels. Stock: smartlink, electronic firing, melee hardening. |
| Colt Inception | GH3 | Automatics | 7(8) | 10P | -1 | SA/BF | 1(3) | 35(c) | 11R | 2,250¥ | Stock: Bipod, Electronic Firing, Laser Sight, Melee Hardening. |
| Krupp Arms Kriegfaust | GH3 | Automatics | 8 | 9P | -1 | SA/BF | 1 | 25(d) | 10R | 1,300¥ | Metahuman-sized. Stock: metahuman customization, melee hardening, imaging scope. |
| SBd-44 | GH3 | Automatics | 3 | 10P | -1 | SA/BF/FA | - | 32(c) | 4R | 500¥ | Stock: **Vintage**. |
| Ultimax Rain Forest Carbine | GH3 | Automatics | 7 | 14P | -4 | SA | 1 | 18(c) | 5R | 2,800¥ | Stock: imaging scope (flare comp, image link, low-light), retractable stock. |

### Shotguns (GH3)

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Krime Boss | GH3 | Longarms | 3 | 13P | -1 | SA | 1 | 15(d) | 11R | 600¥ | Stock: Metahuman Customization. Slug stats. |
| Winchester Model 201 | GH3 | Longarms | 8 | 11P | -1 | SA | - | 2(b) | 8R | 1,300¥ | Over/under competition. |
| Winchester Model 2066 | GH3 | Longarms | 4 | 11P | -1 | SS | - | 5(m) | 4R | 1,000¥ | Pump-action. |
| Winchester Model 2054 | GH3 | Longarms | 4(5) | 11P | -1 | SA | (1) | 7(m) | 6R | 900¥ | Stock: Laser Sight, Retractable Stock. |
| Shiawase Arms Rain | GH3 | Longarms | 4 | 10P | -1 | SA | (1) | 5(ml) | 4R | 450¥ | Magazine-barrel; stock retractable stock. |
| Cavalier Falchion | GH3 | Longarms | 5(7) | 12P | -1 | SS | - | 8(m) | 9R | 1,200¥ | Stock: Advanced Safety, Melee Hardening, Smartlink, Trigger Removal. |

### Sporting Rifles (GH3)

Skill: Longarms. Default sporting ranges: S 0–50 / M 51–250 / L 251–500 / E 501–750 m unless noted.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Springfield 2003 | GH3 | Longarms | 9 | 12P | -2 | SS | - | 5(m) | 4R | 3,600¥ | Stock: Vintage. |
| Winchester Model 2024 | GH3 | Longarms | 6 | 12P | - | SA | - | 7(m) | 4R | 1,800¥ | Stock: Imaging Scope (vision mag). |
| Marlin 3468SS | GH3 | Longarms | 4 | 13P | -1 | SS | - | 4(m) | 6R | 1,000¥ | .45-70 big-game. |
| Springfield M1A | GH3 | Longarms | 6 | 12P | -1 | SA | - | 20(c) | 6R | 1,700¥ | Stock: Imaging Sight (image link, vision mag, VE 1). |
| M1 Garand | GH3 | Longarms | 5 | 12P | -1 | SA | - | 8(c) | 3R | 1,100¥ | Stock: Vintage. |
| Springfield Model 1855 Reproduction | GH3 | Longarms | 2 | 10P | - | SS | - | 1(cb) | 4R | 850¥ | Stock: Vintage, **Cap & Ball**. |
| Marlin 3041 BL | GH3 | Longarms | 5 | 10P | -3 | SA | - | 6(m) | 5R | 1,100¥ | Stock: Imaging Sight (vision mag). |
| Marlin X71 | GH3 | Longarms | 5 | 12P | -4 | SS | - | 5(m) | 6R | 1,500¥ | Stock: Extreme Environment Mod 1 (Arctic); imaging sight (low-light, VE 2, vision mag). |
| Marlin 79S | GH3 | Longarms | 4 | 6P | - | SA | - | 10(c) | 3R | 300¥ | Small-bore trainer. |
| Winchester Model 2067 | GH3 | Longarms | 5 | 8P | -1 | SA | - | 15(m) | 4R | 650¥ | Uses **SMG ranges**; fires **heavy pistol** ammo; Vintage. |

### Machine Guns / Cannons / Flamethrowers (GH3)

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Krime Wave | GH3 | Heavy Weapons | 5 | 10P | -2 | FA | (2) | 50(d) or 100(belt) | 11F | 2,000¥ | LMG. Stock: Bipod, Metahuman Customization. |
| Krime Bomb | GH3 | Heavy Weapons | 6(7) | 16P | -6 | SS | - | 4(m) | 20F | 23,000¥ | Assault cannon, pump-action. Stock: laser sight, powered slide mount (2). |
| Shiawase Arms Incinerator | GH3 | Exotic Ranged Weapon (Flamethrowers) | 4 | 12P | -6 | SS | - | 6(c) | 12F | 10,000¥ | **Light pistol ranges**; Complex Action to ready. Stock: Powered Slide Mount, Reduced Weight. See Flamethrower basics. |

## Hard Targets firearms

**Verified from:** `Source/PDF/Shadowrun_5E_Hard_Targets.pdf` (`14 - The Wetwork Toolkit.md`).

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cavalier Adder Slivergun | HT | Pistols | 5 | 8P(f) | +5 | SA | - | 20(c) | 7F | 320¥ | Light pistol; flechette only. |
| Colt Manhunter | HT | Pistols | 5(6) | 8P | -1 | SA | - | 16(c) | 5R | 700¥ | Heavy pistol. Mechanical (anti-hack); holographic sight. |
| Lemat 2072 (revolver) | HT | Pistols | 5 | 8P | -1 | SS | - | 9(cy) | 8R | 1,080¥ | Built-in Ammo Skip; switch to shotgun barrel = Simple (wireless Free). |
| Lemat 2072 (shotgun barrel) | HT | Longarms | 5 | 10P(f) | +4 | SS | - | 1(b) | - | - | Same weapon second barrel; Avail/Cost not printed separately. |

## Cutting Aces firearms

**Verified from:** `Source/PDF/Shadowrun_5E_Cutting_Aces.pdf` (`10 - Gats and Glad Rags.md`).

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hammerli 620S | CA | Pistols | 5(7) | 6P | - | SA | 1 | 6(c) | 8R | 325¥ | Light pistol. Gas-Vent 1, Smartlink; **Heavy Pistol ranges**. |
| Yamaha Sakura Fubuki SX | CA | Pistols | 6 | 6P | - | SA/BF | 1 | 8(ml)×4 | 10R | 750¥ | Light pistol. 2×2 magazine-barrel; Electronic Firing in RC. |
| Nemesis Arms Praetorian | CA | Pistols | 4(6) | 8P | -1 | SA | - | 12(c) | 9R | 700¥ | Heavy pistol. Integral bayonet, Custom Look, laser sight. (Also appears in SL with slightly different notes.) |
| Stinger Pen Gun | CA | Pistols | 4 | 6P | - | SS | - | 1(b) | 6R | 325¥ | Hold-out. Conceal −4; no silencer. Print RC cell shows header text `RC` (bleed); treat as **—** (no built-in RC). |

## Assassin's Primer firearms

**Verified from:** `Source/PDF/Shadowrun_5E_Assassins_Primer.pdf`.

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SVD | AP | Longarms | 5(6) | 10P | -2 | SA | - | 10(c) | 6R | 800¥ | Sniper rifle. Standard laser sight (+1 Acc → 6). Nanoforge-revived Soviet squad marksman rifle. |

## Lockdown prototype firearms

**Verified from:** `Source/PDF/shadowrun-lockdown-pdf.pdf` (`13 - Game Information.md`). Street **Cost N/A** (prototypes).

| Name | Src | Skill | Acc | DV | AP | Mode | RC | Ammo | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Microwave Gun (high frequency) | Lockdown | Exotic Ranged Weapon | 6 | 7P | -6 | SS | - | peak-discharge | 20R | N/A | Light Pistol ranges; cooks flesh. 2 power units/shot (*R&G* packs). |
| Microwave Gun (low frequency) | Lockdown | Exotic Ranged Weapon | 4 | 10P* | - | SS | - | peak-discharge | 20R | N/A | *Matrix damage to electronics. Called Shot ≤0.25 m² gear −2; else GM picks hit gear. 1 power unit/shot. |
| Repeating Laser | Lockdown | Exotic Ranged Weapon (Laser Weapons) | 7 | 7P | -8 | SA/BF/FA | - | 10(c) or external | 16F | N/A | SMG ranges. −1 DV per range band beyond Short; −1 DV per Visibility level. Underbarrel/top mods only. |

