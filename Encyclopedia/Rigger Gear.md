# Rigger Gear

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `rigger5.pdf` · `killcode.pdf` (specialty RCCs + personal drone rack)
**Books:** Core · R5 (INDEX). KC specialty RCCs included so the RCC catalog is complete.
**See also:** `Encyclopedia/Drones.md` · `Encyclopedia/Vehicles.md` · `Encyclopedia/Vehicle and Drone Modifications.md` (full mod slot / drone MP catalog; jumped-in essentials duplicated here) · `Encyclopedia/Cyberware.md` (Control Rig) · `Encyclopedia/Commlinks and Electronics.md` (PI-Tac, CCOB, KC RCC rows) · `Encyclopedia/Cyberdecks and Programs.md` · `Encyclopedia/Sensors and Optics.md`
**Out of scope as primary SKUs:** drone/vehicle chassis · full vehicle mod catalog (weapon mounts, ECM, armor, drone racks, etc.) · handheld jammers/commlinks · smart firing platform (Weapon Accessories). Jumped-in / RCC-network mods that are buyable SKUs are cataloged below and also belong in Vehicle and Drone Modifications.

## Schema

| Field | Meaning |
| --- | --- |
| Cat | Implant / Interface / RCC / Pilot / Autosoft / Program / VehicleMod / Mount |
| Src | Book + page |
| Rating / DP / FW | Device Rating / Data Processing / Firewall (`-` if N/A) |
| Avail / Cost | Street Availability / nuyen |
| Rules | Full mechanical notes |

## Common rules

### Jump-in prerequisites (Core p.265-266)

- Implanted Control Rig required.
- Owner or 3 marks on the device.
- Device must have Rigger Interface (built into drones; usually aftermarket on civilian vehicles).
- Jump into Rigged Device: Complex from AR; Simple if already in VR; Simple from meat if direct-cabled into vehicle/RCC.

### Control Override order (Core p.265)

Highest wins: **Rigger control > Remote control (Control Device) > Manual > Autopilot**. Once overridden, equal/lower methods cannot regain control until the Initiative Pass after the current controller relinquishes.

### Jumped-in specials (Core p.266)

- Always VR (cold-sim or hot-sim). Vehicle actions treated like Matrix actions (Matrix action bonuses apply to Vehicle Control / Gunnery / Sensor tests).
- Cold-sim: +2D6 Initiative (3D6 total); biofeedback is Stun. Hot-sim: +3D6 Initiative (4D6 total) and +1 dice to all Matrix tests (including Vehicle actions); biofeedback is Physical.
- Control Rig Rating adds to limits: Handling, Speed, Sensor, mounted weapon Accuracy.
- Wireless Noise applies unless direct cable.
- Physical damage to jumped-in vehicle: resist half (round up) as Biofeedback.
- Matrix damage hits persona device (commlink/RCC used to enter VR), or the vehicle if direct-connected without that middle device.
- Destroyed jumped-in device: dumpshock (6 DV biofeedback). Jump out via Switch Interface Mode, or Jump into another PAN device from RCC.

### RCC core functions (Core p.266-268)

- Noise Reduction + Sharing: set on boot; sum cannot exceed Device Rating; retune with Change Device Mode.
- Sharing = number of autosofts on RCC that run on all slaves at once. If a drone runs any of its own autosofts, it cannot use RCC shared autosofts.
- Data Processing: VR Initiative attribute and Command test limit. Firewall: network defense for slaves.
- Slave capacity: Device Rating x 3. Slaves may use master's attributes on defense tests. Mark on slave = mark on master. Direct connection to drone bypasses master help.
- Group command: one Simple Action (Send Message) to one/some/all slaves. Commands resolve on drone Action Phases. Contradictory same-level commands before resolve = none of them + error.
- Jump between slaved drones without jumping out first.
- On-the-fly Noise reduction: Complex Action Electronic Warfare + Logic [Data Processing]; hits = Noise reduction for rest of Combat Turn (stacks with other Noise reduction). Same action expanded as Suppress Noise in R5 (below).

