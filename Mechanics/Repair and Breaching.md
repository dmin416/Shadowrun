# Repair and Breaching

Agent reference (SR5). Gear repair thresholds and demolitions/breaching from *Run & Gun* Ch. 10 and 12. Core Build/Repair basics remain in [Advancement](Advancement.md) and [Barriers](Barriers.md).

**Src PDFs:** `Source/PDF/runandgun.pdf`
**Source Text:** `10 - Fixin All the Broken Drek.md` · `12 - Blow Up Good.md`
**See also:** [Barriers](Barriers.md) · [Combat/Damage Armor and Wounds](Combat/Damage%20Armor%20and%20Wounds.md) · Encyclopedia [Grenades and Explosives](../Encyclopedia/Grenades%20and%20Explosives.md)

**Scope:** Called-shot healing thresholds; broken weapons/gear/vehicles; demolitions structure breach; building implosion; breaching/cutting charges; charge complexity
**Out of scope:** Full explosives catalog (Encyclopedia); every detonator SKU

---

## Called-shot repair (eyes/ears)

Any Healing Test (First Aid, Medicine, Heal, etc.) on eye or ear called-shot injuries: **threshold +1**.

Once healed boxes equal the **Called Shot DV Limit**, the sensory injury is repaired regardless of remaining damage on the target.

---

## Broken melee weapons

Beyond Core Build/Repair: **Extended Test**, **Long Interval (1 hour)**.

| Loss | Repair threshold | Material cost (% of original weapon cost) |
| --- | --- | --- |
| Accuracy | Average (12) | 3% per Accuracy point |
| AP | Hard (18) | 5% per AP point |
| Reach | Very Hard (24) | 10% per Reach point |

**Craftsman labor:** (Skill Rating x hours x 10)¥ + materials.

---

## Other broken gear

| Category | Material cost | Labor |
| --- | --- | --- |
| Commlinks, cars, general gear | 2% original cost per CM box repaired | Mechanic: (Rating x hours x 10)¥ + materials; shop mechanic ~4 h/day on one vehicle unless paid extra |
| Everyday disposable gear | 10% original cost per CM box | (Skill Rating x hours x 5)¥ |
| Everyday threshold estimate | Device Rating x 3 | Adjust up/down for complexity |

### Vehicle part repair (*Fixin' That Old Beater*)

| Part | Threshold | Price |
| --- | --- | --- |
| Antenna | 4 | 20¥ |
| Axle | 18 | 2,000¥ |
| Door lock | 12 | 800¥ |
| Engine block | 24 | 25% of vehicle cost |
| Fuel tank/battery | 18 | 1,200¥ |
| Window motor | 12 | 800¥ |
| Window | 12 | 300¥ |

---

## Demolitions overview

**Commercial** explosives: reliable rated DV. **Homemade:** variable; Demolitions + Logic Extended Test while cooking; no hits on a roll = ±1 effective rating; glitch = ±5; critical glitch = detonation at desired rating DV.

**Charge complexity**

| Type | Limits |
| --- | --- |
| Simple | One detonator (not optical), one power supply, ≤5 kg/device; no anti-removal; not wired in circuit (timer/radio sync OK); not tamped |
| Average | Up to 3 detonators, up to 4 anti-removal mods, ≤10 kg/device; may use det cord/safety fuse circuit; may tamp |
| Complex | May use optical detonator (one); full anti-removal (max 12); any size; may tamp |

**Building charges (multiple devices):** threshold = number of charges; interval Simple 30 min / Average 1 h / Complex 1 day per Extended Demolitions Test hit.

**Single device:** threshold Simple 10 min / Average 1 h / Complex 1 day.

---

## Structure breach procedure (5 steps)

1. **Structure + Armor** x blast-radius percentage (25 cm = 25%, 1.25 m = 125%, etc.).
2. If charge is **on** the structure: apply **-half AP** to modified Armor.
3. Add modified Structure + modified Armor (after -half AP).
4. **Buying Hits** (Core p. 45): hits absorbed before damage = threshold component.
5. **DV threshold** = Structure + bought hits. **Partial breach:** explosive DV **below** full threshold.

**Demolitions + Logic hits:** each hit raises/lowers effective explosive rating by 1 (when shaping/cooking).

---

## Building/structure destruction DV thresholds

Minimum cumulative DV to destroy (controlled collapse). Demolitions + Logic (6) to estimate charge load; blueprints/specs lower threshold to (4). Miss by 20P per failed estimate; glitch ±40P; critical glitch ±60P.

| Structure | Minimum DV |
| --- | --- |
| Apartment | 75P |
| Medium house | 100P |
| Small retail (Stuffer Shack) | 128P |
| Warehouse | 160P |
| Small office (<5 stories) | 200P |
| Tunnel / overpass | 175P |
| Medium office (5-15 stories) | 128-640P |
| Medium factory | 200P |
| Large office (16-25 stories) | 256-960P |
| Military installation | 500P |
| Hardened secret research facility | 550P |
| Skyscraper / arcology (26+) | 960P+ |

