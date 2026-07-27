# -*- coding: utf-8 -*-
"""Generate Encyclopedia/Rigger Gear.md"""
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Encyclopedia\Rigger Gear.md")

def E(**kw):
    return kw

ITEMS = []

# ========== CONTROL RIG (cyberware; essential for jump-in) ==========
ITEMS += [
E(name="Control Rig (Rating 1)", cat="Implant", src="Core p.452 / Cyberware table; Being the Machine p.265-266",
  skill="n/a (implant)",
  rating="1", dp="-", fw="-", avail="5R", cost="43,000¥",
  rules="Essence 1. Jump-in prerequisite. Built-in sim module + universal data connector + ~1 m retractable cable (datajack-like). +Rating dice to Vehicle skill tests when jumped in; +Rating to Handling and Speed limits; reduce Vehicle Test thresholds by Rating (min 1). Also increases Sensor / Speed / Handling / mounted weapon Accuracy limits by Rating when jumped in. Full row also in Cyberware.md."),
E(name="Control Rig (Rating 2)", cat="Implant", src="Core p.452",
  skill="n/a (implant)",
  rating="2", dp="-", fw="-", avail="10R", cost="97,000¥",
  rules="Essence 2. Same Control Rig rules as Rating 1 at Rating 2. Also in Cyberware.md."),
E(name="Control Rig (Rating 3)", cat="Implant", src="Core p.452",
  skill="n/a (implant)",
  rating="3", dp="-", fw="-", avail="15R", cost="208,000¥",
  rules="Essence 3. Same Control Rig rules as Rating 1 at Rating 3. Also in Cyberware.md."),
]

# ========== RIGGER INTERFACE ==========
ITEMS += [
E(name="Rigger Interface", cat="Interface", src="Core p.461; R5 p.171 cosmetic table + narrative",
  skill="n/a (install: Kit)",
  rating="-", dp="-", fw="-", avail="4", cost="1,000¥",
  rules="Install: Slots none (cosmetic), Threshold 8, Kit, Avail 4, 1,000¥. Aftermarket 'black box' + sensor/relay suite so a control-rigged rigger can jump in with full sensory experience (fiber or wireless). All drones ship with interface built-in. Military/LE vehicles often factory-equipped. Also listed under Related Vehicle Mods when tracking install slots."),
]

# ========== CORE RCCs ==========
ITEMS += [
E(name="Scratch-Built Junk RCC", cat="RCC", src="Core p.267 Command Console Table",
  skill="n/a",
  rating="1", dp="3", fw="2", avail="2R", cost="1,400¥",
  rules="Noise Reduction + Sharing pool = Device Rating (split on boot; Change Device Mode to retune). Slave capacity DR x 3. Commlink-like DP/FW (not hot-swappable like a deck)."),
E(name="Radio Shack Remote Controller RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="2", dp="3", fw="3", avail="6R", cost="8,000¥",
  rules="Standard RCC rules (Common rules)."),
E(name="Essy Motors DroneMaster RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="3", dp="4", fw="4", avail="6R", cost="16,000¥",
  rules="Standard RCC rules."),
E(name="CompuForce TaskMaster RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="4", dp="5", fw="4", avail="8R", cost="32,000¥",
  rules="Standard RCC rules."),
E(name="Maersk Spider RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="4", dp="4", fw="5", avail="8R", cost="34,000¥",
  rules="Standard RCC rules. Example Spider WAN/security spider use in Core rigger chapter."),
E(name="Maser Industrial Electronics RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="5", dp="3", fw="4", avail="8R", cost="64,000¥",
  rules="Standard RCC rules. High DR, low DP."),
E(name="Vulcan Liegelord RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="5", dp="5", fw="6", avail="10R", cost="66,000¥",
  rules="Standard RCC rules."),
E(name="Proteus Poseidon RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="5", dp="5", fw="6", avail="12R", cost="68,000¥",
  rules="Standard RCC rules."),
E(name="Lone Star Remote Commander RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="6", dp="6", fw="5", avail="14R", cost="75,000¥",
  rules="Standard RCC rules."),
E(name="MCT Drone Web RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="6", dp="7", fw="6", avail="16R", cost="95,000¥",
  rules="Standard RCC rules."),
E(name="Triox UberMensch RCC", cat="RCC", src="Core p.267",
  skill="n/a",
  rating="6", dp="8", fw="7", avail="18R", cost="140,000¥",
  rules="Standard RCC rules. Top Core table DP/FW."),
]

