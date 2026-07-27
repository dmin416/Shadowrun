# Vehicles

Agent reference (SR5). LLM layout; vehicle stats, Vehicle Tests, tactical driving, chase combat, ramming, crashes, attacks vs vehicles/passengers, suppression note.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Vehicle Combat ~p.198-205; passenger fire ~p.183; sensors ~p.184
**Source Text:** `11 - Combat.md` · control modes pointer `15 - Riggers.md` · Rigger 5 for advanced chase (after Core)
**See also:** [Combat/Ranged Combat](Combat/Ranged%20Combat.md) · [Combat/Called Shots and Special](Combat/Called%20Shots%20and%20Special.md) · [Rigging Basics](Rigging%20Basics.md) · Encyclopedia Vehicles / Drones

**Scope:** Vehicle attributes; Vehicle Tests + terrain/modifiers; Movement Rates; driver actions; Ramming; Chase Combat (ranges, environments, Chase Actions); Crashes; attacks vs vehicle/passengers; Evasive Driving; suppression vs vehicles; passenger -2 from moving vehicle
**Out of scope:** Full GridGuide travel tables reprint; Rigger 5 Maximum Pursuit depth; full drone Pilot/autosoft catalog (Rigging Basics)

## Inventory (completeness checklist)

- [x] Chase / tactical vehicle combat steps
- [x] Ramming; vehicle Condition; passenger attacks
- [x] Suppression vs vehicles

---

## Schema

| Token | Meaning |
| --- | --- |
| Vehicle Test | Vehicle Skill + Reaction [Handling] (or Speed when chase env says so) |
| Condition Monitor | Vehicles: 12 + half Body (up). Drones: 6 + half Body |
| Resist | Body + Armor; ignore if modified DV < Armor; ignore Stun (elec → Physical) |
| Chase Range | Short / Medium / Long / Extreme brackets |
| Control Vehicle | Complex Action once per Combat Turn or vehicle goes uncontrolled |

---

## Vehicle stats

| Stat | Role |
| --- | --- |
| Handling | Limit when maneuvering matters |
| Speed | Top-end; Limit when raw speed matters |
| Acceleration | Max Chase Range Categories changeable in one Catch-Up/Break Away |
| Body | Size/structure; damage resist pool; ram DV base |
| Armor | Toughness; with Body resists damage |
| Pilot | Autopilot Mental/Reaction stand-in when no metahuman driver |
| Sensor | Limit for Perception / detection via vehicle systems |

---

## Vehicle Tests (non-chase)

Everyday driving: usually no roll. Extreme/dangerous: Vehicle Skill + Reaction [Handling] vs threshold.

### Vehicle Test Threshold Table

| Situation | Threshold | Examples |
| --- | --- | --- |
| Easy | 1 | Merge, pass, sudden stop, gradual turn (<75°) |
| Average | 2 | Avoid obstacle, narrow spot, tight turn (75-130°) |
| Hard | 3 | Hairpin, stoppie, drive through mall, turn >130° |
| Extreme | 4+ | Jump obstacle, squeeze impossible gap, cinematic stunts |
| Driver Jumped In (Control Rig) | -Control Rig rating | Min threshold 1 |

Add **Terrain** to threshold:

| Terrain | Modifier | Examples |
| --- | --- | --- |
| Open | 0 | Highway, open sea, clear sky |
| Light | +1 | Main streets, rolling hills, dock, city air traffic |
| Restricted | +2 | Side streets, light woods, light traffic, low flight over clutter |
| Tight | +4 | Alleys, heavy woods, swamp, street-level flight in city |

### Vehicle Test Modifier Table (dice / Handling)

| Situation | Modifier |
| --- | --- |
| Impaired Visibility | Visibility column (Combat env) |
| Limited Light | Light column (Combat env) |
| Pilot unaware / Surprised | No Vehicle Test vs that threat |
| Pilot wounded | Wound mods |
| Damaged vehicle | -(damage modifier) to Handling (min 1) |
| Driving AR | +1 Handling Limit |
| Driving VR | +2 Handling Limit |
| Jumped In + Control Rig | Also cut threshold by Rig rating |

Fail / glitch: often uncontrolled or crash. Critical glitch: crash.

---

## Tactical combat (mixed pedestrians + vehicles)

Vehicle is extension of driver. Movement rate from Speed attribute (pick walk/run rate at start of Combat Turn).

### Movement Rates Table

| Speed Attr | Walking (m/turn) | Running (m/turn) |
| --- | --- | --- |
| 1 | 5 | 10 |
| 2 | 10 | 20 |
| 3 | 20 | 40 |
| 4 | 40 | 80 |
| 5 | 80 | 160 |
| 6 | 160 | 320 |
| 7 | 320 | 640 |
| 8 | 640 | 1,280 |
| 9 | 1,280 | 2,560 |
| 10 | 2,560 | 5,120 |

### Driver must Control Vehicle

Spend **≥1 Complex Action / Combat Turn** driving or vehicle is **uncontrolled** at end of Turn (-2 to all actions aboard). Next Turn: regain with Vehicle Test, or Pilot autopilot takes over (if present), else coasts/crashes per GM.

