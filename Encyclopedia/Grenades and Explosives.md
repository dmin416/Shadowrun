# Grenades and Explosives

Agent reference (SR5). Compact layout; full mechanical detail for grenades, rockets, missiles, launched special munitions, bulk explosives, detonators, and demolition accessories.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` (chapter extract: `Source Texts/Shadowrun Fifth Edition Core Rulebook/21 - Street Gear.md`) - `runandgun.pdf` (extract: `Source/_extract/rng_grenades.txt`) - `streetlethal.pdf` (extracts: `Source/_extract/sl_grenades.txt`, `Source/_extract/sl_corpsec_arsenal.txt`)
**Books:** Core - RnG - SL (Expanded Arsenal, plus the speculative "Military and Future Weapons" chapter, tagged SL-Future below) - SL-CorpSec (Opposition Report). CT has no grenade/explosive SKU list.
**See also:** `Encyclopedia/Firearms.md` (grenade, missile, rocket, and torpedo launcher hardware; also reprints the Hornet ammo note and HEAP/Depth Charge torpedo stats alongside the PTL-02 launcher) - `Encyclopedia/Ammunition.md` (Maker Mag magazine SKUs, rocket/missile ammo summary, firearm explosive rounds) - `Encyclopedia/Projectile Weapons.md` (bows, crossbows, arrow/bolt heads) - `Encyclopedia/Weapon Accessories.md` (airburst link) - `Mechanics/Combat/Ranged Combat.md` (grenade/launcher Scatter Table and blast resolution procedure, p. 181-182) - `Mechanics/Barriers.md` (Structure/Armor, p. 194).

**Out of scope:** grenade launchers, missile launchers, rocket launchers, and the PTL-02 torpedo launcher themselves (see Firearms; this file only covers what they fire) - non-explosive RnG "Tools of the Trade" gear (battering rams, PED, Ultra-Glide, Hold-Fast, Grenade-Cam, Periscope Cam, PI-Tac, telescoping mirror-on-a-stick; Ultra-Glide may still be loaded into a Paint Grenade per that row) - Maker Mag magazine SKUs, which are ammunition rather than grenades (see Ammunition) - arrow/bolt explosive heads (see Projectile Weapons / Ammunition) - firearm explosive, flechette, and APDS ammunition (see Ammunition) - Seattle Gambit *Incendiary Rocket* and *Halloweener Molotov Cocktail* (no local PDF; unverified stubs live only in Ammunition.md) - SL-Future's Gravity Shielding/Armor and Personal Gravity Devices (armor/mobility tech, not grenades) - SL-Future's FAB-ulous Armor, Mag Rounds, Microwave weapons, and Smart Bullets (unrelated speculative tech from the same chapter as the GravJack grenade and Maker munitions) - RnG Gear Qualities (Counterfeit / Defective / Hot) as general black-market tags, not explosive SKUs.

## Schema

### Grenades / rockets / missiles / special munitions

| Col | Meaning |
| --- | --- |
| Src | Core / RnG / SL / SL-CorpSec / SL-Future (SL's speculative "Military and Future Weapons" chapter) |
| DV | Damage Value. `P`/`S` = Physical/Stun; `(f)` = flechette-factored; `as Chemical` = payload-dependent; `Special` = see Rules |
| AP | Armor penetration. `-` = none |
| Blast | Blast Value falloff. `Xm Radius` = flat-radius cloud/burst; `-N/m` = circular blast dropping N per meter from center; `Target` = affects only what it directly contacts, no per-meter falloff |
| Avail / Cost | Street Availability / nuyen. `-` = none, N/A, or not sold as a finished product |
| Rules | All per-item mechanical notes (no flavor) |

### Bulk explosives

| Col | Meaning |
| --- | --- |
| Src | Core / RnG |
| Rating | Explosive Rating used in the DV formula (see Common rules). A range (e.g. `6-25`) means the buyer picks a Rating in that band |
| Unit | `kg` unless the Rules cell says otherwise (det cord and linear charge are sold per meter) |
| Avail / Cost | Street Availability / nuyen for one unit at the printed (or chosen) Rating |

### Detonators / demolition accessories

| Col | Meaning |
| --- | --- |
| Src | Core / RnG |
| Rating | `-` = no Rating (flat item); a number or range = the Rating band sold |
| Avail / Cost | Street Availability / nuyen. Formulas scale off the chosen Rating |

## Common rules

- **Skills:** Throwing Weapons for any hand-thrown grenade (including the GravJack). Heavy Weapons for anything fired from a grenade, missile, rocket, or torpedo launcher (minigrenades, rockets, missiles, the Hornet, Maker Missile, HEAP/Depth Charge torpedoes) - launcher hardware itself is in Firearms.md. Exotic Ranged Weapon (Man-Catcher) for Man-Catcher ammo via its launcher. Demolitions for placed/shaped bulk-explosive charges, cooking, breaching, cutting, and booby-trapping. Exotic Melee Weapon (Blast Shield) for the Blast Shield's shield/bludgeon melee use.
- **Minigrenade arming (Core):** Minigrenades (any grenade type loaded into a launcher) arm after traveling 5 meters from the muzzle and explode on impact, unless fired with an airburst link (`Encyclopedia/Weapon Accessories.md`). Minigrenades share the same cost and effects as the hand-thrown version of the same grenade type.
- **Rocket/missile arming (Core):** Rockets and missiles arm after traveling 10 meters from the muzzle and explode on impact.
- **Disable arming safety (Core):** Either arming distance can be defeated with an Armorer + Logic [Mental] (4, 5 minutes) Extended Test.
- **Wireless link trigger (Core):** All grenades, rockets, and missiles can be set off via the wireless link trigger without needing a DNI. This applies on top of any other wireless bonus called out on a specific row.
- **Tripwire booby-trap (Core):** Rig any grenade or similar explosive to a tripwire with an Extended Demolitions + Logic [Mental] (8, 1 Complex Action) Test.
- **Bulk explosive DV formula (Core):** DV = effective Rating x floor(square root of kilograms used). A Demolitions + Logic [Mental] Test's hits add directly to the explosive's effective Rating before applying the formula.
- **Blast falloff (Core):** Circular blast = -2 per meter from the center. Directional blast (up to a 60-degree arc) = -1 per meter. Grenades/rockets that print their own Blast value (below) use that value instead of these defaults.
- **AP for bulk/placed explosives (Core):** -2 by default. If the charge is attached directly to the target, the target's Armor is halved instead of applying that AP.
- **Tamping (RnG):** A properly tamped charge doubles DV (the baseline "doubling" car-bomb / breaching prose assumes). Linear cutting charges automatically tamp for a x4 multiplier instead. A door-panel / compartment-panel car bomb (explosive packed inside a sealed panel cavity) multiplies DV by 4 instead of doubling. Breaching charges on a barrier surface also double DV and apply an extra -half AP to the barrier's Armor (see Shared procedures -> Breaching).
- **Barrier shrapnel (Core):** If an explosion destroys a barrier, it also throws a shrapnel cloud with DV = the explosive's DV minus the barrier's Structure rating, Blast -1/m.
- **Explosive damage is always Physical (RnG):** Never convert explosive damage to Stun, even if it does not exceed the target's modified Armor Rating.
- **Purchased detonators include power/primer (RnG):** A bought detonator is always assumed to come with the appropriate power supply or primer for the explosive in question. Power-supply reliability only becomes an issue for detonators that print Ratings (see Shared procedures -> Detonator rating power-fail rolls).
- **Optional chemical detection (RnG):** If using RnG's kilogram-scaled Chemical Detection Modifiers (optional rewrite of Core p. 365): +1 per 1 kg of non-plastique explosive, +1 per 2 kg of plastique (plastic / foam / liquid plastique).
- **Smoke grenade print conflict:** the Core chapter's prose describes the Smoke grenade's cloud as a 10-meter diameter, but the Core stat table prints its Blast as `10m Radius`. This file uses the table value (a Radius, not a diameter) per file policy of preferring stat blocks over descriptive prose; flagged here since the two are not interchangeable and no errata resolves it.
- **Paint Grenade blast (RnG):** the printed stat block already shows a 10-meter radius blast (matching a standard high-explosive grenade's coverage); no separate errata adjustment is needed.

## Shared procedures

### Cooking explosives (RnG)

1. Requires at least a demolitions shop; a kit can only make, arm, or disarm devices, not cook raw explosive from chemicals. A permanent facility instead of a shop reduces the Extended Test threshold by 4; a chemistry shop/facility can substitute at a -2 dice pool penalty (inadequate tools). Mixing in a vehicle-mounted shop while the vehicle is moving reduces the glitch threshold by 1 (glitches occur on 1 fewer ones).
2. Requires separately-purchased chemicals. Choose the target Rating, then roll a Demolitions + Logic [Mental] (30 minutes) Extended Test against the threshold below.
3. **Volatility:** a roll with zero hits shifts the batch's final Rating by +-1 (GM's choice); a glitch shifts it by +-5; the maximum cumulative drift is +-15. A critical glitch detonates the batch immediately at its current effective Rating (circular Blast -2/m, AP -2) - a shop is destroyed (and may ignite/wreck its vehicle); a facility survives but may need repairs costing up to half its original price.

Making Explosives Table (raw-material threshold and precursor pricing; distinct from the finished-product Avail/Cost in the Bulk explosives catalog below):

| Explosive | Threshold (Shop) | Threshold (Facility) | Avail | Cost |
| --- | --- | --- | --- | --- |
| Ammonium nitrate | 12 | 8 | 5 | 75¥ |
| ANFO | 16 | 12 | 5 | 65¥ |
| Commercial | 16 | 12 | 5 | 60¥ |
| Dynamite | 16 | 12 | 6 | 80¥ |
| Foam | 20 | 16 | 8R | Rating x 200¥ |
| Gunpowder | 16 | 12 | 3 | 25¥ |
| Liquid | 20 | 16 | 8R | Rating x 225¥ |
| Nitroglycerin | 16 | 12 | 10 | 150¥ |
| Plastic | 16 | 12 | 8R | Rating x 200¥ |
| TNT | 16 | 12 | 10R | 100¥ |

Gunpowder has no finished-product buy line in the Bulk explosives catalog; this table is the only printed way to price it, or strip it from cased ammunition (roughly 500 rounds per kilogram recovered; caseless ammo uses plastic explosive instead and yields none). Like ammonium nitrate, gunpowder must be in a container before a detonator can be inserted; setting fire to loose/unenclosed gunpowder only burns it; wet gunpowder neither burns nor detonates.

### Breaching and cutting charges (RnG)

1. Determine the barrier's thickness (a Complex Action with ultrasound sensors for an exact reading, or a Knowledge skill for an estimate) and whether the goal is a full breach or a partial breach (e.g. destroying a lock without opening the rest of a vault).
2. Scale the barrier's Structure and Armor by the percentage its thickness differs from the 1-meter benchmark, rounding up (e.g. a 20 cm door uses 20% of both, rounded up).
3. A breaching charge always sits on the surface, so its DV is doubled and the barrier's Armor takes an additional -half AP on top of the normal explosive AP.
4. A Demolitions + Logic [Mental] Test's hits can trim the explosive's effective Rating down for a smaller, more precise charge.
5. Cutting charges (linear charge, detonating cord, or explosive foam) count as a single device. Plant one with a Demolitions + Logic [Mental] (5 minutes) Extended Test, threshold = 2 x kilograms of explosive used (or 2 x meters of det cord used). Cylindrical targets use their diameter as the thickness to cut through. A frame charge (a wooden jig sized to the intended hole) can be built ahead of time and attached with a Complex Action, but is large and conspicuous.

### Atomizer cloud (RnG)

Holds a number of liters equal to its Rating; sprays at 1 liter per Complex Action (roughly 1 kilogram of plastic-explosive equivalent per liter). Each liter fills one cubic meter when properly atomized and settles to the ground in about 1 minute. The liquid must still be airborne to be ignited by a detonator (once settled, atomization advantage is gone). While airborne, DV is uniform throughout the cloud; normal circular Blast falloff only applies outside the cloud's edge.

### Anti-removal disarm (RnG)

Each anti-removal trick built into a device (redundant detonators, redundant power supplies/blast machines, all-identical wire colors, false wires/leads, metal shielding over the detonator, fake countdown displays, mixed detonator types) grants the bomb 1 die (maximum dice pool 12) toward resisting disarm. Resolve either as a single Opposed Demolitions + Logic Test (attacker's hits vs. the bomb's pool; if the bomb wins, it detonates), or as a Test per modification where each attacker success strips one die from the bomb's pool until it reaches zero (fully disarmed).

### Detonator rating power-fail rolls (RnG)

Where a detonator's Rating governs its power supply's reliability: Rating 1 fails on a 1D6 result of 1-2; Rating 2 fails only on a 1; Rating 3 is reliable enough to ignore in game terms. A Redundant Power Supply (Demolition accessories) backs up a failed primary supply.

### Radio noise mods (RnG)

Radio detonators: Rating 1 increases Noise Level by 2, Rating 2 by 1, Rating 3 decreases Noise Level by 1. A disposable/makeshift radio detonator from a commlink (Hardware + Logic [Mental] (4) Test, then Demolitions + Logic [Mental] (3) Test) can be programmed to accept only one chosen trigger number; Rating equals the commlink's Device Rating capped at 3; always runs silent.

### Timer drift (RnG)

Timer detonators: Rating 1 may fail to work at all and can drift +-2 minutes; Rating 2 drifts +-1 minute; Rating 3 keeps exact time. Optional countdown display on purchased timers (often omitted); decoy timers with conflicting displays are a common anti-removal trick. A commlink rigged as a makeshift timer detonator (Hardware + Logic [Mental] (3) Test, then Demolitions + Logic [Mental] (3) Test) counts as Rating 3 while it has an active Matrix connection, or Rating 1 without one; it always displays a countdown and always runs silent.

### Pull/push modes (RnG)

**Pull:** triggers when a ring is pulled from the housing, via tripwire or a tied object. "Pull release" mode also fires if tension on the ring is removed instead of only when pulled, defeating a simple wire-cut; disarming it safely requires a Demolitions + Logic [Mental] (5) Test. **Push:** triggers once an operator-chosen pressure threshold (in kilograms) is met, optionally with a minimum and maximum weight window, or set to a "release" mode that fires once weight is lifted off it instead.

### Optical ID (RnG)

Optical detonators carry a commlink-grade processor (Device Rating = Rating 1-6) and are planted via fiber-optic cable in cyberware, drones, computers, or commlinks. Sensor links (camera, biometric/nanoprint scanners) may be wired by fiber or wireless. Roll Device Rating against threshold 1 to positively identify a target. A failed roll is inconclusive and needs 1 minute before retrying. A glitch or critical glitch detonates on the wrong person, or fails to recognize the real target and never detonates at all. Any explosive device using an optical detonator is a complex device.

### Nitroglycerin handling (RnG)

Treat 1 liter as 1 kilogram of Rating 6 explosive. Whenever a character handles it, roll Agility + Reaction (hits do not matter; only checking for a glitch) - a glitch means accidental detonation. Transporting it in a vehicle requires a Vehicle Test (Core); a glitch sets it off (passengers resist the blast before the vehicle does, subtracting their Damage Resistance hits from the DV the vehicle then resists). If anyone carrying it is knocked down, or if it falls more than half a meter, roll an Object Resistance dice pool of 8; on a glitch it detonates. Follow the car-bomb passenger/vehicle resistance order from RnG's car-bomb section when relevant.

### GravJack settings (SL-Future)

The A-G/GravJack Grenade throws like a normal grenade, but first needs one additional Simple Action (Free if wireless is active) to set four options: Detonation (Impact, Timed, or Wireless), Duration (1-4 Combat Turns), Gravity Effect (Anti or Increased/Heavy), and Blast Radius (4-10 meters, dome-shaped).

- **Anti-Gravity:** Immediate Agility (8) Test; Physical dice pool modifier of (8 minus hits); Disorientation for Duration + 2 Combat Rounds; leaving the field requires an Agility (8 + meters to the edge) Extended Test.
- **Heavy Gravity:** Immediate Strength (8) Test; Physical dice pool modifier of (8 minus hits); knocked prone for Duration (a Lift/Carry (6) Test is needed to stand); leaving the field requires a Strength (8 + meters to the edge) Extended Test.
- **Vehicles** caught in either effect immediately resist Crash damage, and the driver also makes a Piloting (6) Test or loses control.
- **Glitch:** the particle dispersion triggers before the throw and the user suffers the chosen effect instead. **Critical glitch:** an overly dense field forms at half the set blast radius; everyone in that reduced area resists 18P damage at AP -8.

### Hornet six-projectile (SL-CorpSec)

A fired Hornet is treated as a six-round burst-fire attack under normal burst-fire rules. On a glitch when firing, the projectiles fail to separate: the round instead deals its base DV -2 with no AP.

### Maker payload swap (SL-Future)

Maker Missiles reconfigure their warhead payload via a wireless link, before or after launch. Per the sourcebook's field-test reports, most swaps complete in under 3 seconds and the most drastic changes under 10 seconds. Incomplete transitions (including a hacker intercepting the swap request in transit) can produce duds, split effects, stronger or weaker effects, or other unpredictable results at GM discretion; no fixed dice mechanic is printed. Maker Grenades are framed as sharing the same nanotech/wireless-reconfiguration concept, but no further prose describes them beyond their Avail/Cost line - do not invent a payload-swap mechanic or DV/AP/Blast for them beyond what a GM assigns from a base grenade type.

### Blast Shield use (RnG)

Carried like a shield (melee Acc 4, Exotic Melee Weapon (Blast Shield) skill) until deployed. Adhesives or magnets fix it to any surface; it detonates on a timer or remotely. See the Placed Charges & Shields catalog entry below for the stat-block reading and a flagged double-AP print quirk in the source.

### Drone-carried charges (RnG)

Microdrones and minidrones are too small to carry an explosive device. Small and medium drones may carry kilograms of explosive up to Body / 2 (round up). Large drones may carry kilograms up to Body. Planting usually needs a rigger or an appropriate Mechanic skill (internal fittings may need modification). Resolve detonation against the drone and its surroundings with the same car-bomb / vehicle-explosion resistance order below.

### Car bombs (RnG)

**Dumb bombs:** trigger on a nonspecific condition (electrical detonator wired to ignition; push/pressure detonator under a seat; radio detonator after visual confirmation). Easy to hit the wrong person (rigger interface remote-start, valet, family car-swap, remote commlink start). Radio triggers also fight Noise (see Radio noise mods).

**Smart bombs:** always use an optical detonator and are always complex devices. Sensors (hidden micro-camera with facial recognition, or biometric/DNA / nanoprint scanners on seat belt, steering wheel, glove box, etc.) confirm the target before detonation. May text the team and/or send pre-blast camera footage as proof of death; more wireless links mean more discovery risk. Biometric variants need a sample of the target's DNA.

**Passenger-kill placement:** put the charge inside the passenger compartment (e.g. under a seat) and shape it as a directional blast toward the victim. Barriers between charge and target (seat, etc.) are treated as penetrated: the barrier itself absorbs 1 box, and remaining DV transfers to the target and anyone in a 60-degree arc. Outside that arc, treat as circular blast (-2/m). Damage passengers first (always Physical). Then the vehicle resists remaining DV (subtract passenger Damage Resistance hits from the DV the vehicle faces) at only AP -2 against the vehicle. If the vehicle takes at least 1 box but is not destroyed, it is on fire: 1 automatic box per Combat Turn; a fuel-engine vehicle that fills its damage track from fire explodes for another 20P to anyone still inside.

**Door-panel tamped bomb:** packing a tamped charge inside removed door (or similar) paneling multiplies DV by 4 instead of doubling (reserved for hard-to-kill targets).

### Axle / component sabotage (RnG)

Shape a charge to cut a specific vehicle component (e.g. axle). Scale the component's Structure/Armor from the material and thickness (same percentage-of-1m approach as breaching). Planting requires Demolitions + Logic [Mental] (3); a glitch hits the gas tank (if the vehicle has one) and adds +20P to the explosion's DV. Attached-to-component charges use the attached-target AP rule (Armor halved). If the blast destroys the targeted support and leftover DV is high enough, the vehicle can flip or roll (10P more than needed to destroy the component flips it onto its side; each box above that 10P surplus can roll it further, including onto the roof).

### Drone planting penalty (RnG)

Drones can scout unconventional entry points and carry charges, but most lack the dexterity to plant: -3 dice pool on the planting Demolitions Test. Exception: drones with articulated arms that match metahuman hand/arm dexterity take no penalty. Payload weight limits are under Drone-carried charges above.

### Erasing explosive fingerprints (RnG)

To mimic another bomb-maker's forensic signature, the character needs a copy of a classified forensics report on that signature, then rolls Forgery + Logic [Mental] while crafting. Double the Extended Test thresholds for making the devices (extra care to forge the signature).

## Catalog

### Grenades (hand-thrown / minigrenade)

Skill: Throwing Weapons when hand-thrown, Heavy Weapons when loaded as a minigrenade and fired from a launcher (see Common rules for minigrenade arming/disable). Any row below can be bought/loaded either way at the same cost and effect unless its Rules say otherwise.

| Name | Src | DV | AP | Blast | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flash-bang | Core | 10S | -4 | 10m Radius | 6R | 100¥ | Concussion/stun grenade: bright, loud, shocking blast distributed equally over the radius |
| Flash-pak | Core | Special | - | Special | 4 | 125¥ | Not a true grenade: cigarette-pack-sized unit with four strobing quartz-halogen micro-flashes. Anyone looking toward it takes a -4 dice pool penalty on attack tests (flare compensation goggles/glasses reduce this to -2; flare compensation cybereyes/retinal mods reduce it to -1). 10 charges; 1 charge/Combat Turn while active; plugged-in recharge is 1 charge/10 seconds. Wireless: a subscribed user takes only half the glare penalty (round down); recharges by induction at 1 charge/hour |
| Fragmentation | Core | 18P(f) | +5 | -1/m | 11F | 100¥ | Classic shrapnel-cloud killer; flechette-factored DV, directional-style -1/m falloff even though it is thrown/launched like other grenades |
| High explosive | Core | 16P | -2 | -2/m | 11F | 100¥ | Concentrated blast and concussion; standard circular falloff |
| Gas | Core | as Chemical | - | 10m Radius | 2 + Chemical Avail | 40¥ + Chemical cost | Releases a gas cloud instead of exploding; the toxin/drug payload is a separate purchase (see Drugs Toxins and Chemicals). Cloud lasts about 4 Combat Turns (less if windy, longer if confined with poor ventilation, GM's discretion) |
| Smoke | Core | - | - | 10m Radius | 4R | 40¥ | Obscures vision per the smoke visibility modifiers; lasts about 4 Combat Turns (less if windy, longer if confined with poor ventilation, GM's discretion). See Common rules for the diameter/radius print conflict |
| Thermal smoke | Core | - | - | 10m Radius | 6R | 60¥ | As Smoke, but the cloud also carries hot particles that obscure thermographic vision (apply thermal smoke visibility modifiers); same ~4 Combat Turn duration and wind/confinement notes as Smoke |
| Paint Grenade | RnG | - | - | 10m Radius | 8R | 100¥ | Marks everyone in the blast with a splatter of paint instead of dealing damage; defeats invisibility spells and other purely-visual concealment. Optional radioactive tracking dye additive: +50¥. RnG Ultra-Glide lubricant can also be loaded into a standard paint grenade (Ultra-Glide SKU itself is Tools of the Trade, not catalogued here) |
| A-G/GravJack Grenade | SL-Future | - | - | 4m-10m (dome) | - | - | No Avail/Cost printed (Evo field-test prototype, not a market item). See Shared procedures -> GravJack settings for the full detonation/duration/effect/radius rules |

### Rockets & Missiles

Skill: Heavy Weapons. Rockets and missiles arm at 10 meters and explode on impact (see Common rules); launcher hardware (Aztechnology Striker, Onotari Interceptor, Ballista MML, Yakusoku MRL, M79B1 LAW, Vogeljager II, etc.) is catalogued in `Encyclopedia/Firearms.md`.

| Name | Src | DV | AP | Blast | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Anti-vehicle Rocket | Core | 24P | -4/-10 | -4/m | 18F | 2,800¥ | Shaped-charge warhead: AP -10 against vehicles/barriers, -4 against other targets. Blast is limited compared to a High-Explosive warhead |
| Fragmentation Rocket | Core | 23P(f) | +5 | -1/m | 12F | 2,000¥ | High-speed metal/plastic-metal fragments; very effective vs. unprotected targets, weak vs. barriers/structures/vehicles |
| High-explosive Rocket | Core | 21P | -2 | -2/m | 18F | 2,100¥ | Heavy area blast using standard grenade blast rules at rocket scale; not especially effective against hardened targets (vehicles / protected military structures) |
| Missile (any type) | Core | as chosen Rocket | as chosen Rocket | as chosen Rocket | that Rocket's Avail + 4 | that Rocket's Cost + (Sensor Rating x 500¥) | A missile is the self-guided version of one of the three rocket types above; pick a base rocket row for DV/AP/Blast, then apply this row's Avail/Cost adjustment on top of it. Same wireless link-trigger as rockets |

### Special / launched munitions

Skill: Heavy Weapons for Hornet / Maker Missile / HEAP / Depth Charge (standard grenade, missile/rocket, or PTL-02 launcher; hardware in Firearms.md). Man-Catcher ammo uses Exotic Ranged Weapon (Man-Catcher) via its launcher. GravJack is Throwing Weapons (Grenades section above).

| Name | Src | DV | AP | Blast | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hornet direct-fire mini-grenade | SL-CorpSec | 12P | -2 | Special | 16F | 400¥ | MCT/Winchester-Howe. Fires from any standard grenade launcher; unlike a normal grenade it is direct-fire (no arc), single-target, and splits into six projectiles before impact. Can be programmed to detonate on a timer or by proximity (like a grenade). Targeting sensors often malfunction and cancel separation. See Shared procedures -> Hornet six-projectile. Also reprinted in Firearms.md -> Cannons & Launchers |
| HEAP Torpedo | SL-CorpSec | 14P | -4 | -2/m | 14F | 300¥ | Impact-detonating, armor-piercing torpedo-grenade for the Wuxing/ArmTech PTL-02 underwater launcher (launcher stats in Firearms.md) |
| Depth Charge Torpedo | SL-CorpSec | 12S | -4 | 10m | 12F | 175¥ | Area-effect concussive torpedo-grenade for the same PTL-02 launcher |
| Maker Missile | SL-Future | Special (payload-set) | Special (payload-set) | Special (payload-set) | 24F | 5,000¥ | Nanotech missile whose warhead reconfigures in flight or pre-launch via wireless link; DV/AP/Blast are whichever base missile type (see Rockets & Missiles) it is currently set to, not a separate printed profile. See Shared procedures -> Maker payload swap |
| Maker Grenade | SL-Future | Special (payload-set) | Special (payload-set) | Special (payload-set) | 18F | 500¥ | Nanotech grenade from the same Maker product line as the Maker Missile; the source prints only its price, no separate prose. Do not invent stats beyond a GM-assigned base grenade type. See also `Encyclopedia/Ammunition.md` -> Maker Mag for the related (but out-of-scope-here) magazine SKU |
| Man-Catcher ammo compound | SL-CorpSec | Special (grapple) | - | 10m | 18 | 200¥ (10 shots) | Warhead payload for the Nemesis Arms Man-Catcher launcher (launcher in Firearms.md). Impact detonation only works on 4+ on 1D6 (no Edge rerolls); timer/proximity also available. Anyone in the blast must win an opposed grapple test vs. dice pool 12 or become trapped as the compound hardens and expands another meter |

### Placed Charges & Shields

| Name | Src | Skill | Acc | DV | AP | Blast | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Blast Shield | RnG | Exotic Melee Weapon (Blast Shield) for melee use; Demolitions to place/detonate | 4 | 20P | -4 | Target | 8R | 20,000¥ | 2m x 1m variable-geometry shaped charge (thermite strips plus several HE devices); carried and usable like a shield until deployed, then fixed to a surface with adhesives or magnets and set off by timer or remotely. Blast is local to whatever it is attached to, with no printed per-meter falloff. Source print quirk: the RnG stat block literally reads `DAM AP BLAST AP AVAIL COST` / `20P - Target -4 8R 20,000¥`, i.e. two AP-labeled columns; this file reads the first as blank (no incidental AP) and the second (-4) as the shaped/directed hit against whatever it contacts, since that is the only damage-relevant AP printed. Flagged as a source formatting oddity, not an invented stat |

### Bulk explosives

Skill: Demolitions. Cost/Avail below are for finished, ready-to-use product; see Shared procedures -> Cooking explosives for raw-material pricing to cook your own. Rows marked `Core, RnG` print identical stats in both books (no conflict).

| Name | Src | Rating | Unit | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Ammonium nitrate | RnG | 4 | kg | 5 | 80¥ | Fertilizer-industry precursor/oxidizer; powder/granules that require a container before a detonator can be fitted; catches fire but only explodes if burned while enclosed; will not detonate wet; often used to modify other explosives' detonation rates. Legal bulk buys are tracked |
| ANFO | RnG | 6 | kg | 7 | 100¥ | Ammonium nitrate/fuel oil binary mix; blasting-cap insensitive, needs a primer charge (e.g. a small amount of dynamite or TNT) to set off |
| Commercial | Core, RnG | 5 | kg | 8R | 100¥ | General construction-grade compound, sold solid or liquid |
| Dynamite | RnG | 3 | kg | 8R | 350¥ | Sold per kilogram; individual 0.25 kg sticks can be taped together for larger charges; can also prime other explosives such as ANFO |
| Foam | Core, RnG | 6-25 | kg | 12F | Rating x 100¥ | Plastic explosive with a shaving-cream consistency, stored in an aerosol can; sprays into crevices and detonates the same way as regular plastic explosive |
| Nitroglycerin | RnG | 6 | kg (or liter) | 11F | 350¥ | Extremely unstable. See Shared procedures -> Nitroglycerin handling |
| TNT | RnG | 5 | kg | 12R | 200¥ | Sold in blocks; cut down or taped together to size a charge; any detonator type can set it off |
| Plastic | Core, RnG | 6-25 | kg | 16F | Rating x 100¥ | Highly stable, moldable, adhesive, military-grade; color-tinted by the current/voltage needed to detonate it (black = magnetic-field induction, chalky white = 440-volt industrial) |
| Detonating cord, Low Yield | RnG | 3 | meter | 10R | 100¥ | Base DV 3P per meter; +-1P per additional/removed one-third meter (34 cm) of total cord length. Usable alone, wrapped as a cutting charge, or as a simultaneous-fuse line between other charges |
| Detonating cord, High Yield | RnG | 6 | meter | 14R | 150¥ | Base DV 6P per meter, same +-1P per one-third-meter scaling; for heavier materials than low-yield cord |
| Binary | RnG | 1-20 | kg | 18F | Rating x 125¥ | Two-part explosive listed on the RnG buy table; no further prose beyond Rating/Avail/Cost |
| Linear charge | RnG | 1-25 | meter | 16R | Rating x 250¥ | Inverted-V cutting sheath (lead, copper, or tin) packed with granular high explosive (RDX/PETN typical); automatically tamped for a x4 damage multiplier when detonated; 1 meter of charge contains 1 kilogram of explosive at the charge's Rating |
| Liquid | RnG | 1-25 | liter | 16F | Rating x 150¥ | "Liquid plastique": functions as plastic explosive but is pourable (1 liter is roughly equivalent to 1 kilogram of plastic explosive); commonly paired with an atomizer |

Note: Gunpowder has no finished-product buy line in this table (see Shared procedures -> Cooking explosives for its raw-material price, or strip it from cased ammunition).

### Detonators

Skill: Demolitions to build/arm/disarm. See Shared procedures for the Rating-specific power-fail, radio noise, and timer-drift mechanics.

| Name | Src | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Detonator cap | Core | - | 8R | 75¥ | Set off by a programmable timer or radio signal; setting the timer is a Complex Action. Wireless: set the timer with a Simple Action, or trigger without a countdown as a Free Action |
| Blasting cap | RnG | - | 8R | 20¥ | Wired into a primary explosive to set off the secondary charge; comes in electric, non-electric, and fuse-cap variants; needs a manual trigger (lit fuse or exploder plunger) rather than a self-contained remote supply |
| Electrical (detonator) | RnG | (see Rules) | (Rating x 4)R | Rating x 30¥ | Sends an electrical charge to sensitive explosives; can be wired to a light switch, appliance, or vehicle ignition for a "dumb" booby-trap. Needs a strong pulse (an exploder, car battery, wall socket, or dedicated supply); normal appliance-battery current is not enough. Source print quirk: the Detonators table prints Rating as blank (`-`) while Avail/Cost still scale off Rating; the Accessories table's like-named Electrical line is Rating 1-6 - do not invent a detonator Rating band |
| Optical (detonator) | RnG | 1-6 | (Rating x 7)F | Rating x 200¥ | Commlink-grade processor (Rating = Device Rating). See Shared procedures -> Optical ID for fiber plant-in, sensor links, ID rolls, and complex-device status |
| Pull | RnG | - | 9F | 80¥ | Detonates when a ring is pulled from the housing (tripwire/attached object); see Shared procedures -> Pull/push modes for the pull-release anti-tamper variant |
| Push | RnG | - | 9F | 80¥ | Detonates at an operator-set pressure threshold; see Shared procedures -> Pull/push modes for min/max windows and the pressure-release variant |
| Radio | RnG | 1-3 | 10R | 75¥ | Wireless-enabled, triggered by a commlink signal. See Shared procedures -> Radio noise mods for per-Rating Noise Level modifiers and the disposable-commlink conversion |
| Timer | RnG | 1-3 | (Rating x 6)F | Rating x 50¥ | Electronic or mechanical countdown/scheduled trigger. Optional display; see Shared procedures -> Timer drift for per-Rating accuracy, decoys, and the commlink conversion |

### Demolition accessories

Skill: Demolitions. The RnG "Demolitions Supplies and Equipment" accessories table separately lists `Electrical` and `Optical` entries with different Ratings/Avail/Cost from the like-named Detonators above; both are printed as-is and disambiguated here with a parenthetical, flagged as a same-name source oddity rather than resolved by guesswork.

| Name | Src | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Atomizer | RnG | 1-10 | (Rating x 2)R | Rating x 300¥ | Sprays a cloud of liquid explosive. See Shared procedures -> Atomizer cloud (airborne-ignition requirement, uniform DV, falloff outside the cloud) |
| Exploder | RnG | (has Rating; band unprinted) | - | - | Handheld device that supplies the electrical pulse for electrical or optical detonators (each exploder type only works its matching detonator type). Needed for manually detonated wired setups (blasting caps, detonating cord); many remote detonators carry their own power supply and do not need one. Connects a number of circuits equal to its Rating, firing them simultaneously or staggered for a chosen blast pattern; charges wired to the same circuit always fire together; can set off up to Rating x 4 detonators at once. Triggering it is a Complex Action regardless of circuit count. No Avail/Cost printed in the RnG extract |
| Hard-shell briefcase (hermetically sealed) | RnG | 1-12 | 10R | Rating x 100¥ | Smuggles explosives past chemsniffers; Rating is a negative dice pool modifier applied to chemsniffer/olfactory detection attempts |
| Safety Fuse | RnG | - | 6R | 5¥ per meter | Waterproof cord that burns at 1 cm/second (3 cm per Combat Turn); lit with any flame source and inserted into a blasting cap for a cheap, simple manual delay |
| Redundant Power Supply | RnG | - | 6R | 50-500¥ | Backup power for a detonator so a failed primary supply still triggers the charge; same idea as the "multiple blast machines/power supplies" anti-removal trick. Adds build complexity/time at GM discretion |
| Nanoprint Scanners | RnG | 1-6 | 16F | Rating x 500¥ | Spray-on fingerprint/DNA sensors that feed an optical detonator for smart-bomb target confirmation (steering wheel, seat belt, glove compartment, etc.); biometric setups need a sample of the target's DNA |
| Electrical (accessory) | RnG | 1-6 | 8R | Rating x 150¥ | Distinct line item from the Electrical detonator above (Detonators table); same name, different Rating band and price in the RnG accessories table - see table intro note |
| Optical (accessory) | RnG | 1-6 | 14R | Rating x 250¥ | Distinct line item from the Optical detonator above (Detonators table); same name, different price in the RnG accessories table - see table intro note |

## Kill Code Matrix grenades

**Verified from:** `killcode.pdf`. Also listed under Commlinks and Electronics.

| Name | Avail | Cost | Effect |
| --- | --- | --- | --- |
| Fuzzy Boom Boom Bunnies | 10R | 20¥ × Power (max 20) | Noise = Power (−1 per 2 m); lasts 2 CT. |
| CoS (Cancellation of Service) | 10R | 500¥ | 5 m pulse; dumps VR; drones keep last orders; devices reboot; TMs resist 10S. |
| Douser | (Rating × 2)F | Rating × 50¥ | Rating 1–10; 5 m; nanites reduce Firewall. |
| DumDum | (Rating × 2)R | Rating × 50¥ | Rating 1–10; 5 m; reduces Data Processing. |

**Painade (CA):** Fichetti Pain Induction Area Denial Grenade. Toxin field Power **8**, Speed **Immediate**; resist Body + Willpower; if modified Power > Mental limit, next Action Phase must flee; if stuck in field, incapacitated (DP mod = modified Power). Field **5 Combat Turns**; single-use (electronics fry). **Avail/Cost/Blast:** print row is Lapel Dagger bleed (`4 / — / (STR+1)P / −1 / 5` copied from the dagger table on the same page) — not usable. JackPoint calls it an "expensive gadget"; leave buy stats blank until errata.

