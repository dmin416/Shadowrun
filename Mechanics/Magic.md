# Magic

Agent reference (SR5). LLM layout; full Core play ref for mage/adept/mystic adept: spellcasting, Drain, traditions, full spell catalog, counterspelling, conjuring, spirits, enchanting, adept powers, mentor spirits, astral, mana barriers, reagents, foci.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Magic chapter ~p.276-327 (basics, sorcery/spells, conjuring/spirits, enchanting, adepts, astral, mana barriers, reagents, foci, mentor spirits, initiation overview)
**Source Text:** `17 - Magic.md`
**See also:** [Dice and Tests](Dice%20and%20Tests.md) · [Healing and Injuries](Healing%20and%20Injuries.md) · [Background Count](Background%20Count.md) · [Metamagics and Arts](Metamagics%20and%20Arts.md) · [Magic Supplemental](Magic%20Supplemental.md) · [Character Creation/Magic and Resonance](Character%20Creation/Magic%20and%20Resonance.md) · [Magic Basics](Magic%20Basics.md) · [Critter and Spirit Powers](Critter%20and%20Spirit%20Powers.md) · Encyclopedia [Magical Goods](../Encyclopedia/Magical%20Goods.md)

**Scope:** Core-complete magic play plus supplement pointers: Hermetic/Shamanic traditions; full Core spell catalog; conjuring/enchanting/adepts/mentors/astral; **Shadow Spells** traditions/spells/adept powers; **Hard Targets** Obeah/Santería and mentors; **Aetherology** phenomena brief; initiation overview.
**Out of scope:** Full SG/FA spell and ritual libraries (see source books); full BGC tables duplicated here ([Background Count](Background%20Count.md)).

## Inventory (completeness checklist)

- [x] Magic attribute, Essence loss, Power Points, traditions, lodges
- [x] Noticing magic
- [x] Spellcasting steps, multi-spell, targeting, combat spell patterns, Drain
- [x] Full Core spell catalog: Combat / Detection / Health / Illusion / Manipulation
- [x] Counterspelling: spell defense (protecting others) + dispelling; Object Resistance Table
- [x] Ritual Spellcasting steps + full Core ritual list (incl. Watcher/Homunculus stat blocks)
- [x] Learning spells/rituals/preparations
- [x] Conjuring: summon/bind/banish steps, spirit services, Edge
- [x] Full Core spirit stat blocks: Air, Beasts, Earth, Fire, Man, Water
- [x] Spirit/critter power procedures: general power rules + full write-up of every power the 6 Core spirits use (see [Critter and Spirit Powers](Critter%20and%20Spirit%20Powers.md))
- [x] Enchanting: Alchemy preparations, Artificing foci creation, Disenchanting/Disjoining
- [x] Adept Power Points rules + full Core adept powers list
- [x] Mentor Spirit table: all 16 Core archetypes
- [x] Astral: perception/projection/movement/manifesting/staying astral, full Assensing Table, astral detection, astral combat, astral tracking
- [x] Mana barriers/wards deepened: getting around, astral intersections
- [x] Reagents: uses + harvesting
- [x] Foci: 7 types, bonding rules
- [x] Background count: full rules in [Background Count](Background%20Count.md)
- [x] Shadow Spells / Hard Targets / Aetherology supplement blocks (below)
- [x] Book of the Lost mentors (Raven Alt, Lion); full SS/SS spells in [Magic Supplemental](Magic%20Supplemental.md)

---

## Schema

| Token | Meaning |
| --- | --- |
| Force | Spell/spirit/focus power rating; often the Limit |
| Drain | Stun (or Physical if overcast / high Force); resist with tradition attrs |
| Overcast | Hits (not net) after Limit > Magic causes Physical Drain |
| Service | What a spirit owes; lost at sunrise/sunset if only summoned |
| P / M | Physical spell / Mana spell |
| LOS / T / (A) | Line of Sight / Touch / Area (radius = Force in meters unless stated) |
| I / S / P (duration) | Instantaneous / Sustained / Permanent |
| F | Force, used in Drain formulas (e.g. F-3, min Drain always 2) |

---

## Magical skills

| Group | Skills |
| --- | --- |
| Sorcery | Spellcasting, Counterspelling, Ritual Spellcasting |
| Conjuring | Summoning, Binding, Banishing |
| Enchanting | Alchemy, Artificing, Disenchanting |

**Magic attribute:** 1-6 at chargen (7 with Exceptional Attribute); max = 6 + Initiation grade. Essence loss reduces current and max Magic by 1 per full point (or fraction) of Essence lost. Magic 0: cannot use Magic-linked skills (can still raise Magic with Karma). Max Magic burned to 0: mundane forever (burned out); magical active skills except Arcana become Knowledge skills.

**Force:** Choose up to **Magic x 2** for spells/spirits/preparations. Higher Force = stronger effect + worse Drain. Force is the Limit for magic performed without reagents/foci.

**Drain:** Cannot be healed by magic or medkits; only natural recovery. Minimum DV always **2**. Sorcery/Enchanting Drain Value is listed per spell/ritual/preparation; Conjuring Drain = 2x hits (not net) on the spirit's defense.

**Astral Limit:** Inherent Limit for astral tests = your Mental or Social limit, whichever is greater.