**Placement:** charges on structural columns/beams at **multiples of 4 per level**; ground/basement + every **5th floor** (5, 10, 15, 20…). Proper placement on structural point: **DV x2** (see Barriers). Charge must produce **1 m hole** in that structural point.

**Tamping:** directional force; tamping material Structure ≥ half target Structure (or Force ≥ half for Physical Barrier). **Tamped DV x4** (not x2). May reduce required structural points (minimum 4).

**Small buildings (<5 stories):** single key support + threshold (≤250P) may suffice; **gas leak** tampering adds **+20P** to device DV.

**Collateral:** exceeding building threshold by **>50P** causes neighborhood damage. Underestimating by **>half** threshold: building may not collapse (repairable).

**Implosion steps:** (1) calculate DV needed; (2) Demolitions Tests to shape charges; (3) plant charges (identify structural point: Demolitions + Logic threshold 6, or 4 with specs); total per-floor DV must meet structure threshold.

---

## Material DV thresholds (1 m hole)

Verified from *Run & Gun* p. 179 (PDF).

| Barrier material | Structure | Armor | Minimum DV* |
| --- | --- | --- | --- |
| Fragile | 1 | 2 | 2 |
| Cheap | 2 | 4 | 3 |
| Average | 4 | 6 | 6 |
| Heavy | 6 | 8 | 9 |
| Reinforced | 8 | 12 | 13 |
| Structural | 10 | 16 | 16 |
| Heavy Structural | 12 | 20 | 20 |
| Armored/Reinforced | 14 | 24 | 23 |
| Hardened | 16+ | 32+ | 28+ |

\* For producing a 1-meter hole or cutting through material. Smaller/larger holes: see breaching rules below.

**Example structural points:** Structural (Structure 10, Armor 16); Heavy structural (Structure 12, Armor 20).

---

## Vehicle minimum DV (destroy body)

Verified from *Run & Gun* p. 179.

| Vehicle type | Minimum DV |
| --- | --- |
| Bike | 9 |
| Car | 14 |
| Boat | 18 |
| Limousine | 22 |
| Truck/Van | 26 |

Average vehicles only; increase for heavier custom armor.

---

## Breaching charges

1. Measure thickness (ultrasound Complex Action, or Knowledge skill estimate).
2. Scale Structure/Armor by **thickness / 1 m** (20 cm door = 20% of 1 m benchmark).
3. Decide **full breach** vs **partial breach** (e.g., destroy lock only).
4. Apply **-half AP** to Armor; **DV doubled** when charge placed on surface.
5. Demolitions + Logic may **lower effective rating** to fine-tune charge strength.

---

## Cutting charges

Linear cutting charge, det cord, or explosive foam. Count as **one device** for Extended Test intervals.

**Plant cutting charge:** Demolitions + Logic (5 min) Extended Test; threshold = **2 x kg** explosive used, or **2 x meters** det cord.

**Det cord DV:** low-yield **3P/m**; high-yield **6P/m**; adjust ±1P per ±34 cm length.

**Linear cutting charge:** inverted-V sheath; auto-tamped (**x4** DV); 1 m = 1 kg at charge rating.

**Cylindrical targets:** use **diameter** as thickness. Frame charges: attach = Complex Action (conspicuous).

---

## Vehicle explosives (summary)

**Destroy vehicle body:** see Vehicle Damage Threshold table in *Run & Gun* p. 191 (Boat, Bike, Car, Limousine, Truck/Van minimum DVs; source text table incomplete in extract).

**Car bomb vs building:** perimeter design reduces circular blast **-20P** before structure; improved design another **-20P**.

**Disable vehicle:** charge on axle/transaxle; resist with component material (usually Heavy Structure 6 / Armor 8; security vehicles Reinforced 8/12). Use breaching rules; cylindrical = diameter as thickness.

**Weaken chassis for bigger external blast:** Automotive Mechanic + Logic; each hit **-1 Armor** (minimum 1).

**Fuel engine destroyed:** add **+20P** to external blast DV.

**Passenger-kill bomb:** charge inside compartment; directional; penetrating weapon vs seat; **x4** if tamped in door panel; damage to occupants first, then vehicle (-2 AP to vehicle).

---

## Cooking explosives (facility)

Requires **demolitions shop** (kit can arm/disarm only). **Facility** lowers Extended threshold by 4. Chemistry shop: **-2** dice (inadequate tools). No chemicals = cannot cook.

Extended Demolitions + Logic (30 min); rating drift ±1 per no-hit roll, ±5 glitch, crit glitch detonates batch.

---

## Coverage notes

- Material and vehicle minimum-DV tables verified from `Source/PDF/runandgun.pdf` p. 179.
- Astral background count from large blasts: see *Run & Gun* p. 177 (BGC from explosion DV: 1 at 35P+, +1 per 20P above; max 3 for normal explosives unless exotic payload).
