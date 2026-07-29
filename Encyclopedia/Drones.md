# Drones

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only.

**Src PDFs:** Core · `rigger5.pdf` · `Shadowrun_5E_Bullets_&_Bandages.pdf` · `Shadowrun_5E_Hard_Targets.pdf` · `Shadowrun_5E_Cutting_Aces.pdf` · `howlingshadows.pdf`
**Books:** Core · Rigger 5.0 · B&B · HT · CA · HS (biodrones)
**See also:** `Encyclopedia/Vehicles.md` · `Encyclopedia/Vehicle and Drone Modifications.md` · `Encyclopedia/Rigger Gear.md` · `Mechanics/Rigging.md` · `Mechanics/Vehicles.md`
**Out of scope here:** RCC models (Rigger Gear); full vehicle-mod slot system for cars (Vehicle and Drone Modifications / R5 Building the Perfect Beast); smart firing platform (Weapon Accessories; drone-like Pilot but not a drone SKU).

## Schema

| Field | Meaning |
| --- | --- |
| Size | Micro / Mini / Small / Medium / Large / Huge / Anthro / Missile / Chassis |
| Src | Book + page (Core print ~465-466; R5 catalog ~128-149; R5 compiled tables ~189-191) |
| Skill | Pilot skill to operate that drone |
| Handl | Handling; `A/B` = on-road/off-road or mode pair as printed; `-` = immobile/n/a |
| Speed | Speed rating; optional letter = movement mode for R5 chase mixing (see Common rules). `A/B` = dual-mode |
| Accel | Acceleration; dual-mode when paired with dual Speed |
| Body | Body, or `X(Y)` where X = Body and Y = free Mod Points (R5). If no `(Y)`, treat available mod points = Body unless Body 0 |
| Armor | Armor |
| Pilot | Pilot program Rating (= Device Rating / Matrix attributes) |
| Sensor | Sensor array Rating |
| Seats | Passenger seats if any; usually `-` |
| Avail / Cost | Street Availability / nuyen |
| Std upgrades | Factory gear already consuming Mod Points / included kit |
| Rules | All per-SKU mechanical notes |

## Common rules

### Core (all drones)

- Drones ship with built-in rigger interface (jump-in ready). Device Rating = Pilot Rating; Matrix attributes = Pilot.
- Pilot programs are device-specific dog-brains; cannot freely copy between units (Core Riggers).
- Autosoft Rating cannot exceed the drone's Pilot unless shared from an RCC (Core / R5).
- Autosofts are model-specific (Clearsight for Crawler does nothing in Proletarian).
- Weapon mounts: unaugmented Body ÷ 3 (round down) mounts; standard mount = assault rifle or smaller + 250 rounds; heavy = 2 mounts, any weapon + 500 belt or Body rockets/missiles; remote only on drones (no manual op) - Core Street Gear.
- Sensor housings by size (Core): small-or-smaller drone max Sensor Rating 3; medium 4; large 5 (arrays often factory-fit at listed Sensor).
- Concealability (Core table): microdrone -6; minidrone -2; small +2; medium +8 (vs Perception to notice carried/stowed as gear).
- Condition / damage: treat as vehicles unless anthro special rule.

### Rigger 5.0 size / chase helpers

- Target size modifiers (R5 Maximum Pursuit): Micro -3; Mini -2; Small -1; Average (vehicles/drones Body ≤8) 0; then Body 9-14 +1; 15-20 +2; >20 +3 (+2 Body per 10 seats when sizing).
- Speed mode letters on R5 Speed column (chase Speed multiplier vs pedestrians/mixed): W Water ×0.8; G Ground ×1; R Rotor ×3; J Jet ×4. Letter **P** appears on many R5 prop/VTOL/LtA aircraft Speeds (not in that multiplier list; GM picks Rotor or Jet as fits the airframe).
- Operational time (R5): normal run ~6 hours before refuel/recharge; idle longer; top-speed continuous shorter. Track narratively, not minute-by-minute.
- Swarms (R5): slave drones to RCC running Swarm program; up to Device Rating × 3 slaves. Swarm Pilot = highest member Pilot or RCC Device Rating (higher); uses highest autosofts/Sensor; lowest Handling/Speed/Accel; action bonus = (drones in swarm - 1) to dice and limit. Combat: one weapon profile represents the volley. Target drones individually.

### R5 Body X(Y) and light mods

- Mod Points = Body. `Body X(Y)`: X = Body, Y = free Mod Points left after factory gear. Attribute +1 (or Armor +3) once with no Mod Point cost; further raises cost Mod Points = increase - 1. Body itself cannot be raised. Cap: attributes ≤ 2× starting (use 0.5 if starting 0). See R5 Drone Modification for costs; deeper vehicle-slot system is separate chapter.

### Anthropomorphic drones (R5)

- Come with two drone arms + two drone legs (Obvious; may be Synthetic).
- Physical Condition Monitor = 8 + (Body / 2) (more durable than typical drones).
- Can use many metahuman items (clothing, weapons, tools).

### Pilots / autosofts (R5 price reminder)

- Pilot Rating 1 Avail 4 Cost 100¥; 2 - / 400¥; 3 8R / 1,800¥; 4 12R / 3,200¥; 5 16F / 10,000¥; 6 24F / 20,000¥.
- Autosoft Rating 1-6: Avail Rating×2, Cost Rating×500¥.
- Smartsoft (Restricted): treated as Rating 3 autosoft; full smartgun use via sensors.
- Group autosoft: Rating 2; shared-signal group commands.
- Personality tweak Avail 4 / 100¥; Linguistics Avail 4 / 50¥ (verbal command vocab limited; Language Skillset autosoft is real translation).

### Core vs R5 Core reprints

- R5 compiled tables reprint Core drones and state R5 Mod Point / adjusted lines replace originals when using R5. This file lists Core page for Core SKUs and uses R5 compiled stats where both appear.

## Catalog

