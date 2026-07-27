# Security and Surveillance

Agent reference (SR5). Compact; full mechanical detail; no flavor.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `runandgun.pdf` · `runfaster.pdf` (PACK note)
**Books:** Core · RnG · RF (PACK composition only)
**Printed:** Core Security Devices / B&E Street Gear ~447-448 (PDF ~452-453); Security in the Sixth World devices/sensors ~362-366 (PDF ~367-371); RnG Tools of the Trade entry gear ~103-105
**See also:** `Encyclopedia/Sensors and Optics.md` (cameras, sensor housings/arrays/functions, Periscope Cam, ultrasound as buy gear) · `Encyclopedia/Commlinks and Electronics.md` (bug scanner, jammers, white noise, RFID) · `Encyclopedia/Melee Weapons.md` (Ash Arms combat chainsaws) · `Encyclopedia/Tools Kits and Survival.md` (generic kits; survival) · `Encyclopedia/Drones.md` (fixed automated gun drones) · `Encyclopedia/Drugs Toxins and Chemicals.md` (security gases) · `Mechanics/` barriers / Perception

**In scope:** locks and maglocks (+ options), restraints, breaking-and-entering defeat tools, Core B&E industrial chemicals, facility security device procedures (alarms, trip beams, pads/mesh, motion/capacitance/sound detectors, cameras as security use, olfactory/MAD/cyberware scanners, fencing hazards, automated defenses overview), RnG breaching/entry tools.
**Out of scope:** personal vision/audio housings and Sensor Function *buy* rows (Sensors and Optics; facility scanners use those Ratings); bug scanner / jammer SKUs (Electronics); combat monofilament chainsaws as primary weapons (Melee; Core B&E chainsaw row kept here); magical wards/spirits as services (not shop SKUs); landscaping fluff without buy lines.

## Schema

| Col | Meaning |
| --- | --- |
| Src | Core / RnG / RF |
| Rating | Device/lock Rating when applicable |
| Avail / Cost | Street Availability / nuyen. `-` = none. `+N` = add to parent Avail/Cost |
| Rules | Full mechanical notes |

## Common rules

### Key / combination locks (Core)

- Mechanical tumbler or combination. Less common than maglocks.
- Defeat: Locksmith + Agility [Physical] (Lock Rating, 1 Combat Turn) Extended.
- **Autopicker:** adds Rating to dice pool on that test; Rating may replace Locksmith skill.
- **Transponder-embedded keys:** also need electronics kit; Hardware + Logic [Mental] (Lock Rating, 1 minute) Extended while picking. Same character doing both: -2 to both tests.

### Maglocks (Core 363-364)

- Powered magnetic locks. Keys: physical (keypad, swipe/proximity card, memory string), biometric, or combo. Often networked; usage logs common.
- **Open case:** Locksmith + Agility [Physical] (Maglock Rating x 2, 1 Combat Turn) Extended. Or smash/shoot case: Barrier rating = Maglock Rating (overkill may wreck electronics). Reassemble: same Extended Test.
- **Anti-tamper (Rating 1-4):** extra Locksmith + Agility [Physical] (anti-tamper Rating) Test or alarm triggers.
- **Keypad:** rewire after case open: Locksmith + Agility [Physical] (Maglock Rating x 2, 1 Combat Turn) Extended; **or** sequencer Opposed Test (sequencer Rating vs maglock Rating; case must still be opened). Wireless sequencer: +1 Rating.
- **Cardreader:** same case rewire as keypad; **or** maglock passkey (no case open). Passkey/forged keycard vs maglock: Opposed Ratings; passkey/forge wins = open. Wireless passkey: +1 Rating.
- **Forge keycard:** keycard copier copies in seconds; Hardware kit + ~10 min + Hardware + Logic [Mental] (2). Forge uses Rating x 2 vs Maglock Rating x 2. Logs may flag duplicate use.
- **Print scanners** (finger/palm/retina/vessel): coerce authorized user; or cellular glove molder sleeve (needs sample) Opposed vs maglock; or retinal duplication cybereye.
- **Voice recognition:** must answer as approved voice in time or alarm. Recording/sim/real voice or voice modulator cyberware; Opposed vs recognition gear.
- **Breath / cellular / DNA:** need correct genetic sample in enzyme bath. Chemistry shop: Chemistry + Logic (5, 1 hour) Extended to synthesize bath.
- **Facial recognition:** Disguise + Intuition [Mental] vs Device Rating; +2 if picking disguised character from a crowd. Prosthetic makeup / biosculpting apply.