# ========== KC RCCs ==========
ITEMS += [
E(name="Shiawase Cyber-6 RCC", cat="RCC", src="Kill Code p.68-69 / table p.69,75; also Commlinks and Electronics.md",
  skill="n/a",
  rating="5", dp="5", fw="5", avail="12R", cost="72,000¥",
  rules="While jumped in: all drones commanded from this console gain +2 Initiative and +1 limit on all tasks. Dumpshock from this console +4 DV. INDEX primary books are Core+R5; KC specialty included for complete RCC catalog."),
E(name="Spinrad Global Skirmisher RCC", cat="RCC", src="Kill Code p.68-69 / table p.69,75",
  skill="n/a",
  rating="4", dp="5", fw="5", avail="8R", cost="50,000¥",
  rules="Drones commanded via Control Device from this RCC: +2 dice and +1 limit on Gunnery and Perception Tests."),
]

# ========== PILOTS ==========
ITEMS += [
E(name="Pilot Program (Rating 1)", cat="Pilot", src="R5 p.126-127 Pilots table; Core Pilot rules p.269",
  skill="n/a",
  rating="1", dp="-", fw="-", avail="4", cost="100¥",
  rules="Device-specific dog-brain. Device Rating of vehicle/drone = Pilot. Caps max autosoft Rating runnable on the device (unless RCC shares higher). Novel/confused situations: Pilot x 2 vs GM threshold or continues prior action / waits. Adapts to specific device in ~1 week (not portable to another unit). Civilian often 1-2."),
E(name="Pilot Program (Rating 2)", cat="Pilot", src="R5 p.127",
  skill="n/a",
  rating="2", dp="-", fw="-", avail="-", cost="400¥",
  rules="Typical civilian Pilot. Same Pilot rules."),
E(name="Pilot Program (Rating 3)", cat="Pilot", src="R5 p.127",
  skill="n/a",
  rating="3", dp="-", fw="-", avail="8R", cost="1,800¥",
  rules="Restricted security-grade Pilot band (3-4). Same Pilot rules."),
E(name="Pilot Program (Rating 4)", cat="Pilot", src="R5 p.127",
  skill="n/a",
  rating="4", dp="-", fw="-", avail="12R", cost="3,200¥",
  rules="Restricted security-grade. Same Pilot rules."),
E(name="Pilot Program (Rating 5)", cat="Pilot", src="R5 p.127",
  skill="n/a",
  rating="5", dp="-", fw="-", avail="16F", cost="10,000¥",
  rules="Forbidden military-grade Pilot band (5-6). Same Pilot rules."),
E(name="Pilot Program (Rating 6)", cat="Pilot", src="R5 p.127",
  skill="n/a",
  rating="6", dp="-", fw="-", avail="24F", cost="20,000¥",
  rules="Forbidden military-grade. Same Pilot rules."),
]

