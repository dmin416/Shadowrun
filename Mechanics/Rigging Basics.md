# Rigging Basics

Agent reference (SR5). LLM layout; control modes, Jump In, Control Rig, RCC sharing, drones/Pilot/autosofts, Noise, dumpshock.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Riggers ~p.264-271; Control Rig gear ~p.452; vehicle combat cross-ref ~p.198+
**Source Text:** `15 - Riggers.md` · Control Rig table in `21 - Street Gear.md` · chases in `11 - Combat.md`
**See also:** [Vehicles](Vehicles.md) · [Matrix Basics](Matrix%20Basics.md) · Encyclopedia Rigger Gear / Drones · *Rigger 5.0*

**Scope:** Four control modes + override order; Jump In prerequisites/actions; cold/hot-sim rigging; Control Rig Limit bonus + grades; RCC Noise Reduction/Sharing/PAN; Pilot/autosofts; drone Initiative; EW Noise compensation; dump when jumped in
**Out of scope:** Full RCC shop table reprint; Rigger 5 Maximum Pursuit / swarm deep rules; every drone chassis

## Inventory (completeness checklist)

- [x] Control modes; Jump In; RCC sharing
- [x] Drone Init / Pilot / autosofts; Noise
- [x] Rigger Interface / Control Rig grades pointer

---

## Schema

| Token | Meaning |
| --- | --- |
| Control Rig | Implant required to Jump In |
| Rigger Interface | Vehicle hardware (built into drones; aftermarket on most cars) |
| RCC | Rigger Command Console; drone PAN master |
| Sharing | How many RCC autosofts broadcast to all slaves |
| Jump In | Merge persona with device; VR vehicle control |

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

**Destroyed / bricked while in:** Dumpshock (6S/6P) and lose control ([Matrix Basics](Matrix%20Basics.md)).

---

## Noise and connections

Wireless rigging takes **Noise** penalties like other Matrix actions. **Direct cable:** no Noise. RCC Complex Action: Electronic Warfare + Logic [Data Processing]; hits = extra Noise reduction for the rest of the Combat Turn (stacks with gear).

Matrix damage while jumped in via link/RCC hits the **persona device** (RCC/commlink), not the vehicle, unless you are directly cabled into the vehicle.

---

## RCC

Commlink features + drone PAN tools. Boot: split Device Rating between **Noise Reduction** and **Sharing** (sum ≤ Device Rating).

| Feature | Effect |
| --- | --- |
| Noise Reduction | Cumulative Noise Reduction |
| Sharing | That many autosofts on the RCC run on **all** slaves (drone running its own programs loses RCC share) |
| Data Processing | VR Initiative; Limit for Command tests |
| Firewall | Defends the whole slaved swarm |
| Slaves | Up to Device Rating × 3 drones |

Send Message / group command: one Simple Action can order one, some, or all slaves; they act on **their** Action Phase. Contradictory same-level commands before they act → error, no action.

Slave defense may use master's ratings (same PAN rules). Mark slave → mark RCC. Direct connection on drone: no master help.

WAN: spider-rigger slaves RCC to a building host; distance to host-slaved drones treated as zero inside that host.

---

## Drones

| Rule | Detail |
| --- | --- |
| Device Rating | = Pilot Rating; Matrix attrs = Pilot |
| Condition | Physical + Matrix tracks; either full = wrecked/bricked |
| Pilot "dog-brain" | Novel situations: Device Rating × 2 vs GM threshold or keep prior orders / idle |
| Autosoft slots | Half Device Rating (up), rounded up |
| Swap programs | Complex Matrix Action |

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

---

## Getting dumped

Force-ejected when: vehicle destroyed/bricked; RCC/commlink destroyed/bricked while that was your persona path; data cable yanked. Suffer dumpshock; vehicle uncontrolled until Pilot resumes next Turn or someone else takes control.

Full Matrix Defense available when under Matrix attack.

---

## Skills

Pilot [Vehicle type] skills + **Gunnery**. Expanded chassis, mods, chase: *Rigger 5.0* and [Vehicles](Vehicles.md).