### Facility alarms and passive sensors (Core 364-366)

- **Circuit alarms** (doors/windows/glass): Hardware + Logic [Mental] (5, 1 minute) Extended to fool contacts while open (GM may raise).
- **Wire / monowire:** fail Perception → trigger alarm and/or fencing-table damage.
- **Trip beams:** Perception + Intuition [Mental] (2) visible / (3) IR; smoke/aerosol → threshold 1. Squeeze past: Escape Artist + Agility [Physical] vs GM threshold. Proxy lasers / mirror rearrange: similar Escape Artist test.
- **Pressure pads / mesh:** spot thresholds 3 pads / 4 mesh; after stepping, second Perception (1 pads / 3 mesh) then Reaction + Intuition (3) with Body as negative DP to lift before trip.
- **Motion sensors (ultrasonic):** detect field with ultrasound sensor passive within 5 m. Defeat: move 0.5 m / Combat Turn + Sneaking + Agility [Physical] (3); -DP equal to extra Initiative Dice beyond first.
- **Capacitance / proximity wire:** detects body charge within 2 m; alarm and/or cameras.
- **Sound / vibration detectors:** Infiltration + Agility [Physical] (3) (or Silence/Stealth spells). May be pattern-filtered (e.g. gunshots only).
- **Security cameras:** visual / low-light / IR / UV. Typical mounts easy if looking; micro-cameras Perception threshold 3; hidden = Perception Thresholds table. IR fooled by Improved Invisibility; low-light overwhelmed by bright light / flash-bangs.
- **Olfactory / chemsniffer:** Rating dice vs threshold 2 (3 if hermetically sealed) for explosives/ammo; apply Chemical Detection Modifiers. As pheromone scanner: Rating vs threshold 3 (2 if tailored pheromones); gender/metatype vs animal, not individual ID.
- **MAD:** Rating dice; 1 hit detects ferrous metal weapons/objects. Useless vs non-metal.
- **Millimeter-wave / cyberware scanner:** Rating dice vs Cyberware Scanner Table thresholds; range 15 m; detects non-bio items in DB; more hits = more detail.
- **Buy path for scanners/cameras as gear:** Sensor housings + Single Sensor / Sensor Array + Sensor Functions (Sensors and Optics). Facility install often wall-mounted housing. Device Rating for Opposed Tests = sensor/device Rating as GM.

### Fencing hazards (Core; not separate shop SKUs)

Climbing past fencetop wire: Climbing + Agility (3); fail → damage. Spot electrified fence / monowire: Perception thresholds below. Mats over wire/electric fence: climb without that damage.

| Type | Spot threshold | Damage if hit |
| --- | --- | --- |
| Barbed | 1 | 4P |
| Concertina | 1 | 5P |
| Monowire | 3 | 8P |
| Electrified | 2 | 6S (Electricity rules) |

### Automated defenses (Core overview; not buy table)

- **Fixed/track gun drones:** standard drone rules; sensors + Targeting autosofts.
- **Containment:** shutters, locking doors, sliding walls, laser/monowire mazes, jamming when alarm trips.
- **Gas delivery:** fills ~30 m³ / Combat Turn; Perception to notice; olfactory scanner may warn; toxin rules apply.

### Chemical Detection Modifiers (Core)

| Situation | Mod to chemsniffer |
| --- | --- |
| Every 10 rounds of ammo | +1 |
| Every grenade | +1 |
| Every 30 g non-plastique explosive | +1 |
| Every 100 g plastique | +1 |
| Item in plastic | -1 |

### Cyberware Scanner thresholds (Core)

| Item | Threshold |
| --- | --- |
| Standard cyberware, weapons | 1 |
| Alphaware, other items | 2 |
| Betaware | 3 |
| Deltaware | 5+ |

| Situation | Mod |
| --- | --- |
| 2+ implants/items | +1 |
| 4+ | +2 |
| 6+ | +3 |

Roll Device Rating; meet threshold to detect general location/type; extra hits add detail (function, model, grade). Range 15 m.

### Marking systems (Core; no shop SKU)

Alarm/exit spray tags: UV dye, RFID, DNA-encoded material, nanites. Identify later if captured.

### Restraints (Core)

- Break/cut: Barriers rules. Armor / Structure as listed per type.
- Metal: mechanical or wireless lock.
- Plasteel: flash-fused; cut free only.
- Plastic: disposable straps, sold per 10.
- Containment manacles: wrists or ankles; no faster than shuffle; blocks extending cyber-implant weapons.