# ========== AUTOSOFT PRICE + CORE TYPES ==========
ITEMS += [
E(name="Autosoft (generic Rating 1-6)", cat="Autosoft", src="Core p.442 Software table; R5 p.127 Autosoft Prices (SR5 errata reprint)",
  skill="as program type",
  rating="1-6", dp="-", fw="-", avail="Rating x 2", cost="Rating x 500¥",
  rules="People have skills; drones have autosofts. Model-specific where tagged [Model] or [Weapon]. Drone program slots = ceil(Device Rating / 2) for own autosofts+cyberprograms; swap = Complex Matrix Action. If slaved to RCC and running NONE of its own programs, uses RCC-shared autosofts (can exceed onboard slot limit). Pilot cannot run autosoft Rating > Pilot unless RCC shares higher. RCC Sharing rating = how many shared autosofts apply to all slaves simultaneously."),
E(name="Clearsight Autosoft", cat="Autosoft", src="Core p.269",
  skill="Perception (drone)",
  rating="1-6", dp="-", fw="-", avail="as Autosoft", cost="as Autosoft",
  rules="Acts as drone Perception skill. Autonomous perception: Pilot + Clearsight [Sensor]. Jumped-in: rigger Perception + Intuition [Sensor]."),
E(name="Electronic Warfare Autosoft", cat="Autosoft", src="Core p.269",
  skill="Electronic Warfare",
  rating="1-6", dp="-", fw="-", avail="as Autosoft (Restricted per R5 Skillset note when Skillset form)", cost="as Autosoft",
  rules="Exactly like the Electronic Warfare skill for the drone."),
E(name="[Model] Evasion Autosoft", cat="Autosoft", src="Core p.269",
  skill="Sensor evasion",
  rating="1-6", dp="-", fw="-", avail="as Autosoft", cost="as Autosoft",
  rules="Model-specific. Teaches autopilot to avoid Sensor locks. Useless in wrong model."),
E(name="[Model] Maneuvering Autosoft", cat="Autosoft", src="Core p.269",
  skill="Pilot [vehicle type] for that model",
  rating="1-6", dp="-", fw="-", avail="as Autosoft", cost="as Autosoft",
  rules="Model-specific Pilot [Vehicle] equivalent for one drone/vehicle model only."),
E(name="[Model] Stealth Autosoft", cat="Autosoft", src="Core p.269-270",
  skill="Infiltration / Stealth",
  rating="1-6", dp="-", fw="-", avail="as Autosoft", cost="as Autosoft",
  rules="Model-specific. Autonomous: Pilot + Stealth [Handling] vs Perception + Intuition [Mental]. Jumped-in: Stealth + Intuition [Handling] vs same. Often pair with silent running."),
E(name="[Weapon] Targeting Autosoft", cat="Autosoft", src="Core p.269",
  skill="Gunnery for that weapon model",
  rating="1-6", dp="-", fw="-", avail="as Autosoft", cost="as Autosoft",
  rules="Weapon-model-specific Gunnery (e.g. Ingram Smartgun Targeting only for that gun). Melee Targeting variant exists under Skillset Melee."),
E(name="Smartsoft (Restricted)", cat="Autosoft", src="R5 p.127",
  skill="smartlink via sensors",
  rating="counts as 3", dp="-", fw="-", avail="as Rating 3 Autosoft (Restricted)", cost="as Rating 3 Autosoft (1,500¥)",
  rules="Sensor-integrated smartlink. Counts as Rating 3 autosoft. Enables full smartgun use through vehicle/drone sensors."),
E(name="Group Autosoft", cat="Autosoft", src="R5 p.127",
  skill="shared command signal",
  rating="counts as 2", dp="-", fw="-", avail="as Rating 2 Autosoft", cost="as Rating 2 Autosoft (1,000¥)",
  rules="Shared-signal: drones with Group answer the same command together instead of one-by-one. Counts as Rating 2 autosoft. Distinct from RCC group Send Message (RCC already commands many with one Simple Action)."),
E(name="Skillset Autosoft", cat="Autosoft", src="R5 p.127",
  skill="listed skill",
  rating="1-6", dp="-", fw="-", avail="as Autosoft; some skills Restricted", cost="as Autosoft",
  rules="Gives the listed skill to the drone at Rating. Allowed skills: Academic Knowledge (single); Chemistry (R); Demolitions (R); Electronic Warfare (R); First Aid; Hardware; Instruction; Language (single; real translation, not Linguistics tweak); Lockpicking (R); Mechanic (single Mechanic skill); Medicine (R); Melee (as Targeting for a specific melee weapon); Navigation; Performance (single); Professional Knowledge (single). Model-specificity still applies where relevant."),
E(name="Personality Tweak", cat="Autosoft", src="R5 p.127-128",
  skill="n/a (flavor)",
  rating="tweak", dp="-", fw="-", avail="4", cost="100¥",
  rules="Software tweak. Pilot develops unique flavor over time (playful, territorial, clumsy, calm, etc.). Can specify at purchase or allow natural development. No combat bonus."),
E(name="Linguistics Autosoft (verbal command vocab)", cat="Autosoft", src="R5 p.128",
  skill="limited verbal commands",
  rating="tweak / language pack", dp="-", fw="-", avail="4", cost="50¥",
  rules="Not full Language Skillset. Factory: typically 2 languages (mfr + sales region). Pilot may hold Linguistics packs up to its Rating. Very limited vocabulary (come here, go there, shoot that, find McHugh's, etc.); cannot translate eavesdropped speech. For real translation use Language Skillset autosoft."),
]

