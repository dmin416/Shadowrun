# Rigging

Agent reference (SR5). LLM layout; control modes, Jump In, Control Rig, RCC sharing, drones/Pilot/autosofts, Noise, sensors, dumpshock.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Riggers ~p.264-271; Sensor Attacks/Targeting ~p.184-185; Control Rig gear ~p.452; vehicle combat cross-ref ~p.198+
**Source Text:** `15 - Riggers.md` · Control Rig table in `21 - Street Gear.md` · Sensor Attacks/Targeting + chases in `11 - Combat.md`
**See also:** [Vehicles](Vehicles.md) · [Matrix](Matrix.md) · [Maximum Pursuit](Maximum%20Pursuit.md) · Encyclopedia [Drones](../Encyclopedia/Drones.md) / [Vehicles](../Encyclopedia/Vehicles.md)

**Scope:** Four control modes + override order; Jump In; Control Rig; RCC sharing; drones/Pilot/autosofts; Noise; sensors; dumpshock; **Swarm** (R5)
**Out of scope:** Full RCC shop table reprint (Encyclopedia); full vehicle/drone chassis catalog (Encyclopedia); deep mod install (R5 encyclopedia)

## Inventory (completeness checklist)

- [x] Control modes; Jump In; RCC sharing + worked example
- [x] Drone Init / Condition Monitor / Pilot / autosofts; Noise
- [x] Electronic Warfare Noise actions (compensation; Jam Signals)
- [x] Sensor Targeting (passive/active) + Sensor Defense + Signature tables
- [x] Rigger Interface / Control Rig grades pointer
- [x] Swarm program rules (Rigger 5)

---

## Schema

| Token | Meaning |
| --- | --- |
| Control Rig | Implant required to Jump In |
| Rigger Interface | Vehicle hardware (built into drones; aftermarket on most cars) |
| RCC | Rigger Command Console; drone PAN master |
| Sharing | How many RCC autosofts broadcast to all slaves |
| Jump In | Merge persona with device; VR vehicle control |
| Pilot Rating | Drone's Device Rating; also its Mental/Reaction stand-in when autonomous |

---

## Prerequisites

1. Implanted **Control Rig** (Rating 1-3).
2. Target has **rigger interface** (drones included; most civilian vehicles need the mod).
3. You are **owner** or have **3 marks** on the device.

Built-in: sim module, universal connector, ~1 m retractable cable (like a free datajack).

### Control Rig grades (Street Gear)

| Rating | Essence | Avail | Cost |
| --- | --- | --- | --- |
| 1 | 1 | 5R | 43,000¥ |
| 2 | 2 | 10R | 97,000¥ |
| 3 | 3 | 15R | 208,000¥ |

---

## Control modes (override order)

Highest wins; lower methods blocked until current controller releases (next Initiative Pass).

1. **Rigger control** (jumped in)
2. **Remote control** (Control Device Matrix action)
3. **Manual** (wheel, AR sticks, etc.)
4. **Autopilot** (Pilot program)

One method at a time (no stacking turret fire from two controllers).

---

## Jump In / Out

| From | Action |
| --- | --- |
| AR → Jump In | Complex |
| Already VR → Jump In | Simple |
| Direct cable into vehicle/RCC from meat | Simple |

Jumped in = **VR**. Vehicle actions count as Matrix actions for bonuses. Control Rig rating adds to device Limits: Sensor, Speed, Handling, and Accuracy of mounted weapons you fire.

| Sim | Init dice | Other |
| --- | --- | --- |
| Cold-sim | +2D6 (3D6 total) | Biofeedback Stun |
| Hot-sim | +3D6 (4D6 total) | +1 DP Matrix/Vehicle tests; biofeedback Physical |

**Jump out:** Switch Interface Mode to AR/VR, or Jump into another slaved device via RCC without leaving first.

**Destroyed / bricked while in:** Dumpshock (6S/6P) and lose control ([Matrix](Matrix.md)).

---

## Noise and connections

Wireless rigging takes **Noise** penalties like other Matrix actions (full Noise distance/situation tables: [Matrix](Matrix.md)). **Direct cable:** no Noise.

### Electronic Warfare (Noise actions)

| Action | Type | Test | Effect |
| --- | --- | --- | --- |
| Noise compensation | Complex | Electronic Warfare + Logic [Data Processing] | Hits = extra Noise reduction for the rest of the Combat Turn (stacks with gear) |
| Jam Signals | Complex (needs the jammer device) | Electronic Warfare + Logic [Attack] | Hits = Noise added within 100 m of the jammer while it stays active/idle in that spot |

Matrix damage while jumped in via link/RCC hits the **persona device** (RCC/commlink), not the vehicle, unless you are directly cabled into the vehicle.

---

## RCC

Commlink features + drone PAN tools. Boot: split Device Rating between **Noise Reduction** and **Sharing** (sum ≤ Device Rating; adjust later via Change Device Mode).

| Feature | Effect |
| --- | --- |
| Noise Reduction | Cumulative Noise Reduction |
| Sharing | That many autosofts on the RCC run on **all** slaves (drone running its own programs loses RCC share) |
| Data Processing | VR Initiative; Limit for Command tests |
| Firewall | Defends the whole slaved swarm |
| Slaves | Up to Device Rating × 3 drones |

### RCC Sharing worked example

Device Rating 5 RCC: split as **3 Noise Reduction / 2 Sharing**, or **5 / 0**, or any split summing to ≤5.

