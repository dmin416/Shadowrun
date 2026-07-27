# -*- coding: utf-8 -*-
out = r"c:\Users\admin\Desktop\Shadowrun\Encyclopedia\Vehicle and Drone Modifications.md"

parts = []

def A(s=""):
    parts.append(s)

A("# Vehicle and Drone Modifications")
A()
A("Agent reference (SR5). LLM layout; full mechanical detail; no flavor.")
A()
A("**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `rigger5.pdf`")
A("**Books:** Core · R5")
A("**Printed:** Core Street Gear vehicles/drones ~PDF 466 (print ~461); R5 Drone Modification ~PDF 123-128 (print ~122-127); R5 Building the Perfect Beast ~PDF 151-172 (print ~150-171)")
A("**See also:** `Encyclopedia/Vehicles.md` · `Encyclopedia/Drones.md` · `Encyclopedia/Rigger Gear.md` (Pilot Enhancement, Retrans, Satellite Link, Manual Control Override, Rigger Cocoon, Touch Sensors, Interior Cameras; pilots/autosofts) · `Encyclopedia/Medical Gear.md` (Valkyrie) · `Encyclopedia/Sensors and Optics.md` (ECM/Signature Masking cross) · `Encyclopedia/Commlinks and Electronics.md` (handheld sat link) · `Encyclopedia/Armor Modifications.md` (special armor mod bases) · `Encyclopedia/Tools Kits and Survival.md` (kits/shops/facilities)")
A()
A("**Scope:** Core vehicle mod buy lines; R5 vehicle equipment (non-slot); R5 vehicle mods (6 slot categories); R5 drone Mod Points system and drone-specific mods.")
A("**Not here:** vehicle/drone chassis SKUs; RCC/autosoft price catalog (Rigger Gear); handheld jammer as non-vehicle gear (Commlinks / Sensors).")
A()
A("## Inventory (completeness checklist)")
A()
A("**Core (4):** Rigger interface; Standard weapon mount; Heavy weapon mount; Manual operation (+per mount)")
A("**R5 Vehicle Equipment (8):** Morphing license plate; Spoof chip; Spike / Zapper / Tracking strips; Off-road / Racing / Run flat tires")
A("**R5 Power Train:** Acceleration Enhancement R1-2; Gecko Tips (Body bands); Gliding System (2 Body bands); Handling Enhancement R1-3; Improved Economy; Manual Control Override; Multifuel Engine; Off-Road Suspension; Rigger Cocoon; Removed Manual Controls; Rocket Booster; Secondary Manual Controls; Secondary Propulsion x6 (Amphib Surface/Sub, Hovercraft, Rotor, Tracked, Walker); Speed Enhancement R1-3")
A("**R5 Protection:** Anti-Theft R1-4; Armor Standard/Concealed; PPS R1-6; Personal Armor R1-10; Special Armor Modification")
A("**R5 Weapons:** Ammo Bin; Standard Drone Rack Mini/Small/Medium/Large; Landing Drone Rack Mini/Small/Medium/Large; Gun Port; Missile Defense System; Oil Slick Sprayer; Smoke Projector (+Thermal); Road Strip Ejector; Weapon Mount Size/Visibility/Flexibility/Control options")
A("**R5 Weapons rules-only (no buy row in print tables):** Ram Plate; Micro drone rack (text size only)")
A("**R5 Body:** Assembly/Disassembly; Chameleon Coating; Extra Entry/Exit Points; Extreme Environment; Increased Seating; Life Support L1-2; Mechanical Arm Basic/Articulated; Nanomaintenance R1-4; Realistic Features R1-4; Smuggling Compartment; Shielding (on compartment); Special Equipment (GM); Valkyrie Module; Winch Basic/Enhanced; Workshop")
A("**R5 Body rules-only (no buy row):** Ejection Seats")
A("**R5 Electromagnetic:** EM Shielding; ECM R1-6; Gridlink; Gridlink Override; Pilot Enhancement R1-6; Retrans Unit; Satellite Link; Sensor Enhancement R1-6; Signature Masking R1-6; SunCell; Touch Sensors")
A("**R5 Cosmetic (0 slots):** Amenities Squatter/Middle/High/Luxury; Enhanced Image Screens; Metahuman Adjustment; Rigger Interface; Interior Cameras; Searchlight; Vehicle Tag Eraser; Yerzed Out R1-4")
A("**R5 Drone mods:** Attribute up/down formulas; Weapon Mounts Micro-Heavy; Pop-out (blow-away / pop-up); Expanded Ammo Bay; Belt-feed; Realistic Features R1-4; Amphibious R1-2; Assembly Time Improvement; Customized; Drone Arm (+Primitive); Drone Leg; Gecko Grips; Immobile; SkyGuide; Spotlight; Suspension Mod; Tire Mod. Pilots/autosofts/tweaks -> Rigger Gear.")
A("**R5 Core vehicle Standard Upgrades sidebar:** listed under Common rules (does not consume slots)")
A()
A("---")
A()
A("## Schema")
A()
A("| Col | Meaning |")
A("| --- | --- |")
A("| Src | Core / R5 |")
A("| Cat | Equipment (no slots) / Power / Protection / Weapons / Body / Electromagnetic / Cosmetic / Drone |")
A("|Slots| Modification slots in that category, or Mod Points (drone), or `-` |")
A("| Thresh | Install Extended Test threshold (Mechanic + Logic [Logic], 1 hour); drone often Kit/Shop note instead |")
A("| Tools | Kit / Shop / Facility |")
A("| Skill | Special Skill + Logic [Logic] (4) after Mechanic install if listed; else `-` |")
A("| Avail / Cost | Street Availability / nuyen (formulas use **unmodified** base vehicle attrs; Handling uses **higher** of on/off-road) |")
A("| Rules | Full mechanical effect |")
A()
A("---")
A()
A("## Common rules")
A()
A("### Install procedure (R5 Building the Perfect Beast ~p.151)")
A()
A("- Need: parts (+ optional plan), tools, skill.")
A("- Parts threshold = listed Threshold (GM may modify). Plan optional; if present, Build/Repair bonus (Core p.146).")
A("- Install: relevant **Mechanic** skill (Automotive, Nautical, etc.) + Logic [Logic] (threshold, **1 hour**) Extended Test; Build/Repair modifiers apply.")
A("- Inadequate/missing tools: Inadequate / Unavailable modifiers (Core p.146).")
A("- One modification at a time. Critical glitch: fail; parts ruined; restart.")
A("- If Special Skill listed: after Mechanic hits, also (Special Skill) + Logic [Logic] (4).")
A("- Remove: same tools/skills; threshold **halved**. Parts generally not reusable on other vehicles (GM: may reinstall on same).")
A("- Unless stated, each modification **once** per vehicle.")
A()
A("### Modification slots (vehicles; R5)")
A()
A("- Six categories: **Power Train, Protection, Weapons, Body, Electromagnetic, Cosmetic**.")
A("- Slots per category = vehicle **Body** (e.g. Body 16 Bulldog = 16 slots in *each* category).")
A("- Mods consume slots only in their category. Cannot exceed slots in a category.")
A("- **Cosmetic** listed mods take **0** slots (still install rows).")
A("- Factory **Standard Upgrades** (vehicle/drone Std Equip) do **not** consume slots and are already in printed stats.")
A()
A("### Cost math (R5)")
A()
A("- When Cost uses Speed, Acceleration, Body, etc.: use **base unmodified** attribute.")
A("- Handling formulas: use the **higher** of on-road / off-road.")
A("- Secondary propulsion mode H/S/A **cannot** be improved.")
A()
A("### Core vs R5 weapon mounts")
A()
A("- **Core:** mounts = unaugmented Body / 3 (round down). Standard = assault rifle or smaller + 250 rounds; Heavy = costs 2 mounts, any weapon + 500 belt or Body rockets/missiles. Remote; 90 deg H/V. Manual +cost, vehicles only (not drones). Buy table below.")
A("- **R5:** Weapons-category slot builds (Size + Visibility + Flexibility + Control). Sum Slots/Threshold/Avail/Cost; Tools = highest among options. Prefer R5 when using Perfect Beast. Core Body/3 remains the Core Street Gear limit if not using R5 slot system.")
A()
A("### Drone Mod Points (R5 ~p.122-123; optional vs vehicle slot system)")
A()
A("- Mod Points = Body. `Body X(Y)`: X = Body, Y = free Mod Points after factory gear.")
A("- First +1 to any attribute (or +3 Armor) free (0 MP). Further raises cost MP = (increase - 1). Body never raised.")
A("- Cap: attributes <= 2x starting (use 0.5 if starting 0 for math).")
A("- Downgrade: worsen one attribute by 1 (or Armor by 3) for +1 MP; cannot go below 1 except Speed to 0; **only one** extra MP from all downgrades combined.")
A("- Body downgrade special: -1 Body -> +2 MP (net +1); Body not below half starting.")
A("- +1 attribute: toolkit; more extensive: shop.")
A("- Players may instead use full vehicle slot system on drones (R5 option).")
A()
A("### Secondary propulsion modes (R5)")
A()
A("When switched to secondary mode, use these H/S/A instead of primary (cannot improve):")
A()
A("| Mode | Handling | Speed | Accel |")
A("| --- | --- | --- | --- |")
A("| Amphibious (Surface) | 2 | 2 | 1 |")
A("| Amphibious (Submersible) | 2 | 2 | 2 |")
A("| Hovercraft | 2/2 | 3 | 2 |")
A("| Rotor | 2 | 3 | 2 |")
A("| Tracked | 2/4 | 2 | 1 |")
A("| Walker | 5 | 1 | 1 |")
A()
A("### Core vehicle Standard Upgrades (R5 sidebar ~p.155; no slot cost)")
A()
A("| Vehicle/drone | Standard upgrades |")
A("| --- | --- |")
A("| Dodge Scoot | Improved economy |")
A("| Harley-Davidson Scorpion | Metahuman adjustment (troll) |")
A("| Yamaha Growler | Off-road suspension |")
A("| Hyundai Shin-Hyung | Four extra Body Modification Slots |")
A("| Eurocar Westwind 3000 | PPS (Rating 6); Anti-theft (Rating 2) |")
A("| Mitsubishi Nightsky | Amenities (Luxury); Life support (Level 1) |")
A("| Toyota Gopher | Off-road suspension; Special equipment (open box storage) |")
A("| GMC Bulldog | Four extra Body Modification Slots |")
A("| Yongkang Gala Trinity | Assembly/disassembly; Smuggling compartment |")
A("| Morgan Cutlass | Two heavy weapon mounts (external, turret, armored manual) |")
A("| Proteus Lamprey | Standard drone rack (medium) |")
A("| Artemis Nightwing | Signature masking (Rating 4) |")
A("| R-F Fokker Tundra-9 | Alternate propulsion: amphibious (surface) |")
A("| Nissan Hound | Two standard weapon mounts (external, flexible, remote) |")
A("| Northrup Wasp | Heavy weapon mount (external, flexible, remote) |")
A("| GMC Banshee | Rigger cocoon; ECM 4 |")
A("| Shiawase Kanmushi | Gecko tips |")
A("| MCT Fly-Spy | Realistic features (Rating 2) |")
A("| Lockheed Optic-X2 | Signature masking (Rating 3) (explains Core p.466 penalty; does not stack extra) |")
A("| Ares Duelist | Two light weapon mounts (external, flexible, remote); Realistic features (Rating 1) |")
A("| GM-Nissan Doberman | Standard weapon mount (external, flexible, remote) |")
A("| MCT-Nissan Roto-Drone | Three extra Weapon Modification Slots |")
A("| Steel Lynx | Heavy weapon mount (external, turret, remote) |")
A()
A("---")
A()
A("## Core buy lines")
A()
A("| Name | Src | Cat | Avail | Cost | Rules |")
A("| --- | --- | --- | --- | --- | --- |")
A("| Rigger interface | Core | Cosmetic equiv. | 4 | 1,000Y | Jump in via control rig (fiber or wireless). Drones include by default. R5 cosmetic install row matches. Being the Machine Core p.265. |".replace("Y", "\u00a5"))
# Use yen symbol via escape in later rows - actually use ¥ directly in UTF-8 file