# ========== RCC CYBERPROGRAMS (buy RCC versions) ==========
# Common: Avail - / 80¥. Hacking: Avail 6R / 250¥ (Core Software table p.442; Matrix listing also shows hacking 4R / 250¥ - use Software table).
_RCC_PROG_NOTE = "RCC-bought copy cannot run on a cyberdeck (and deck copies cannot run on RCC). RCC cannot run more than one of the same program type."
ITEMS += [
E(name="Encryption (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price Software table p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="-", cost="80¥",
  rules=f"Common. +1 Firewall. {_RCC_PROG_NOTE}"),
E(name="Signal Scrub (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="-", cost="80¥",
  rules=f"Common. Rating 2 noise reduction. {_RCC_PROG_NOTE}"),
E(name="Toolbox (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="-", cost="80¥",
  rules=f"Common. +1 Data Processing. {_RCC_PROG_NOTE}"),
E(name="Virtual Machine (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="-", cost="80¥",
  rules=f"Common. Run 2 additional programs; when persona takes Matrix damage, take +1 unresisted Matrix damage box. {_RCC_PROG_NOTE}"),
E(name="Armor (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="6R", cost="250¥",
  rules=f"Hacking. +2 dice to resist Matrix damage. {_RCC_PROG_NOTE}"),
E(name="Biofeedback Filter (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="6R", cost="250¥",
  rules=f"Hacking. +2 dice to resist biofeedback damage. {_RCC_PROG_NOTE}"),
E(name="Guard (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="6R", cost="250¥",
  rules=f"Hacking. Reduce extra damage from marks by 1 DV per mark. {_RCC_PROG_NOTE}"),
E(name="Shell (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="6R", cost="250¥",
  rules=f"Hacking. +1 dice to resist Matrix and biofeedback damage; stacks with other programs. {_RCC_PROG_NOTE}"),
E(name="Sneak (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="6R", cost="250¥",
  rules=f"Hacking. +2 dice to defend against Trace User. If demiGOD converges while running, they do not get physical location (other convergence effects still apply). {_RCC_PROG_NOTE}"),
E(name="Wrapper (RCC)", cat="Program", src="Core p.269 / Matrix p.245; price p.442",
  skill="n/a", rating="-", dp="-", fw="-", avail="6R", cost="250¥",
  rules=f"Hacking (per Software table buy row). Defy Matrix iconography: Change Icon can make icons look like anything; Matrix Perception reveals true form if someone checks. {_RCC_PROG_NOTE}"),
E(name="Swarm (RCC program)", cat="Program", src="R5 p.31 Swarms + Rigging Program Cost table",
  skill="n/a", rating="-", dp="-", fw="-", avail="not printed", cost="600¥",
  rules="RCC program. Slave drones/vehicles to one RCC running Swarm; as many as slave capacity (DR x 3) or split across several swarms under that limit. Each swarm acts as one drone with multiple bodies. Pilot = highest member Pilot or RCC Device Rating (whichever higher). Uses highest of each autosoft on any member/RCC and highest Sensor; uses lowest Handling/Speed/Acceleration among members. Action dice pool and limit bonus = (drones in swarm - 1). Combat: all fire but use one weapon's stats for the attack (scatter explosives separately); attack drones individually; losses update bonuses immediately. Distinct from Swarm vehicle action (R5 p.179 teamwork attack), which is not a buyable SKU."),
]