### Pilots and autosofts (Core p.269; R5 p.126-128)

- Pilot = Device Rating; Matrix attributes = Pilot when relevant.
- Autosoft Rating 1-6; model/weapon specific where noted.
- Onboard slots = ceil(Pilot/2). RCC share can exceed.
- Pilot cannot native-run autosoft > Pilot Rating; RCC can share higher.

### Dumpshock / dump (Core p.268-269)

- Dumped if jumped-in vehicle destroyed/bricked, RCC/commlink destroyed/bricked while used as persona device, or cable yanked.
- Dumpshock + lose control. Piloted vehicles resume autopilot next Combat Turn start; else uncontrolled until someone takes control.

### R5 Electronic Warfare actions (R5 p.30-31; all Matrix actions)

RCC Noise Reduction rating adds as a dice pool bonus to each of these.

- **Break Target Lock** (Simple): EW + Intuition [DP] vs Logic + Sensors; each net hit reduces target's lock by 1 hit.
- **Confuse Pilot** (Complex): EW + Logic [Attack] vs Pilot + Firewall; on success, target Pilot makes Simple Pilot x 2 vs threshold = half your net hits.
- **Detect Target Lock** (Free): Computer + Logic [DP] (2); need Owner marks; device must be wireless-enabled.
- **Suppress Noise** (Complex): EW + Logic [DP]; hits = Noise reduction rest of Combat Turn (stacks); Owner marks.
- **Target Device** (Complex): EW + Logic [DP] vs Willpower + Firewall; for rest of Combat Turn, slaved Sensor/smartlink attackers get +net hits vs that device.

### Swarm program vs Swarm action

- **Swarm program** (R5 p.31, 600¥): see catalog; merges slaved drones into one multi-body unit.
- **Swarm vehicle action** (R5 p.179): jumped-in coordinator makes Vehicle Skill + Reaction [Handling] (Terrain + number of drones); net hits as Teamwork bonus to involved drones' subsequent attacks same Combat Turn (fail: penalty = miss amount). Not a gear SKU.

## Catalog