# Rewrite Core section with proper yen
parts[-1] = "| Name | Src | Cat | Avail | Cost | Rules |"
# wait, I already appended header then a broken row. Fix by rebuilding core from here more carefully.

# Remove the last two lines (header duplicate mess) - actually last is replace result and before that header
# Simpler: write whole file cleanly in one go without the mistake.

text_body = r'''# Vehicle and Drone Modifications

Agent reference (SR5). LLM layout; full mechanical detail; no flavor.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `rigger5.pdf`
**Books:** Core · R5
**Printed:** Core Street Gear vehicles/drones ~PDF 466 (print ~461); R5 Drone Modification ~PDF 123-128 (print ~122-127); R5 Building the Perfect Beast ~PDF 151-172 (print ~150-171)
**See also:** `Encyclopedia/Vehicles.md` · `Encyclopedia/Drones.md` · `Encyclopedia/Rigger Gear.md` (Pilot Enhancement, Retrans, Satellite Link, Manual Control Override, Rigger Cocoon, Touch Sensors, Interior Cameras; pilots/autosofts) · `Encyclopedia/Medical Gear.md` (Valkyrie) · `Encyclopedia/Sensors and Optics.md` (ECM/Signature Masking cross) · `Encyclopedia/Commlinks and Electronics.md` (handheld sat link) · `Encyclopedia/Armor Modifications.md` (special armor mod bases) · `Encyclopedia/Tools Kits and Survival.md` (kits/shops/facilities)

**Scope:** Core vehicle mod buy lines; R5 vehicle equipment (non-slot); R5 vehicle mods (6 slot categories); R5 drone Mod Points system and drone-specific mods.
**Not here:** vehicle/drone chassis SKUs; RCC/autosoft price catalog (Rigger Gear); handheld jammer as non-vehicle gear (Commlinks / Sensors).

## Inventory (completeness checklist)

**Core (4):** Rigger interface; Standard weapon mount; Heavy weapon mount; Manual operation (+per mount)
**R5 Vehicle Equipment (8):** Morphing license plate; Spoof chip; Spike / Zapper / Tracking strips; Off-road / Racing / Run flat tires
**R5 Power Train:** Acceleration Enhancement R1-2; Gecko Tips (Body bands); Gliding System (2 Body bands); Handling Enhancement R1-3; Improved Economy; Manual Control Override; Multifuel Engine; Off-Road Suspension; Rigger Cocoon; Removed Manual Controls; Rocket Booster; Secondary Manual Controls; Secondary Propulsion x6 (Amphib Surface/Sub, Hovercraft, Rotor, Tracked, Walker); Speed Enhancement R1-3
**R5 Protection:** Anti-Theft R1-4; Armor Standard/Concealed; PPS R1-6; Personal Armor R1-10; Special Armor Modification
**R5 Weapons:** Ammo Bin; Standard Drone Rack Mini/Small/Medium/Large; Landing Drone Rack Mini/Small/Medium/Large; Gun Port; Missile Defense System; Oil Slick Sprayer; Smoke Projector (+Thermal); Road Strip Ejector; Weapon Mount Size/Visibility/Flexibility/Control options
**R5 Weapons rules-only (no buy row in print tables):** Ram Plate; Micro drone rack (text size only)
**R5 Body:** Assembly/Disassembly; Chameleon Coating; Extra Entry/Exit Points; Extreme Environment; Increased Seating; Life Support L1-2; Mechanical Arm Basic/Articulated; Nanomaintenance R1-4; Realistic Features R1-4; Smuggling Compartment; Shielding (on compartment); Special Equipment (GM); Valkyrie Module; Winch Basic/Enhanced; Workshop
**R5 Body rules-only (no buy row):** Ejection Seats
**R5 Electromagnetic:** EM Shielding; ECM R1-6; Gridlink; Gridlink Override; Pilot Enhancement R1-6; Retrans Unit; Satellite Link; Sensor Enhancement R1-6; Signature Masking R1-6; SunCell; Touch Sensors
**R5 Cosmetic (0 slots):** Amenities Squatter/Middle/High/Luxury; Enhanced Image Screens; Metahuman Adjustment; Rigger Interface; Interior Cameras; Searchlight; Vehicle Tag Eraser; Yerzed Out R1-4
**R5 Drone mods:** Attribute up/down formulas; Weapon Mounts Micro-Heavy; Pop-out (blow-away / pop-up); Expanded Ammo Bay; Belt-feed; Realistic Features R1-4; Amphibious R1-2; Assembly Time Improvement; Customized; Drone Arm (+Primitive); Drone Leg; Gecko Grips; Immobile; SkyGuide; Spotlight; Suspension Mod; Tire Mod. Pilots/autosofts/tweaks -> Rigger Gear.
**R5 Core vehicle Standard Upgrades sidebar:** listed under Common rules (does not consume slots)

---

## Schema

| Col | Meaning |
| --- | --- |
| Src | Core / R5 |
| Cat | Equipment (no slots) / Power / Protection / Weapons / Body / Electromagnetic / Cosmetic / Drone |
| Slots | Modification slots in that category, or Mod Points (drone), or `-` |
| Thresh | Install Extended Test threshold (Mechanic + Logic [Logic], 1 hour); drone often Kit/Shop note instead |
| Tools | Kit / Shop / Facility |
| Skill | Special Skill + Logic [Logic] (4) after Mechanic install if listed; else `-` |
| Avail / Cost | Street Availability / nuyen (formulas use **unmodified** base vehicle attrs; Handling uses **higher** of on/off-road) |
| Rules | Full mechanical effect |

---

## Common rules

### Install procedure (R5 Building the Perfect Beast ~p.151)

- Need: parts (+ optional plan), tools, skill.
- Parts threshold = listed Threshold (GM may modify). Plan optional; if present, Build/Repair bonus (Core p.146).
- Install: relevant **Mechanic** skill (Automotive, Nautical, etc.) + Logic [Logic] (threshold, **1 hour**) Extended Test; Build/Repair modifiers apply.
- Inadequate/missing tools: Inadequate / Unavailable modifiers (Core p.146).
- One modification at a time. Critical glitch: fail; parts ruined; restart.
- If Special Skill listed: after Mechanic hits, also (Special Skill) + Logic [Logic] (4).
- Remove: same tools/skills; threshold **halved**. Parts generally not reusable on other vehicles (GM: may reinstall on same).
- Unless stated, each modification **once** per vehicle.

### Modification slots (vehicles; R5)

- Six categories: **Power Train, Protection, Weapons, Body, Electromagnetic, Cosmetic**.
- Slots per category = vehicle **Body** (e.g. Body 16 Bulldog = 16 slots in *each* category).
- Mods consume slots only in their category. Cannot exceed slots in a category.
- **Cosmetic** listed mods take **0** slots (still install rows).
- Factory **Standard Upgrades** (vehicle/drone Std Equip) do **not** consume slots and are already in printed stats.

### Cost math (R5)

- When Cost uses Speed, Acceleration, Body, etc.: use **base unmodified** attribute.
- Handling formulas: use the **higher** of on-road / off-road.
- Secondary propulsion mode H/S/A **cannot** be improved.

### Core vs R5 weapon mounts

- **Core:** mounts = unaugmented Body / 3 (round down). Standard = assault rifle or smaller + 250 rounds; Heavy = costs 2 mounts, any weapon + 500 belt or Body rockets/missiles. Remote; 90 deg H/V. Manual +cost, vehicles only (not drones). Buy table below.
- **R5:** Weapons-category slot builds (Size + Visibility + Flexibility + Control). Sum Slots/Threshold/Avail/Cost; Tools = highest among options. Prefer R5 when using Perfect Beast. Core Body/3 remains the Core Street Gear limit if not using R5 slot system.

### Drone Mod Points (R5 ~p.122-123; optional vs vehicle slot system)

- Mod Points = Body. `Body X(Y)`: X = Body, Y = free Mod Points after factory gear.
- First +1 to any attribute (or +3 Armor) free (0 MP). Further raises cost MP = (increase - 1). Body never raised.
- Cap: attributes <= 2x starting (use 0.5 if starting 0 for math).
- Downgrade: worsen one attribute by 1 (or Armor by 3) for +1 MP; cannot go below 1 except Speed to 0; **only one** extra MP from all downgrades combined.
- Body downgrade special: -1 Body -> +2 MP (net +1); Body not below half starting.
- +1 attribute: toolkit; more extensive: shop.
- Players may instead use full vehicle slot system on drones (R5 option).

### Secondary propulsion modes (R5)

When switched to secondary mode, use these H/S/A instead of primary (cannot improve):

| Mode | Handling | Speed | Accel |
| --- | --- | --- | --- |
| Amphibious (Surface) | 2 | 2 | 1 |
| Amphibious (Submersible) | 2 | 2 | 2 |
| Hovercraft | 2/2 | 3 | 2 |
| Rotor | 2 | 3 | 2 |
| Tracked | 2/4 | 2 | 1 |
| Walker | 5 | 1 | 1 |

### Core vehicle Standard Upgrades (R5 sidebar ~p.155; no slot cost)

| Vehicle/drone | Standard upgrades |
| --- | --- |
| Dodge Scoot | Improved economy |
| Harley-Davidson Scorpion | Metahuman adjustment (troll) |
| Yamaha Growler | Off-road suspension |
| Hyundai Shin-Hyung | Four extra Body Modification Slots |
| Eurocar Westwind 3000 | PPS (Rating 6); Anti-theft (Rating 2) |
| Mitsubishi Nightsky | Amenities (Luxury); Life support (Level 1) |
| Toyota Gopher | Off-road suspension; Special equipment (open box storage) |
| GMC Bulldog | Four extra Body Modification Slots |
| Yongkang Gala Trinity | Assembly/disassembly; Smuggling compartment |
| Morgan Cutlass | Two heavy weapon mounts (external, turret, armored manual) |
| Proteus Lamprey | Standard drone rack (medium) |
| Artemis Nightwing | Signature masking (Rating 4) |
| R-F Fokker Tundra-9 | Alternate propulsion: amphibious (surface) |
| Nissan Hound | Two standard weapon mounts (external, flexible, remote) |
| Northrup Wasp | Heavy weapon mount (external, flexible, remote) |
| GMC Banshee | Rigger cocoon; ECM 4 |
| Shiawase Kanmushi | Gecko tips |
| MCT Fly-Spy | Realistic features (Rating 2) |
| Lockheed Optic-X2 | Signature masking (Rating 3) (explains Core p.466 penalty; does not stack extra) |
| Ares Duelist | Two light weapon mounts (external, flexible, remote); Realistic features (Rating 1) |
| GM-Nissan Doberman | Standard weapon mount (external, flexible, remote) |
| MCT-Nissan Roto-Drone | Three extra Weapon Modification Slots |
| Steel Lynx | Heavy weapon mount (external, turret, remote) |

---

## Core buy lines

| Name | Src | Cat | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Rigger interface | Core | Cosmetic equiv. | 4 | 1,000¥ | Jump in via control rig (fiber or wireless). Drones include by default. R5 cosmetic install row matches. Being the Machine Core p.265. |
| Standard weapon mount | Core | Weapons | 8F | 2,500¥ | Assault rifle or smaller + 250 rounds. Remote; 90 deg H/V. Count toward Body/3 mounts. Prefer R5 mount builder if using Perfect Beast. |
| Heavy weapon mount | Core | Weapons | 14F | 5,000¥ | Costs **2** mount slots. Any weapon + 500 belt or Body rockets/missiles. |
| Manual operation | Core | Weapons | +1 | +500¥ | Per mount; vehicles only (not drones). Mechanical firer instead of remote. |

---

## Vehicle equipment (R5; not slot mods)

Easy install/use; not significant vehicle-system integration.

| Name | Src | Cat | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Morphing license plate | R5 | Equipment | 8F | 1,000¥ | Smart materials; Complex Action reshape to any government plate form. Often paired with spoof chip. |
| Spoof chip | R5 | Equipment | 8F | 500¥ | Mimics vehicle ID broadcast; Complex Action -> new random authentic-looking ID. Install: Hardware + Logic [Logic] (2). |
| Spike strip | R5 | Equipment | 8R | 200¥ | Myomeric ~15 m (~4 lanes). Blow tires unless run flat; Vehicle Test to avoid crash; even if OK, -2 Vehicle Tests while flat. |
| Zapper strip | R5 | Equipment | 12R | 2,500¥ | On pass: 10 DV(e) to vehicle. 10 discharges then recharge. |
| Tracking strip | R5 | Equipment | 8R | 600¥ | Fires stealth tag (Core p.440) onto passing vehicle. Holds 50 stealth tags. |
| Off-road tires | R5 | Equipment | 6 | 400¥/tire | +1 off-road Handling, -1 on-road. Count as run flat. Change tires: Automotive Mechanic + Logic [Logic] (4, 5 min) Extended. |
| Racing tires | R5 | Equipment | 6 | 250¥/tire | +1 on-road Handling, -1 off-road. |
| Run flat tires | R5 | Equipment | 4 | 250¥/tire | Foam-filled; keep rolling when punctured; deteriorate if significant structure damage. |

Note: Tool kits in vehicle -> Tools Kits file (Core p.443); not a vehicle mod SKU.

---

## Power Train

| Name | Src | Cat | Slots | Thresh | Tools | Skill | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Acceleration Enhancement R1 | R5 | Power | 4 | 12 | Shop | - | 6 | Accel x 10,000¥ | +Rating to Acceleration (R1 or R2 only). |
| Acceleration Enhancement R2 | R5 | Power | 8 | 24 | Facility | - | 6 | Accel x 25,000¥ | +2 Acceleration. |
| Gecko Tips (Body 1-3) | R5 | Power | 1 | 8 | Shop | - | 6 | 1,000¥ | Climb/adhere including vertical. Body 7+: not possible. |
| Gecko Tips (Body 4-6) | R5 | Power | 4 | 16 | Shop | - | 6 | 5,000¥ | As above for mid Body. |
| Gliding System (Body <=12) | R5 | Power | 5 | 16 | Facility | - | 12R | Body x 3,000¥ | Non-flying vehicle fall: parachute + thrusters. Land: (Body/2) crash damage. Release chute wireless/manual; repack ~1 hour. |
| Gliding System (Body >12) | R5 | Power | 10 | 24 | Facility | - | 16R | Body x 4,000¥ | Heavier multi-chute/retro version; same landing damage. |
| Handling Enhancement R1 | R5 | Power | 4 | 8 | Shop | - | 6 | Handl x 2,000¥ | +Rating to Handling on- and off-road (R1-3). |
| Handling Enhancement R2 | R5 | Power | 10 | 16 | Facility | - | 8 | Handl x 5,000¥ | +2 Handling both. |
| Handling Enhancement R3 | R5 | Power | 18 | 24 | Facility | - | 10 | Handl x 12,000¥ | +3 Handling both. |
| Improved Economy | R5 | Power | 2 | 12 | Facility | - | 4 | 7,500¥ | Double operational time if within normal params (no high-speed chases). Harvests ambient power. |
| Manual Control Override | R5 | Power | 1 | 4 | Shop | - | 6 | 500¥ | Mechanical switch (Free Action, in reach): manual priority; AR/VR piloting impossible while on. |
| Multifuel Engine | R5 | Power | 4 | 20 | Shop | - | 10 | Body x 1,000¥ | Plasma furnace + engine: nearly any matter as fuel. |
| Off-Road Suspension | R5 | Power | 2 | 8 | Shop | - | 4 | Vehicle cost x 25% | +1 Handling off-road, -1 on-road. Stacks with off-road tires. |
| Rigger Cocoon | R5 | Power | 2 | 6 | Kit | - | 8 | 1,500¥ | Barrier Armor 12 / Structure 8. Occupant +6 dice vs crash/maneuver damage. Enter ~1 min; exit Complex (quick-release). O2 + biomed sensors + fire resist. |
| Removed Manual Controls | R5 | Power | 1 | 4 | Shop | - | 2 | 200¥ | No manual pilot; non-owner needs Control Device. |
| Rocket Booster | R5 | Power | 10 | 36 | Facility | - | 16F | Body x 5,000¥ | Complex Action: jump ~5 m lift / semi-trailer gap. Aircraft: half takeoff distance. Land: resist Body DV crash; Vehicle Test or crash. |
| Secondary Manual Controls | R5 | Power | 2 | 10 | Shop | - | 4 | 1,000¥ | Second full manual set; primary always priority (or switch if Manual Control Override). |
| Secondary Propulsion: Amphibious Surface | R5 | Power | 4 | 10 | Shop | - | 6 | Body x 200¥ | Float/travel on water; obvious mods. Use mode table. |
| Secondary Propulsion: Amphibious Submersible | R5 | Power | 8 | 20 | Shop | - | 12R | Body x 2,000¥ | Watertight + underwater drive + ballast. Depth ~100 m. Use mode table. |
| Secondary Propulsion: Hovercraft | R5 | Power | 8 | 16 | Shop | - | 12 | Body x 1,000¥ | Skirt; few cm hover; water OK; sluggish. Use mode table. |
| Secondary Propulsion: Rotor | R5 | Power | 10 | 24 | Facility | - | 12R | Body x 3,000¥ | Folding rotors + tail; flies poorly. Use mode table. |
| Secondary Propulsion: Tracked | R5 | Power | 6 | 14 | Shop | - | 10 | Body x 1,000¥ | Deploy tracks; rough terrain; pivot in place. Use mode table. |
| Secondary Propulsion: Walker | R5 | Power | 8 | 16 | Shop | - | 12 | Body x 2,000¥ | 4-8 retractable legs; metahuman-like pivot/stop. Use mode table. |
| Speed Enhancement R1 | R5 | Power | 5 | 8 | Shop | - | 6 | Speed x 2,000¥ | +Rating Speed (R1-3). |
| Speed Enhancement R2 | R5 | Power | 14 | 16 | Facility | - | 8 | Speed x 5,000¥ | +2 Speed. |
| Speed Enhancement R3 | R5 | Power | 20 | 24 | Facility | - | 12 | Speed x 12,000¥ | +3 Speed. |

---

## Protection

| Name | Src | Cat | Slots | Thresh | Tools | Skill | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Anti-Theft System R1 | R5 | Protection | 1 | 4 | Kit | - | 4 | 500¥ | Unauthorized intrusion: lights/sound and/or electronic alert. |
| Anti-Theft System R2 | R5 | Protection | 2 | 8 | Kit | - | 6 | 1,000¥ | + remote lockdown (cannot drive until owner release). Circumvent: deck OR Hardware + Logic [Logic] (4). |
| Anti-Theft System R3 | R5 | Protection | 4 | 12 | Shop | - | 8R | 2,500¥ | + electroshock 9S(e) OR gas with chosen toxin (Core p.409). |
| Anti-Theft System R4 | R5 | Protection | 6 | 16 | Shop | Demolitions | 12F | 5,000¥ | + remote self-destruct: vehicle to parts; blast 12P -2 AP, -2/m. |
| Armor (Standard) | R5 | Protection | Rating x 2 | Rating x 2 | Shop | Armorer | 6R | Rating x 500¥ | Obvious plating. +Armor to vehicle DR. Max added Armor = Body (cap Armor = Body + factory Armor). Choose Standard **or** Concealed for all added armor (no mix). |
| Armor (Concealed) | R5 | Protection | Rating x 3 | Rating x 3 | Shop | Armorer | 12R | Rating x 3,000¥ | Notice: Perception (4). Same Armor cap as Standard. |
| PPS (Rating 1-6) | R5 | Protection | 2 | Rating x 4 | Shop | - | 6 | Rating x 2,000¥ | Passenger Protection System: +Rating dice to passenger DR vs crashes/ramming/vehicular non-weapon damage. |
| Personal Armor (Rating 1-10) | R5 | Protection | 2 | Rating x 2 | Shop | Armorer | (Rating)R | Rating x 500¥ | +Rating armor for passengers vs attacks from **outside** the vehicle. |
| Special Armor Modification | R5 | Protection | 2 | 12 | Shop | Armorer | (As Mod) | (As Mod) x 2 | Vehicle armor mods like personal armor (Core 437-438): Chemical Protection, Fire Resistance, Insulation, Nonconductivity, Radiation Shielding, Universal Mirror Material only. Max Rating = vehicle Armor. Multiple times, different type each. |

---

## Weapons

| Name | Src | Cat | Slots | Thresh | Tools | Skill | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ammo Bin | R5 | Weapons | 1 | 4 | Shop | Armorer | 6R | 200¥ | +250 rounds for one weapon mount. Multiple OK (same or different mounts). |
| Standard Drone Rack (Mini) | R5 | Weapons | 1 | 8 | Kit | - | 4 | 500¥ | Deploy: Complex (Simple if wireless). Re-embark manual ~1 min. Holds up to Mini. |
| Standard Drone Rack (Small) | R5 | Weapons | 2 | 10 | Shop | - | 4 | 1,000¥ | Up to Small. |
| Standard Drone Rack (Medium) | R5 | Weapons | 3 | 12 | Shop | - | 6 | 2,000¥ | Up to Medium. |
| Standard Drone Rack (Large) | R5 | Weapons | 4 | 16 | Shop | - | 8 | 4,000¥ | Up to Large. |
| Landing Drone Rack (Mini) | R5 | Weapons | 2 | 10 | Shop | - | 6 | 1,000¥ | Auto re-embark Complex if drone beneath/adjacent matching speed (even while moving). |
| Landing Drone Rack (Small) | R5 | Weapons | 3 | 12 | Shop | - | 6 | 4,000¥ | As landing. |
| Landing Drone Rack (Medium) | R5 | Weapons | 4 | 14 | Facility | - | 8 | 10,000¥ | As landing. |
| Landing Drone Rack (Large) | R5 | Weapons | 5 | 20 | Facility | - | 12 | 20,000¥ | As landing. |
| Gun Port | R5 | Weapons | 1 | 4 | Kit | - | 6R | 500¥ | Fire handheld out while protected by vehicle armor. 90 deg cone; +4 RC. Multiple up to passengers. |
| Missile Defense System | R5 | Weapons | 3 | 16 | Facility | Software | 12R | 15,000¥ | Needs Sensor >=5 + FA or laser on remote turret. Seizes tied weapons vs incoming missiles/rockets. Ballistic: 20 rnds/activation, +2 Defense each; laser +4 each. |
| Oil Slick Sprayer | R5 | Weapons | 2 | 8 | Shop | - | 8F | 500¥ | Free Action. Ground pursuers Short Range: Reaction + Vehicle Skill [Handling] (2) or crash. 6 charges; refill 50¥. |
| Smoke Projector | R5 | Weapons | 2 | 8 | Shop | - | 6R | 750¥ | Free Action: Moderate Smoke Visibility (Core p.175) for vehicles up to 100 m behind. |
| Thermal Smoke (option) | R5 | Weapons | - | - | - | - | - | +100¥ | Smoke Projector with thermal smoke (Core p.435). |
| Road Strip Ejector | R5 | Weapons | 2 | 10 | Shop | - | 10F | 800¥ + strips | Free Action deploy. Holds 6 of one strip type. Refill = 6x strip cost. |
| Weapon Mount Light (Size) | R5 | Weapons | 1 | 4 | Kit | Armorer | 6F | 750¥ | Size base. Holds: Melee, Tasers, Hold-outs, Light/Heavy pistols, Machine pistols, SMGs. |
| Weapon Mount Standard (Size) | R5 | Weapons | 2 | 6 | Shop | Armorer | 8F | 1,500¥ | + Assault rifles, sniper, shotguns, exotic ranged, flamethrowers, special; also pistols/tasers/hold-outs. |
| Weapon Mount Heavy (Size) | R5 | Weapons | 4 | 10 | Shop | Armorer | 12F | 4,000¥ | + MGs, cannons, launchers, lasers (and all prior). |
| Visibility: External | R5 | Weapons | - | - | - | - | - | - | Default. Obvious on hull. |
| Visibility: Internal | R5 | Weapons | +2 | +6 | Shop | - | +2 | +1,500¥ | Hidden until deploy Simple Action; then obvious. |
| Visibility: Concealed | R5 | Weapons | +4 | +10 | Shop | - | +4 | +4,000¥ | Internal + false panels; Perception + Intuition [Intuition] (4) to find even inside. |
| Flexibility: Fixed | R5 | Weapons | - | - | - | - | - | - | Default. Aim only by turning vehicle. |
| Flexibility: Flexible | R5 | Weapons | +1 | +4 | Shop | - | +2 | +2,000¥ | 90 deg H and V. |
| Flexibility: Turret | R5 | Weapons | +2 | +12 | Facility | - | +6 | +5,000¥ | 360 deg (hull placement may constrain). |
| Control: Remote | R5 | Weapons | - | - | - | - | - | - | Default. Control Device (owner auto-succeeds). |
| Control: Manual | R5 | Weapons | +1 | +4 | Shop | - | +1 | +500¥ | Mechanical only; no remote. Operator at risk. |
| Control: Armored Manual | R5 | Weapons | +2 | +6 | Shop | - | +4 | +1,500¥ | Manual + firer +6 armor vs ranged while operating. |
| Ram Plate | R5 | Weapons | ? | ? | ? | ? | ? | ? | **Rules only; no printed buy row.** Ramming damage +1 speed category; damage to rammer unchanged. Do not invent slots/cost. |
| Micro drone rack | R5 | Weapons | ? | ? | ? | ? | ? | ? | **Text only:** holds up to 10 micro drones. No printed Standard/Landing Micro buy row (Mini+ listed). |

Weapon mount final: start from Size; add Visibility + Flexibility + Control modifiers to Slots/Thresh/Avail/Cost; Tools = highest requirement. R5 p.152 worked example (heavy / "concealed" / turret): Slots 8, Thresh 28, Avail 20, Cost 10,500¥, Facility. Adder arithmetic vs Concealed+Turret+Heavy may disagree with that example; prefer explicit option sum, note the printed example if adjudicating.

---

## Body

| Name | Src | Cat |Slots| Thresh | Tools | Skill | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Assembly/Disassembly | R5 | Body | 2 | Body x 4 (min 1) | Facility | - | 6 | 1,000¥ | Break into parts / reassemble: Mechanic + Logic [Logic] (Body, 30 min) Extended. Parts hard to ID: Perception + Intuition [Intuition] (4) + appropriate Knowledge. |
| Chameleon Coating | R5 | Body | 2 | 10 | Facility | - | 12F | Body x 1,000¥ | Display any image Free Action. Sensor-mimic cloak: if <= Walking rate, Perception to find -3. |
| Extra Entry/Exit Points | R5 | Body | 1 | 8 | Shop | - | 8 | 2,500¥ | Convenient entry/exit from any orientation/position. |
| Ejection Seats | R5 | Body | ? | ? | ? | ? | ? | ? | **Rules only; no printed buy row.** Free Action eject any seat (optional chute; direction configurable). |
| Extreme Environment Modification | R5 | Body | 2 | 12 | Shop | - | 6 | 2,000¥ | Per take: operate in one chosen environment (desert, arctic, etc.). Damaging environments still need Special Armor Mod. Does not protect occupants (use Life Support). |
| Increased Seating | R5 | Body | 2 | 6 | Shop | - | 4 | 2,000¥ | Up to +50% passenger capacity (GM final). Includes PPS integration if present. |
| Life Support Level 1 | R5 | Body | 2 | 10 | Shop | - | 8 | Body x 500¥ | Sealed leak points; filtered ventilation. Occupants +4 resist airborne drug/toxin/disease from outside. |
| Life Support Level 2 | R5 | Body | 4 | 20 | Shop | - | 12 | Body x 2,000¥ | + shut intakes; independent air (underwater/space). Counts as Chemical Seal (Core p.437). |
| Mechanical Arm (Basic) | R5 | Body | 2 | 8 | Shop | - | 4 | 1,000¥ | Reach Body x 10 cm (5 cm if Body 0). Strength Body/2 (up). Limited grasp/carry/load. |
| Mechanical Arm (Articulated) | R5 | Body | 3 | 16 | Facility | - | 6 | 5,000¥ | Fine motor; Technical Skills when jumped in (GM penalty if one arm). Melee: Melee + Agility [Accuracy] or autosoft + Pilot. |
| Nanomaintenance System (R1-4) | R5 | Body | Rating | Rating x 4 | Shop | - | (R x 5)R | Rating x 5,000¥ | Auto: roll Rating; hits = boxes repaired; 1 hour. Or assist Repair Test +Rating. Not both on same damage instance. |
| Realistic Features (R1-4) | R5 | Body | Rating | Rating x 4 | Shop | Medicine | (R x 3)R | Rating x Body x 1,000¥ | Threshold = Rating Perception to spot machine. Choose one living form. Large-animal size max (GM). Assensing sees truth instantly. |
| Smuggling Compartment | R5 | Body | 3 | 16 | Facility | - | 8F | 1,500¥ | Hidden; Perception -6 if searching thoroughly. Non-visual senses no penalty unless Shielding. ~10-20% vehicle size (GM). |
| Shielding (smuggling) | R5 | Body | n/a | 12 | Facility | - | 12F | 3,000¥ | Apply -6 to one non-visual sense type on a smuggling compartment. Multiple OK (different senses). |
| Special Equipment | R5 | Body | var | var | var | var | var | var | Catch-all (dozer, snowplow, paint, temp storage, etc.). GM sets stats/effects. |
| Valkyrie Module | R5 | Body | 4 | 6 | Shop | Hardware | 8 | 2,000¥ | Auto-stabilize (Core p.209). Rating 6 medkit + autodoc (remote OK). See Medical Gear. |
| Winch (Basic) | R5 | Body | 1 | 8 | Shop | - | 4 | 750¥ | Front/rear; ~100 m cable; up to 10 tons if vehicle can. Wireless: release hook Free. |
| Winch (Enhanced) | R5 | Body | 2 | 12 | Facility | - | 8 | 4,000¥ | Gecko/magnet attach; up to 100 tons; ground stabilizers double towing vehicle weight for lifting. Wireless activate/deactivate. |
| Workshop | R5 | Body | 6 | 20 | Facility | - | - | - (blank) | Vehicle counts as a Shop (Core p.443); choose type at install (Automotive, Armorer, etc.); immutable. Printed Avail/Cost columns blank (community lists often 0¥). |

---

## Electromagnetic

| Name | Src | Cat | Slots | Thresh | Tools | Skill | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Electromagnetic Shielding | R5 | EM | 2 | 20 | Facility | - | 6R | Body x 500¥ | Enclosed vehicles only: Faraday cage (Noise Core p.231); no wireless through hull. Optional wired pass-throughs at install. |
| ECM (Rating 1-6) | R5 | EM | 2 | 20 | Shop | Hardware | (R x 3)F | Rating x 500¥ | Area jammer (Core p.441) rules. |
| Gridlink | R5 | EM | 2 | 4 | Shop | Hardware | 4 | 750¥ | Unlimited run time on powered roads. Host has 3 marks / owner while connected; tracked; speed-limited; remote shutdown. Many vehicles have factory. |
| Gridlink Override | R5 | EM | 1 | 8 | Kit | Hardware | 8F | 1,000¥ | Appears normal but no shutdown, can exceed limit, rotates ID. Still draws grid power. |
| Pilot Enhancement R1-3 | R5 | EM | [Rating] | Rating x 3 | Kit | Hardware | R x 2 | Rating x 2,000¥ | **Replaces** Pilot (does not add). Table R1-6; text says up to 9 (conflict; table caps buy). |
| Pilot Enhancement R4-6 | R5 | EM | [Rating] | Rating x 4 | Shop | Hardware | R x 3 | Rating x 5,000¥ | As above. |
| Retrans Unit | R5 | EM | 2 | 4 | Kit | Hardware | 8 | 4,000¥ | Noise vs distance: use greater of source<->retrans or retrans<->dest instead of full path. Chains take single highest Noise. Network/PAN only; not a hack bridge. Multiple in one vehicle no benefit. |
| Satellite Link | R5 | EM | 1 | 6 | Kit | Hardware | 6 | 500¥ | As Core satellite link accessory (p.439). |
| Sensor Enhancement R1-3 | R5 | EM | [Rating] | Rating x 3 | Shop | Hardware | R x 2 | Rating x 2,000¥ | **Replaces** Sensor rating (1-6). |
| Sensor Enhancement R4-6 | R5 | EM | [Rating] | Rating x 4 | Shop | Hardware | R x 3 | Rating x 5,000¥ | As above. |
| Signature Masking (R1-6) | R5 | EM | [Rating] | Rating x 6 | Facility | - | 14F | Rating x 2,000¥ | -Rating dice to Sensor find or Active/Passive Targeting vs vehicle (plus Signature Modifiers Core p.184). |
| SunCell | R5 | EM | 2 | 16 | Shop | Hardware | 6 | Body x 500¥ | Sunny daylight: unlimited run, no other fuel. Else drains battery then normal fuel. Mixed: ~double operational time. |
| Touch Sensors | R5 | EM | 3 | 16 | Shop | Hardware | 8 | Body x 500¥ | Jumped-in: +2 Perception/Sensor; Handling +1; -2 resist Biofeedback when vehicle damaged. |

---

## Cosmetic (0 slots)

| Name | Src | Cat |Slots| Thresh | Tools | Skill | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Amenities (Squatter) | R5 | Cosmetic | - | 6 | Shop | - | - | 100¥ | Downgrade from Low default; auto-gains Increased Seating effects. Lifestyle-equivalent for Social/Healing in vehicle. Living in vehicle still pays full lifestyle. |
| Amenities (Middle) | R5 | Cosmetic | - | 6 | Shop | - | 2 | 500¥ | Comfort fabric, basic AR entertainment. |
| Amenities (High) | R5 | Cosmetic | - | 10 | Shop | - | 8 | 1,000¥ | Fine seating, temp control, refreshments, full Matrix/non-e entertainment. |
| Amenities (Luxury) | R5 | Cosmetic | - | 20 | Shop | - | 16 | 10,000¥ | Max comfort; real food/alcohol; full entertainment. |
| Enhanced Image Screens | R5 | Cosmetic | - | 12 | Shop | - | 8 | 5,000¥ | Flat surfaces/windows display hyper-real images. Fake exterior: Perception -4 to notice false. Show PAN feeds / Matrix AROs to non-AR users. |
| Metahuman Adjustment | R5 | Cosmetic | - | 4 | Kit | - | 4 | 500¥/seat | Without: ork/elf -1 Pilot Tests; dwarf/troll -2. Pixie/centaur: GM says no. |
| Rigger Interface | R5 | Cosmetic | - | 8 | Kit | - | 4 | 1,000¥ | Same as Core. Drones default. |
| Interior Cameras | R5 | Cosmetic | - | 6 | Kit | Hardware | 6 | 2,000¥ | Perception inside vehicle even while full VR. |
| Searchlight | R5 | Cosmetic | - | 4 | Kit | - | 4 | 800¥ | Exterior light; remote or manual. Reduce darkness penalties one step (Core p.173). |
| Vehicle Tag Eraser | R5 | Cosmetic | - | 8 | Shop | Hardware | 6R | 750¥ | Tag eraser (Core p.441) powered by vehicle; activate once / 10 minutes. |
| Yerzed Out (R1-4) | R5 | Cosmetic | - | Rating x 4 | Shop | - | (R x 2) | Rating x 1,000¥ | Social +Rating where impressed by yerzing; -Rating where frowned on. Info-gather about owner +Rating (memorable). |

---

## Drone modifications (R5 ~p.122-127)

Attribute costs use **upgraded** rating in formulas below. Cap <= 2x start (0.5 if start 0).

### Attribute upgrades (buy formulas)

| Attribute | Avail | Cost | Notes |
| --- | --- | --- | --- |
| Handling | Upgraded x 2 | (Upgraded Handling x Body) x 200¥ | |
| Speed | Upgraded x 2 | ((Upgraded Speed x Body) x 2) x 200¥ | |
| Acceleration | Upgraded x 4 | (Upgraded Accel x Body) x 200¥ | |
| Body | Mod Points gained x 3 | (downgrade only) | -1 Body -> +2 MP (net +1); not below half start |
| Armor | Upgraded (R if >6, F if >12) | (Upgraded Armor x Body) x 200¥ | Armor <= 3x Body free of H/S/A penalty; then -1 H and Speed per +3 Armor; -1 Accel per +6. If H <1 or Speed/Accel <0: cannot move |
| Sensor | Upgraded x 2 | Upgraded x 1,000¥ (array); single sensor Upgraded x 100¥ | |
| Pilot | (see Rigger Gear) | (see Rigger Gear) | Software Solutions |

### Other drone mods

| Name | Src | Cat | MP | Tools | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Weapon Mount Micro | R5 | Drone | 0 | - | 8R | (weapon separate; no separate mount ¥ in print) | SS bullet or dart. All mounts >=R; weapons often illegal on drones (CAS exception for lethal). |
| Weapon Mount Mini | R5 | Drone | 1 | - | 4R | - | Hold-out, light pistol, Reach 0 melee, SS grenade. |
| Weapon Mount Small | R5 | Drone | 2 | - | 8R | - | Heavy pistol, machine pistol. |
| Weapon Mount Standard | R5 | Drone | 3 | - | 10F | - | SMG, underbarrel GL. |
| Weapon Mount Large | R5 | Drone | 4 | - | 12F | - | Shotgun, hunting/assault rifle, GL. |
| Weapon Mount Huge | R5 | Drone | 5 | - | 16F | - | Sniper, LMG/MMG. |
| Weapon Mount Heavy | R5 | Drone | 6 | - | 20F | - | HMG, rocket launcher, assault cannon. |
| Blow-away panels | R5 | Drone | 0 extra | Kit | - | 25¥ x mount MP | Perception + Intuition [Mental] (2) sees cover not contents. One-shot eject. |
| Pop-up mount | R5 | Drone | +1 MP | Shop | - | 100¥ x **increased** MP | Free Action deploy/retract. Perception (4) to detect. |
| Expanded ammo bay (2nd bin) | R5 | Drone | 1 | Kit | - | 50¥ | Second magazine-size bin + switch. Drone mounts use weapon normal ammo limits (not vehicle bins) unless upgraded. |
| Belt-feed | R5 | Drone | 2 | Shop | - | 500¥ | Belt-fed; 100-round belt space. Additional expanded bays hold another 100 each. |
| Realistic Features R1 | R5 | Drone | (see tools) | Shop (R3+ Facility) | 2 | (Body x Body) x 100¥ | Perception threshold = Rating to spot artificial. Most drones max R1. |
| Realistic Features R2 | R5 | Drone | - | Shop | 4 | (Body x Body) x 500¥ | |
| Realistic Features R3 | R5 | Drone | - | Facility | 8 | (Body x Body) x 1,000¥ | |
| Realistic Features R4 | R5 | Drone | - | Facility | 12R | (Body x Body) x 5,000¥ | |
| Amphibious R1 | R5 | Drone | 1 | Shop | - | (Body x Body) x 100¥ | Float calm surface; underbody waterproof. Still need motive system. |
| Amphibious R2 | R5 | Drone | 2 | Facility | - | (Body x Body) x 1,000¥ | Fully waterproof / submersible. |
| Assembly Time Improvement | R5 | Drone | 1 | Shop | - | Body x 100¥ | Assemble/disassemble: Body minutes; Mechanic + Logic (2). |
| Customized | R5 | Drone | 0 | Kit | - | 10-10,000¥ | Cosmetic only; no game effect. |
| Drone Arm | R5 | Drone | 1 | Shop | - | 1/2 cyberarm price; upgrades full price | Str = Body, Agi = Pilot start; may double starting limb attrs. Limb armor does not armor drone; +1 Physical CM box. Agility tests with arm use limb Agi. |
| Primitive Arm option | R5 | Drone | (with arm) | - | - | 10% of normal cyberarm (not 50%) | -2 limit on fine manip / weapon use with limb. |
| Drone Leg | R5 | Drone | (as cyberleg half) | - | - | half cyberleg | Like arms; Speed not from limb Agi; no extra CM boxes; limb armor irrelevant. |
| Gecko Grips | R5 | Drone | 1 | Shop | - | (Body x 3) x 50¥ | Climb/hang if surface Barrier >= Body x 3. |
| Immobile | R5 | Drone | +2 (gain) | Shop | - | 0¥ (day labor) | Speed/Accel 0 forever; +2 MP for no drivetrain. |
| SkyGuide | R5 | Drone | 0 | Kit | - | 5¥ + 10¥/year | Nav (6) + Maneuver (6) while logged in; Guide can override owner. Factory on flying drones from 2078. |
| Spotlight | R5 | Drone | 0 | Kit | - | 50¥ | Flashlight rules. |
| Suspension Mod | R5 | Drone | 0 | Shop | - | (Body x 3) x 100¥ | Ground: swap to Standard 4/2, Tracked 3, or Off-road 2/4 Handling base. |
| Tire Mod | R5 | Drone | 0 | Kit | - | (Body x 3) x 25¥ | Wheeled: lower Handling +1, better Handling -2 until swapped back. |

Pilots, autosofts (Clearsight, EW, Evasion, Maneuvering, Stealth, Targeting, Smartsoft, Group, Skillset), Personality, Linguistics -> `Encyclopedia/Rigger Gear.md`.

---

## Print gaps / conflicts

- **Workshop:** Avail and Cost columns blank in R5 PDF table; Slots 6 / Thresh 20 / Facility known.
- **Ejection Seats, Ram Plate:** full rules text; no buy-table row in local R5 PDF.
- **Micro drone rack:** size described; no Mini-style buy row for Micro.
- **Weapon mount example (R5 p.152):** numbers may not match Concealed+Turret+Heavy adder math; use option table.
- **Pilot Enhancement:** prose "Rating of 1 to 9"; buy table only R1-6.
- **Core vs R5 mounts:** different systems; do not double-apply Body/3 and full R5 slot costs without table ruling.

---

## Item index

Acceleration Enhancement; Amenities; Ammo Bin; Amphibious (drone / vehicle secondary); Anti-Theft System; Armor (vehicle); Assembly/Disassembly; Assembly Time Improvement; Belt-feed; Blow-away panels; Chameleon Coating; Customized; Drone Arm; Drone Leg; Drone Rack (standard/landing); ECM; Ejection Seats; Electromagnetic Shielding; Enhanced Image Screens; Expanded ammo bay; Extra Entry/Exit Points; Extreme Environment Modification; Gecko Grips; Gecko Tips; Gliding System; Gridlink; Gridlink Override; Gun Port; Handling Enhancement; Immobile; Improved Economy; Increased Seating; Interior Cameras; Life Support; Manual Control Override; Manual operation (Core); Mechanical Arm; Metahuman Adjustment; Missile Defense System; Morphing license plate; Multifuel Engine; Nanomaintenance System; Off-Road Suspension; Off-road / Racing / Run flat tires; Oil Slick Sprayer; Personal Armor; Pilot Enhancement; Pop-up mount; PPS; Ram Plate; Realistic Features; Removed Manual Controls; Retrans Unit; Rigger Cocoon; Rigger interface; Road Strip Ejector; Road strips (Spike/Zapper/Tracking); Rocket Booster; Satellite Link; Searchlight; Secondary Manual Controls; Secondary Propulsion (6); Sensor Enhancement; Shielding (smuggling); Signature Masking; SkyGuide; Smoke Projector; Smuggling Compartment; Special Armor Modification; Special Equipment; Speed Enhancement; Spoof chip; Spotlight; Standard/Heavy weapon mount (Core); SunCell; Suspension Mod; Thermal Smoke; Tire Mod; Touch Sensors; Valkyrie Module; Vehicle Tag Eraser; Weapon Mount (vehicle builder / drone sizes); Winch; Workshop; Yerzed Out.
'''

# Fix accidental header typo "Slots|" spacing and em dashes
text_body = text_body.replace("—", "-").replace("–", "-")
text_body = text_body.replace("|Slots|", "| Slots |")
text_body = text_body.replace("| Cat |Slots|", "| Cat | Slots |")

with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(text_body)

print("wrote", out, "lines", text_body.count("\n") + 1)