### Battering rams (RnG)

- Attack: Strength + Agility; Destroying Barriers (Core 197). Exotic Melee (Battering Rams) if used as melee.
- Not recommended as weapons; still usable.

## Shared procedures

### Maglock option stacking

Buy base Maglock (Rating x 100¥, Avail = Rating). Add keypad and/or card reader (+50¥ each, no Avail listed). Anti-tamper +Rating Avail and +(Rating x 250)¥. Biometric reader +4 Avail and +200¥ (same cost as Core Electronics biometric reader SKU; here as lock option).

### Cellular glove molder

Takes finger/palm print; molds wearable sleeve for print scanners. Opposed Rating vs maglock when used.

### Miniwelder

Electric arc; 30 min fuel. DV **25** vs barriers when cutting. Too small as a practical weapon. Fuel canister separate.

### Monofilament chainsaw (Core B&E tool)

DV **8P** vs barriers (double when used against barriers per Core B&E text). Acc 3, Reach 1, AP -6, Exotic Melee if swung. Combat Ash Arms models → Melee Weapons (different Avail/Cost).

### Thermite burning bar

Fire Damage **30P** vs barriers; must be set carefully (not a thrown weapon). Wireless: can activate remotely.

### Glue sprayer

Bond two rigid surfaces; ~1 m²; hardens in 1 Combat Turn. Force: Opposed Body + Strength using glue Body 5 and Strength 5. Solvent removes ~1 m².

## Catalog

### Locks and maglocks (Core)

| Name | Src | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Key / combination lock | Core | 1-6 | Rating | Rating x 10¥ | Shared → Key locks. |
| Maglock | Core | (Rating) | Rating | Rating x 100¥ | Shared → Maglocks. |
| Keypad (maglock option) | Core | - | - | +50¥ | Access codes; defeat per Maglocks → Keypad. |
| Card reader (maglock option) | Core | - | - | +50¥ | Swipe/RFID cards; Maglocks → Cardreader. |
| Anti-tamper circuits | Core | 1-4 | +Rating | +(Rating x 250)¥ | Maglocks → Anti-tamper. |
| Biometric reader (maglock option) | Core | - | +4 | +200¥ | Print/voice/DNA/facial options per Maglocks biometrics. |

### Restraints (Core)

| Name | Src | Armor | Structure | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Metal restraints | Core | 16 | 2 | - | 20¥ | Mechanical or wireless lock. |
| Plasteel restraints | Core | 20 | 2 | 6R | 50¥ | Flash-fused; cut free. |
| Plastic restraints | Core | 6 | 1 | - | 5¥ / 10 | Disposable straps. |
| Containment manacles | Core | 16 | 2 | 6R | 250¥ | Shuffle only; blocks cyber-implant weapon extension. |

### Breaking and entering tools (Core)

| Name | Src | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Autopicker | Core | 1-6 | 8R | Rating x 500¥ | +Rating dice to mechanical lockpicking; Rating may replace Locksmith. **Wireless:** +Rating dice (online lock DB). |
| Cellular glove molder | Core | 1-4 | 12F | Rating x 500¥ | Shared → Cellular glove molder. |
| Chisel / crowbar | Core | - | - | 20¥ | Double effective Strength forcing door/container. |
| Keycard copier | Core | 1-6 | 8F | Rating x 600¥ | Copy card in seconds; forge per Maglocks → forge keycard. |
| Lockpick set | Core | - | 4R | 250¥ | Required tools for manual lockpicking. |
| Maglock passkey | Core | 1-4 | (Rating x 3)F | Rating x 2,000¥ | Defeat cardreaders; Opposed vs maglock. **Wireless:** +1 Rating. |
| Miniwelder | Core | - | 2 | 250¥ | Shared → Miniwelder. |
| Miniwelder fuel canister | Core | - | 2 | 80¥ | Refuel miniwelder. |
| Monofilament chainsaw | Core | - | 8 | 500¥ | Shared → Monofilament chainsaw (B&E). Acc 3 / Reach 1 / 8P / AP -6 if used as Exotic Melee. |
| Sequencer | Core | 1-6 | (Rating x 3)F | Rating x 250¥ | Defeat keypads after case open; Opposed vs maglock. **Wireless:** +1 Rating. |

### B&E industrial chemicals (Core; Street Gear after B&E)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Glue solvent | Core | 2 | 90¥ | Dissolves ~1 m² aerosol superglue. |
| Glue sprayer | Core | 2 | 150¥ | Shared → Glue sprayer. |
| Thermite burning bar | Core | 16R | 500¥ | Shared → Thermite burning bar. |