- With **2 Sharing**: load Clearsight and Electronic Warfare on the RCC. Every slaved drone now effectively "has" those two autosofts too (any drone not running its own copy uses the RCC's), even if that drone's own autosoft slots are empty or full of other programs.
- A drone running its **own** copy of an autosoft ignores the RCC's shared copy of that same autosoft (no stacking); it can still benefit from Sharing for autosofts it doesn't carry itself.
- Raising Sharing to 3 (dropping Noise Reduction to 2) would let the rigger add a third shared autosoft (e.g. a Targeting autosoft) at the cost of 1 less cumulative Noise Reduction for the whole PAN.

Send Message / group command: one Simple Action can order one, some, or all slaves; they act on **their** Action Phase. Contradictory same-level commands before they act → error, no action.

Slave defense may use master's ratings (same PAN rules). Mark slave → mark RCC. Direct connection on drone: no master help.

WAN: spider-rigger slaves RCC to a building host; distance to host-slaved drones treated as zero inside that host.

---

## Drones

| Rule | Detail |
| --- | --- |
| Device Rating | = Pilot Rating; Matrix attrs = Pilot |
| Condition Monitor | **6 + half Body** (round up); ignore Stun (electricity → Physical); no damage if modified DV ≤ modified Armor ([Vehicles](Vehicles.md)) |
| Pilot "dog-brain" | Novel situations: Device Rating × 2 vs GM threshold or keep prior orders / idle |
| Autosoft slots | Half Device Rating (round up) |
| Swap programs | Complex Matrix Action |

Pilot Rating is baked into a given drone model (Street Gear stat lines); Core does not sell a separate "Pilot rating" upgrade item beyond swapping in a different Pilot program of the drone's own Device Rating or lower.

### Common autosofts (Rating 1-6)

| Autosoft | Acts as |
| --- | --- |
| Clearsight | Perception |
| Electronic Warfare | Electronic Warfare skill |
| [Model] Evasion | Avoid sensor lock |
| [Model] Maneuvering | Pilot for that model |
| [Model] Stealth | Infiltration for that model |
| [Weapon] Targeting | Gunnery for that weapon model |

### Drone Initiative

Autonomous: Initiative = Pilot × 2, **+3D6** (4D6 total). Jumped in: use rigger's VR Initiative.

Attacks: Pilot + [Weapon] Targeting [Accuracy] (need the autosoft). Gunnery from vehicle mounts: see [Vehicles](Vehicles.md).

### Swarms (Rigger 5)

RCC running **Swarm** program (600¥) may slave **Device Rating x 3** drones and split them among swarms.

| Rule | Detail |
| --- | --- |
| Acts as | One drone for initiative and actions |
| Pilot | Highest member Pilot **or** RCC Device Rating |
| Stats | Highest autosofts/Sensor; **lowest** Handling/Speed/Acceleration |
| Dice / limits | Add **(drones in swarm - 1)** to dice pools and limits |
| Weapons | One weapon profile per volley; scatter explosives separately |
| Damage | Target drones individually; update swarm bonuses immediately as drones are lost |

Chase **Swarm** action (jumped-in controller): [Maximum Pursuit](Maximum%20Pursuit.md).

Normal operating time ~6 hours (longer idle, shorter at sustained top speed). Takeoff/landing distances: Long 2,000/1,800 m; Short 200/300 m; VTOL none/none.

---

## Sensor Targeting

A rigger/vehicle can use the vehicle's **Sensor** attribute to help Gunnery, in two ways:

| Mode | Action | Test | Effect |
| --- | --- | --- | --- |
| Passive targeting | (part of the attack) | Gunnery + Logic [**Sensor**] instead of [Accuracy] | Target's Signature modifier also applies to the attack pool |
| Active targeting | Simple (to lock), then attack normally | Sensor Test: Perception + Intuition [Sensor] (character) or Pilot + Clearsight [Sensor] (vehicle/drone), opposed if target evades | Net hits = negative modifier to the target's Defense Test; once locked, no re-test needed until contact breaks |

Detecting a target at all (before targeting) uses the same **Sensor Test** vs the target's evasion below, modified by the Signature Table.

### Sensor Defense Table

| Defender | Sensor Defense Test |
| --- | --- |
| Metahuman, Critter | Infiltration + Agility [Physical] |
| Vehicle | Infiltration (Vehicle) + Reaction [Handling] |
| Drone | Pilot + [Model] Evasion [Handling] |

### Signature Table

| Target Size | Modifier |
| --- | --- |
| Large/oversized vehicles (trains, construction vehicles, zeppelins, tractor-trailers, airliners) | +3 |
| Electric-powered vehicles | -3 |
| Metahumans, Critters | -3 |
| Drones | -3 |
| Micro-drones | -6 |

If a locked target breaks sensor contact, re-acquire with another Sensor Test (Evade Detection = target's Opposed Sensor Defense Test above).

---

## Getting dumped

Force-ejected when: vehicle destroyed/bricked; RCC/commlink destroyed/bricked while that was your persona path; data cable yanked. Suffer dumpshock; vehicle uncontrolled until Pilot resumes next Turn or someone else takes control.

Full Matrix Defense available when under Matrix attack.

---

## Skills

Pilot [Vehicle type] skills + **Gunnery**. Expanded chassis, mods, chase: *Rigger 5.0* and [Vehicles](Vehicles.md). Chassis/model stat lines: [Encyclopedia/Drones](../Encyclopedia/Drones.md) and [Encyclopedia/Vehicles](../Encyclopedia/Vehicles.md).
