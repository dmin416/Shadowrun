# Sensors and Optics

Agent reference (SR5). Compact layout; full mechanical detail for vision housings, optical devices, vision/audio enhancements, audio devices, sensor packages/functions, RnG recon gadgets, and R5 vehicle/drone sensor mods.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` (chapter extract: `Source Texts/Shadowrun Fifth Edition Core Rulebook/21 - Street Gear.md`) - `runandgun.pdf` (extract: `Source/_extract/rng_grenades.txt`, Tactics & Tools) - `rigger5.pdf` (extracts: `Source/_extract/elec_r5_sat.txt`, `Source/_extract/r5_p124.txt`)
**Books:** Core - RnG - R5. DT and KC have no additional Sensors/Optics shop SKUs in available extracts (INDEX lists DT for the category; none found).
**See also:** `Encyclopedia/Weapon Accessories.md` (weapon imaging scope, weapon periscope 70¥, smartgun camera Cap 1, guncam, weapon flashlights, improved rangefinder) - `Encyclopedia/Commlinks and Electronics.md` (RFID / Sensor tags, bug scanner, white noise generator, micro-transceiver, simrig, PI-Tac sensor network) - `Encyclopedia/Armor Modifications.md` (Capacity costs to mount vision/audio/sensors in armor) - `Encyclopedia/Armor and Clothing.md` (helmet Cap 6 for vision/audio) - `Encyclopedia/Cyberware.md` (cybereyes/cyberears, implanted ultrasound, olfactory booster) - `Encyclopedia/Projectile Weapons.md` (Horizon BoomerEye recon-camera boomerang; no separate Sensors buy row) - `Encyclopedia/Vehicle and Drone Modifications.md` (Signature Masking, ECM, sat link; sensor mods also listed here) - `Encyclopedia/Vehicles.md` / `Encyclopedia/Drones.md` (factory Sensor attribute) - `Encyclopedia/Security and Surveillance.md` (facility cameras/maglocks) - `Encyclopedia/Tools Kits and Survival.md` (standalone flashlight / low-light / IR versions) - `Mechanics/Combat/Ranged Combat.md` (vision magnification in ranged combat).

**Out of scope:** cybereye / cyberear / implanted ultrasound / olfactory booster as implants (Cyberware; olfactory sensor function below still cross-refs the booster rules) - weapon-mounted optics sold as firearm accessories (Weapon Accessories; Imaging Scopes also print as a Core Optical/Imaging housing row here because Street Gear lists them in both places) - RFID family other than the Sensor-tag pointer (Electronics) - bug scanner / white noise / micro-transceiver / simrig as standalone Electronics SKUs (Radio signal scanner function aliases the bug scanner) - survival/weapon flashlights (Tools / Weapon Accessories) - Horizon BoomerEye (Projectile Weapons; recon camera on a boomerang, no separate Avail/Cost optics row) - facility security systems (Security and Surveillance) - Street Grimoire quicksilver camera / mana plates (full Magical Goods entries; R5 Shamus drone references them; no Sensors shop row) - inventing an X-ray Sensor Function buy line (appears only as a factory function on the R5 Telestrian Shamus, not a Core function table entry).

## Schema

### Housings / devices

| Col | Meaning |
| --- | --- |
| Src | Core / RnG / R5 |
| Cap | Device Capacity for enhancements, or `-` if none. `N-M` = buyer picks Capacity in that band |
| Avail / Cost | Street Availability / nuyen. `-` = none. Cost often scales off Cap or Rating |
| Rules | Full mechanical notes (no flavor) |

### Enhancements

| Col | Meaning |
| --- | --- |
| Cap | Capacity cost to install in a housing (`[n]` or `[Rating]`) |
| Avail / Cost | Printed as deltas (`+N`, `+(formula)`); add to the housing's Avail/Cost when installed |

### Sensors / vehicle mods

| Col | Meaning |
| --- | --- |
| Rating | Sensor or mod Rating band |
| Cap / Slots | Gear Capacity cost `[n]`, or vehicle mod slots |
| Avail / Cost | Street Availability / nuyen (or install cost for mods) |

## Common rules

- **Wireless (Core):** Optical/imaging devices have wireless by default; most can also use a universal data cable. Contacts are wireless-only (no room for a UDC). Wireless bonuses require Matrix access and Noise from situation (not distance) ≤ Device Rating.
- **Capacity:** Housings have Capacity for vision or audio enhancements. Bracketed `[n]` on an enhancement is its Capacity cost. Cameras may take both vision and audio enhancements. Sensor Array Cap cost is `[6]`, so it cannot fit in a Handheld Housing (Cap 1-3); use Wall-Mounted Housing (Cap 1-6) or another Cap ≥ 6 device.
- **Sensor data I/O (Core):** Sensors can record data themselves or forward it wirelessly in real time or as files to other devices.
- **Optical vs electronic (Core):** Pure optical devices (Endoscope, Mage Sight Goggles, optical Binoculars, optical Periscope, RnG MOAS) cannot take vision enhancements. A magician can get spellcasting LOS through optics from cover; spellcasting through optics takes a -3 dice pool modifier. Electronic devices cannot provide that optical LoS trick.
- **Two Periscopes:** Optical Devices Periscope (50¥, L-tube mirrors, no enhancements) vs Firearm Accessories Periscope (70¥, Top mount, takes vision enhancements, corner attack -3 to -2 / wireless -1). Different SKUs.
- **Imaging Scopes:** Same Cap 3 / Avail 2 / Cost 300¥ as the Firearm Accessories imaging scope; includes micro camera + vision magnification when bought as the weapon accessory. Catalogued here as the Street Gear Optical/Imaging housing and again by pointer under Weapon Accessories.
- **Monocle cost print quirk:** Core table lists Monocle Capacity 1-4 but Cost as `Rating x 120¥`. Reproduced as printed; likely Capacity was meant. Do not invent a separate Rating band.
- **Vision enhancement Rating band:** Gear table prints Cap `[Rating]` and Cost/Avail formulas but no max Rating. Cybereye Vision Enhancement is Rating 1-3; do not invent a gear max.
- **Vision magnification page refs:** Vision Enhancements cite Core p.177; Sensor Functions Vision magnification cites p.178. Same zoom rules either way; flag only.
- **Sensor Ratings are 2-8** (seven steps), not 1-6.
- **Sensor array Perception (Core):** When using a sensor array for Perception Tests, may substitute Electronic Warfare for Perception, and may use the sensor's Rating as the limit.
- **Sensor array vs single:** Array = up to 8 Sensor Functions. Single = exactly 1 function. Functions that share a name with imaging/audio devices use those rules, with Capacity equal to the sensor's Rating.
- **Housing Rating caps (Core):** Max Sensor Rating by package: RFID / audio or visual device / headware = 2; handheld / small-or-smaller drone = 3; wall-mounted / medium drone = 4; large drone / cyberlimb = 5; motorcycle = 6; vehicle larger than motorcycle = 7; buildings / airports = 8.
- **Helmet Capacity:** Helmet / full-body-armor helmet Cap 6 for vision or audio enhancements (Armor and Clothing).
- **Concealability examples (Core):** contact lenses -6; glasses -4; goggles 0.

## Shared procedures

### Building a worn/handheld optics kit (Core)

1. Buy a housing (contacts, glasses, goggles, monocle, binoculars electronic, camera, etc.) at the chosen Capacity.
2. Install vision enhancements whose Cap costs sum to ≤ housing Cap. Add each enhancement's Avail delta and Cost.
3. Optional: cameras also accept audio enhancements into the same Cap budget.
4. Contacts must stay wireless; other housings may run wireless or UDC.

### Building a sensor package (Core)

1. Choose Single Sensor (1 function) or Sensor Array (up to 8 functions) at Rating 2-8.
2. Place it in a housing or device whose package type allows that Rating (housing table above), or pay for Handheld / Wall-Mounted Housing Capacity.
3. Pick function(s) from the Sensor Functions catalog. Named imaging/audio functions inherit those device rules at Cap = Rating.
4. Sensor Tags (Electronics): RFID housing Max Rating 2; buy a Single Sensor ≤ Rating 2 separately.

### Optical LoS for magicians (Core)

Only non-electronic optical devices. Spellcasting through the optic: -3 dice pool. Cannot stack vision enhancements on the optic itself.

## Catalog

### Optical and imaging housings (electronic unless noted)

| Name | Src | Cap | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Binoculars (electronic) | Core | 1-3 | - | Cap x 50¥ | Handheld; built-in vision magnification; takes vision enhancements |
| Binoculars, Optical | Core | - | - | 50¥ | Optical only; cannot take vision enhancements; see Optical LoS |
| Camera | Core | 1-6 | - | Cap x 100¥ | Still / video / trideo including sound; may take vision and audio enhancements |
| Micro-Camera | Core | 1 | - | 100¥ | Micro camera version (Cap 1 only) |
| Contacts | Core | 1-3 | 6 | Cap x 200¥ | Worn on eyes; nearly undetectable; wireless only (no UDC) |
| Glasses | Core | 1-4 | - | Cap x 100¥ | Worn frames; enhancement models hard to tell from ordinary glasses |
| Goggles | Core | 1-6 | - | Cap x 50¥ | Strapped to head (hard to dislodge); wide enhancement Capacity |
| Imaging Scopes | Core | 3 | 2 | 300¥ | Vision enhancer/display; usually weapon top-mount. Same Cap/Avail/Cost as Firearm Accessories Imaging scope (micro camera + vision magnification on the accessory writeup). See Weapon Accessories for mount/wireless share-LOS |
| Monocle | Core | 1-4 | - | Rating x 120¥ | Headband/helmet flip-down or chain. Cost column prints Rating (see Common rules print quirk) |

### Optical devices (non-electronic)

Cannot take vision enhancements. Magician optical LoS: -3 dice on spellcasting through the device.

| Name | Src | Cap | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Endoscope | Core | - | 8 | 250¥ | Fiber-optic cable ≥1 m; first 20 cm either side = myomeric rope + optical lens. Look around corners, under doors, into narrow spaces. Any length; longer can be unwieldy |
| Mage Sight Goggles | Core | - | 12R | 3,000¥ | Heavy goggles + myomeric rope wrapped around fiber-optic ending in an optical lens. Rope lengths 10, 20, or 30 m |
| Periscope (optical) | Core | - | 3 | 50¥ | L-shaped tube with two mirrors; look, shoot, or cast around corners. Distinct from weapon Periscope (70¥) |

### Vision enhancements

Install in visual sensors and imaging devices (contacts through cameras, scopes, etc.). Cap costs stack against housing Cap.

| Name | Src | Cap | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Low-light vision | Core | [1] | +4 | +500¥ | See normally in light as low as starlight; does not help in total darkness |
| Flare compensation | Core | [1] | +1 | +250¥ | Protects from blinding flashes of light as well as simple glare; mitigates glare vision modifiers; reduces the penalty from flashing lights (e.g. flash-pak) |
| Image link | Core | [1] | - | +25¥ | Display text/pictures/movies/time/AROs in field of view; share tactical info; required to truly "see" AR |
| Smartlink | Core | [1] | +4R | +2,000¥ | Required to receive smartgun system benefits (range, ammo type/level, heat, stress, etc.). Without a smartlink, a smartgun only broadcasts data that nobody receives and has no effect. Smartlink in a natural eye or cybereyes is more effective than external gear (see Smartgun System / Weapon Accessories) |
| Thermographic vision | Core | [1] | +6 | +500¥ | Infrared / heat patterns; spot living beings in total darkness; check if motors/machines ran recently |
| Vision enhancement | Core | [Rating] | +Rating x 2 | +(Rating x 500)¥ | Sharpens vision all ranges; +Rating to limit on visual Perception Tests. Wireless: +Rating dice pool to visual Perception Tests. Gear table prints no max Rating (see Common rules) |
| Vision magnification | Core | [1] | +2 | +250¥ | Digital zoom up to 50x; ranged combat rules Core p.177 (Sensor Functions cite p.178) |

### Audio devices

Each has Capacity for audio enhancements.

| Name | Src | Cap | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Directional mic | Core | 1-6 | 4 | Cap x 50¥ | Listen to distant conversations; solid objects or loud sounds along the line interfere; treat as up to 100 m closer along aim |
| Ear buds | Core | 1-3 | - | Cap x 50¥ | Ergonomic plugs; hard to spot / hard to tell from music/commlink buds |
| Headphones | Core | 1-6 | - | Cap x 50¥ | Full headset with strap; more Capacity than ear buds |
| Laser mic | Core | 1-6 | 6R | Cap x 100¥ | Laser off a solid surface (e.g. window) reads vibrations as sound on the other side; max range 100 m; cannot fit Spatial recognizer |
| Omni-directional mic | Core | 1-6 | - | Cap x 50¥ | Standard pickup/recorder; often linked to a commlink. Micro versions: Cap 1 only, Maximum Range 5 m (same Cap x 50¥ formula → 50¥ at Cap 1) |

### Audio enhancements

Installable on the audio devices above. Each can play audio input from AR or other sources.

| Name | Src | Cap | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Audio enhancement | Core | [Rating] | 1-3 | +Rating x 2 | +(Rating x 500)¥ | Broader frequencies including high/low outside the normal metahuman audible spectrum; fine discrimination; block background noise. +Rating to limit on audio Perception Tests. Wireless: +Rating dice pool to audio Perception Tests |
| Select sound filter | Core | [Rating] | 1-3 | +Rating x 3 | +(Rating x 250)¥ | Focus on specific sounds/patterns (speech/word/pattern recognition). Each Rating point = one sound group. Actively listen to one group at a time; others can record or use triggered monitoring |
| Spatial recognizer | Core | [2] | - | +4 | +1,000¥ | +2 to limit on Perception Tests to find a sound's source. Wireless: +2 dice pool on those tests. Cannot install on a laser microphone |

### Sensor packages and housings

| Name | Src | Cap | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Single Sensor | Core | [1] | 2-8 | 5 | Rating x 100¥ | Exactly one Sensor Function. Place in a housing/device allowed for that Rating. Can record locally or forward wirelessly (real-time or files) |
| Sensor Array | Core | [6] | 2-8 | 7 | Rating x 1,000¥ | Up to eight Sensor Functions. Perception may use Electronic Warfare and Rating as limit. Can record locally or forward wirelessly (real-time or files). Cap cost [6] needs Cap ≥ 6 housing (not Handheld 1-3) |
| Handheld Housing | Core | 1-3 | - | - | Cap x 100¥ | Housing only; Max Sensor Rating 3 when used as handheld package. Cap too small for a Sensor Array |
| Wall-Mounted Housing | Core | 1-6 | - | - | Cap x 250¥ | Housing only; Max Sensor Rating 4 as wall-mounted package; Cap 6 can hold a Sensor Array |

Sensor Tags (RFID, Device Rating 2, Avail 5, 40¥ per 10): buy in `Encyclopedia/Commlinks and Electronics.md`. Equip with one Single Sensor ≤ Rating 2 (sold separately); records ≤24 h then stop or overwrite; Wireless: owner monitors real-time and still keeps last 24 h. Max Sensor Rating in RFID package = 2.

### Sensor Functions

Not separate Avail/Cost rows. Choose when buying Single Sensor or Sensor Array. Same-named imaging/audio functions use those device rules with Capacity = sensor Rating.

| Function | Src | Max Range | Rules |
| --- | --- | --- | --- |
| Atmosphere sensor | Core | - | Up-to-the-second local air/weather analysis |
| Camera | Core | - | Same as Camera imaging device (Cap = Rating) |
| Cyberware scanner | Core | 15 m | Millimeter-wave; primarily cyber-implants; also other contraband |
| Directional microphone | Core | - | Same as directional mic (Cap = Rating) |
| Geiger counter | Core | - | Ambient radioactivity |
| Laser microphone | Core | 100 m | Same as laser mic (Cap = Rating); still cannot take Spatial recognizer |
| Laser range finder | Core | 1,000 m | Laser out/back; exact distance to target |
| MAD scanner | Core | 5 m | Magnetic Anomaly Detection; weapons / metal concentrations |
| Motion sensor | Core | 25 m | Ultrasound + low-power IR; motion and drastic ambient temperature changes |
| Olfactory sensor | Core | - | Same rules as Olfactory Booster cyberware (analyze air molecules; +Rating scent Perception, cutoff, etc.). Booster implant stats stay in Cyberware; this function uses those mechanics on a sensor |
| Omni-directional microphone | Core | - | Same as omni mic (Cap = Rating) |
| Radio signal scanner | Core | 20 m | Usable as a bug scanner (Electronics bug-scanner procedures; Core p.440) |
| Ultrasound | Core | 50 m | Continuous ultrasonic pulses + receiver → topographic ultrasound map (textures, distances between objects, things invisible to naked eye such as Invisibility). No colors/brightness. Cannot penetrate materials transparent to optical sensors (e.g. glass). Passive mode: no emit, still receive outside ultrasound (motion sensors, others' active ultrasound, bats) |
| Vision magnification | Core | - | Digital zoom up to 50x with clear LOS; ranged combat Core p.178 |

### RnG recon gadgets

| Name | Src | Cap | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Telescoping Mirror on a Stick (MOAS) | RnG | - | 10 | 35¥ | Hand-sized optical mirror; 15 cm telescoping probe with magnetic clamp for extra length. Around-corner surveillance when wireless/tech is not feasible. Optical (no vision enhancements) |
| Grenade-Cam (G-Cam) | RnG | 1-5 | 16R | Cap x 1,500¥ | Dodecahedron multi-sensor platform ~2x baseball size; throw into unknown areas. Reinforced casing survives a 20 m fall; shape eventually stops rolling. Multi-aperture 3D imagery. Image link standard; extra sensor options via Cap |
| Periscope Cam | RnG | 1-3 | 10R | Cap x 600¥ | Handheld peek around corners / over obstacles. Image link standard; limited upgrades. Access wirelessly or via small viewfinder at the base |

### R5 vehicle / drone sensor mods

Flagged as vehicle/drone modifications (also relevant to Vehicle and Drone Modifications). Not handheld shop optics.

| Name | Src | Slots / notes | Threshold | Tools / skill | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sensor Enhancement (vehicle) Rating 1-3 | R5 | [Rating] slots | Rating x 3 | Shop; Hardware | Rating x 2 | Rating x 2,000¥ | Replaces the vehicle's Sensor rating (does not stack/add). Rating band 1-6 total across both rows |
| Sensor Enhancement (vehicle) Rating 4-6 | R5 | [Rating] slots | Rating x 4 | Shop; Hardware | Rating x 3 | Rating x 5,000¥ | Same replace-not-stack rule |
| Touch Sensors | R5 | 3 slots | 16 | Shop; Hardware | 8 | Body x 500¥ | Jumped-in rigger: +2 dice to Perception or Sensor Tests; vehicle Handling +1. When the vehicle takes damage, rigger takes -2 to resist Biofeedback Damage. Avail parsed from R5 Electromagnetic Modifications table line `Hardware 8` (same pattern as Gridlink `Hardware 4` / Satellite Link `Hardware 6`) |
| Drone Sensor upgrade (array) | R5 | Attribute mod | - | - | Upgraded Sensor x 2 | Upgraded Sensor x 1,000¥ | Replaces/upgrades drone Sensor rating; Sensors ignore drone frame size for this cost |
| Drone single-sensor upgrade | R5 | Attribute mod | - | - | (see Rules) | Rating x 100¥ | Upgrade one sensor instead of the whole array. Source prints Avail = Upgraded Sensor x 2 on the SENSOR section header before both cost formulas; may share that Avail, but no separate single-sensor Avail line is printed |

## Cross-refs (do not duplicate full SKUs here)

| Item | Lives in | Why pointed |
| --- | --- | --- |
| Imaging scope (weapon), weapon Periscope 70¥, smartgun internal/external, Guncam, Improved range finder, weapon flashlights | Weapon Accessories | Mount/fire-control SKUs; vision enh Cap still uses this file |
| Sensor tags, bug scanner, white noise generator, micro-transceiver, simrig, PI-Tac | Commlinks and Electronics | RFID/comms/countermeasures / tac-net / simsense recorder |
| Standalone flashlight (incl. low-light / IR) | Tools Kits and Survival (weapon mounts in Weapon Accessories) | Survival gear, not Sensors housings |
| Horizon BoomerEye | Projectile Weapons | Recon camera on a boomerang; no separate Sensors Avail/Cost row |
| Armor Capacity cheat-sheet installs (camera, ultrasound, MAD, etc.) | Armor Modifications | Install Cap costs only (buy the Street Gear sensor/device separately) |
| Cybereyes, cyberears, Ultrasound Sensor implant, Olfactory Booster | Cyberware | Essence SKUs |
| Factory Sensor on chassis; Shamus X-ray / quicksilver camera | Vehicles / Drones | Chassis attributes / unique drone gear |
| Maglocks, facility cameras | Security and Surveillance | Facility security, not personal optics |