### RnG tactical entry / containment tools

| Name | Src | Acc | Reach | Dam | AP | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard battering ram | RnG | 4 | - | (STR+2)P | -1 | 10R | 2,000¥ | ~20 kg; normally 1 user; heavier 2-human versions exist. Shared → Battering rams. |
| Fluid-motion ram | RnG | 5 | 1 | (STR*+3)P | -1 | 10R | 3,500¥ | Internal fluid reservoir. Needs 2 average humans or 1 average troll. *STR = (combined Strength of users) / (number of users). |
| Pneumatic ram (P-Ram) | RnG | 6 | - | 16P | -4 | 18R | 10,000¥ | Quad-leg; position then trigger (touch / wireless). Deploy needs 4 average humans. |
| Shock ram | RnG | 4 | 1 | (STR+2)P + 12(e) | -3 | 10R | 15,000¥ | Spikes deliver shock through barrier; wireless discharge. Glitch: batteries fail; critical glitch: shocks operator. Frequent maintenance. |
| Blast shield | RnG | 4 (melee) | - | 20P | - | 8R | 20,000¥ | 2 m x 1 m variable thermite + HE shaped charge; strap-carry as shield; adhesive/magnet deploy; timer or remote detonate. Blast AP -4 vs target. Melee needs Exotic (Blast Shield). |
| Ares PED Mark III | RnG | - | - | Armor 12 | - | 10R | 2,500¥ | Kevlar body bag / extrication; metatype sizes; optional airtight + 1 h O2 tank; GPS beacon. Not a lock tool. |
| Ultra-Glide industrial lubricant | RnG | - | - | - | - | 12 | 30¥ / L | Zero-friction coat; Gymnastics + Agility (3) [Physical] per meter to cross, or Agility (4) to hold coated item. Squirt / paint-grenade delivery OK. |
| Hold-Fast adhesive spray | RnG | Acc -2 | - | Special | - | 12 | 50¥ | Sprayer (taser ranges); hardens ~30 s; Strength (4) to break free. Standard brittle after 2 h; long-lasting until solvent. Ammo 10. |

### Facility sensor / camera installs (buy via Sensors and Optics)

Not duplicate SKUs. Typical facility build:

1. Wall-mounted housing (Cap 1-6) and/or Handheld (Cap 1-3).
2. Single Sensor or Sensor Array (Rating 2-8).
3. Functions: Camera, Motion Sensor, Ultrasound, Olfactory, MAD (as applicable function names), etc. (Sensor Functions table).
4. Apply facility procedures above (trip beams, pads, capacitance wire often GM-built from those components + alarm circuit).

| Component | Where | Note |
| --- | --- | --- |
| Wall-mounted housing | Sensors | Cap x 250¥ |
| Sensor Array / Single | Sensors | Rating-scaled |
| Camera / micro-camera housings | Sensors | Security camera use rules above |
| Bug scanner / jammer / white noise | Electronics | Counter-surveillance |
| Automated gun mount | Drones / Vehicle mods | Fixed drone rules |

### RF PACK note (composition)

Breaking and Entering PACK (RF): 6,000¥ / 3 Karma, Avail 12F = Autopicker (4) + Sequencer (4) + Keycard copier (5). Component stats above.

## Item index

**Locks:** Key/combination lock; Maglock; Keypad; Card reader; Anti-tamper; Biometric reader option
**Restraints:** Metal; Plasteel; Plastic (10); Containment manacles
**B&E Core:** Autopicker; Cellular glove molder; Chisel/crowbar; Keycard copier; Lockpick set; Maglock passkey; Miniwelder (+ fuel); Monofilament chainsaw; Sequencer
**Chemicals:** Glue solvent; Glue sprayer; Thermite burning bar
**RnG entry:** Standard / Fluid-motion / Pneumatic / Shock rams; Blast shield; PED Mk III; Ultra-Glide; Hold-Fast
**Facility procedures (no unique SKU):** Alarms; wires; trip beams; pressure pads/mesh; motion; capacitance; sound/vibration; security cameras; chemsniffer; pheromone; MAD; cyberware scanner; fencing table; automated guns/containment/gas
**RF:** B&E PACK note

**Total shop SKUs (excl. facility procedure-only / PACK):** 30 Core lock/restraint/B&E/chem + 8 RnG entry lines = 38 catalog rows (options counted).