# ========== RELATED JUMPED-IN / RCC NETWORK MODS ==========
ITEMS += [
E(name="Manual Control Override", cat="VehicleMod", src="R5 p.154-155 / Power Train table p.158",
  skill="n/a (install: Shop)", rating="-", dp="-", fw="-", avail="6", cost="500¥",
  rules="Slots 1, Threshold 4, Shop, Avail 6, 500¥. Mechanical Free Action switch (usually driver's seat): while on, AR/VR piloting impossible; manual controls always take precedence. Cannot be remotely deactivated."),
E(name="Removed Manual Controls", cat="VehicleMod", src="R5 p.155 / Power Train table p.158",
  skill="n/a (install: Shop)", rating="-", dp="-", fw="-", avail="2", cost="200¥",
  rules="Slots 1, Threshold 4, Shop, Avail 2, 200¥. Strips manual controls; electronic only. Non-owner must succeed on Control Device to pilot."),
E(name="Secondary Manual Controls", cat="VehicleMod", src="R5 p.156 / Power Train table p.158",
  skill="n/a (install: Shop)", rating="-", dp="-", fw="-", avail="4", cost="1,000¥",
  rules="Slots 2, Threshold 10, Shop, Avail 4, 1,000¥. Second full manual control set; either set can pilot, primary always priority. With Manual Control Override, can require a manual switch to hand off."),
E(name="Rigger Cocoon", cat="VehicleMod", src="R5 p.155-156 / Power Train table p.158",
  skill="n/a (install: Kit)", rating="-", dp="-", fw="-", avail="8", cost="1,500¥",
  rules="Slots 2, Threshold 6, Kit, Avail 8, 1,500¥. Armored fire-resistant pod with oxygen + biomed sensors for jumped-out meat body. Enter ~1 minute; exit Complex Action (quick-release). Barrier Armor 12 / Structure 8. Occupant +6 dice vs crash/maneuver damage. (GMC Banshee ships with one.)"),
E(name="Interior Cameras", cat="VehicleMod", src="R5 p.171 / Cosmetic table",
  skill="Hardware (install: Kit)", rating="-", dp="-", fw="-", avail="6", cost="2,000¥",
  rules="Slots none (cosmetic), Threshold 6, Kit, Hardware, Avail 6, 2,000¥. Feed cabin into PAN so jumped-in / VR rigger can make a standard Perception Test for people/things inside the vehicle."),
E(name="Touch Sensors", cat="VehicleMod", src="R5 p.169 / Electromagnetic table",
  skill="Hardware (install: Shop)", rating="-", dp="-", fw="-", avail="8", cost="Body x 500¥",
  rules="Slots 3, Threshold 16, Shop, Hardware, Avail 8, Body x 500¥. Jumped-in: +2 dice Perception or Sensor Tests; vehicle Handling +1. When vehicle takes damage, jumped-in rigger -2 to resist biofeedback."),
E(name="Pilot Enhancement (Rating 1-6 buy rows; text to 9)", cat="VehicleMod", src="R5 p.167-168 / Electromagnetic table p.169",
  skill="Hardware", rating="1-9 (replaces Pilot)", dp="-", fw="-", avail="see rules", cost="see rules",
  rules="Replaces Pilot Rating (does not add). Text allows Pilot Rating 1-9. Printed install: Rating 1-3: Slots = Rating, Thresh Rating x 3, Kit, Hardware, Avail Rating x 2, Cost Rating x 2,000¥. Rating 4-6: Slots = Rating, Thresh Rating x 4, Shop, Hardware, Avail Rating x 3, Cost Rating x 5,000¥. Ratings 7-9: no separate install row printed; do not invent. Separate from buying a Pilot program (R5 Pilots table) for a device that accepts a drop-in Pilot."),
E(name="Retrans Unit", cat="VehicleMod", src="R5 p.168 / Electromagnetic table p.169",
  skill="Hardware (install: Kit)", rating="-", dp="-", fw="-", avail="8", cost="4,000¥",
  rules="Slots 2, Threshold 4, Kit, Hardware, Avail 8, 4,000¥. For Noise due to physical distance on the drone/vehicle network: use greater of (source-to-retrans, retrans-to-dest) instead of full path. Network-only (not a bridge for outside hackers). Multiple units in one vehicle: no benefit; chain across vehicles: use single highest Noise hop. Serves all devices on the PAN."),
E(name="Satellite Link (vehicle)", cat="VehicleMod", src="R5 p.168 / Electromagnetic table p.169; Core sat link p.439",
  skill="Hardware (install: Kit)", rating="-", dp="-", fw="-", avail="6", cost="500¥",
  rules="Slots 1, Threshold 6, Kit, Hardware, Avail 6, 500¥. Vehicle communicates as if equipped with the Core satellite link accessory."),
]