## MICRODRONES
### Shiawase Kanmushi
- Size: Micro
- Src: Core p.465; R5 table p.190
- Skill: Pilot Walker
- Handl: 4 | Speed: 2 | Accel: 1
- Body: 0 | Armor: 0 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 8 | Cost: 1,000¥
- Std upgrades/downgrades: Gecko tips (walls/ceilings)
- Rules: Four-legged bug crawler; hard to tell from insect at a glance. Fragile: easily destroyed by being stepped on or a tag eraser. Confined-space infiltration.
### Sikorsky-Bell Microskimmer
- Size: Micro
- Src: Core p.465; R5 table p.190
- Skill: Pilot Ground Craft (Hovercraft specialization applies)
- Handl: 3 | Speed: 3 | Accel: 1
- Body: 0 | Armor: 0 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 6 | Cost: 1,000¥
- Rules: Disc-shaped skimmer smaller than a frisbee; can skim over water via weak hoverjets. Easier to spot than Kanmushi but still very small.
### Horizon "NoizQuito"
- Size: Micro
- Src: R5 p.128
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 3R | Accel: 2
- Body: 1 | Armor: 0 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 10R | Cost: 2,000¥
- Std upgrades/downgrades: Flying; speakers; strobes
- Rules: Mosquito-like. Speakers blast up to 160 dB. Wings/body LEDs produce blinding strobes. GAME: Strobes impose -2 to all actions by those looking at the drone (-1 with flare compensation). Speakers impose -2 to all actions by those in earshot (-1 with sound damper). Multiple drones in a group: penalties stack per drone (up to -12 from three drones with both effects). Earshot = GM call.
### Sony Goldfish
- Size: Micro
- Src: R5 p.128-129
- Skill: Pilot Watercraft
- Handl: 2/4 | Speed: 1W | Accel: 1
- Body: 0 | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 6 | Cost: 500¥
- Std upgrades/downgrades: Submersible (dives up to 4 m)
- Similar models: Mitsuhama Minnow; NeoNET Pinkeens
- Rules: Realistic fish proportions. Entry-level water microdrone. Water heavily degrades wireless signal.
## MINIDRONES
### Horizon Flying Eye
- Size: Mini
- Src: Core p.465-466; R5 table p.190
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 3 | Accel: 2
- Body: 1 | Armor: 0 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 8 | Cost: 2,000¥ (flash-pak/smoke variant +500¥)
- Rules: Eyeball-sized spherical VTOL with omnidirectional thrust. Can roll on ground; must fly to clear stairs/curbs. Optional built-in flash-pak + smoke grenade (+500¥); detonating either destroys the drone. Cybereye ocular drone (Core) functions as this model when removed.
### MCT Fly-Spy
- Size: Mini
- Src: Core p.466; R5 table p.190
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 3 | Accel: 2
- Body: 1 | Armor: 0 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 8 | Cost: 2,000¥
- Rules: Large-insect sized/shaped flyer; better altitude than micro bugs. Eye-in-sky / shadowing; relatively hard to spot.
### Aerodesign Systems Condor LDSD-23
- Size: Mini
- Src: R5 p.129
- Skill: Pilot Aircraft
- Handl: 2 | Speed: 0R | Accel: 0
- Body: 1(1) | Armor: 0 | Pilot: 2 | Sensor: 4 | Seats: -
- Avail: 6R | Cost: 4,000¥
- Similar models: Ares Cloudship; Renraku Buzzard
- Rules: Solar-powered hydrogen balloon long-duration observation drone. Transparent / radar-invisible materials. Can hover for days-weeks. Deflated: smaller than bowling pin; inflated balloon ~kitchen table. Completely vulnerable if detected; cannot flee.
### Aztechnology Hedgehog
- Size: Mini
- Src: R5 p.129
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 1G | Accel: 1
- Body: 1(0) | Armor: 0 | Pilot: 4 | Sensor: 3 | Seats: -
- Avail: 8F | Cost: 8,000¥
- Std upgrades/downgrades: Electronic Warfare (2) autosoft
- Similar models: Ares NS-Aardvark; Lone Star Mockingbird
- Rules: Crawler sub-design of Aztechnology Crawler. Security-sniffing: find C3 broadcasts; passive listen + decrypt. Hidden: up to 48 hours on one charge.
### Cyberspace Designs Dragonfly
- Size: Mini
- Src: R5 p.129
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 2P | Accel: 1
- Body: 1(0) | Armor: 3 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 12R | Cost: 4,000¥
- Std upgrades/downgrades: Melee Bite Acc 3, Reach -, DV 3P, AP -2; Targeting (Melee) autosoft
- Similar models: Ares Sparrowhawk (mounts modified Ares Light Fire 70); Renraku Yokujin
- Rules: Quad-copter anti-drone hunter. Protected in-body rotors. Beak shears mini/micro drones. Can swarm larger drones but not designed vs appreciable armor.
### Festo Pigeon 2.0
- Size: Mini
- Src: R5 p.129
- Skill: Pilot Exotic Vehicle
- Handl: 4 | Speed: 2P | Accel: 1
- Body: 1(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 8 | Cost: 3,000¥
- Std upgrades/downgrades: Realistic Features (1)
- Similar models: Sony Nightingale; Renraku Bluebird
- Rules: Lifelike flying bird drone (baseline chrome; lifelike model common for surveillance).
### Horizon CU^3
- Size: Mini
- Src: R5 p.130
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 1P | Accel: 1
- Body: 1(1) | Armor: 0 | Pilot: 2 | Sensor: 3 | Seats: -
- Avail: 4 | Cost: 3,000¥
- Std upgrades/downgrades: Clearsight (2) autosoft
- Similar models: MCT Redlight; Evo CultureCapture
- Rules: Single-fan vectored-thrust camera drone; stable, quiet. Optional Professional Upgrade: Pilot 4 + Clearsight 4 for +3,000¥. Pros often run three for multi-angle.
### Renraku Gerbil
- Size: Mini
- Src: R5 p.130
- Skill: Pilot Ground Craft
- Handl: 4/2 | Speed: 2G | Accel: 1
- Body: 1(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 4 | Cost: 2,000¥
- Similar models: GM-Nissan Mouse; MCT Zipper
- Rules: Tiny wheeled; fits ventilation shafts and most pipes. Quick/nimble vs metahuman pursuit.
### Renraku Scuttler Remote Cyberhand
- Size: Mini
- Src: R5 p.130
- Skill: Pilot Walker
- Handl: n/a | Speed: n/a | Accel: n/a
- Body: n/a | Armor: n/a | Pilot: n/a | Sensor: - | Seats: -
- Avail: 8 | Cost: 8,000¥
- Similar models: Evo Hi-Five; Ares Thing
- Rules: Detachable cyberhand with remote rigger controls + computer. Middle digit: poor sensor suite; other four digits for locomotion. Better manipulation than similar-size drones; less quick/nimble due to hand shape. No Capacity for further upgrades. CYBERWARE TABLE: Essence 0.25, Capacity (5), Avail 8, Cost 8,000¥.
## SMALL DRONES
### Aztechnology Crawler
- Size: Small
- Src: Core p.466; R5 table p.189
- Skill: Pilot Walker
- Handl: 4 | Speed: 3 | Accel: 1
- Body: 3 | Armor: 3 | Pilot: 4 | Sensor: 3 | Seats: -
- Avail: 4 | Cost: 4,000¥
- Rules: Handles stairs/obstacles. Remote snooper for rough rural/urban terrain. Pilot a step above most of its class.
### Lockheed Optic-X2
- Size: Small
- Src: Core p.466; R5 table p.191
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 4 | Accel: 3
- Body: 2 | Armor: 2 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 10 | Cost: 21,000¥
- Std upgrades/downgrades: Signature-limiting stealth
- Rules: VSTOL stealth. Wings folded: cyberdeck-sized; deployed: large hawk / bird of prey. Radar systems and visual/audio Perception Tests: -3 dice pool to spot.
### Ares Arms Sentry V
- Size: Small
- Src: R5 p.130-131
- Skill: Pilot Ground Craft
- Handl: 4/- | Speed: 1G | Accel: 1
- Body: 2(0) | Armor: 6 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 4R | Cost: 4,000¥
- Std upgrades/downgrades: Standard weapon mount; Colt Cobra TZ-120; 30 standard ammo; Targeting (3); SmartSoft
- Similar models: Shpagina Evo-2; Shiawase Minebea GridSys
- Rules: Rail-drone: hangs from facility rails; traverses facility via high wall doggie doors. Draws power and accepts commands via rail (impervious to wireless hijack; secondary dedicated power keeps it up in facility blackouts). See Mercury for unarmed rail courier sibling.

### Ares Arms Mercury
- Size: Small
- Src: R5 p.130-131 (same entry as Sentry V; no separate compiled-table row)
- Skill: Pilot Ground Craft
- Handl: 4/- | Speed: 1G | Accel: 1
- Body: 2(0) | Armor: 6 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 4R | Cost: 4,000¥ (same chassis price as Sentry unless GM prices courier lower)
- Std upgrades/downgrades: None of the Sentry combat load (no weapon mount / Cobra / Targeting / SmartSoft). Same rail interface and power feed.
- Similar models: Shares Sentry rail ecosystem
- Rules: Unarmed rail courier / mobile mailbox on the Sentry rail system. Mid-60s Ares add-on; in 90%+ of Ares facilities per R5. On active hostiles: Mercuries store themselves clear of rails so Sentries can deploy. Same Handl/Speed/Accel/Body/Armor/Pilot/Sensor as Sentry V chassis; combat gear stripped.
### Citron-Brouillard Smoke Generator
- Size: Small
- Src: R5 p.130-132
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 1G | Accel: 1
- Body: 2(0) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 8 | Cost: 4,000¥
- Std upgrades/downgrades: Smoke generator: 12 one-minute doses normal smoke + 3 one-minute doses thermal (IR-blocking) smoke
- Rules: Tracked. Stationary: billowing screen ~150 m diameter. Rolling: trail ~100 m wide × 250 m long. Cloud ~10 m high. Begins dissipating 1 minute after shutoff (becomes light cloud); fully gone 1 minute later. Other gases fit tank but not at proprietary smoke volume.
### Cyberspace Designs Wolfhound
- Size: Small
- Src: R5 p.131-132
- Skill: Pilot Aircraft
- Handl: 3 | Speed: 2J | Accel: 1
- Body: 2(1) | Armor: 0 | Pilot: 2 | Sensor: 4 | Seats: -
- Avail: 12 | Cost: 30,000¥
- Similar models: Ares Sergeant; S-K Dawnrider
- Rules: Recon: high sensors + speed over durability/arms. Only drone of its size to break sound barrier; usually stays subsonic to conceal location.
### Evo Proletarian
- Size: Small
- Src: R5 p.131-132
- Skill: Pilot Ground Craft
- Handl: 4/2 | Speed: 2G | Accel: 1
- Body: 2(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 6 | Cost: 4,000¥
- Std upgrades/downgrades: Drone arm (STR 4, AGI 2); Automotive Mechanic Toolkit; Automotive Mechanic (2) autosoft
- Rules: Three-wheeled mechanic assistant (dents, tires, oil, tools, schematics display, undercarriage watch, speakers). Many repair/construction/butler autosofts available.
### Ferret RPD-5X Wheeled Perimeter Drone
- Size: Small
- Src: R5 p.132 (chapter title also says RPD-1X; stats table and compiled list use RPD-5X)
- Skill: Pilot Ground Craft
- Handl: 4/2 | Speed: 1G | Accel: 1
- Body: 2(1) | Armor: 3 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 8R | Cost: 4,000¥
- Std upgrades/downgrades: Mini weapon mount; Defiance Shocker; 4 taser darts; flashlight
- Similar models: Aztechnology IDS; NeoNET Janus
- Rules: Cheap light security patrol (campuses, malls, homes). Awful off-road; stay on established paths. Prefer RPD-5X as official SKU name (compiled tables).
### Festo Sewer Snake
- Size: Small
- Src: R5 p.132
- Skill: Pilot Ground Craft / water as applicable
- Handl: 3 | Speed: 1G/1W | Accel: 1/1
- Body: 2(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 10 | Cost: 6,000¥
- Std upgrades/downgrades: Submersible; gecko grips
- Rules: Slither + swim; long narrow body. Gecko grips for vertical climb. Handles 10 m dive pressure. Little room for further mods.
### Horizon Mini-Zep
- Size: Small
- Src: R5 p.132
- Skill: Pilot Aircraft
- Handl: 2 | Speed: 0P | Accel: 0
- Body: 2(4) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: 4
- Avail: 4 | Cost: 2,000¥
- Std upgrades/downgrades: Electrochromatic coating on airbag
- Rules: LtA ad drone. Electrochromic ads; small radio transmitter for AR spam to nearby commlinks. Loiter ~8 hours via fans. Can rebroadcast weather/APB/etc. Seats 4 in compiled table (passenger/rack capacity as printed).
### Knight Errant P5 Pursuit Drone
- Size: Small
- Src: R5 p.133-134
- Skill: Pilot Ground Craft
- Handl: 4/2 | Speed: 6G | Accel: 2
- Body: 2(1) | Armor: 0 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 10R | Cost: 8,000¥
- Rules: Limpet pursuit drone from KE cruisers. Top speed: batteries last 10 minutes. Magnetically attaches to pursued vehicle undercarriage; KE tracks wireless signal. Broadcast uses second battery (~24 hour life).
### Lone Star Castle Guard
- Size: Small
- Src: R5 p.133-134
- Skill: Pilot Ground Craft
- Handl: 4/2 | Speed: 1G | Accel: 1
- Body: 2(0) | Armor: 6 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 8R | Cost: 10,000¥
- Std upgrades/downgrades: Light weapon mount; Targeting (3); Smartsoft; four SmartSafety bracelets
- Rules: Home-security pistol-armed drone (CAS common). Extra SmartSafety bracelets/pet collars: 50¥ each. CAS tooling differs from metric (repair kit note).
### Mitsuhama Gun Turret
- Size: Small
- Src: R5 p.133-134
- Skill: No Pilot skill required (immobile)
- Handl: - | Speed: - | Accel: -
- Body: 2(0) | Armor: 6 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 4R | Cost: 4,000¥
- Std upgrades/downgrades: Standard weapon mount. Standard Downgrade: Immobile
- Rules: Rotates only; cheap Zero-Zone staple. Common variants: Retractable or Up-Armored; some take larger mount.
### Mitsuhama Seven (compiled base row)
- Size: Small
- Src: R5 compiled table p.191; chapter p.133-135
- Skill: Pilot Aircraft (Speed 1P on this row)
- Handl: 4 | Speed: 1P | Accel: 1
- Body: 1(1) | Armor: 0 | Pilot: 2 | Sensor: 3 | Seats: -
- Avail: 4 | Cost: 3,000¥
- Std upgrades/downgrades: Fragile (1) per chapter
- Rules: Master-chart "Seven" line. Chapter sells locomotion packs (Wheelie/Treads/Dirty/Quad/Swims/Hovers/Soars) with different stats. Prefer the chassis row for the purchased pack; keep this row when citing compiled tables literally.
### NeoNET Prairie Dog
- Size: Small
- Src: R5 p.134-135
- Skill: Pilot Ground Craft
- Handl: 2/4 | Speed: 2G | Accel: 1
- Body: 2(0) | Armor: 3 | Pilot: 3 | Sensor: 4 | Seats: -
- Avail: 12F | Cost: 8,000¥
- Std upgrades/downgrades: Electronic Warfare (3) autosoft; directional jammer (4); area jammer (6)
- Rules: Decommissioned PCC military ECM/jamming infantry drone. Large off-road wheels; keeps pace with dismounted infantry. Demilitarized civilian version still antenna-heavy.
### Pratt & Whitney Sundowner
- Size: Small
- Src: R5 p.134-135
- Skill: Pilot Aircraft
- Handl: 3 | Speed: 4P | Accel: 1
- Body: 2(0) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 8 | Cost: 10,000¥
- Std upgrades/downgrades: Aerial chemical sprayer: 10 doses; each covers line 125 m long × 25 m wide × 10 m high; large spray doses cost 10× normal dose cost
- Similar models: Shiawase Hyakusho; Aztechnology Roundup
- Rules: Low-speed agricultural spray / skywriting aircraft.
### Proteus A.G. "Krake"
- Size: Small
- Src: R5 p.134-137
- Skill: Pilot Watercraft
- Handl: 5 | Speed: 3W | Accel: 4
- Body: 2(0) | Armor: 2 | Pilot: 4 | Sensor: 3 | Seats: -
- Avail: 18F | Cost: 10,000¥
- Std upgrades/downgrades: Plasma torch; specialized weapon (ink pouch); Nautical Mechanic toolkit; weapon mount
- Rules: Squid-form; six tentacles for propulsion/agility. One tentacle: plasma torch + multitool (touch range only; useless in combat). Optional security retrofit: micro-torpedo cluster + ink pouch. INK: cloud of ink + metal-flake chafe; obscures vision (even electronic) in 5 m radius; Heavy Smoke penalty for attacks through cloud. Micro-torpedo warheads bought separately (see next entry); not in Krake base cost.
### Micro-torpedo (Krake payload)
- Size: Ammo / drone payload (not a drone)
- Src: R5 p.137 (under Proteus Krake)
- Skill: n/a
- Handl: n/a | Speed: n/a | Accel: n/a
- Body: n/a | Armor: n/a | Pilot: n/a | Sensor: n/a | Seats: -
- Chemical warhead: DV 6P; AP -4; Blast 1 m radius; Avail 18F; Cost 3,000¥; acidic adhesive deals continuous damage each Combat Turn until glue solvent (Core p.448)
- Explosive warhead: DV 18P; AP -4/-10; Blast -6/m; Avail 18F; Cost 2,500¥; as anti-vehicle rockets (-4 AP vs non-vehicles, -10 AP vs vehicles)
- Avail: 18F | Cost: 3,000¥ chemical / 2,500¥ explosive
- Rules: Fired from Krake weapon mount / cluster retrofit.
### SAAB-Thyssen Bloodhound
- Size: Small
- Src: R5 p.136-137
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 1G | Accel: 1
- Body: 2(0) | Armor: 0 | Pilot: 2 | Sensor: 4 | Seats: -
- Avail: 8 | Cost: 10,000¥
- Std upgrades/downgrades: Geiger counter (6); olfactory scanner (8)
- Rules: Hazmat exploration. Identifies bio/chem/rad; marks with color-coded RFID flags; scoop + storage for soil samples.
### Renraku Dove
- Size: Small
- Src: R5 p.136-137
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 2P | Accel: 1
- Body: 2(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 4 | Cost: 5,000¥
- Std upgrades/downgrades: Radio signal scanner (6)
- Rules: Licensed exclusively to GOD. Quiet sprawl patrol for illegal wireless; alerts GOD for heavier response. Table name Dove-4 in writeup header.
### Renraku Jardinero
- Size: Small
- Src: R5 p.136-137
- Skill: Pilot Ground Craft
- Handl: 2/4 | Speed: 1G | Accel: 1
- Body: 2(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 4 | Cost: 2,000¥
- Similar models: Dozens of Renraku chassis variants (vacuum, floor polish, parking-lot paint, etc.)
- Rules: Automated lawn mower (silent electric). Shared Renraku chassis family.
### Renraku Job-a-Mat
- Size: Small
- Src: R5 p.137-138
- Skill: No Pilot skill required (immobile)
- Handl: - | Speed: - | Accel: -
- Body: 2(2) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 4 | Cost: 3,000¥
- Std upgrades/downgrades: Profession or Knowledge (2) autosoft. Downgrade: Immobile
- Rules: Immobile service kiosk chassis (BarristaBot, Intern paperwork, etc.). ~two dozen marketed models. Odd requests escalate to rigger backup. Renraku branding often omitted.
### Renraku Pelican
- Size: Small
- Src: R5 p.137-138
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 2P | Accel: 1
- Body: 2(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 2 | Cost: 4,000¥
- Std upgrades/downgrades: Storage compartment (heated/cooled modular underhung)
- Similar models: MCT Transporter-3; Evo Kourier
- Rules: Quad-copter delivery drone (food wholesale).
### Telestrian Industries Shamus
- Size: Small
- Src: R5 p.137-139
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 3G | Accel: 1
- Body: 4(0) | Armor: 4 | Pilot: 3 | Sensor: 8 | Seats: -
- Avail: 10 | Cost: 30,000¥
- Std upgrades/downgrades: Quicksilver camera; Sensor array Rating 8 with: atmosphere sensor; camera (low-light, normal, thermographic); Geiger; MAD; olfactory; radio signal scanner; ultrasound; X-ray
- Rules: Forensic walker (canine/arachnid). Projects trideo crime-scene reconstruction to investigator PAN. Quicksilver camera: needs mana-sensitive film plate (Street Grimoire p.214) per use. Vs standard quicksilver: development 5 minutes (not 2); thresholds for tests with developed images +1.
## MEDIUM DRONES
### Ares Duelist
- Size: Medium
- Src: Core p.466; R5 table p.190
- Skill: Pilot Walker
- Handl: 3 | Speed: 3 | Accel: 1
- Body: 4 | Armor: 4 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 5R | Cost: 4,500¥
- Std upgrades/downgrades: Unique Targeting (Swords) Rating 3 autosoft; pair of standard swords in special mounts (cannot swap those swords; additional mounts use normal rules)
- Rules: Anthropomorphic patrol walker styled after Renraku Red Samurai oyoroi. Blade arms primary.
### GM-Nissan Doberman
- Size: Medium
- Src: Core p.466; R5 table p.190
- Skill: Pilot Ground Craft
- Handl: 5 | Speed: 3 | Accel: 1
- Body: 4 | Armor: 4 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 4R | Cost: 5,000¥
- Std upgrades/downgrades: Standard weapon mount
- Rules: Tracked perimeter-patrol drone; day/night.
### MCT-Nissan Roto-Drone
- Size: Medium
- Src: Core p.466; R5 table p.191
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 4 | Accel: 2
- Body: 4 | Armor: 4 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 6 | Cost: 5,000¥
- Rules: Modular rotor-wing. Treat Body as 3 higher than actual for how many weapon mounts or customizations it can integrate.
### Ares Cheetah
- Size: Medium
- Src: R5 p.138-140
- Skill: Pilot Walker
- Handl: 4 | Speed: 6G | Accel: 2
- Body: 2(0) | Armor: 6 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 12R | Cost: 14,000¥
- Std upgrades/downgrades: Fragile (1); Jaws Acc 3, Reach -, DV 5P, AP -3
- Rules: Fastest quad mech; claws for traction. Rare taser-head swap replaces jaws.
### Evo Krokodil
- Size: Medium
- Src: R5 p.139-141
- Skill: Pilot Ground Craft / Pilot Watercraft
- Handl: 3 | Speed: 2G/3W | Accel: 1
- Body: 3(1) | Armor: 6 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 8R | Cost: 12,000¥
- Std upgrades/downgrades: Amphibious
- Rules: Tracked amphibious; can roll into river and out without slowing. Not submersible: dies if dunked >1 m. Must reseal after mods or sinks. Can float nearly submerged for loiter/record.
### Federated-Boeing Kull
- Size: Medium
- Src: R5 p.140-141
- Skill: Pilot Aircraft
- Handl: 3 | Speed: 4P | Accel: 2
- Body: 3(3) | Armor: 0 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 4 | Cost: 10,000¥
- Std upgrades/downgrades: Two single-use underwing bomb racks (parachute supply crates)
- Similar models: Esprit Industries Recon-TF1; Saeder-Krupp Bussard
- Rules: Mid aerial with small internal cargo. Short landing strip vs full plane.
### MCT Tunneler
- Size: Medium
- Src: R5 p.140-141
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 0P | Accel: 0
- Body: 3(2) | Armor: 6 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 8R | Cost: 10,000¥
- Std upgrades/downgrades: Drill: dig through barrier Armor 12 or less at 1 meter per hour
- Rules: Mine rescue crawler; tunnel large enough for humans/dwarfs/elves to shimmy (orks/trolls need larger gear). Loud and slow. Tunnels often unstable.
### Renraku LEBD-2 Law Enforcement Backup Drone
- Size: Medium
- Src: R5 p.140-141
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 2P | Accel: 1
- Body: 3(0) | Armor: 9 | Pilot: 4 | Sensor: 4 | Seats: -
- Avail: 12R | Cost: 20,000¥
- Std upgrades/downgrades: Mini weapon mount; Yamaha Pulsar; 4 taser darts; Smartsoft; Targeting (4); Clearsight (4); Knowledge: Legal Codes (4)
- Rules: Roto-drone for Neo-PD one-officer/one-drone teams; charges on patrol-car back mount. Assaulting often treated as assaulting an officer. Strong facial-recognition / warrant pipeline via Renraku DBs.
### Transys Steed
- Size: Medium
- Src: R5 p.140-142
- Skill: Pilot Ground Craft
- Handl: 4/2 | Speed: 1G | Accel: 1
- Body: 3(1) | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 2 | Cost: 4,000¥
- Similar models: Evo Freedom; DocWagon Chariot
- Rules: Motorized wheelchair; trode-based DNI control. Street-legal; indoor-capable.
## LARGE DRONES
### Cyberspace Designs Dalmatian
- Size: Large
- Src: Core p.466; R5 table p.189
- Skill: Pilot Aircraft
- Handl: 5 | Speed: 5 | Accel: 3
- Body: 5 | Armor: 5 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 6R | Cost: 10,000¥
- Rules: Large VTOL recon; can hover. Stored ~lawn-mower size; deployed ~large hang glider. Licensed by Lone Star / Knight Errant for urban patrol.
### Steel Lynx Combat Drone
- Size: Large
- Src: Core p.466; R5 table p.190
- Skill: Pilot Ground Craft
- Handl: 5 | Speed: 4 | Accel: 2
- Body: 6 | Armor: 12 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 10R | Cost: 25,000¥
- Std upgrades/downgrades: Heavy weapon mount
- Rules: Hardened ground combat; four wheeled legs.
### Ares Matilda
- Size: Large
- Src: R5 p.141-142
- Skill: Pilot Ground Craft
- Handl: 1 | Speed: 2G | Accel: 1
- Body: 8 | Armor: 8 | Pilot: 2 | Sensor: 1 | Seats: -
- Avail: 12R | Cost: 18,000¥
- Std upgrades/downgrades: Two riot shields; standard weapon mount; underbarrel grenade launcher; Targeting (3)
- Rules: Tracked refrigerator-shaped mobile cover. Side blast doors (riot shields) fold out for advancing officers. Minigrenade launcher for gas ahead. If shot hits from rear flank while shields deployed: Armor halved.
### Ares Mule
- Size: Large
- Src: R5 p.141-143
- Skill: Pilot Walker
- Handl: 4 | Speed: 1G | Accel: 1
- Body: 4(3) | Armor: 6 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 4 | Cost: 8,000¥
- Std upgrades/downgrades: Drone arm (STR 6, AGI 2)
- Rules: Four-legged cargo hauler (~marching soldier speed); carries squad supplies. Head/neck grip like primitive cyberarm.
### Ares Paladin
- Size: Large
- Src: R5 p.142-143
- Skill: Pilot Ground Craft
- Handl: 5 | Speed: 4G | Accel: 1
- Body: 5(0) | Armor: 18 | Pilot: 3 | Sensor: 2 | Seats: -
- Avail: 8R | Cost: 5,000¥
- Std upgrades/downgrades: Tracked platform
- Rules: Hydraulic arms lift plasteel/Kevlar plate to intercept rounds when networked sensors detect shot. GAME: In network, on shot within detection range of any networked device: Perception test; hits = extra Armor for protected VIP that Initiative Pass; then plate = Good Cover (Core p.190) while VIP uses Take Cover. Solo: no Armor bonus on shot; only Good Cover.
### CrashCart "MediCart"
- Size: Large
- Src: R5 p.142-144
- Skill: Pilot Ground Craft
- Handl: 5 | Speed: 5G | Accel: 1
- Body: 6(2) | Armor: 5 | Pilot: 4 | Sensor: 4 | Seats: -
- Avail: 6 | Cost: 10,000¥
- Std upgrades/downgrades: Tracked; hydraulic rescue tools; medkit
- Rules: Disaster-recovery. Arms lift up to 200 kg. GAME: Acts needing STR+Body use 3× Body (carry 270 kg without test). Deploys medkit within 2 m; Pilot replaces medkit Rating; 20 uses; cannot use medkit without drone; refill with normal replacement components.
### GTS Tower
- Size: Large
- Src: R5 p.143-144
- Skill: Pilot Aircraft
- Handl: 2 | Speed: 1P | Accel: 1
- Body: 4(0) | Armor: 6 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 8 | Cost: 10,000¥
- Std upgrades/downgrades: Drone rack (4)
- Similar models: Cyberspace Designs Nexus; GN-Nissan Beehive
- Rules: LtA retrans + airbase for up to 4 minidrones or 8 microdrones.
### Saeder-Krupp Mk-17D Neptune
- Size: Large
- Src: R5 p.143-144
- Skill: Pilot Watercraft
- Handl: 2 | Speed: 3W | Accel: 1
- Body: 5(0) | Armor: 3 | Pilot: 4 | Sensor: 3 | Seats: -
- Avail: 10R | Cost: 17,500¥
- Std upgrades/downgrades: Submersible; Searchlight
- Similar models: Proteus Tiefaucher; Shiawase Suredo
- Rules: Fits standard torpedo tube. Fully submersible to 1 km. Advanced Pilot for autonomous deep ops (radio hard underwater); surfaces at designated times/places for data transfer.
### Mitsuhama Malakim
- Size: Large
- Src: R5 p.143-144
- Skill: Pilot Aircraft
- Handl: 3 | Speed: 6P | Accel: 2
- Body: 4(0) | Armor: 9 | Pilot: 4 | Sensor: 4 | Seats: -
- Avail: 20F | Cost: 40,000¥
- Std upgrades/downgrades: Standard weapon mount; area jammer (6); directional jammer (6); Targeting (4)
- Rules: GOD response quad-copter; non-lethal focus + jamming; works with Dove spotters.
## HUGE DRONES
### Ares KN-Y0 Phobos (Y1)
- Size: Huge
- Src: R5 p.143-145; table p.189
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 2G | Accel: 1
- Body: 6(0) | Armor: 18 | Pilot: 5 | Sensor: 3 | Seats: -
- Avail: 16F | Cost: 250,000¥
- Std upgrades/downgrades: Targeting (5); Smartsoft; heavy weapon mount; RPK HMG + 200 rounds
- Rules: Unmanned micro-tank anti-infantry turret variant. Intended to deploy with Deimos/Eris.
### Ares KN-Y0 Deimos (Y2)
- Size: Huge
- Src: R5 p.143-145; table p.189
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 2G | Accel: 1
- Body: 6(0) | Armor: 18 | Pilot: 5 | Sensor: 3 | Seats: -
- Avail: 20F | Cost: 220,000¥
- Std upgrades/downgrades: Targeting (5); Smartsoft; heavy weapon mount; Panther XXL assault cannon + 15 rounds
- Rules: Anti-armor KN-Y0 variant.
### Ares KN-Y0 Eris (Y4)
- Size: Huge
- Src: R5 p.143-145; table p.189
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 2G | Accel: 1
- Body: 6(0) | Armor: 18 | Pilot: 5 | Sensor: 3 | Seats: -
- Avail: 24F | Cost: 270,000¥
- Std upgrades/downgrades: Targeting (5); Smartsoft; large weapon mount; Antioch MGL-12 with clip-switch among up to 24 grenades; area jammer (6); directional jammer (6); Electronic Warfare (5)
- Rules: Grenade/C3-inhibition KN-Y0 variant. No Y3 listed.
### Mesametric Kodiak
- Size: Huge
- Src: R5 p.145-146
- Skill: Pilot Ground Craft
- Handl: 2/4 | Speed: 2G | Accel: 1
- Body: 6(2) | Armor: 12 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 12R | Cost: 40,000¥
- Std upgrades/downgrades: Drone arm (STR 12, AGI 2); bulldozer blade; Road Engineering (2) autosoft
- Rules: Road work / clear / construct / destroy. Industrial variants exist (timber, powerline, etc.).
### NeoNET Avenging Angel
- Size: Huge
- Src: R5 p.145-146
- Skill: Pilot Aircraft
- Handl: 3 | Speed: 6J | Accel: 2
- Body: 6(0) | Armor: 12 | Pilot: 6 | Sensor: 6 | Seats: -
- Avail: 40F | Cost: 1,000,000¥
- Std upgrades/downgrades: Heavy weapon mount (single fuel-air bomb payload)
- Rules: Multi-MACH milspec GOD strike drone; city-block fuel-air bomb. Officially never used.
## ANTHROPOMORPHIC DRONES
### Aztechnology Criado Juan
- Size: Anthro
- Src: R5 p.145-147
- Skill: Pilot Walker (anthro)
- Handl: 2 | Speed: 2G | Accel: 1
- Body: 2 | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 2 | Cost: 8,000¥
- Std upgrades/downgrades: Full anthro limb set (see Anthro rules)
- Similar models: Renraku Manservant; Telestrian Industries Jeeves
- Rules: Budget house-bot. Domestic cleaning baseline; specialty autosofts expensive.
### Horizon Little Buddy
- Size: Anthro
- Src: R5 p.146-147
- Skill: Pilot Walker (anthro)
- Handl: 2 | Speed: 1G | Accel: 1
- Body: 1 | Armor: 0 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 4 | Cost: 2,000¥
- Std upgrades/downgrades: Instruction (2) autosoft
- Similar models: Hasbro Playsalot; Sony Headstart
- Rules: Child-sized nanny/teacher/playmate. Contacts parents on unprogrammed situations / wounded or missing child. Optional First Aid autosofts marketed.
### MCT Kenchiku-Kikai
- Size: Anthro
- Src: R5 p.146-148
- Skill: Pilot Walker (anthro)
- Handl: 2 | Speed: 2G | Accel: 1
- Body: 5 | Armor: 3 | Pilot: 2 | Sensor: 2 | Seats: -
- Avail: 8R | Cost: 20,000¥
- Std upgrades/downgrades: Industrial Mechanic (2) autosoft; limbs enhanced to Strength 8
- Similar models: S-K Colossus; Ares JHI-65
- Rules: Ork-sized construction anthro; uses metahuman tools. Many pre-wireless units still in field.
### NeoNET Juggernaught
- Size: Anthro
- Src: R5 p.147-148
- Skill: Pilot Walker (anthro)
- Handl: 3 | Speed: 4G | Accel: 1
- Body: 6 | Armor: 12 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 14R | Cost: 100,000¥
- Std upgrades/downgrades: One standard weapon mount per arm; two one-use grenade drops; anti-riot / point-blank gas dispensers (as marketed)
- Rules: Largest two-legged mecha on market (~head taller than average troll). Articulated hands for tools/restraint. Heavy, clumsy; floors/stairs risk.
### Saeder-Krupp Direktionssekretar
- Size: Anthro
- Src: R5 p.148-149
- Skill: Pilot Walker (anthro)
- Handl: 4 | Speed: 4G | Accel: 2
- Body: 4 | Armor: 3 | Pilot: 4 | Sensor: 4 | Seats: -
- Avail: 12R | Cost: 40,000¥
- Std upgrades/downgrades: Advanced knowbot Pilot; subtle armored core; fully articulated hands
- Similar models: Sony Orderly-4; Ares Pygmalion
- Rules: Executive secretary anthro: datapush, finances, books, clean, file, notes; capable security/unarmed lethality. Highly customizable appearance.
### Shiawase i-Doll
- Size: Anthro
- Src: R5 p.148-149
- Skill: Pilot Walker (anthro)
- Handl: 3 | Speed: 3G | Accel: 1
- Body: 3 | Armor: 0 | Pilot: 3 | Sensor: 3 | Seats: -
- Avail: 4 | Cost: 20,000¥
- Std upgrades/downgrades: Realistic Features (1); Cooking (3) autosoft
- Similar models: Renraku Nadeshiko; Spinrad OoLaLa
- Rules: Customizable domestic servant. Higher realism classes (2-4) cost more (Class 4 most lifelike). Only expensive models approach human pass.
## DRONE MISSILES
### Ares "Garuda"
- Size: Missile
- Src: R5 p.149-150
- Skill: Pilot Aircraft
- Handl: 6 | Speed: 3J/6J | Accel: 2/4
- Body: 2 | Armor: 2 | Pilot: 4 | Sensor: 3 | Seats: -
- Avail: 20F | Cost: 8,500¥
- Std upgrades/downgrades: Launched; cluster munitions; laser guidance
- Rules: Rigged cluster-munition missile drone. Dual mode: cruise like drone then booster (Speed/Accel second values). Cluster munitions = multiple small explosives; warhead stats from Core Grenades/Rockets/Missiles p.435 (anti-vehicle, fragmentation, or HE). Explosive costs NOT included. Shoulder-launchable or from mounted launcher. No underwater (needs oxygen). Cluster design lets rigger fire submunitions and keep moving to avoid dumpshock vs older single-warhead rigged missiles.
## CHASSIS PACKS (Mitsuhama Seven)
### Mitsuhama Seven Wheelie
- Size: Chassis
- Src: R5 p.135; table p.191
- Skill: Pilot Ground Craft
- Handl: 4/2 | Speed: 2G | Accel: 1
- Body: 1(3) | Armor: 0 | Pilot: 1 | Sensor: 1 | Seats: -
- Avail: - | Cost: 2,000¥
- Std upgrades/downgrades: Fragile (1)
- Rules: Core wheeled Seven chassis (nickname Wheelie).
### Mitsuhama Seven Treads
- Size: Chassis
- Src: R5 p.135; table p.191
- Skill: Pilot Ground Craft
- Handl: 3 | Speed: 2G | Accel: 1
- Body: 1(3) | Armor: 0 | Pilot: 1 | Sensor: 1 | Seats: -
- Avail: 2 | Cost: 2,000¥
- Std upgrades/downgrades: Fragile (1)
- Rules: Tracked Seven chassis.
### Mitsuhama Seven Dirty
- Size: Chassis
- Src: R5 p.135; table p.191
- Skill: Pilot Ground Craft
- Handl: 2/4 | Speed: 2G | Accel: 1
- Body: 1(3) | Armor: 0 | Pilot: 1 | Sensor: 1 | Seats: -
- Avail: 2 | Cost: 2,000¥
- Std upgrades/downgrades: Fragile (1)
- Rules: Off-road suspension Seven chassis.
### Mitsuhama Seven Quad
- Size: Chassis
- Src: R5 p.135; table p.191
- Skill: Pilot Walker
- Handl: 4 | Speed: 1G | Accel: 1
- Body: 1(3) | Armor: 0 | Pilot: 1 | Sensor: 1 | Seats: -
- Avail: 4 | Cost: 2,000¥
- Std upgrades/downgrades: Fragile (1)
- Rules: Four-legged Seven chassis.
### Mitsuhama Seven Swims
- Size: Chassis
- Src: R5 p.135; table p.191
- Skill: Pilot Watercraft
- Handl: 3 | Speed: 2W | Accel: 1
- Body: 1(3) | Armor: 0 | Pilot: 1 | Sensor: 1 | Seats: -
- Avail: 4 | Cost: 1,000¥
- Std upgrades/downgrades: Fragile (1)
- Rules: Surface-aquatic Seven chassis.
### Mitsuhama Seven Hovers
- Size: Chassis
- Src: R5 p.135; table p.191
- Skill: Pilot Aircraft
- Handl: 4 | Speed: 1P | Accel: 1
- Body: 1(3) | Armor: 0 | Pilot: 1 | Sensor: 1 | Seats: -
- Avail: 6 | Cost: 4,000¥
- Std upgrades/downgrades: Fragile (1)
- Rules: Quad-copter Seven chassis.
### Mitsuhama Seven Soars
- Size: Chassis
- Src: R5 p.135; table p.191
- Skill: Pilot Aircraft
- Handl: 3 | Speed: 2J | Accel: 1
- Body: 1(3) | Armor: 0 | Pilot: 1 | Sensor: 1 | Seats: -
- Avail: 8 | Cost: 4,000¥
- Std upgrades/downgrades: Fragile (1)
- Rules: Traditional flyer Seven chassis.
## Bullets & Bandages / Hard Targets / Cutting Aces / Howling Shadows drones

### Aeroquip M.E.D.-1 "Dustoff"
- Size: Large
- Src: B&B (also pointed from R5 p.141). **Verified from** `Shadowrun_5E_Bullets_&_Bandages.pdf`.
- Skill: Pilot Aircraft (VTOL)
- Handl: 3 | Speed: 4 | Accel: 4
- Body: 4 | Armor: 5 | Pilot: 4 | Sensor: 3 | Seats: patient bay (Valkyrie)
- Avail: 10R | Cost: 12,000¥
- Std: Armoured patient compartment; Improved Takeoff and Landing 2; Rigger Adaptation; Valkyrie module
- Rules: VTOL medevac; large profile = easy target on takeoff/landing.

### Shiawase Caduceus "CAD" 7
- Size: Medium anthroform autodoc
- Src: B&B
- Handl: 4 | Speed: 2 | Accel: 1 | Body: 5 | Armor: 3 | Pilot: 2 | Sensor: 1
- Avail: 12R | Cost: 16,500¥
- Rules: R4 autodoc; 2× Snake Finger arms; Medkit 4 built-in; walker.

### Hard Targets drones
| Name | Size | Hand | Accel | Speed | Pilot | Bod | Arm | Sens | Avail | Cost | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ammo Drone | Small | 2 | 2 | 2 | 3 | 2 | 4 | 2 | 5 | 3,000¥ | Holds 6 pistol / 4 SMG+ / 1 drum clips. Autosoft Handling 2. |
| Reloading Drone | Medium | 4 | 2 | 3 | 3 | 3 | 4 | 2 | 6R | 4,500¥ | Armorer autosoft; forbidden soft 250¥. |
| Sparring Drone | Large | 3 | 2 | 2 | 3 | 4 | 2 | Special | 3 | 5,000¥ | Immune unarmed P; Tutor Blades/Clubs/Unarmed 1. |
| MCT Akiyama | Medium anthro | 5 | 2 | 3 | 3 | 4 | 6 | 3 | 24F | 200,000¥ | Ruthenium −6 Perception; gecko +4 climb; STR=Body melee; Cap 8/arm cyberweapons; ≤SMG firearms. |

### Cutting Aces drones
| Name | Size | Hand | Speed | Accel | Bod | Arm | Pil | Sens | Avail | Cost | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Holo-Conference | Small | 3 | 2 | 1 | 2 | 3 | 3 | 3 | 11 | 18,000¥ | Fake holo conference participant; Perception (2) spots fake. |
| Medusa Extensions | Mini | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 7 | 600¥ | Trode tendril wearable. |
| Microweave Spider | Mini | 4 | 1 | 1 | 1 | 0 | 4 | 2 | 11 | 18,000¥ | R4 Armorer autosoft; repairs clothing/armor. |

### Howling Shadows biodrones (packages)
| Name | Avail | Cost | Notes |
| --- | --- | --- | --- |
| SkySpy (crow-based) | 16R | 30,000¥ | Aerial recon; CAST/orientation goad package. |
| Roachdrone | 14R | 25,000¥ | Tiny stealth crawler with CAST. |
| Junkyard Dog | 20F | 225,000¥ | Guard biodrone; Armor 2 (12 w/ armor). |
| Cybertooth Tiger | 25F | 600,000¥ | Stirrup-controlled combat predator; Armor 0 (10 w/ armor). |

Full biodrone attribute/skill blocks: `Source Texts/Howling Shadows/`. Critter Body Armor 50¥/Armor point Avail 6; Critter Earphones/Goggles R1–6 Avail 3 / R×50¥; Sensor Collar Avail 2 / 200¥; Training Kit Avail 1 / 250¥ → Tools Kits and Survival / this file notes.

### Street Lethal — Battle Buddy (*BASES* power armor)

Companion drone for Prometheus **BASES** power armor (not sold separately in condensed extract).

| Drone | Hand | Speed | Accel | Body | Armor | Pilot | Sens | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle Buddy | 1 | 1 | 1 | 5 | 5 | 2 | 1 | Recharge BASES 1 hour per charge; drone rack on BASES |

**Verified from:** `Street Lethal Condensed.md` (Military and Future Weapons / CorpSec).

## Inventory checklist
Total SKUs in this file: Core 11 + R5 catalog + B&B Dustoff/CAD-7 + HT ×4 + CA ×3 + HS biodrones ×4 + **SL Battle Buddy**.

Core Street Gear drones (11): Kanmushi, Microskimmer, Flying Eye, Fly-Spy, Crawler, Optic-X2, Duelist, Doberman, Roto-Drone, Dalmatian, Steel Lynx.

R5 catalog: NoizQuito, Goldfish, Condor, Hedgehog, Dragonfly, Pigeon 2.0, CU^3, Gerbil, Scuttler, Sentry V, Mercury, Smoke Generator, Wolfhound, Proletarian, Ferret RPD-5X, Sewer Snake, Mini-Zep, KE P5, Castle Guard, Gun Turret, Seven (+7 chassis), Prairie Dog, Sundowner, Krake (+micro-torpedo ammo table), Bloodhound, Dove, Jardinero, Job-a-Mat, Pelican, Shamus, Cheetah, Krokodil, Kull, Tunneler, LEBD-2, Steed, Dustoff (B&B, verified), CAD-7 (B&B), Matilda, Mule, Paladin, MediCart, Tower, Neptune, Malakim, KN-Y0 Phobos/Deimos/Eris, Kodiak, Avenging Angel, Criado Juan, Little Buddy, Kenchiku-Kikai, Juggernaught, Direktionssekretar, i-Doll, Garuda.

R5 compiled-table coverage: every named drone row on pp.189-191 is present (Dustoff absent from that table by design; Mercury has no separate row).