## CONTROL RIG (cyberware; jump-in core)
### Control Rig (Rating 1)
- Cat: Implant
- Src: Core p.452 / Cyberware table; Being the Machine p.265-266
- Rating: 1 | DP: - | FW: -
- Avail: 5R | Cost: 43,000¥
- Rules: Essence 1. Jump-in prerequisite. Built-in sim module + universal data connector + ~1 m retractable cable (datajack-like). +Rating dice to Vehicle skill tests when jumped in; +Rating to Handling and Speed limits; reduce Vehicle Test thresholds by Rating (min 1). Also increases Sensor / Speed / Handling / mounted weapon Accuracy limits by Rating when jumped in. Full row also in Cyberware.md.
### Control Rig (Rating 2)
- Cat: Implant
- Src: Core p.452
- Rating: 2 | DP: - | FW: -
- Avail: 10R | Cost: 97,000¥
- Rules: Essence 2. Same Control Rig rules as Rating 1 at Rating 2. Also in Cyberware.md.
### Control Rig (Rating 3)
- Cat: Implant
- Src: Core p.452
- Rating: 3 | DP: - | FW: -
- Avail: 15R | Cost: 208,000¥
- Rules: Essence 3. Same Control Rig rules as Rating 1 at Rating 3. Also in Cyberware.md.
## RIGGER INTERFACE
### Rigger Interface
- Cat: Interface
- Src: Core p.461; R5 p.171 cosmetic table + narrative
- Rating: - | DP: - | FW: -
- Avail: 4 | Cost: 1,000¥
- Rules: Install: Slots none (cosmetic), Threshold 8, Kit, Avail 4, 1,000¥. Aftermarket 'black box' + sensor/relay suite so a control-rigged rigger can jump in with full sensory experience (fiber or wireless). All drones ship with interface built-in. Military/LE vehicles often factory-equipped. Also listed under Related Vehicle Mods when tracking install slots.
## RIGGER COMMAND CONSOLES
### Scratch-Built Junk RCC
- Cat: RCC
- Src: Core p.267 Command Console Table
- Rating: 1 | DP: 3 | FW: 2
- Avail: 2R | Cost: 1,400¥
- Rules: Noise Reduction + Sharing pool = Device Rating (split on boot; Change Device Mode to retune). Slave capacity DR x 3. Commlink-like DP/FW (not hot-swappable like a deck).
### Radio Shack Remote Controller RCC
- Cat: RCC
- Src: Core p.267
- Rating: 2 | DP: 3 | FW: 3
- Avail: 6R | Cost: 8,000¥
- Rules: Standard RCC rules (Common rules).
### Essy Motors DroneMaster RCC
- Cat: RCC
- Src: Core p.267
- Rating: 3 | DP: 4 | FW: 4
- Avail: 6R | Cost: 16,000¥
- Rules: Standard RCC rules.
### CompuForce TaskMaster RCC
- Cat: RCC
- Src: Core p.267
- Rating: 4 | DP: 5 | FW: 4
- Avail: 8R | Cost: 32,000¥
- Rules: Standard RCC rules.
### Maersk Spider RCC
- Cat: RCC
- Src: Core p.267
- Rating: 4 | DP: 4 | FW: 5
- Avail: 8R | Cost: 34,000¥
- Rules: Standard RCC rules. Example Spider WAN/security spider use in Core rigger chapter.
### Maser Industrial Electronics RCC
- Cat: RCC
- Src: Core p.267
- Rating: 5 | DP: 3 | FW: 4
- Avail: 8R | Cost: 64,000¥
- Rules: Standard RCC rules. High DR, low DP.
### Vulcan Liegelord RCC
- Cat: RCC
- Src: Core p.267
- Rating: 5 | DP: 5 | FW: 6
- Avail: 10R | Cost: 66,000¥
- Rules: Standard RCC rules.
### Proteus Poseidon RCC
- Cat: RCC
- Src: Core p.267
- Rating: 5 | DP: 5 | FW: 6
- Avail: 12R | Cost: 68,000¥
- Rules: Standard RCC rules.
### Lone Star Remote Commander RCC
- Cat: RCC
- Src: Core p.267
- Rating: 6 | DP: 6 | FW: 5
- Avail: 14R | Cost: 75,000¥
- Rules: Standard RCC rules.
### MCT Drone Web RCC
- Cat: RCC
- Src: Core p.267
- Rating: 6 | DP: 7 | FW: 6
- Avail: 16R | Cost: 95,000¥
- Rules: Standard RCC rules.
### Triox UberMensch RCC
- Cat: RCC
- Src: Core p.267
- Rating: 6 | DP: 8 | FW: 7
- Avail: 18R | Cost: 140,000¥
- Rules: Standard RCC rules. Top Core table DP/FW.
### Shiawase Cyber-6 RCC
- Cat: RCC
- Src: Kill Code p.68-69 / table p.69,75; also Commlinks and Electronics.md
- Rating: 5 | DP: 5 | FW: 5
- Avail: 12R | Cost: 72,000¥
- Rules: While jumped in: all drones commanded from this console gain +2 Initiative and +1 limit on all tasks. Dumpshock from this console +4 DV. INDEX primary books are Core+R5; KC specialty included for complete RCC catalog.
### Spinrad Global Skirmisher RCC
- Cat: RCC
- Src: Kill Code p.68-69 / table p.69,75
- Rating: 4 | DP: 5 | FW: 5
- Avail: 8R | Cost: 50,000¥
- Rules: Drones commanded via Control Device from this RCC: +2 dice and +1 limit on Gunnery and Perception Tests.
## PILOT PROGRAMS
### Pilot Program (Rating 1)
- Cat: Pilot
- Src: R5 p.126-127 Pilots table; Core Pilot rules p.269
- Rating: 1 | DP: - | FW: -
- Avail: 4 | Cost: 100¥
- Rules: Device-specific dog-brain. Device Rating of vehicle/drone = Pilot. Caps max autosoft Rating runnable on the device (unless RCC shares higher). Novel/confused situations: Pilot x 2 vs GM threshold or continues prior action / waits. Adapts to specific device in ~1 week (not portable to another unit). Civilian often 1-2.
### Pilot Program (Rating 2)
- Cat: Pilot
- Src: R5 p.127
- Rating: 2 | DP: - | FW: -
- Avail: - | Cost: 400¥
- Rules: Typical civilian Pilot. Same Pilot rules.
### Pilot Program (Rating 3)
- Cat: Pilot
- Src: R5 p.127
- Rating: 3 | DP: - | FW: -
- Avail: 8R | Cost: 1,800¥
- Rules: Restricted security-grade Pilot band (3-4). Same Pilot rules.
### Pilot Program (Rating 4)
- Cat: Pilot
- Src: R5 p.127
- Rating: 4 | DP: - | FW: -
- Avail: 12R | Cost: 3,200¥
- Rules: Restricted security-grade. Same Pilot rules.
### Pilot Program (Rating 5)
- Cat: Pilot
- Src: R5 p.127
- Rating: 5 | DP: - | FW: -
- Avail: 16F | Cost: 10,000¥
- Rules: Forbidden military-grade Pilot band (5-6). Same Pilot rules.
### Pilot Program (Rating 6)
- Cat: Pilot
- Src: R5 p.127
- Rating: 6 | DP: - | FW: -
- Avail: 24F | Cost: 20,000¥
- Rules: Forbidden military-grade. Same Pilot rules.
## AUTOSOFTS AND SOFTWARE TWEAKS
### Autosoft (generic Rating 1-6)
- Cat: Autosoft
- Src: Core p.442 Software table; R5 p.127 Autosoft Prices (SR5 errata reprint)
- Rating: 1-6 | DP: - | FW: -
- Avail: Rating x 2 | Cost: Rating x 500¥
- Rules: People have skills; drones have autosofts. Model-specific where tagged [Model] or [Weapon]. Drone program slots = ceil(Device Rating / 2) for own autosofts+cyberprograms; swap = Complex Matrix Action. If slaved to RCC and running NONE of its own programs, uses RCC-shared autosofts (can exceed onboard slot limit). Pilot cannot run autosoft Rating > Pilot unless RCC shares higher. RCC Sharing rating = how many shared autosofts apply to all slaves simultaneously.
### Clearsight Autosoft
- Cat: Autosoft
- Src: Core p.269
- Rating: 1-6 | DP: - | FW: -
- Avail: as Autosoft | Cost: as Autosoft
- Rules: Acts as drone Perception skill. Autonomous perception: Pilot + Clearsight [Sensor]. Jumped-in: rigger Perception + Intuition [Sensor].
### Electronic Warfare Autosoft
- Cat: Autosoft
- Src: Core p.269
- Rating: 1-6 | DP: - | FW: -
- Avail: as Autosoft (Restricted per R5 Skillset note when Skillset form) | Cost: as Autosoft
- Rules: Exactly like the Electronic Warfare skill for the drone.
### [Model] Evasion Autosoft
- Cat: Autosoft
- Src: Core p.269
- Rating: 1-6 | DP: - | FW: -
- Avail: as Autosoft | Cost: as Autosoft
- Rules: Model-specific. Teaches autopilot to avoid Sensor locks. Useless in wrong model.
### [Model] Maneuvering Autosoft
- Cat: Autosoft
- Src: Core p.269
- Rating: 1-6 | DP: - | FW: -
- Avail: as Autosoft | Cost: as Autosoft
- Rules: Model-specific Pilot [Vehicle] equivalent for one drone/vehicle model only.
### [Model] Stealth Autosoft
- Cat: Autosoft
- Src: Core p.269-270
- Rating: 1-6 | DP: - | FW: -
- Avail: as Autosoft | Cost: as Autosoft
- Rules: Model-specific. Autonomous: Pilot + Stealth [Handling] vs Perception + Intuition [Mental]. Jumped-in: Stealth + Intuition [Handling] vs same. Often pair with silent running.
### [Weapon] Targeting Autosoft
- Cat: Autosoft
- Src: Core p.269
- Rating: 1-6 | DP: - | FW: -
- Avail: as Autosoft | Cost: as Autosoft
- Rules: Weapon-model-specific Gunnery (e.g. Ingram Smartgun Targeting only for that gun). Melee Targeting variant exists under Skillset Melee.
### Smartsoft (Restricted)
- Cat: Autosoft
- Src: R5 p.127
- Rating: counts as 3 | DP: - | FW: -
- Avail: as Rating 3 Autosoft (Restricted) | Cost: as Rating 3 Autosoft (1,500¥)
- Rules: Sensor-integrated smartlink. Counts as Rating 3 autosoft. Enables full smartgun use through vehicle/drone sensors.
### Group Autosoft
- Cat: Autosoft
- Src: R5 p.127
- Rating: counts as 2 | DP: - | FW: -
- Avail: as Rating 2 Autosoft | Cost: as Rating 2 Autosoft (1,000¥)
- Rules: Shared-signal: drones with Group answer the same command together instead of one-by-one. Counts as Rating 2 autosoft. Distinct from RCC group Send Message (RCC already commands many with one Simple Action).
### Skillset Autosoft
- Cat: Autosoft
- Src: R5 p.127
- Rating: 1-6 | DP: - | FW: -
- Avail: as Autosoft; some skills Restricted | Cost: as Autosoft
- Rules: Gives the listed skill to the drone at Rating. Allowed skills: Academic Knowledge (single); Chemistry (R); Demolitions (R); Electronic Warfare (R); First Aid; Hardware; Instruction; Language (single; real translation, not Linguistics tweak); Lockpicking (R); Mechanic (single Mechanic skill); Medicine (R); Melee (as Targeting for a specific melee weapon); Navigation; Performance (single); Professional Knowledge (single). Model-specificity still applies where relevant.
### Personality Tweak
- Cat: Autosoft
- Src: R5 p.127-128
- Rating: tweak | DP: - | FW: -
- Avail: 4 | Cost: 100¥
- Rules: Software tweak. Pilot develops unique flavor over time (playful, territorial, clumsy, calm, etc.). Can specify at purchase or allow natural development. No combat bonus.
### Linguistics Autosoft (verbal command vocab)
- Cat: Autosoft
- Src: R5 p.128
- Rating: tweak / language pack | DP: - | FW: -
- Avail: 4 | Cost: 50¥
- Rules: Not full Language Skillset. Factory: typically 2 languages (mfr + sales region). Pilot may hold Linguistics packs up to its Rating. Very limited vocabulary (come here, go there, shoot that, find McHugh's, etc.); cannot translate eavesdropped speech. For real translation use Language Skillset autosoft.
## RCC CYBERPROGRAMS AND SWARM
### Encryption (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price Software table p.442
- Rating: - | DP: - | FW: -
- Avail: - | Cost: 80¥
- Rules: Common. +1 Firewall. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Signal Scrub (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: - | Cost: 80¥
- Rules: Common. Rating 2 noise reduction. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Toolbox (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: - | Cost: 80¥
- Rules: Common. +1 Data Processing. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Virtual Machine (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: - | Cost: 80¥
- Rules: Common. Run 2 additional programs; when persona takes Matrix damage, take +1 unresisted Matrix damage box. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Armor (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: 6R | Cost: 250¥
- Rules: Hacking. +2 dice to resist Matrix damage. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Biofeedback Filter (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: 6R | Cost: 250¥
- Rules: Hacking. +2 dice to resist biofeedback damage. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Guard (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: 6R | Cost: 250¥
- Rules: Hacking. Reduce extra damage from marks by 1 DV per mark. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Shell (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: 6R | Cost: 250¥
- Rules: Hacking. +1 dice to resist Matrix and biofeedback damage; stacks with other programs. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Sneak (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: 6R | Cost: 250¥
- Rules: Hacking. +2 dice to defend against Trace User. If demiGOD converges while running, they do not get physical location (other convergence effects still apply). RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Wrapper (RCC)
- Cat: Program
- Src: Core p.269 / Matrix p.245; price p.442
- Rating: - | DP: - | FW: -
- Avail: 6R | Cost: 250¥
- Rules: Hacking (per Software table buy row). Defy Matrix iconography: Change Icon can make icons look like anything; Matrix Perception reveals true form if someone checks. RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type.
### Swarm (RCC program)
- Cat: Program
- Src: R5 p.31 Swarms + Rigging Program Cost table
- Rating: - | DP: - | FW: -
- Avail: not printed | Cost: 600¥
- Rules: RCC program. Slave drones/vehicles to one RCC running Swarm; as many as slave capacity (DR x 3) or split across several swarms under that limit. Each swarm acts as one drone with multiple bodies. Pilot = highest member Pilot or RCC Device Rating (whichever higher). Uses highest of each autosoft on any member/RCC and highest Sensor; uses lowest Handling/Speed/Acceleration among members. Action dice pool and limit bonus = (drones in swarm - 1). Combat: all fire but use one weapon's stats for the attack (scatter explosives separately); attack drones individually; losses update bonuses immediately. Distinct from Swarm vehicle action (R5 p.179 teamwork attack), which is not a buyable SKU.
## JUMPED-IN / RCC NETWORK VEHICLE MODS
### Manual Control Override
- Cat: VehicleMod
- Src: R5 p.154-155 / Power Train table p.158
- Rating: - | DP: - | FW: -
- Avail: 6 | Cost: 500¥
- Rules: Slots 1, Threshold 4, Shop, Avail 6, 500¥. Mechanical Free Action switch (usually driver's seat): while on, AR/VR piloting impossible; manual controls always take precedence. Cannot be remotely deactivated.
### Removed Manual Controls
- Cat: VehicleMod
- Src: R5 p.155 / Power Train table p.158
- Rating: - | DP: - | FW: -
- Avail: 2 | Cost: 200¥
- Rules: Slots 1, Threshold 4, Shop, Avail 2, 200¥. Strips manual controls; electronic only. Non-owner must succeed on Control Device to pilot.
### Secondary Manual Controls
- Cat: VehicleMod
- Src: R5 p.156 / Power Train table p.158
- Rating: - | DP: - | FW: -
- Avail: 4 | Cost: 1,000¥
- Rules: Slots 2, Threshold 10, Shop, Avail 4, 1,000¥. Second full manual control set; either set can pilot, primary always priority. With Manual Control Override, can require a manual switch to hand off.
### Rigger Cocoon
- Cat: VehicleMod
- Src: R5 p.155-156 / Power Train table p.158
- Rating: - | DP: - | FW: -
- Avail: 8 | Cost: 1,500¥
- Rules: Slots 2, Threshold 6, Kit, Avail 8, 1,500¥. Armored fire-resistant pod with oxygen + biomed sensors for jumped-out meat body. Enter ~1 minute; exit Complex Action (quick-release). Barrier Armor 12 / Structure 8. Occupant +6 dice vs crash/maneuver damage. (GMC Banshee ships with one.)
### Interior Cameras
- Cat: VehicleMod
- Src: R5 p.171 / Cosmetic table
- Rating: - | DP: - | FW: -
- Avail: 6 | Cost: 2,000¥
- Rules: Slots none (cosmetic), Threshold 6, Kit, Hardware, Avail 6, 2,000¥. Feed cabin into PAN so jumped-in / VR rigger can make a standard Perception Test for people/things inside the vehicle.
### Touch Sensors
- Cat: VehicleMod
- Src: R5 p.169 / Electromagnetic table
- Rating: - | DP: - | FW: -
- Avail: 8 | Cost: Body x 500¥
- Rules: Slots 3, Threshold 16, Shop, Hardware, Avail 8, Body x 500¥. Jumped-in: +2 dice Perception or Sensor Tests; vehicle Handling +1. When vehicle takes damage, jumped-in rigger -2 to resist biofeedback.
### Pilot Enhancement (Rating 1-6 buy rows; text to 9)
- Cat: VehicleMod
- Src: R5 p.167-168 / Electromagnetic table p.169
- Rating: 1-9 (replaces Pilot) | DP: - | FW: -
- Avail: see rules | Cost: see rules
- Rules: Replaces Pilot Rating (does not add). Text allows Pilot Rating 1-9. Printed install: Rating 1-3: Slots = Rating, Thresh Rating x 3, Kit, Hardware, Avail Rating x 2, Cost Rating x 2,000¥. Rating 4-6: Slots = Rating, Thresh Rating x 4, Shop, Hardware, Avail Rating x 3, Cost Rating x 5,000¥. Ratings 7-9: no separate install row printed; do not invent. Separate from buying a Pilot program (R5 Pilots table) for a device that accepts a drop-in Pilot.
### Retrans Unit
- Cat: VehicleMod
- Src: R5 p.168 / Electromagnetic table p.169
- Rating: - | DP: - | FW: -
- Avail: 8 | Cost: 4,000¥
- Rules: Slots 2, Threshold 4, Kit, Hardware, Avail 8, 4,000¥. For Noise due to physical distance on the drone/vehicle network: use greater of (source-to-retrans, retrans-to-dest) instead of full path. Network-only (not a bridge for outside hackers). Multiple units in one vehicle: no benefit; chain across vehicles: use single highest Noise hop. Serves all devices on the PAN.
### Satellite Link (vehicle)
- Cat: VehicleMod
- Src: R5 p.168 / Electromagnetic table p.169; Core sat link p.439
- Rating: - | DP: - | FW: -
- Avail: 6 | Cost: 500¥
- Rules: Slots 1, Threshold 6, Kit, Hardware, Avail 6, 500¥. Vehicle communicates as if equipped with the Core satellite link accessory.
## RELATED CARRY / MOUNT GEAR
### Personal Drone Rack
- Cat: Mount
- Src: Kill Code p.73 / table p.75; also Commlinks and Electronics.md
- Rating: - | DP: - | FW: -
- Avail: 12R | Cost: 500¥
- Rules: Mount 3 micro drones or 1 small drone. Requires 1 micro-hardpoint (CCOB / similar). Carry/deploy accessory, not a vehicle drone rack mod.
## Inventory checklist
Total entries: 56

Control Rig (3): Rating 1 / 2 / 3.

Rigger Interface (1): Core/R5 cosmetic install (Slots none, Thresh 8, Kit, Avail 4, 1,000¥).

Core RCCs (11): Scratch-Built Junk, Radio Shack Remote Controller, Essy Motors DroneMaster, CompuForce TaskMaster, Maersk Spider, Maser Industrial Electronics, Vulcan Liegelord, Proteus Poseidon, Lone Star Remote Commander, MCT Drone Web, Triox UberMensch.

KC RCCs (2): Shiawase Cyber-6, Spinrad Global Skirmisher.

Pilots (6): Rating 1-6 with R5 price table (Rating 2 Avail blank in table).

Autosofts / tweaks (12): generic price row; Clearsight; Electronic Warfare; [Model] Evasion; [Model] Maneuvering; [Model] Stealth; [Weapon] Targeting; Smartsoft; Group; Skillset; Personality; Linguistics.

RCC programs (11): Encryption, Signal Scrub, Toolbox, Virtual Machine (common 80¥); Armor, Biofeedback Filter, Guard, Shell, Sneak, Wrapper (hacking 6R / 250¥ Software table); Swarm (R5, 600¥, Avail not printed).

Jumped-in / network vehicle mods (9): Manual Control Override; Removed Manual Controls; Secondary Manual Controls; Rigger Cocoon; Interior Cameras; Touch Sensors; Pilot Enhancement; Retrans Unit; Satellite Link (vehicle).

Mount (1): Personal Drone Rack (KC).

Pointers only: full vehicle mod catalog (weapon mounts, ECM, drone racks, armor, etc.) -> Vehicle and Drone Modifications; drones -> Drones.md; PI-Tac / CCOB -> Commlinks; deck program catalog -> Cyberdecks and Programs.