| Action type | Examples |
| --- | --- |
| Free | Change linked device mode (rigger/DNI); status report |
| Simple | Use Sensors; Use Simple Device (manual systems) |
| Complex | Control Vehicle; Fire Vehicle Weapon; Make Vehicle Test |

Mounted weapons: Complex Action; Gunnery + Agility [Accuracy] manual / Gunnery + Logic [Accuracy] remote. Handheld from moving vehicle: normal ranged rules **-2**. RC for vehicle mounts = Body + weapon RC.

---

## Ramming (tactical)

Treat as melee. Target in Walk or Run rate (-3 if must use Running rate).

```
Attacker: Vehicle Skill + Reaction
vs
Pedestrian: Reaction + Intuition (Full Defense / Dodge OK; not Block/Parry)
Other vehicle: Reaction + Intuition [Handling]
```

Hit → Damage Resistance. Base DV from Ramming Damage Table (Body × speed band). Rammer resists **half** (up). Characters: Body + Armor **-6 AP**.

Both drivers then Vehicle Test: rammer threshold **2**, rammed **3**, or become uncontrolled.

### Ramming Damage Table

| Speed (m/turn) | Damage Value |
| --- | --- |
| 1-10 | Body / 2 |
| 11-50 | Body |
| 51-200 | Body × 2 |
| 201-300 | Body × 3 |
| 301-500 | Body × 5 |
| 501+ | Body × 10 |

---

## Chase Combat

Use when **all** parties are in moving vehicles.

1. Determine Chase Environment (Speed or Handling) for the Turn.
2. Establish Chase Ranges between vehicles/groups.
3. Roll Initiative.
4. Act in order. Drivers: Chase Actions or normal combat actions. Passengers: normal combat only.

### Chase Ranges Table

| Range | Speed Env approx (m) | Handling Env approx (m) |
| --- | --- | --- |
| Short | 0-10 | 0-5 |
| Medium | 11-50 | 6-20 |
| Long | 51-150 | 21-80 |
| Extreme | 151-300 | 81-150 |

**Speed Environment:** open highway/field/sea/sky; Speed Limit matters.  
**Handling Environment:** tight streets/canyons/harbor/street flight; Handling Limit matters.

### Chase Actions (all Complex; need listed Range)

| Action | Range | Test / effect |
| --- | --- | --- |
| Catch-Up / Break Away | Any | Reaction + Vehicle Skill [Speed or Handling] vs maneuver threshold. Shift up to Acceleration Categories by net hits. Leaving Extreme: pursuer may test to keep sight |
| Cut-Off | Short | Opposed Reaction + Vehicle Skill [Handling]. Net hits → target Vehicle Test (threshold = net hits) or crash |
| Ram | Short | Opposed Vehicle Skill + Reaction [Speed or Handling]. Hit: target takes Body + net hits; rammer takes half Body |
| Stunt | Any | Vehicle Skill + Reaction [Speed/Handling] vs GM threshold. Success: pursuers must match threshold or lose a Range (Extreme fail = escape) |

Passenger attacks vs outside targets with non-mounted weapons: **-2**.

---

## Crashes

On Ram, failed collision course, or GM call. Vehicle + passengers resist DV = vehicle **Body** with Body + Armor **-6 AP**. Stun if Body < character Armor, else Physical.

Also Composure (4); penalty = hits missed for that many Combat Turns.

---

## Attacks against vehicles

| Case | Defense |
| --- | --- |
| Driven vehicle | Driver Reaction + Intuition |
| Drone | Pilot + Autosoft [Handling] |
| Jumped in | See Rigging Basics |

Resist Body + Armor; no damage if modified DV < Armor. Evasive Driving: Free Action; -10 Init; +Intuition dice to defense (not vs rams).

Called shots can trash components (tire = -2 Vehicle Tests each).

### Passengers vs vehicle targeting

Normally attack **either** passengers **or** vehicle, not both. Exceptions: ram, suppression, shotguns shot, AE (grenades/rockets) hit both.

Passenger-targeted: Good Cover + often +3 moving vehicle; Blind Fire possible. Defender inside: **-2** Defense. Add **vehicle Armor** to personal Armor.

### Suppression vs vehicles

Cover bonus for passengers. Hit the Dirt: do not auto-avoid; instead gain vehicle Armor on Damage Resistance. If weapon DV ≤ vehicle Armor, no penetrate. Driver may Reaction + Edge to leave the zone with everyone aboard.

---

## Sensors (detect)

Passive/active Sensor Tests: characters Perception + Intuition [Sensor]; vehicles Pilot + Clearsight [Sensor]. Evading: Opposed vs Infiltration + Agility, Infiltration (Vehicle) + Reaction [Handling], or Pilot + Stealth [Handling] (drones). Signature modifiers apply (Combat Sensor section).

---

## Rigging pointer

Control Rig / Jump In / RCC: [Rigging Basics](Rigging%20Basics.md). Advanced pursuit: Rigger 5 Maximum Pursuit after Core chase is mastered.