**Power Points:** See [Adepts](#adepts) below.

---

## Traditions (Core)

| Tradition | Drain resist | Spirit affinities (category: type) |
| --- | --- | --- |
| Hermetic (mage) | Logic + Willpower | Combat: Fire, Detection: Air, Health: Man, Illusion: Water, Manipulation: Earth |
| Shamanic (shaman) | Charisma + Willpower | Combat: Beasts, Detection: Water, Health: Earth, Illusion: Air, Manipulation: Man |

Hermetics tend to bind spirits (see them as servants); shamans tend to summon fresh rather than bind (see spirits as elders/relations). More traditions in *Street Grimoire* / *Forbidden Arcana*.

**Magical Lodges:** Force x 500 nuyen materials; days to build = lodge Force. Needed to learn spells/rituals, craft foci, perform rituals. Acts as a mana barrier and carries your astral signature. Moving: 1 day to dismantle, then rebuild elsewhere. Improving: bring more materials, spend days = target Force. Temporary lodge via reagents: drams = Force, hours to build = Force, lasts until next sunrise/sunset.

---

## Perceiving Magic (Noticing magic)

Simple **Perception + Intuition [Mental]** Test. Threshold = caster's Skill Rating - Force of the magic, or **6 - Force** if no skill involved (minimum 1 either way). +2 dice pool if you have any magic-related Active or Knowledge skill. Obvious magic (fireballs, visible casting) needs no roll.

---

## Spellcasting

1. **Choose Spell:** must already know it.
2. **Choose Target(s):** natural vision (incl. Essence-paid cybereyes) or touch establishes the link; digitized feeds (cameras, Matrix) never work for LOS. Physical-world casters can only target physical-world targets; astral/dual-natured casters can target either plane, but only mana spells work in astral space. **Area spells:** sphere radius = Force in meters unless noted; hits all visible targets, friend and foe.
3. **Choose Force:** the Limit; up to **Magic x 2**. If hits (not net) after the Limit exceed Magic, Drain is Physical.
4. **Cast:** Complex Action (or **Reckless Spellcasting**: Simple Action, +3 Drain; two Simple-cast spells same Phase both get +3). Spellcasting + Magic [Force] +/- mods (wounds, **-2 per sustained spell** cumulative, visibility for LOS spells).
5. **Determine Effect:** resolve opposed test/threshold per spell; effect applies even if Drain later drops the caster.
6. **Resist Drain:** tradition Drain pool; each hit reduces Drain by 1; min DV 2.
7. **Ongoing Effects:** sustained spells keep the -2/spell penalty. Sustained area spells can be moved as a Complex Action within LOS; targets entering/leaving the area gain/lose the effect accordingly.

**Multi-spell casting:** Split Spellcasting + Magic dice pool among spells (min 1 die each); per-spell modifiers apply after the split; max simultaneous spells = Magic.

**Glitch:** extra Drain (+2 typical), wrong element, wrong target, or GM mischief. Critical glitch: spell can get away from you, no Drain resistance, or worse.

### Combat spell patterns

| Type | Opposed / Damage |
| --- | --- |
| Direct | Spellcasting + Magic [Force] vs Body (physical spell) or Willpower (mana spell); net hits = boxes of damage; no separate Damage Resistance |
| Indirect | Spellcasting + Magic [Force] vs Reaction + Intuition; DV = Force + net hits; AP = -(Force); resisted with Body + Armor. Area indirect: Spellcasting + Magic [Force] (3) vs scatter 2D6m like a grenade; net hits add to DV if threshold beaten, else reduce scatter |

---

## Spell Catalog (Core)

Drain values assume Force F; minimum Drain is always 2. "Kind" lists the spell's keywords (see category notes below each table).

### Combat Spells

Direct spells: net hits = damage boxes, opposed by target's Body (P) or Willpower (M), no separate resistance. Indirect spells: DV = Force + net hits, AP = -(Force), resisted with Body + Armor. Elemental spells apply their listed special damage type (Acid/Fire/Electricity).

| Spell | Kind | Type | Range | Dmg | Duration | Drain |
| --- | --- | --- | --- | --- | --- | --- |
| Acid Stream | Indirect, Elemental | P | LOS | P | I | F-3 |
| Toxic Wave | Indirect, Elemental (A) | P | LOS (A) | P | I | F-1 |
| Punch | Indirect | P | T | S | I | F-6 |
| Clout | Indirect | P | LOS | S | I | F-3 |
| Blast | Indirect (A) | P | LOS (A) | S | I | F |
| Death Touch | Direct | M | T | P | I | F-6 |
| Manabolt | Direct | M | LOS | P | I | F-3 |
| Manaball | Direct (A) | M | LOS (A) | P | I | F |
| Flamethrower | Indirect, Elemental (Fire) | P | LOS | P | I | F-3 |
| Fireball | Indirect, Elemental (Fire, A) | P | LOS (A) | P | I | F-1 |
| Lightning Bolt | Indirect, Elemental (Electricity) | P | LOS | P | I | F-3 |
| Ball Lightning | Indirect, Elemental (Electricity, A) | P | LOS (A) | P | I | F-1 |
| Shatter | Direct | P | T | P | I | F-6 |
| Powerbolt | Direct | P | LOS | P | I | F-3 |
| Powerball | Direct (A) | P | LOS (A) | P | I | F |
| Knockout | Direct | M | T | S | I | F-6 |
| Stunbolt | Direct | M | LOS | S | I | F-3 |
| Stunball | Direct (A) | M | LOS (A) | S | I | F |

Notes: Acid Stream/Toxic Wave = Acid damage, corrosive. Flamethrower/Fireball = Fire damage, can ignite flammables. Lightning Bolt/Ball Lightning = Electricity damage. Punch/Clout/Blast = Stun psychokinetic force (Punch is touch-only). Death Touch/Manabolt/Manaball and Shatter/Powerbolt/Powerball = Physical damage lines (mana vs physical energy respectively). Knockout/Stunbolt/Stunball = Stun "sleep" mana line.

### Detection Spells

Standard sense range = Force x Magic meters (radius); Extended-range versions = Force x Magic x 10 meters. **Active** spells: Opposed Spellcasting + Magic [Force] vs Willpower + Logic (+Counterspelling) [Mental] for living targets, Force x 2 for magical objects, or Object Resistance for mundane objects; Counterspelling can defend even if target is unaware. **Passive** spells: always on, no interpretation test; while sustained, Perception Tests with the sense use net hits from casting as their limit; cannot be Counterspelled (only dispelled).

| Spell | Kind | Type | Range | Duration | Drain |
| --- | --- | --- | --- | --- | --- |
| Analyze Device | Active, Directional | P | T | S | F-3 |
| Analyze Magic | Active, Directional | P | T | S | F-3 |
| Analyze Truth | Active, Directional | M | T | S | F-2 |
| Clairaudience | Passive, Directional | M | T | S | F-3 |
| Clairvoyance | Passive, Directional | M | T | S | F-3 |
| Combat Sense | Passive, Psychic | M | T | S | F |
| Detect Enemies | Active, Area | M | T | S | F-2 |
| Detect Enemies, Extended | Active, Extended Area | M | T | S | F |
| Detect Individual | Active, Area | M | T | S | F-3 |
| Detect Life | Active, Area | M | T | S | F-3 |
| Detect Life, Extended | Active, Extended Area | M | T | S | F-1 |
| Detect [Life Form] | Active, Area | M | T | S | F-2 |
| Detect [Life Form], Extended | Active, Extended Area | M | T | S | F |
| Detect Magic | Active, Area | M | T | S | F-2 |
| Detect Magic, Extended | Active, Extended Area | M | T | S | F |
| Detect [Object] | Active, Area | P | T | S | F-2 |
| Mindlink | Active, Psychic | M | T | S | F-1 |
| Mind Probe | Active, Directional | M | T | S | F |

Effects: Analyze Device = net hits give info about a device + bonus die operating it. Analyze Magic = treat net hits as hits on the Assensing Table without needing astral perception. Analyze Truth = detects if target's spoken statement is a lie (1+ net hit). Clairaudience/Clairvoyance = remote hearing/sight point, movable as Complex Action, blocks normal use of that sense. Combat Sense = +1 die/hit to Surprise and to defend vs ranged/melee. Detect Enemies = senses hostile intent aimed at subject. Detect Individual = senses a specific known person in range. Detect Life = senses living beings' number/location (crowds blur results); see Detection Results table below. Detect [Life Form] = as Detect Life but one species (separate spells). Detect Magic = senses foci/spells/wards/lodges/preparations/active rituals/spirits (not Awakened people or signatures). Detect [Object] = senses a specified object type (separate spells). Mindlink = 2-way mental link with a willing subject. Mind Probe = telepathically read a target's mind (target knows); see Mind Probe table below.

**Detection Spell Results (net hits, e.g. Detect Life):** 1 = general knowledge only. 2 = major details, no minor. 3 = major + some minor details. 4+ = fully detailed information.

**Mind Probe Table:** 1-2 hits = surface thoughts only. 3-4 hits = anything consciously known + recent memories (72 hrs). 5+ hits = subconscious: fears, quirks, hidden memories.

### Health Spells

All require touching the subject. Most are a simple Spellcasting + Magic [Force] Test (exceptions noted). "Essence" keyword: dice pool penalty equal to (target's actual Essence - max Essence), rounded up (0 or negative).

| Spell | Keyword | Type | Range | Duration | Drain |
| --- | --- | --- | --- | --- | --- |
| Antidote | | M | T | P | F-3 |
| Cure Disease | Essence | M | T | P | F-4 |
| Decrease [Attribute] | Essence | P | T | S | F-2 |
| Detox | | M | T | P | F-6 |
| Heal | Essence | M | T | P | F-4 |
| Increase [Attribute] | Essence | P | T | S | F-3 |
| Increase Reflexes | Essence | P | T | S | F |
| Oxygenate | | P | T | S | F-5 |
| Prophylaxis | | M | T | S | F-4 |
| Resist Pain | | M | T | P | F-4 |
| Stabilize | | M | T | P | F-4 |

Effects: Antidote = adds spell hits to target's Toxin Resistance Test (cast before that test). Cure Disease = net hits become bonus dice to Disease Resistance until recovery/death; does not heal existing damage. Decrease/Increase [Attribute] = opposed by (Attribute+Willpower); one spell per Physical/Mental attribute (not Special attrs); Increase caps at augmented max, Decrease to 0 incapacitates (Physical) or confuses (Mental). Detox = Force must equal/exceed toxin's base DV; removes side effects, not damage. Heal = heals Physical boxes = hits; hits can instead cut the time-to-permanent (1 Combat Turn/hit); remaining damage needs natural healing. Increase Reflexes = +1 Initiative/hit, +1 Initiative Die per 2 hits (max +5D6 total); one at a time. Oxygenate = +1 Body die/hit vs suffocation/drowning/gas; lets subject breathe underwater. Prophylaxis = +1 die/hit resisting infection/drugs/toxins (also blocks beneficial drugs: -1 bonus/hit, 3+ hits blocks non-bonus effects). Resist Pain = removes wound penalty per hit (not the damage itself); one active at a time (highest hits); ends if damage changes or heals. Stabilize = Force must equal/exceed overflow damage; prevents death from Physical Overflow; full time needed unless hits reduce it (1 Combat Turn/hit).

### Illusion Spells

Illusions never cause direct physical harm. **Mana illusions:** resisted by Logic + Willpower; ineffective vs cameras/tech; astral perception always sees through them (Assensing can't be fooled). **Physical illusions:** resisted by Intuition + Logic (or Object Resistance for devices); affect both living and tech; caster must beat the resister's hits to be "real."

| Spell | Kind | Type | Range | Duration | Drain |
| --- | --- | --- | --- | --- | --- |
| Agony | Realistic, Single-Sense | M | LOS | S | F-4 |
| Mass Agony | Realistic, Single-Sense (A) | M | LOS (A) | S | F-2 |
| Bugs | Realistic, Multi-Sense | M | LOS | S | F-3 |
| Swarm | Realistic, Multi-Sense (A) | M | LOS (A) | S | F-1 |
| Confusion | Realistic, Multi-Sense | M | LOS | S | F-3 |
| Mass Confusion | Realistic, Multi-Sense (A) | M | LOS (A) | S | F-1 |
| Chaos | Realistic, Multi-Sense | P | LOS | S | F-2 |
| Chaotic World | Realistic, Multi-Sense (A) | P | LOS (A) | S | F |
| Entertainment | Obvious, Multi-Sense (A) | M | LOS (A) | S | F-3 |
| Trid Entertainment | Obvious, Multi-Sense (A) | P | LOS (A) | S | F-2 |
| Invisibility | Realistic, Single-Sense | M | LOS | S | F-2 |
| Improved Invisibility | Realistic, Single-Sense | P | LOS | S | F-1 |
| Mask | Realistic, Multi-Sense | M | T | S | F-2 |
| Physical Mask | Realistic, Multi-Sense | P | T | S | F-1 |
| Phantasm | Realistic, Multi-Sense (A) | M | LOS (A) | S | F-1 |
| Trid Phantasm | Realistic, Multi-Sense (A) | P | LOS (A) | S | F |
| Hush | Realistic, Single-Sense (A) | M | LOS (A) | S | F-2 |
| Silence | Realistic, Single-Sense (A) | P | LOS (A) | S | F-1 |
| Stealth | Realistic, Single-Sense | P | LOS | S | F-2 |

Effects: Agony/Mass Agony = illusory pain, 1 Physical + 1 Stun box (fake) per net hit; full boxes = helplessly racked with pain; ends instantly on drop. Bugs/Swarm = -2 Initiative Score per net hit (per turn if sustained). Confusion/Mass Confusion (mana) and Chaos/Chaotic World (physical, also hits tech/sensors) = -1 dice pool per net hit. Entertainment/Trid Entertainment = obvious captivating illusion, not deceptive; Trid also works on tech. Invisibility/Improved Invisibility = visual stealth; caster rolls once, hits become threshold for later resistance; Improved also fools tech sensors. Mask/Physical Mask = touch-cast disguise of appearance/voice/scent; Physical also fools tech. Phantasm/Trid Phantasm = area illusion of any object/scene caster has seen; Trid also fools tech. Hush/Silence = dampens sound in area, -1 die/hit to sonic attacks; Silence also jams tech (alarms, sonar). Stealth = makes subject's own noise quieter.

### Manipulation Spells

Keywords: **Damaging** = DV equal to Force (unmodified by hits), 0 AP, resisted Body + Armor. **Mental** = resisted Logic + Willpower; net hits gate sustain duration; target can spend a Complex Action to fight free (Logic+Willpower vs penalty = spell Force; each hit reduces caster's net hits by 1; spell ends at 0). **Environmental** = affects an area, no single target. **Physical** = resisted by living target's Body+Strength or object's Object Resistance.

| Spell | Kind | Type | Range | Duration | Drain |
| --- | --- | --- | --- | --- | --- |
| Animate | Physical | P | LOS | S | F-1 |
| Mass Animate | Physical (A) | P | LOS (A) | S | F+1 |
| Armor | Physical | P | LOS | S | F-2 |
| Control Actions | Mental | M | LOS | S | F-1 |
| Mob Control | Mental (A) | M | LOS (A) | S | F+1 |
| Control Thoughts | Mental | M | LOS | S | F-1 |
| Mob Mind | Mental (A) | M | LOS | S | F+1 |
| Fling | Physical, Damaging | P | LOS | I | F-2 |
| Ice Sheet | Environmental (A) | P | LOS (A) | I | F |
| Ignite | Physical | P | LOS | P | F-1 |
| Influence | Mental | M | LOS | P | F-1 |
| Levitate | Physical | P | LOS | S | F-2 |
| Light | Environmental (A) | P | LOS (A) | S | F-4 |
| Magic Fingers | Physical | P | LOS | S | F-2 |
| Mana Barrier | Environmental (A) | M | LOS (A) | S | F-2 |
| Physical Barrier | Environmental (A) | P | LOS (A) | S | F-1 |
| Poltergeist | Environmental (A) | P | LOS (A) | S | F-2 |
| Shadow | Environmental (A) | P | LOS (A) | S | F-3 |

Effects: Animate/Mass Animate = move inanimate object(s) per net hits vs Object Resistance (+2 per full 200kg over 200kg); Simple Action to control; max speed = Force m/turn. Armor = Armor rating = hits, cumulative, no encumbrance. Control Actions/Mob Control = puppeteer target's body (own skills used), Complex Action per command. Control Thoughts/Mob Mind = command target's mind directly, obeys as own idea. Fling = throws an object up to Force kg, uses Spellcasting vs Ranged Combat, Magic instead of Strength for DV/range (grenade ranges). Ice Sheet = slick area, Agility+Reaction test (threshold = hits) or fall prone; vehicles Crash Test; melts naturally. Ignite = sets target ablaze once permanent (Object Resistance for objects, Body+Reaction opposed for living targets); Fire damage. Influence = single post-hypnotic suggestion, fades after minutes = net hits, resistible per Mental Manipulation rules. Levitate = telekinetic lift/move, threshold = mass/200kg; unwilling target/holder resists Strength+Body. Light = mobile light source, radius = Force meters, offsets darkness penalties (1 die/hit). Magic Fingers = telekinetic hand, hits = effective Strength/Agility, uses Force as limit for remote skill use. Mana Barrier = mana barrier (see Mana Barriers section), rating = net hits, blocks spirits/foci/spells, not living beings/objects. Physical Barrier = physical wall/dome, Armor+Structure = hits each, regenerates each Combat Turn while sustained, collapses at Structure 0. Poltergeist = whirls small objects, Light Fog visibility penalty, 2 Stun boxes/turn to those inside (Body+Armor resisted). Shadow = darkness globe, +1 light category per 2 hits (max Total Darkness).

---

## Counterspelling

Counterspelling grants **spell defense** and **dispelling**. Does not work vs spirit/critter powers or alchemical preparations.

### Spell Defense (including protecting others)

Declare protection as a Free Action (or Interrupt Action, -5 Initiative Score, if no Free Action left) against any hostile spell cast at you or at anyone in your line of sight. You have a **Counterspelling-rated dice pool** per Combat Turn (refreshes each Turn). Per incoming spell, allocate some/all remaining dice and choose who they cover, up to **Magic rating** people at once (including yourself); those dice add to each covered person's Defense Test against that spell.

### Dispelling

Targets a **sustained or quickened spell**. Dispelling Test: **Counterspelling + Magic [Astral]** vs (spell's Force + caster's Magic + Karma spent quickening, if any). May use a counterspelling focus or reagents (set the limit). Every net hit reduces the caster's original casting hits by 1; at 0 hits the spell ends completely. Dispeller takes Drain as if they had cast the spell (Physical if the spell's Force > dispeller's Magic, else Stun).

**Dispelling a ritual:** requires a spell keyword and an ongoing duration. Opposed Counterspelling + Magic [Astral] vs (ritual's Force + sum of all participants' Magic). Net hits reduce the ritual's sealing net hits by 1 each. Drain = 2x hits (not net) on the opposing test; Physical if ritual Force > dispeller's Magic.

#### Object Resistance Table

| Initiative Type | Dice Pool |
| --- | --- |
| Natural objects (trees, soil, hand-worked metal) | 3 |
| Manufactured low-tech (brick, leather, simple plastics) | 6 |
| Manufactured high-tech (alloys, electronics, sensors) | 9 |
| Highly processed (computers, drones, vehicles) | 15+ |

---

## Ritual Spellcasting

Rituals shape mana over a longer time than spellcasting allows. Learned separately from spells (same Karma cost), but a spell woven into a ritual (e.g. Prodigal Spell) does not need separate learning.

1. **Choose Ritual Leader:** must know the ritual and perform the final sealing step. Participants of a different tradition take -2 to all actions for the ritual.
2. **Choose Ritual** (and any spell it requires; only the leader needs to know it).
3. **Choose the Force** of the ritual (and of any woven spell).
4. **Set Up the Foundation:** a magical lodge of the leader's tradition, Force >= ritual Force. No participant (except a spotter) may leave before completion or the ritual fails.
5. **Give the Offering:** leader spends reagents = ritual Force; extra reagents (per Force spent, after the initial offering) reduce Drain by 1 each, min 2.
6. **Perform the Ritual:** duration per ritual description, usually based on Force.
7. **Seal the Ritual:** Leader's **Ritual Spellcasting + Magic [Force]** vs (Force x 2), with Teamwork from participants. Net hits resolve the ritual's effect per its description. Every participant then takes Drain = 2x hits (not net) on the defense side, min 2; Physical if leader's hits > her Magic.

**Failure:** leaving the foundation, leader incapacitated/killed, or foundation disrupted after Step 4 all fail the ritual; everyone still takes Drain (Force x 2 test, Stun, 2x hits).

**Glitch:** extra Drain, +2 to resisting Force, or leader forced to seal alone. Critical: GM's call, up to metaplanar mishap.

### Rituals (Core)

Keywords: **Anchored** = needs a physical/mystic anchor object that cannot move for the duration. **Material Link** = needs something once part of the target (see Material Link sidebar below). **Minion** = creates a semi-autonomous entity bound to the leader (max minions = Charisma). **Spell** = incorporates a spell the leader knows; susceptible to dispelling. **Spotter** = needs a team member (or their bound spirit) to astrally assense a target the leader can't see.

| Ritual | Keywords | Duration to Perform | Effect |
| --- | --- | --- | --- |
| Curse | Material Link, Spell | Force hours | Casts a chosen Illusion spell through a material link instead of LOS; link destroyed as offering |
| Prodigal Spell | Spell, Spotter | Force hours | Casts any Combat spell (direct or indirect) at a distant target out of LOS |
| Remote Sensing | Spell, Spotter | Force hours | Casts any Detection spell with range = Force x (sum of participants' Magic) x 100m; subject can leave the foundation |
| Ward | Anchored | Force hours | Astral barrier, Force = ritual Force, volume up to 50m^3 x sum of Magic; lasts weeks = net hits (permanent if leader spends Karma = Force) |
| Circle of Protection | Anchored | Force hours | Physical + mana barrier sphere, radius = leader's Magic, Force = ritual Force; lasts hours = net hits; ends if crossed from inside |
| Circle of Healing | Anchored, Spell | Force hours | Applies a Health spell to everyone inside a sphere (radius = leader's Magic); net hits = spell's net hits; lasts Force days |
| Renascence | Anchored, Spell | Force hours | Sustains an area Manipulation spell in a sphere (radius = leader's Magic); base 1 hour duration, doubled per net hit |
| Watcher | Minion | Force minutes | Creates a Watcher (see stat block); bound to leader only; lasts Force x net hits hours; dismissed as Free Action |
| Homunculus | Minion | Force hours | Animates an inanimate object (<= Force x 10 kg) into a servant; lasts Force x net hits days |

**Material Link:** an integral part of the target (structural piece of an object; tissue sample of a living being). Living-being links decay: hair/fluids/clippings last a few hours, larger tissue a few days; chemical preservation destroys viability; freezing preserves it.

#### Watcher / Homunculus Stat Blocks

**Watcher** (no corporeal body; B/A/R/S = "-"): W/L/I/C = F-2. Astral Initiative (Fx2)+1D6. Skills: Assensing, Astral Combat, Perception. Powers: Astral Form, Manifest, Search, Sapience.

**Homunculus** (physical body, Structure = material used): A/R = F-2, S = F, W/L/I = 1. Initiative (F+1)+1D6. Movement x2/x4/+1. Skills: Assensing, Astral Combat, Perception, Unarmed Combat. Powers: Sapience.

---

## Learning Spells, Rituals, and Preparations

Need a **magical lodge of your tradition** plus either a spell/ritual formula (buy from talismongers, see [Magical Goods](../Encyclopedia/Magical%20Goods.md)) or a teacher (charges roughly Instruction skill x formula cost in nuyen).

**Learning Test:** Simple **(Spellcasting, Ritual Spellcasting, or Alchemy) + Intuition [lodge's Force]** Test. Time to learn = 12 days / hits. A teacher can add dice via an Instruction Test. Spend **5 Karma** at the end to learn it. Different-tradition formula/teacher: -4 penalty. Must spend 8 hours/day studying or restart. Zero hits = fail (no Karma spent, instruction fees lost).

**Alchemy (preparations) overview:** Alchemy lets a magician imbue a small object (a "lynchpin") with a spell to release later, following steps like Spellcasting but with an added **trigger** (Command +2 Drain, Contact +1 Drain, Time +2 Drain) and a **Potency** (net hits on Alchemy + Magic [Force] vs Force) instead of a live Spellcasting roll. Potency stays full for (Potency x 2) hours, then decays 1/hour; lynchpin breaking or Potency 0 destroys the preparation. When triggered, it resolves like a cast spell using Potency in place of Spellcasting and the preparation's Force in place of Magic/limit; no further Drain (already paid at creation) and no Edge can be spent on activation.

**Foci activation basics:** Bond a focus (Karma cost by type, see Foci below) before use; bonding takes 1 hour/Force. Activating a bonded focus is a **Simple Action**; deactivating is a **Free Action**. A focus deactivates automatically if you lose possession or consciousness. Max bonded foci = Magic; max total Force of bonded foci = Magic x 5; only one focus's Force can apply to any single test.

---

## Conjuring

### Summon (Complex Action)

1. Choose a spirit type available to your tradition and its **Force** (<= Magic x 2). Optional powers: 1 per 3 full points of Force (Force 1-2 = 0, 3-5 = 1, 6-8 = 2, etc.), fixed once summoned.
2. **Summoning + Magic [Force]** vs spirit's Force (Opposed). Reagents can set the limit. Net hits = services owed. No net hits: spirit doesn't show.
3. **Resist Drain:** DV = 2x hits (not net) on the spirit's side, min 2; Physical if spirit's Force > your Magic.

Spirit hangs until services are done or **sunrise/sunset**, whichever first. Only **one summoned spirit at a time** (unbound). **Group summoning:** Teamwork test; all pay the same Drain; only the leader commands the spirit.

### Bind

Requires an already-summoned spirit. Takes **1 hour x Force**; costs **Force x 25 drams** of reagents. **Binding + Magic [Force]** vs (spirit's Force x 2), Opposed. Drain = 2x hits (not net) on spirit's side, min 2. Extra net hits beyond the first add services owed. Bound spirits don't expire at sunrise/sunset; call/dismiss with a Simple Action. Max bound spirits = **Charisma**.

### Banish (Complex Action)

**Banishing + Magic [Astral]** vs spirit's Force (+ summoner's Magic if bound), Opposed; reagents can set the limit. Each net hit removes 1 owed service; at 0 the spirit leaves on its next action. Drain = 2x hits (not net) on spirit's side, min 2; Physical if spirit's Force > your Magic. Before it departs, anyone present may attempt to **Summon** it fresh (any tradition, since it's already manifest).

**Edge:** Summoner's Edge applies to conjuring tests like other Magician tests (see [Edge](Edge.md)); spirits do not have/spend their own Edge, but the summoner can spend Edge on the spirit's tests.

Disruption (filling a spirit's Condition Monitor) sends it home and **loses all remaining services**.

### Spirit Basics

Spirits exist astrally with astral attributes = Force; must **materialize** to affect the physical plane (dual-natured while materialized). Combat follows normal rules; a filled Condition Monitor disrupts the spirit (sent home, services lost). **Spirit-Summoner Link:** telepathic, no metaplane range limit, summoner feels a disruption instantly. **Spirit Range:** cannot move farther than Magic x 100 meters from summoner without it counting as a remote service (and being released on completion). Movement: Walk = Agility x2, Run = Agility x4, ignores gravity.

#### Spirit Services

Services owed = net hits on Summoning/Binding. Lost if time runs out (unbound, sunrise/sunset).

| Unbound Spirit Services | Bound Spirit Services (also gets all unbound options) |
| --- | --- |
| Combat (whole fight = 1 service) | Aid Alchemy/Sorcery/Study (+Force dice, matching category) |
| Power use (1 target/action, sustain included) | Spell Sustaining (spirit takes -2/spell instead of you, up to Force Combat Turns/service) |
| Physical task (materialize to act) | Spell Binding (spell sustains indefinitely; spirit's Force drops 1/day, dissipates at 0; considered abusive) |
| Remote service (beyond Magic x100m; spirit released after, regardless of remaining services) | |

### Spirits (Core, 6 types)

Physical attributes apply when materialized (minimum rating 1 even if formula is lower). Skills = Force rating. Optional powers: 1 per 3 full points of Force, fixed at summoning.

**Spirits of Air:** B F-2, A F+3, R F+4, S F-3, W F, L F, I F, C F, EDG F/2, ESS F, M F. Initiative (Fx2)+4+2D6; Astral Initiative (Fx2)+3D6. Skills: Assensing, Astral Combat, Exotic Ranged Weapon, Perception, Running, Unarmed Combat. Powers: Accident, Astral Form, Concealment, Confusion, Engulf, Materialization, Movement, Sapience, Search. Optional: Elemental Attack, Energy Aura, Fear, Guard, Noxious Breath, Psychokinesis. +10m/hit Sprinting.

**Spirits of Beasts:** B F+2, A F+1, R F, S F+2, W F, L F, I F, C F, EDG F/2, ESS F, M F. Initiative (Fx2)+2D6; Astral (Fx2)+3D6. Skills: Assensing, Astral Combat, Perception, Unarmed Combat. Powers: Animal Control, Astral Form, Enhanced Senses (Hearing, Low-Light, Smell), Fear, Materialization, Movement, Sapience. Optional: Concealment, Confusion, Guard, Natural Weapon (Claws/Bite: DV Force P), Noxious Breath, Search, Venom.

**Spirits of Earth:** B F+4, A F-2, R F-1, S F+4, W F, L F-1, I F, C F, EDG F/2, ESS F, M F. Initiative ((Fx2)-1)+2D6; Astral (Fx2)+3D6. Skills: Assensing, Astral Combat, Exotic Ranged Weapon, Perception, Unarmed Combat. Powers: Astral Form, Binding, Guard, Materialization, Movement, Sapience, Search. Optional: Concealment, Confusion, Engulf, Elemental Attack, Fear.

**Spirits of Fire:** B F+1, A F+2, R F+3, S F-2, W F, L F, I F+1, C F, EDG F/2, ESS F, M F. Initiative ((Fx2)+3)+2D6; Astral (Fx2)+3D6. Skills: Assensing, Astral Combat, Exotic Ranged Weapon, Flight, Perception, Unarmed Combat. Powers: Accident, Astral Form, Confusion, Elemental Attack, Energy Aura, Engulf, Materialization, Sapience. Optional: Fear, Guard, Noxious Breath, Search. Weakness: Allergy (Water, Severe). +5m/hit Sprinting.

**Spirits of Man:** B F+1, A F, R F+2, S F-2, W F, L F, I F+1, C F, EDG F/2, ESS F, M F. Initiative ((Fx2)+2)+2D6; Astral (Fx2)+3D6. Skills: Assensing, Astral Combat, Perception, Spellcasting, Unarmed Combat. Powers: Accident, Astral Form, Concealment, Confusion, Enhanced Senses (Low-Light, Thermographic), Guard, Influence, Materialization, Sapience, Search. Optional: Fear, Innate Spell (any spell known by summoner, Force limited to spirit's Magic), Movement, Psychokinesis.

**Spirits of Water:** B F, A F+1, R F+2, S F, W F, L F, I F, C F, EDG F/2, ESS F, M F. Initiative ((Fx2)+2)+2D6; Astral (Fx2)+3D6. Skills: Assensing, Astral Combat, Exotic Ranged Weapon, Perception, Unarmed Combat. Powers: Astral Form, Concealment, Confusion, Engulf, Materialization, Movement, Sapience, Search. Optional: Accident, Binding, Elemental Attack, Energy Aura, Guard, Weather Control. Weakness: Allergy (Fire, Severe). Moves 2x speed in water.

**See also:** the powers listed above (base and optional) are only named here. For the full mechanics of each (Type/Action/Range/Duration, Opposed Test formulas, DV/AP, etc.) needed to actually run a spirit fighting or using its powers, see [Critter and Spirit Powers](Critter%20and%20Spirit%20Powers.md).

---

## Enchanting

### Alchemy (preparations)

1. **Choose Spell:** the alchemical version of a Sorcery spell you separately know (same Drain/keywords as the spell).
2. **Choose Force** (<= Magic x2, the limit).
3. **Choose the Lynchpin:** a small object with no existing aura (no living beings); high-tech is fine, since it's not being enchanted, just anchoring.
4. **Choose Trigger:** Command (+2 Drain, you trigger it, Simple Action, LOS, only trigger allowed for healing preps), Contact (+1 Drain, next touch triggers it), or Time (+2 Drain, countdown set at creation, must be <= final Potency in hours or it fires early).
5. **Create:** minutes = Force, uninterrupted. Reagents used here set the limit instead of Force.
6. **Test:** Alchemy + Magic [Force] vs Force; net hits = **Potency**. Zero net hits = failure (time/Drain still spent).
7. **Resist Drain:** spell's Drain + trigger's bonus; Physical if hits > Magic.

Potency stays full (Potency x2) hours, then -1/hour; lynchpin breaking or Potency 0 kills it. Using it: resolves like a cast spell (Potency replaces Spellcasting, Force replaces Magic/limit); no further Drain, no Edge. Touch spells affect whoever touches it (or magician's choice with Command); LOS spells hit nearest/chosen target within (Potency x Force) meters; Area spells center on the preparation, radius = Potency.

### Artificing (foci creation)

1. **Choose Focus Formula:** buy or research (Arcana + Magic [Astral], Force x Force days, Extended Test); Force must be <= your Magic.
2. **Obtain the Telesma:** an object matching the formula's specified form.
3. **Prepare a Lodge:** Force >= formula Force, same tradition.
4. **Spend Reagents:** drams = Karma cost to bond the focus at formula Force, min Force drams; spent even on failure.
5. **Craft:** days = formula Force. Then **Artificing + Magic [formula Force]** vs (formula Force + telesma's Object Resistance); no Edge on this roll. Net hits = the focus's actual Force.
6. **Resist Drain:** DV = formula Force + 2/hit (not net) against you; Physical if actual Force > your Magic. If conscious, spend Karma = actual Force to finish (seal) it.

**Artifact Assensing:** Artificing + Magic [Astral] vs (2x focus Force), Opposed; net hits reveal the artificer's aura details per the Assensing Table. Once/day per focus.

### Disenchanting / Disjoining

**Deactivate a focus:** Opposed Disenchanting + Magic [Astral] vs (target's Force + owner's Magic); LOS needed (physical or astral). More successes = deactivates.

**Destroy a focus (recycle to reagents):** touch contact; Opposed Disenchanting + Magic [Astral] vs (target's Force, + owner's Magic if bonded and not yours). Success destroys the telesma; then Alchemy + Magic [Astral], 1 reagent/success up to 1/3 of the reagents originally used; takes hours = target's Force. Drain (all these tests) = 1S/hit (not net) against you; Physical if target's Force > your Magic; cannot attempt if target's Force > 2x your Magic.

**Disjoining** (removes magic from a preparation, like dispelling for Alchemy): must have identified it as a preparation (assensing) and touch it. Complex Action; Opposed Disenchanting + Magic [Astral] vs (preparation's Force + alchemist's Magic + quickening Karma if any). Net hits reduce Potency by 1 each. Take Drain as if you'd created the preparation. Risk: a Contact-trigger preparation fires if you fail the test.

---

## Adepts

**Power Points:** Adepts get PP = Magic at chargen. Mystic adepts buy PP with **Karma (5/PP, max = Magic)**, no free PP on Magic increase. Adepts get **+1 PP whenever Magic rises**, or can take a PP instead of a metamagic at Initiation. Max levels of any one power = Magic (or the power's own listed cap, if lower). Essence loss that drops Magic also drops PP by the same amount (un-buy powers); Magic 0 cuts you off from magic entirely.

**Using Powers:** Powers with an Activation cost need that action each use; powers with none are always-on (intrinsic). **Adept Drain** (where a power causes it) is Stun unless stated, resisted with **Body + Willpower**.

### Adept Powers (Core)

| Power | Cost | Activation | Effect |
| --- | --- | --- | --- |
| Adrenaline Boost | 0.25 PP/level | Free Action | +2 Initiative Score/level this Turn; next turn take Drain = levels |
| Astral Perception | 1 PP | Simple Action | Grants Astral Perception (dual-natured, can fight astral forms) |
| Attribute Boost (Physical Attr) | 0.25 PP/level | Simple Action | Magic+rating Test; hits raise chosen Physical attr (to aug max) for 2x hits Combat Turns; Drain = level when it ends |
| Combat Sense | 0.5 PP/level | | +1 die/level defending ranged/melee; free Perception Test before surprise |
| Critical Strike (Skill) | 0.5 PP | | +1 DV with a chosen melee skill; stacks with weapons/other powers; buyable per skill |
| Danger Sense | 0.25 PP/level | | +1 die/level on Surprise Tests |
| Enhanced Perception | 0.5 PP/level | | +1 die/level to Perception and Assensing Tests |
| Enhanced Accuracy (Skill) | 0.25 PP | | +1 Accuracy with a chosen Combat Skill (not Unarmed); buyable per skill |
| Improved Ability (Skill) | 0.5 PP/level | | +1 Rating/level to a known Combat/Physical/Social/Technical/Vehicle skill, max +1.5x current rating (rounded up) |
| Improved Physical Attribute | 1 PP/level | | +1 Physical attribute/level, exceeds natural max up to augmented max |
| Improved Potential (Limit) | 0.5 PP/level | | +1 to one inherent limit (Physical/Mental/Social); buyable per limit |
| Improved Reflexes | 1.5/2.5/3.5 PP (Lv1/2/3) | | +1 Reaction and +1D6 Initiative Die per level (max 3 levels); no stacking with other Initiative boosts |
| Improved Sense | 0.25 PP each | | Grants a sensory upgrade (low-light, thermographic, Direction Sense, Improved Tactile, Perfect Pitch, Human Scale, etc.) |
| Killing Hands | 0.5 PP | Free Action | Unarmed attacks can deal Physical damage (magical, bypasses Immunity to Normal Weapons; usable in astral combat) |
| Kinesics | 0.25 PP/level | | +1/level to resist Social Tests and tests reading your emotions/truthfulness (Judge Intentions, Assensing) |
| Light Body | 0.25 PP/level | | +level to Agility for jump distance; +1 die/level Gymnastics for jumps; reduces effective fall distance by level (m) |
| Missile Parry | 0.25 PP/level | Interrupt (-5 Init) | +1 die/level defending vs a ranged attack; net hits catch the projectile; needs a free hand |
| Mystic Armor | 0.5 PP/level | | +1 Armor/level, cumulative, no encumbrance; also protects in astral combat |
| Natural Immunity | 0.25 PP/level | | +1 die/level resisting toxins/disease |
| Pain Resistance | 0.5 PP/level | | Wound penalties kick in 1 box later/level (Physical & Stun); +2 dice/level resisting torture/suffering |
| Rapid Healing | 0.5 PP/level | | +1 die/level to Body for Healing Tests and to any test healing you (magical or mundane) |
| Spell Resistance | 0.5 PP/level | | +1 die/level resisting spells, spell rituals, preparations, or Innate Spell critter power |
| Traceless Walk | 1 PP | | No footstep noise/traces even on snow/sand; -4 to hearing Perception vs you; no pressure/vibration sensors; -2 to Track vs you |
| Voice Control | 0.5 PP/level | | Mimic/mask voices (Opposed Impersonation+Charisma [Mental] vs Rating x2 or Perception+Intuition, +level bonus); +1/level Social limit |
| Wall Running | 0.5 PP | Simple Action | Running+Strength [Magic] Test; hits = meters climbed/run across a vertical surface this Phase; falls off at end of movement |

Improved Ability, Attribute Boost, Critical Strike, Enhanced Accuracy, and Improved Potential each require choosing a specific skill/attribute/limit when bought; can be bought multiple times for different choices.

---

## Mentor Spirits

Requires the **Mentor Spirit** quality. Mystic adepts must pick **either** the Magician **or** Adept bonus (not both) when taking the mentor, and can't change later. Bonuses/penalties apply at all times.

| Mentor | All bonus | Magician bonus | Adept bonus | Disadvantage (short) |
| --- | --- | --- | --- | --- |
| Bear | +2 resist damage (not Drain) | +2 Health spells/preps/rituals | 1 free level Rapid Healing | Risk of berserk on Physical damage / when a ward is hurt |
| Cat | +2 Gymnastics or Infiltration | +2 Illusion spells/preps/rituals | 2 free levels Light Body | Can't land a finishing blow without a Charisma+Willpower(3) Test; stops toying if hurt |
| Dog | +2 Tracking | +2 Detection spells/preps/rituals | 2 free Improved Sense | Can't abandon/betray comrades without a Charisma+Willpower(3) Test |
| Dragonslayer | +2 one Social skill | +2 Combat spells/preps/rituals | 1 free Enhanced Accuracy + 1 free Danger Sense | -1 all actions until a broken promise is made good |
| Eagle | +2 Perception | +2 summoning Spirits of Air | 1 free level Combat Sense | Allergy (pollutants, mild), no bonus Karma |
| Fire-Bringer | +2 Artisan or Alchemy | +2 Manipulation spells/preps/rituals | 1 free level Improved Ability (non-combat skill) | Can't refuse a sincere request for help without a Charisma+Willpower(3) Test |
| Mountain | +2 Survival | +2 Counterspelling + anchored rituals | 1 free level Mystic Armor | Must test Charisma+Willpower(3) to abandon a plan or to act without one |
| Rat | +2 Sneaking | +2 Alchemy (reagent harvesting) + any tradition's reagents | 2 free levels Natural Immunity | Must test Charisma+Willpower(3) to avoid fleeing combat |
| Raven | +2 Con | +2 Manipulation spells/preps/rituals | Free Traceless Walk + 1 level Voice Control | Must test Charisma+Willpower(3) to resist a prank/exploiting misfortune |
| Sea | +2 Swimming | +2 summoning Spirits of Water | 1 free level Improved Ability (athletic skill) | Must test Charisma+Willpower(3) to give something away/be charitable |
| Seducer | +2 Con | +2 Illusion spells/preps/rituals | 1 free level Improved Ability (Acting/Influence group) | Must test Charisma+Willpower(3) to resist a vice/indulgence |
| Shark | +2 Unarmed Combat | +2 Combat spells/preps/rituals | Free Killing Hands | Risk of berserk on Physical damage in combat |
| Snake | +2 Arcana | +2 Detection spells/preps/rituals | 2 free levels Kinesics | Must test Charisma+Willpower(3) to resist pursuing secrets/knowledge |
| Thunderbird | +2 Intimidation | +2 summoning Spirits of Air | 1 free level Critical Strike (skill) | Must test Charisma+Willpower(3) to not respond to insults in kind |
| Wise Warrior | +2 Leadership or Instruction | +2 Combat spells/preps/rituals | 1 free level Improved Ability (Combat skill) | -1 all actions until atoning for a dishonorable act |
| Wolf | +2 Tracking | +2 Combat spells/preps/rituals | 2 free levels Attribute Boost (Agility) | Must test Charisma+Willpower(3) to retreat from a fight |
| Raven (Alt) * | +2 Knowledge skill tests | +2 Detection spells/preps/rituals **or** +2 Summoning with Code of Honor bargain (pick one) | 2 free levels Enhanced Perception | Cha+Wil(3) to resist acquiring valuable data/gear |
| Lion * | +2 Survival, Running, or Tracking (choose one) | +2 Combat spells/preps/rituals | 2 free levels Attribute Boost (Strength) | Never leave comrades; Cha+Wil(3) to flee before team safe; -2 limits on selfish actions |

\* *Book of the Lost*. Full write-up: [Magic Supplemental](Magic%20Supplemental.md).

---

## Astral

### Astral Perception

Dual-natured while perceiving (both planes at once); **-2** to physical actions. Available to magicians and to adepts with the Astral Perception power (not other metahumans). Simple **Assensing + Intuition [Astral]** Test to read an aura in detail; no test needed for obvious things. Full detail in the **Assensing Table** below.

#### Assensing Table

| Hits | Information gained |
| --- | --- |
| 0 | None |
| 1 | General health; general emotional state; mundane vs Awakened |
| 2 | Cyberware presence/location; magic class (fire elemental, manipulation spell, power focus, etc.); recognize a previously-read aura despite disguise |
| 3 | Alphaware presence/location; whether subject's Essence/Magic is higher/lower/equal to yours; whether Force is higher/lower/equal to your Magic; general disease/toxin diagnosis; astral signatures present |
| 4 | Bioware/betaware presence/location; exact Essence, Magic, Force; general cause of an astral signature |
| 5+ | Deltaware/gene treatment/nanotech presence; accurate disease/toxin diagnosis; whether subject is a technomancer |

**Astral Signature:** left on anything affected by magic; lasts hours = the effect's Force after it ends. Read with Assensing + Intuition [Astral]; recognizable again once read. A perceiving magician can spend a Complex Action (no test) to erase 1 hour of a signature's remaining life, repeatable; partial erasure is obvious as tampering.

### Astral Projection

**Full Magicians only.** Consciousness leaves the body (comatose, still linked for damage); astral form uses **mental attributes** (see Astral Attributes Table). Always astrally perceiving while projecting; can't target physical-world objects (only what's on your current plane), and mana spells only.

**Movement:** near-instant for nearby spots, blurred travel; deliberate "Walk" = 100m/Combat Turn, "Run" = 5km/Combat Turn (Running penalties apply). No gravity; blocked by the solid Earth and by mana barriers; altitude limit ~80km (madness/death beyond).

**Manifesting:** Complex Action to engage/disengage; appear as a ghostly, audible/visible image; cannot physically interact, cannot cast on physical targets, invisible to tech. Total manifesting time = **Magic x 5 minutes** per projection session.

**Staying Astral:** max duration = **Magic x 2 hours**; exceeding it kills your body. The clock pauses on return to body, but doesn't reset until you've spent at least as long back in the body as you spent out.

**Astral Attributes Table:**

| Physical Attribute | Astral Attribute |
| --- | --- |
| Agility | Logic |
| Body | Willpower |
| Reaction | Intuition |
| Strength | Charisma |
| Astral Initiative | Intuition x 2 |
| Initiative Dice | +2D6 (3D6 total) |

### Astral Detection

Physical beings may sense a passing astral form: **Perception + Intuition (4) [Mental]**, +2 if Awakened (this specialization is "Numinous Perception," also used for noticing magic).

### Astral Combat

Astrally perceiving/dual-natured characters use physical attributes/skills vs bodied foes, or **Astral Combat + Willpower** vs wholly astral entities. Astrally projecting characters use mental attributes (via Astral Attributes Table) with Astral Combat. No ranged weapons work astrally; only unarmed attacks, weapon foci, and mana spells.

| Attack | Test |
| --- | --- |
| Unarmed | Astral Combat + Willpower [Astral] vs Intuition + Logic |
| Weapon Focus | Astral Combat + Willpower [Accuracy] vs Intuition + Logic |

Base DV +1/net hit; attacker chooses Stun or Physical. Astral barriers can only be hurt by Physical damage.

| Source | Base Damage |
| --- | --- |
| Magician (unarmed) | Charisma |
| Weapon Focus | per weapon, using Charisma instead of Strength |
| Spirit | Force |
| Watcher | 1 |

### Astral Tracking

Spells, spirits, projecting magicians, foci, and lodges all carry an astral link back to their source. **Assensing + Intuition (5, 1 hour) [Astral] Extended Test** to follow it, modified by:

| Condition | Threshold mod |
| --- | --- |
| Each hour since the link was active | +1 |
| Target behind a mana barrier | +Force of barrier |
| Tracking a master via a bound spirit | +0 |
| Tracking a master via an unbound spirit | +2 |

---

## Mana Barriers / Wards

Mana barriers block spells and astral forms; may exist on the physical plane, astral plane, or both (dual-natured). **Physical-plane barriers:** invisible except to astral perception; casting through one adds the barrier's Force to the target's defense/resistance (or forces an Opposed Test at the barrier's Force if the spell has none). **Astral-plane barriers:** solid, hazy walls; block movement, impose a visibility penalty = Force, and resist astral spells/forms the same way. Creators pass through freely and can let others pass. Adept powers and most always-on critter powers ignore barriers (GM discretion for ranged/sustained ones).

| Mana Barrier Source | Astral / Physical |
| --- | --- |
| Circle of Protection ritual | Both |
| Magical Lodge | Both |
| Mana Barrier spell | Either (caster's choice) |
| Ward ritual | Both |

**Breaking through:** Armor and Structure = barrier's Force; regenerates fully each Combat Turn; creator is instantly aware of any attack. **Pressing through subtly:** Magic + Charisma [Astral] vs (barrier's Force x 2), Opposed; net hits let you (and 1 companion/foci/spell/astral form per net hit) through. Destroying the source (lodge, ritual anchor, sustaining caster) also drops the barrier, and the creator feels it happen.

**Astral Intersections:** when a barrier/astral form is dragged into contact with another (e.g. a warded van entering a warded garage), each side rolls Opposed: living beings Magic + Charisma, non-living barriers/objects Force x 2. Net-hit winner stays intact; the other(s) are disrupted (ties: everyone disrupted). Disruption: spells/rituals end, preparations go mundane, mana barriers collapse (regain Structure at end of Turn if permanent), foci deactivate, spirits banished, living creatures knocked unconscious (full Stun Monitor).

---

## Reagents

Reagents (measured in **drams of orichalcum**) are naturally mana-charged objects; type varies by tradition (Hermetic: minerals/ores/antiques; Shamanic: plant/animal parts, worn stones, handcrafted items). Off-tradition reagents work at **half strength**. Buy at 20 nuyen/dram from a talismonger.

**Uses:** set the limit (instead of Force/Astral limit) for Spellcasting, Summoning, Banishing, Counterspelling, Disjoining; required to Bind (Force x25 drams) and to Artifice (see Artificing); offset Ritual Spellcasting Drain (1 Drain/Force drams spent, after the offering); build a temporary Magical Lodge (drams = Force, hours to build = Force, lasts to next sunrise/sunset).

**Harvesting:** best in an environment matching your tradition, using Astral Perception; 1 hour searching, then **Alchemy + Magic [Mental]** Test: 1 dram per 2 hits (right environment) or per 4 hits (wrong environment). Harvesting taps a location out for **2 days per dram harvested** (roughly per hectare).

---

## Foci

Foci are astral constructs embedded in physical objects (the "telesma"); Force = power rating. Must be **bonded** (Karma cost by type, below) before use; bonding takes 1 hour/Force and breaks any prior bond. Activate (Simple Action) to use; stays active only while possessed; deactivates automatically if lost/unconscious; deactivate voluntarily as a Free Action. Max bonded foci = Magic; max total bonded Force = Magic x 5; only 1 focus's Force applies per test.

| Focus Type | Bonding Cost (Karma) | Effect summary |
| --- | --- | --- |
| Enchanting (Alchemical / Disenchanting) | Force x 3 | +Force dice to the matching Enchanting skill test |
| Metamagic (Centering / Flexible Signature / Masking / Spell Shaping) | Force x 3 | +Force to initiate grade for the matching metamagic (initiates only) |
| Power | Force x 6 | +Force to effective Magic rating (Sorcery/Conjuring/Enchanting pools and other Magic-linked tests) |
| Qi | Force x 2 | Grants/boosts one specific adept power at a specific level (adepts only); Force = 4x the power's PP cost |
| Spell (Counterspelling / Ritual Spellcasting / Spellcasting / Sustaining) | Force x 2 | +Force dice to the matching Sorcery use, if spell/ritual category matches the focus |
| Spirit (Summoning / Banishing / Binding) | Force x 2 | +Force to the matching Conjuring test (Banishing: to the limit instead), if spirit type matches the focus |
| Weapon | Force x 3 | +Force dice to melee Attack Tests with the weapon; also to Astral Combat Tests when used astrally |

A **Sustaining focus** sustains one spell for you (no -2 penalty), spell Force <= focus Force, matching category; disrupting it ends the spell but not the focus. **Focus addiction** risk (see Advancement/Substance rules) if bonded Force total exceeds Magic for long.

---

## Background Count

Full BGC rules, acclimation, alignment, ebbs/voids/foveae/warps: **[Background Count](Background%20Count.md)** (*Street Grimoire*). Initiate metamagics and arts: **[Metamagics and Arts](Metamagics%20and%20Arts.md)**.

---

## Shadow Spells supplements

**Verified from:** `Shadow Spells Condensed.md`. **Full spell/ritual/adept tables:** [Magic Supplemental](Magic%20Supplemental.md).

### Traditions (drain + spirit affinities)

| Tradition | Combat | Detection | Health | Illusion | Manipulation | Drain |
| --- | --- | --- | --- | --- | --- | --- |
| Aboriginal | Beasts | Earth | Plant | Guidance | Air | Wil + Cha |
| Egyptian (Possession) | Fire | Earth | Air | Guidance | Water | Wil + Int |
| Norse | Guardian | Earth | Plant | Air | Fire | Wil + Log |
| Psionic (Possession) | Fire | Air | Man | Guidance | Task | Wil + Int |

Egyptian and Psionic: Materialization -> Possession. Psionic: no mentor spirits.

### Selected new spells (summary)

| Spell | Cat | Drain | Notes |
| --- | --- | --- | --- |
| Chill / Frigid | Combat | F-1 / F+1 | Stun + -1 Init/hit (max -5) |
| Flame Burst | Combat | F+1 | Pulse each CT while sustained |
| Magebolt | Combat | F-4 | Awakened/dual-natured only |
| Sunbeam | Combat | F-1 | Sunlight allergy interactions |
| Recorded Room | Detection | F | Snapshot room while sustained |
| Rot | Health | F | Flesh destruction; Heal cannot repair |
| False Impression / Manascape | Illusion | F-4 / F-2 | Alter assensed auras |
| Control Emotions / Mob Mood | Manipulation | F-1 / F+1 | Instill emotion; -2 vs actions |
| Petrify | Manipulation | F-2 | Living tissue to stone |

### Shadow Spells rituals

| Ritual | Effect |
| --- | --- |
| Decrystalize | Restore crystallized subject (Material Link, Spotter) |
| Mana Flow | +1 BGC Force hours in **negative** areas only; radius Force x 100 m |
| Mana Ebb | -1 BGC Force hours in **positive** areas only; siphons to metaplane |

### Shadow Spells adept powers (summary)

| Power | Cost | Effect |
| --- | --- | --- |
| Demara | 0.5 | Watch skill 1 hr: use at Rating 1 for Magic hours |
| Living Focus | 1 | Sustain spell like Sustaining focus |
| Supernatural Toughness | 1/lvl | +1 Physical and Stun CM box/level |

Full catalogs (all SS spells, Stolen Souls spells/powers): [Magic Supplemental](Magic%20Supplemental.md).

---

## Hard Targets, Obeah, Santería, mentors

**Verified from:** `Hard Targets Condensed.md`

### Traditions

| | Combat | Detection | Health | Illusion | Manipulation | Drain |
| --- | --- | --- | --- | --- | --- | --- |
| **Obeah** | Fire | Water | Man | Guidance | Task | Wil + Cha |
| **Santería** | Guidance | Guardian | Earth | Man | Water | Wil + Int (possession) |

Santería: only "both" or Rada aspects; Petro = Vodou only. Great Form Possession: two Conjuring + Magic tests at equal Force.

### Mentor spirits (new)

| Mentor | All | Magician | Adept | Disadvantage |
| --- | --- | --- | --- | --- |
| Adversary | +2 Demolitions | +2 Counterspelling & Disenchanting | Free Iron Will | Leadership hurts; Cha+Wil(3) to cooperate |
| Alligator | +2 Intimidation | +2 Conjuring (water or man) | Free Inertia Strike | Cha+Wil(3) to abandon Plan A |
| Bat | +2 Navigation | +1 any Conjuring | Free Motion Sense | -1 Magic 24h if same hangout >1x/week |
| Monkey | +2 Gymnastics (climbing) | +2 Manipulation | 2 free Hang Time | Cha+Wil(3) to hit surprised foe |

---

## Aetherology phenomena

**Verified from:** `Source Texts Condensed/Aetherology Condensed.md` §06. BGC scale: [Background Count](Background%20Count.md).

### Astral Rift

- Barrier thinned into a bridge to a metaplane; Awakened and mundanes can astrally project and cross.
- Uninitiated magicians may travel without the Dweller (SR5 p. 317).
- Unstable rifts: if closed, Awakened must find another way back; may remain on metaplane without ceasing to exist (SR5 p. 314).
- **Mundanes** bound to rift to return. If body leaves rift area or rift closes, fade in **hours equal to Essence**.

### Astral Shallows

- Thin barrier: mundanes perceive astral like a window.
- Awakened with astral perception: switch astral/normal vision as **Free Action** (normally Simple).
- Can look at astral forms but not touch unless dual natured.
- Usually temporary (hours/days); geomancers can make permanent arcane windows.

### Background Count

- Scale **-24 to +24** (0 = normal). Negative = ebbs/voids; positive = aspected domains/warps.
- Use **absolute value** for magic effects unless noted. See *Street Grimoire* p. 30.

### Mana Storm

- See *Street Grimoire* p. 36.

### The Mist (Brittany)

- Positive BGC aspected to Fae spirits; **Force 3-10** (varies by location).
- **Noise** += Mist Force; Mist Force as modifier to ranged attacks and Perception.
- Confusion-like effect: Spellcasting Test **Force x 2 [Force]**.
- Movement power vs living: Mist Magic = Force; vs vehicles **Force x 2** (SR5 p. 399; Mist Willpower 0).
- Composure Tests: **+2 threshold**; every hour in Mist, Composure Test (SR5 p. 152).
- Spirits want to flee; **-1** to all active tests per spirit that must act in Mist; magician may reassert control (SR5 p. 301); on fail, no services until out of Mist or spend extra service.
- Force **6+**: can open astral rifts (including deep rifts).

### Daoineann Draoidheil

- Permanent mana+physical storms aspected to Druidic tradition.
- Force **8-12**, equal positive background count.
- Mana storm qualities; do not dissipate; stay put.
- **All** spells scatter (not only indirect combat; SR5 p. 283); preparations scatter when triggered; GM picks closest target if needed.

### Foveae

- Moving mana voids; Force **7-12**, equal negative background count.
- Astral tornado ~Force km tall.
- After pass: background count = weeks for area to recover reagents (SR5 p. 317).
- Preparations: potency **-1 every half hour** (fixated: every 6 hours instead of daily).
- Last ≤24 hours; Force **-1 every 2 hours**; below Force 4 stop and become temporary mana ebb (recover +1 Force / 2 hours).

### Maya Cloud

- Special mana storm; Force / positive BC **14-16**; dome ~5 million km², up to 100 km thick.
- Aspected to magic unique to specific artifacts.
- Force as Perception DP modifier through cloud; Force as Noise to signals/devices.
- Perpetual ice, lightning, snow outside; hazard to all but sub-orbital flight.

### The Veil

- Permanent storm ring; inverted rain; Force **12-14**, positive BC attuned to certain Awakened elves.
- ~600 km diameter, 20 m thick.
- Sustains **Chaotic World** at Force = Veil Force.
- Confuses travelers without electronic/auto navigation; exit not where intended.

### Void

- Permanent no-mana points; Force **13-20**, equal negative BC.
- Size ~500 m² to ~4 km diameter (Cattenom: 6 km, Force 20).
- Perimeter fluctuates up to ~10 m.
- Reagents instantly drained; foci left **Force hours** (active or not) permanently destroyed.

### New spirits (Aetherology)

Gum Toad and Crawler demon stat blocks: `Aetherology Condensed.md` §06 (SR4A-era blocks in full Rules chapter; Condensed has SR5 Gum Toad/Crawler summaries).

---

## Quick cheat sheet

| Task | Pool |
| --- | --- |
| Cast | Spellcasting + Magic [Force] |
| Resist Drain | Tradition Drain attrs |
| Counterspell (defense) | Counterspelling dice pool, allocated per spell |
| Dispel | Counterspelling + Magic [Astral] vs Force + caster's Magic |
| Summon | Summoning + Magic [Force] vs Force |
| Bind | Binding + Magic [Force] vs Force x 2 |
| Banish | Banishing + Magic [Astral] vs Force (+ Magic if bound) |
| Assense | Assensing + Intuition [Astral] |
| Alchemy (preparation) | Alchemy + Magic [Force] vs Force |
| Artificing (focus) | Artificing + Magic [formula Force] vs Force + Object Resistance |
| Disenchant | Disenchanting + Magic [Astral] vs Force (+ Magic if applicable) |
| Learn a spell/ritual/prep | Spellcasting/Ritual Spellcasting/Alchemy + Intuition [lodge Force] |