# ========== RELATED GEAR ==========
ITEMS += [
E(name="Personal Drone Rack", cat="Mount", src="Kill Code p.73 / table p.75; also Commlinks and Electronics.md",
  skill="n/a",
  rating="-", dp="-", fw="-", avail="12R", cost="500¥",
  rules="Mount 3 micro drones or 1 small drone. Requires 1 micro-hardpoint (CCOB / similar). Carry/deploy accessory, not a vehicle drone rack mod."),
]

header = """# Rigger Gear

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `rigger5.pdf` · `killcode.pdf` (specialty RCCs + personal drone rack)
**Books:** Core · R5 (INDEX). KC specialty RCCs included so the RCC catalog is complete.
**See also:** `Encyclopedia/Drones.md` · `Encyclopedia/Vehicles.md` · `Encyclopedia/Vehicle and Drone Modifications.md` (full mod slot catalog when filled; jumped-in essentials duplicated here) · `Encyclopedia/Cyberware.md` (Control Rig) · `Encyclopedia/Commlinks and Electronics.md` (PI-Tac, CCOB, KC RCC rows) · `Encyclopedia/Cyberdecks and Programs.md` · `Encyclopedia/Sensors and Optics.md`
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

"""

def render(d):
    return "\n".join([
        f"### {d['name']}",
        f"- Cat: {d['cat']}",
        f"- Src: {d['src']}",
        f"- Rating: {d['rating']} | DP: {d['dp']} | FW: {d['fw']}",
        f"- Avail: {d['avail']} | Cost: {d['cost']}",
        f"- Rules: {d['rules']}",
        "",
    ])

CAT_ORDER = ["Implant", "Interface", "RCC", "Pilot", "Autosoft", "Program", "VehicleMod", "Mount"]
CAT_HEAD = {
    "Implant": "CONTROL RIG (cyberware; jump-in core)",
    "Interface": "RIGGER INTERFACE",
    "RCC": "RIGGER COMMAND CONSOLES",
    "Pilot": "PILOT PROGRAMS",
    "Autosoft": "AUTOSOFTS AND SOFTWARE TWEAKS",
    "Program": "RCC CYBERPROGRAMS AND SWARM",
    "VehicleMod": "JUMPED-IN / RCC NETWORK VEHICLE MODS",
    "Mount": "RELATED CARRY / MOUNT GEAR",
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
parts.append("""Control Rig (3): Rating 1 / 2 / 3.

Rigger Interface (1): Core/R5 cosmetic install (Slots none, Thresh 8, Kit, Avail 4, 1,000¥).

Core RCCs (11): Scratch-Built Junk, Radio Shack Remote Controller, Essy Motors DroneMaster, CompuForce TaskMaster, Maersk Spider, Maser Industrial Electronics, Vulcan Liegelord, Proteus Poseidon, Lone Star Remote Commander, MCT Drone Web, Triox UberMensch.

KC RCCs (2): Shiawase Cyber-6, Spinrad Global Skirmisher.

Pilots (6): Rating 1-6 with R5 price table (Rating 2 Avail blank in table).

Autosofts / tweaks (12): generic price row; Clearsight; Electronic Warfare; [Model] Evasion; [Model] Maneuvering; [Model] Stealth; [Weapon] Targeting; Smartsoft; Group; Skillset; Personality; Linguistics.

RCC programs (11): Encryption, Signal Scrub, Toolbox, Virtual Machine (common 80¥); Armor, Biofeedback Filter, Guard, Shell, Sneak, Wrapper (hacking 6R / 250¥ Software table); Swarm (R5, 600¥, Avail not printed).

Jumped-in / network vehicle mods (9): Manual Control Override; Removed Manual Controls; Secondary Manual Controls; Rigger Cocoon; Interior Cameras; Touch Sensors; Pilot Enhancement; Retrans Unit; Satellite Link (vehicle).

Mount (1): Personal Drone Rack (KC).

Pointers only: full vehicle mod catalog (weapon mounts, ECM, drone racks, armor, etc.) -> Vehicle and Drone Modifications; drones -> Drones.md; PI-Tac / CCOB -> Commlinks; deck program catalog -> Cyberdecks and Programs.
""")

text = "".join(parts)
for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"')):
    text = text.replace(a, b)
OUT.write_text(text, encoding="utf-8")
print("Wrote", OUT, "entries", len(ITEMS), "bytes", OUT.stat().st_size)
