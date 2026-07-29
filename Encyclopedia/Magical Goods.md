# Magical Goods

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only; no flavor.

**Src PDFs:** `shadowrunfiftheditioncorerulebook_V2.pdf` · `streetgrimoire.pdf` · `forbiddenarcana.pdf` · `chromeflesh.pdf` · `runfaster.pdf` · `shadow-spells-pdf.pdf` (Reagent Cost Table)
**Books:** Core · SG · FA · CF · RF · Shadow Spells (Reagent Cost Table filled). Court of Shadows: no local PDF (FA cites CoS reagents).
**See also:** `Mechanics/Magic.md` · `Encyclopedia/Sensors and Optics.md` (optics catalog) · `Encyclopedia/Drugs Toxins and Chemicals.md` (Awakened drugs / BADs; also reprints CF magical compounds) · `Encyclopedia/Melee Weapons.md` (base Acc/Reach/DV/AP for Weapon Focus forms)

**Out of scope as primary SKUs:** spell/ritual/adept-power lists · mentor spirits · ally/free-spirit formulae (Karma/quest, no shop Avail/Cost) · blood/toxic plot foci · Philosopher's Stone (legend only; FA sidebar) · CF Awakened drugs / BADs (full rows in Drugs Toxins and Chemicals.md)

## Schema

| Field | Meaning |
| --- | --- |
| Cat | Focus / Formula / Lodge / Reagent / SGShop / SGCompound / CFCompound / FATool / FACompound / FAPrep / FAReagent / Related / RFPack |
| Src | Book + page |
| Force | Force/Rating/`-` |
| Avail / Cost | Street Availability / nuyen |
| Bond | Karma to bond (foci) or `-` |
| Rules | Full mechanical notes |

## Common rules

### Foci (Core p.318-321)

- Bond: Awakened only; hours = Force; breaks prior owner's bond. Activate Simple; deactivate Free; must stay in possession; unconsciousness deactivates.
- Caps: bonded count <= Magic; sum Force <= Magic x 5. One focus may add Force to any given test.
- Active foci have astral form/signature; project with active foci; deactivate while projecting requires return to body to reactivate.
- Addiction: risk if total Force of *active* foci > Magic.

### Reagents (Core p.316-317; FA grades optional)

- Core street: 20¥/dram. Cross-tradition half strength.
- Spend to replace Force/Astral limit with dram count on listed tests; required for Binding, Artificing, offerings, temp lodges.

### Talismonger shop (SG p.211-212)

- Base Potency of purchased SG items = **6**.
- Artificing products must be attuned before use: Intuition + Magic [Astral] (5, 1 hour) Extended Test. Attuned item = sympathetic link for ritual magic.
- Lost/left items: daily Background Count x 2 (3) may break attunement (no Karma re-spend to re-attune). Adept-attuned items/foci lose attunement bonuses until re-attuned the same way.

### Focus upgrade (SG p.231)

- Only the original forging talismonger can upgrade; same focus type, higher Force only. Reagents = difference in bonding Karma costs. Re-Enchanting Test. Owner pays only the Karma difference to rebond.

### Magical compounds (SG p.219-220)

- Creation uses Alchemy prep rules; SG empowered compounds need specific refined reagents. FA compounds need Advanced Alchemy.
- Active duration (Potency x 10) minutes; inactive Potency -1/day.
- Dispel inactive like prep; active: contact + Disenchant vs 2x Force.

### FA buy formula (compounds + named preps)

- Cost `[(Force) + (Current Potency)] x 500¥`, Avail **14R**. Hard to find; scarcity may raise price.

### Side effects (SG p.220-221; apply when listed)

Blinded / Stunned (-10 Initiative) / Deafened / Unable to Speak / Bleed Out / One-Armed Bandit / Weak Side / Broken Grip / Fatigued (Body vs Potency S once) / Winded / Nauseated / Slow Death (2P/min) / Slowed (half Walk/Run).

## Catalog

## FOCI (Core categories + subtypes)
### Enchanting Focus (Alchemical)
- Cat: Focus
- Src: Core p.318-319 / Magical Goods p.326 / Street Gear p.461
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 5,000¥
- Bond: Force x 3 Karma
- Rules: Adds Force dice to Alchemy skill tests. Activate Simple; must be in possession; Free to deactivate. Max bonded foci = Magic; total Force of bonded foci <= Magic x 5. Only one focus may add Force to a given test. Focus addiction risk if total Force of active foci > Magic.
### Enchanting Focus (Disenchanting)
- Cat: Focus
- Src: Core p.318-319 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 5,000¥
- Bond: Force x 3 Karma
- Rules: While in contact with another artifact, add Force dice to Disenchanting Tests. Same bonding/activate/limits as other foci.
### Metamagic Focus (Centering)
- Cat: Focus
- Src: Core p.319 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 9,000¥
- Bond: Force x 3 Karma
- Rules: Adds Force to initiate grade when using Centering on Drain Resistance Tests.
### Metamagic Focus (Flexible Signature)
- Cat: Focus
- Src: Core p.319 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 9,000¥
- Bond: Force x 3 Karma
- Rules: Adds Force to grade when increasing observers' Assensing Test thresholds via Flexible Signature.
### Metamagic Focus (Masking)
- Cat: Focus
- Src: Core p.319 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 9,000¥
- Bond: Force x 3 Karma
- Rules: Add Force dice when resisting someone else's Assensing Test. Does not increase how many bonded foci you can mask.
### Metamagic Focus (Spell Shaping)
- Cat: Focus
- Src: Core p.319 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 9,000¥
- Bond: Force x 3 Karma
- Rules: Treat Magic as increased by Force when determining how much you can shape spells.
### Power Focus
- Cat: Focus
- Src: Core p.319 / p.326
- Force: Force
- Avail: (Force x 4)R | Cost: Force x 18,000¥
- Bond: Force x 6 Karma
- Rules: Temporarily increases effective Magic rating: adds Force to Sorcery, Conjuring, Enchanting pools and any Magic-involved test. Popular forms: rings, amulets.
### Qi Focus
- Cat: Focus
- Src: Core p.319-320 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 3,000¥
- Bond: Force x 2 Karma
- Rules: Adepts only. Object or body mod (tattoo/scar/pierce). Tied to one adept power at a set level. While active: gain that power, or add levels if you already have it (leveled powers only). Force must be 4 x Power Point cost of the held power. Example: Improved Ability (Unarmed) L1 = Force 2; Improved Reflexes L1 = Force 6 if you have no PP in it, Force 4 if you already have levels.
### Spell Focus (Counterspelling)
- Cat: Focus
- Src: Core p.320 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 4,000¥
- Bond: Force x 2 Karma
- Rules: Attuned to one spell category (Combat/Detection/Health/Illusion/Manipulation) at creation. Add Force dice to Counterspelling vs that category; also adds Force to spell defense pool.
### Spell Focus (Ritual Spellcasting)
- Cat: Focus
- Src: Core p.320 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 4,000¥
- Bond: Force x 2 Karma
- Rules: Category-attuned. Add Force dice to Ritual Spellcasting (leader or participant). Usable on non-spell rituals; cannot help a spell ritual of a different category than the focus.
### Spell Focus (Spellcasting)
- Cat: Focus
- Src: Core p.320 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 4,000¥
- Bond: Force x 2 Karma
- Rules: Category-attuned. Add Force dice to Spellcasting for spells in that category.
### Spell Focus (Sustaining)
- Cat: Focus
- Src: Core p.320 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 4,000¥
- Bond: Force x 2 Karma
- Rules: Category-attuned. Cast a matching-category spell through it; focus sustains (no -2 sustain penalty). Sustained spell Force cannot exceed focus Force. Disrupted spell ends but focus stays active/bound. Cannot sustain a spell ritual.
### Spirit Focus (Summoning)
- Cat: Focus
- Src: Core p.320-321 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 4,000¥
- Bond: Force x 2 Karma
- Rules: Attuned to one spirit type. Add Force dice to Summoning that type.
### Spirit Focus (Banishing)
- Cat: Focus
- Src: Core p.320-321 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 4,000¥
- Bond: Force x 2 Karma
- Rules: Attuned to one spirit type. Adds Force to the limit of Banishing Tests vs that type.
### Spirit Focus (Binding)
- Cat: Focus
- Src: Core p.320-321 / p.326
- Force: Force
- Avail: (Force x 3)R | Cost: Force x 4,000¥
- Bond: Force x 2 Karma
- Rules: Attuned to one spirit type. Add Force dice to Binding Tests vs that type.
### Weapon Focus
- Cat: Focus
- Src: Core p.321 / p.326
- Force: Force
- Avail: (Force x 4)R | Cost: Force x 7,000¥
- Bond: Force x 3 Karma
- Rules: Always a melee weapon form (use that weapon's Acc/Reach/DV/AP). Physical combat: +Force dice to melee Attack Test. Astral: +Force to Astral Combat Tests; takeable while projecting; astral DV = weapon DV but choose Stun or Physical.
## FORMULAE
### Focus Formula
- Cat: Formula
- Src: Core p.306 Artificing / Magical Goods p.326
- Force: as designed focus
- Avail: as the Focus | Cost: Focus Cost x 0.25
- Bond: -
- Rules: Complex Arcana recipe for a specific focus type/Force. Too complex to memorize; must be recorded. Bought from lore stores/talismongers.
### Spell Formula (Combat)
- Cat: Formula
- Src: Core p.299 Learning Spells / p.326
- Force: -
- Avail: 8R | Cost: 2,000¥
- Bond: -
- Rules: Buy to learn alone (need lodge of your tradition). Teacher alternate cost ~ Instruction skill x formula cost.
### Spell Formula (Detection)
- Cat: Formula
- Src: Core p.326
- Force: -
- Avail: 4R | Cost: 500¥
- Bond: -
- Rules: Same learning rules as other spell formulae.
### Spell Formula (Health)
- Cat: Formula
- Src: Core p.326
- Force: -
- Avail: 4R | Cost: 500¥
- Bond: -
- Rules: Same learning rules as other spell formulae.
### Spell Formula (Illusion)
- Cat: Formula
- Src: Core p.326
- Force: -
- Avail: 8R | Cost: 1,000¥
- Bond: -
- Rules: Same learning rules as other spell formulae.
### Spell Formula (Manipulation)
- Cat: Formula
- Src: Core p.326
- Force: -
- Avail: 8R | Cost: 1,500¥
- Bond: -
- Rules: Same learning rules as other spell formulae.
## MAGICAL LODGE MATERIALS
### Magical Lodge Materials
- Cat: Lodge
- Src: Core p.280 / Magical Goods p.326
- Force: Force
- Avail: Force x 2 | Cost: Force x 500¥
- Bond: -
- Rules: Tradition-specific materials. Setup: days = Force dedicating space. Active lodge = mana barrier + your astral signature. Tear-down to materials: 1 day; rebuild elsewhere. Improve: add materials + days = new Force. Temporary lodge: spend reagents equal to Force; 1 hour/Force to create; lasts until next sunrise or sunset.
## REAGENTS AND ORICHALCUM
### Reagents (raw, Core street)
- Cat: Reagent
- Src: Core p.316-317 / Magical Goods p.326
- Force: per dram
- Avail: - | Cost: 20¥ / dram
- Bond: -
- Rules: Talismonger price. Cross-tradition: half strength. Spent reagents lose mana (cease being reagents). Uses: set Alchemy/Banishing/Counterspelling/Disjoining/Spellcasting/Summoning limits to drams spent; Binding requires reagents; ritual offering; artificing; temporary lodge. Harvest: Alchemy + Magic [Mental] after 1 hour astral search; 1 dram / 2 hits (suited environ) or / 4 hits (unsuitable). Area tapped 2 days per dram harvested.
### Reagent grade: Tainted
- Cat: Reagent
- Src: FA p.187
- Force: per dram
- Avail: - | Cost: 20¥
- Bond: -
- Rules: Refine time +100%. FA graded market (optional/advanced vs Core flat 20¥).
### Reagent grade: Inferior
- Cat: Reagent
- Src: FA p.187
- Force: per dram
- Avail: 1 | Cost: 30¥
- Bond: -
- Rules: Refine time +50%.
### Reagent grade: Subpar
- Cat: Reagent
- Src: FA p.187
- Force: per dram
- Avail: 4 | Cost: 40¥
- Bond: -
- Rules: Refine time +25%.
### Reagent grade: Baseline
- Cat: Reagent
- Src: FA p.187
- Force: per dram
- Avail: 6R | Cost: 50¥
- Bond: -
- Rules: No refine-time change.
### Reagent grade: Superior
- Cat: Reagent
- Src: FA p.187
- Force: per dram
- Avail: 14R | Cost: 60¥
- Bond: -
- Rules: Refine time -25%. FA rare reagents (baobhan, ghost orchid, etc.) are at least Superior; no separate Avail/Cost rows.
### Reagent grade: Prime
- Cat: Reagent
- Src: FA p.187
- Force: per dram
- Avail: 20R | Cost: 70¥
- Bond: -
- Rules: Refine time -50%.
### Reagent grade: Refined (from type)
- Cat: Reagent
- Src: FA p.187-188; SG p.210
- Force: per dram
- Avail: Type Avail +4 | Cost: Type cost x 5
- Bond: -
- Rules: 10 raw -> 1 refined via Alchemy lab (~10h) Alchemy + Magic [Astral] (3). Fail: replace (threshold - hits) raw drams and retry. Critical glitch: entire batch wasted. FA leverage: -2 Drain Sorcery group; -1 Drain Binding; +5 Magic limits; make SG magical compounds; refine to radical (10 refined -> 1 radical). Bonus effects total <= Magic; Radical effects not cumulative with Refined of same reagent.
### Reagent grade: Radical (from type)
- Cat: Reagent
- Src: FA p.187-188; SG p.210
- Force: per dram
- Avail: Type Avail +8 | Cost: Type cost x 25
- Bond: -
- Rules: Same distill method: 10 refined -> 1 radical. Same fail/critical-glitch rules. FA leverage: -2 Drain Conjuring; -4 Drain Sorcery; -1 Object Resistance per dram; no Force limit on Magic tests (Drain normal); reduce Spirit Index; make orichalcum/fetish/inanimate vessel.
### Reagent buy table (Shadow Spells)
- Cat: Reagent
- Src: Shadow Spells, Adept Powers ~p.23-24 (compiled Reagent Cost Table)
- Force: per dram
- Avail: see Rules | Cost: see Rules
- Bond: -
- Rules: Standalone printed buy table, distinct from the FA graded-market formulas above. Raw (per dram): Avail -, 20¥ (matches Core). Refined: Avail 6, 350¥. Radical: Avail 8, 4,500¥. Orichalum: Avail 12, 140,000¥. Spelling "Orichalum" as printed in Shadow Spells (elsewhere in this file: Orichalcum). Use this table for a flat retail price on Refined/Radical/Orichalcum; use the FA Refined/Radical grade rules above for the distill-from-raw crafting process and its Drain/limit benefits.
### Orichalcum (craft)
- Cat: Reagent
- Src: SG p.209-210 sidebar Creating Orichalcum; FA p.192
- Force: 1 dram / batch
- Avail: craft only | Cost: craft (30 radical: 10 gold + 10 copper + 10 cinnabar)
- Bond: -
- Rules: ~28 days circulation (traditions +/- a day); attend ~every 10h (8h hermetic / sunrise-sunset shaman). End: Alchemy + Magic [Astral] (3). Success: 1 dram. Fail: reagents -> slag; Body + Magic (3) vs lead vapors; fail vapors = disorientation/hallucinations 8h x net deficit (stressful moments); each later orichalcum fail permanently +8h to next vapor duration. Aqua regia dissolves 1 dram/~8 oz (recoverable by neutralize/precipitate). Alloys with iron (weapon foci). Barter: vials of aqua regia + 1 dram orichalcum. FA: orichalcum can remove Force limit / +5 Magic in listed uses.
### Tool cleanser (15 uses)
- Cat: Reagent
- Src: SG p.230 Tool Cleansers
- Force: -
- Avail: 10 | Cost: 50¥
- Bond: -
- Rules: Per tool: Artificing + Magic [4, 10 minutes] Extended to clean before harvest. Unclean tools: roll 1D6; on 1, harvested reagents quality -1 grade. Laser/flame tools that cannot cross-contaminate: exempt.
## STREET GRIMOIRE TALISMONGERS / MANATECH
### Inanimate Vessel Preparation
- Cat: SGShop
- Src: SG p.214; FA Advanced Alchemy (create inanimate vessel)
- Force: min = spirit Force
- Avail: craft only | Cost: radical reagents = 5 x spirit Force
- Bond: -
- Rules: Prepare vessel for possession/inhabitation. Alchemy must exceed vessel Object Resistance or Force (whichever higher). Time: 10 days - net hits (min 1 day). Fail: lose reagents equal to Opposed Test hits; restart. Requires Channeling.
### Aqua fictus
- Cat: SGShop
- Src: SG p.211-217 / Price Index p.217
- Force: -
- Avail: 8 | Cost: 1,000¥
- Bond: -
- Rules: Craft: Alchemy (3), 10h, materials 850¥. Coats object to fake concentrated-mana aura (false reagents, fake prep/circle). Detect: Alchemy + Magic [Mental] (3). Coating fades after 12 hours. Used in paper lotus counterfeits.
### Aqua fortis
- Cat: SGShop
- Src: SG p.211-217
- Force: -
- Avail: 4 | Cost: 50¥
- Bond: -
- Rules: Craft: Alchemy (3), 10h, mat 43¥. Spray ~1 m2 (8 oz bottle). Orichalcum traces glow gold; other Awakened elements violet. Observe in Detail to detect; GM sets threshold.
### Aqua regia
- Cat: SGShop
- Src: SG p.211-217
- Force: -
- Avail: 5 | Cost: 100¥
- Bond: -
- Rules: Craft: Alchemy (3), 10h, mat 85¥. Dissolves 1 dram orichalcum per ~8 oz without destroying it; neutralize to precipitate recoverable orichalcum. Acid DV 14P AP -4. Common barter vial with 1 dram dissolved orichalcum.
### Aqua vitae
- Cat: SGShop
- Src: SG p.211-217
- Force: -
- Avail: 1 | Cost: 15¥
- Bond: -
- Rules: Craft: Alchemy (3), 4h, mat 13¥. Magical alcohol (more potent than standard). Addiction Rating 4.
### Astral powder
- Cat: SGShop
- Src: SG p.212-217
- Force: -
- Avail: 4 | Cost: 120¥
- Bond: -
- Rules: Craft: Alchemy (4), 2 days, mat 70¥. Requires Psychometry. Paper-sphere prep (in formula) detonates into 3 m radius cloud. Clings to spirits, projecting beings, wards, sustained/quickened spells; mundanes Observe in Detail (won't ID type). Physical: stops at walls; drops if spell ends; no FAB glow (visibility mods apply); rain washes off in minutes.
### FAB I
- Cat: SGShop
- Src: SG p.212-217
- Force: -
- Avail: 10 | Cost: 50¥ / m3
- Bond: -
- Rules: Fluorescing astral bacteria. Dies when astral form or magical force (e.g. spell) passes through; death chemical visible under UV.
### FAB II
- Cat: SGShop
- Src: SG p.212-217
- Force: Force
- Avail: 16R | Cost: Force x 50¥ / m3
- Bond: -
- Rules: Dual-natured strain; difficult for astral forms to pass; displacement visible on physical plane.
### FAB III
- Cat: SGShop
- Src: SG p.212-217
- Force: Force
- Avail: 20F | Cost: Force x 25,000¥ / m3
- Bond: -
- Rules: Mutant strain actively seeks and feeds on astral forms; can be lethal to dual-natured creatures. Often treated as environmental hazard.
### Fetish
- Cat: SGShop
- Src: SG p.212-217
- Force: -
- Avail: 4 | Cost: 2,000¥
- Bond: -
- Rules: Craft: Artificing (2), 1 day, mat 1,700¥ + 1 radical dram. Spell must be learned specifically with the fetish (learn twice to cast with and without). Spellcasting or Ritual Spellcasting with fetish: -2 Drain (min 2).
### Govi
- Cat: SGShop
- Src: SG p.212-217
- Force: Force (= watcher Force)
- Avail: Force | Cost: Force x 50¥
- Bond: -
- Rules: Requires Invocation. Prep Drain: roll (Force x 2); hits = Drain (+ trigger mods); resist Watcher ritual Drain separately. Potency -1 Force/week. Offer Potency x 25 drams after create to pause decay 6 months (repeatable). Release watcher: Simple. Destroy govi = destroy watcher (in or out). Found govi: only creator commands watcher; attuning found govi dispels its watcher.
### Hand of Glory
- Cat: SGShop
- Src: SG p.213-217
- Force: Force
- Avail: (Force x Force)R | Cost: Force x 1,500¥
- Bond: bonded on create until destroyed/used
- Rules: Requires Necromancy. Lynchpin = deceased hand; one physical Active skill of corpse; limit = ritual Force (not Accuracy). Refined+ reagents. Trigger: use skill for Potency minutes. Does not lose Potency. Talent fades 24h after use. Recharge without re-prep: take Physical DV = Force (not magically healable), transfer blood to Hand (blood magic path). Owning multiple Hands warned as dangerous.
### Mana-sensitive film plate
- Cat: SGShop
- Src: SG p.214-217
- Force: -
- Avail: 4 | Cost: 25¥
- Bond: -
- Rules: Craft: Alchemy (4), 3 days, mat 21¥. Consumable plate recording auras/spirits/background count for quicksilver camera or mortis optigram.
### Mortis optigram
- Cat: SGShop
- Src: SG p.214-217
- Force: -
- Avail: 6 | Cost: 3,000¥
- Bond: -
- Rules: Craft: Artificing (4), 1 week, mat 2,550¥. Requires Necromancy. Positions deceased eyes at plate; captures last thing seen (~20 min process). Legal weight varies by jurisdiction (lead vs evidence). Cybereyes unusable for this.
### Quicksilver camera
- Cat: SGShop
- Src: SG p.215-217
- Force: -
- Avail: 4 | Cost: 2,500¥
- Bond: -
- Rules: Craft: Artificing (4), 1 week, mat 2,125¥. Holds 5 plates; 2 min exposure (Awakened photographer as catalyst); moving camera ruins shot. Assensing captured auras: threshold +2, limit 4 (copies limit 3). Original = sympathetic link; copies = symbolic link. Wipe via smudging.
### Shofar
- Cat: SGShop
- Src: SG p.216-217
- Force: Force
- Avail: Force | Cost: Force x 800¥
- Bond: -
- Rules: Opposed: spirit Force + Willpower vs shofar Force x 2. Fail: materialized/manifested spirits flee to astral (waste current service); free spirits Fear for Potency Combat Turns; inhabiting spirits -2 all actions that CT. Instant; single-use after activate; Potency -1/week. Exorcism tradition gear.
### Symbolic link
- Cat: SGShop
- Src: SG p.216-217 Symbolic Link Creation table
- Force: see Rules (2-16)
- Avail: - | Cost: craft only (Artificing, 1 day)
- Bond: -
- Rules: Requires Psychometry. Viable days = Artificing net hits. Contains creator's astral signature while viable (can be used as material link against creator). Required Force: knows intimately or has material link = 2; has assensed or original astral photo = 4; copy of astral photo = 8; has met target = 12; personally unfamiliar = 16.
### Paper lotus (counterfeit magic item)
- Cat: SGShop
- Src: SG p.215-216 / Fake Magic Items table
- Force: min Artificing Force by fake type
- Avail: craft fraud (Masking) | Cost: craft (aqua fictus units + Artificing)
- Bond: -
- Rules: Requires Masking. Artificing creates counterfeit magical goods (RnG Counterfeit quality). Looks real until Perception vs Artificing net hits as threshold. Force = days it appears magical. Bonding fails and exposes fakes; fake reagents do nothing when spent; illusion eventually expires. Sympathetic link while illusion lasts. Fake Magic Items min Force / aqua fictus units: Reagent (10 drams) Force 2 / 1 unit; Fetish 4 / 1; Refined (10) 4 / 2; Quicksilver Camera 5 / 1; Radical (10) 5 / 4; Alchemical Preparation 6 / (Force/2); Focus 8 / (Force/2); Artifact GM call.
### Magecuff
- Cat: SGShop
- Src: SG p.215-217
- Force: -
- Avail: 5 | Cost: 1,000¥
- Bond: -
- Rules: Glomoss + light-triggered shock. Detects spellcasting or astral projection: 15S(e) Electricity attack.
### Magemask
- Cat: SGShop
- Src: SG p.215-217
- Force: -
- Avail: 2R | Cost: 200¥
- Bond: -
- Rules: Hood/gag cuts LOS + disorienting light/sound. Astral projection while worn: Willpower + Intuition (4).
### Mystic cuff
- Cat: SGShop
- Src: SG p.214-217
- Force: Force (max 8)
- Avail: (Force)R | Cost: Force x 200¥
- Bond: 1 Karma to permanent-craft
- Rules: Artificing; Force reduces Magic (adepts lose matching PP chosen by them). Ineffective if subject has 1+ cyberarms. Retarget existing: half Force; Intuition + Magic (5, 1 hour) + assense or material link. Flux: reduce effectiveness by initiate grade while aura in flux.
### Mystic mask
- Cat: SGShop
- Src: SG p.214-217
- Force: Force (max 12)
- Avail: (Force)R | Cost: Force x 400¥
- Bond: 1 Karma to permanent-craft
- Rules: Same mystic restraint rules as cuff; steel/leather or ceramic.
### Mystic jacket
- Cat: SGShop
- Src: SG p.214-217
- Force: Force (max 18)
- Avail: (Force)R | Cost: Force x 500¥
- Bond: 1 Karma to permanent-craft
- Rules: Same mystic restraint rules; straitjacket-style with studs/woven symbols.
## SG EMPOWERED MAGICAL COMPOUNDS
### AgHexHex
- Cat: SGCompound
- Src: SG p.217-220
- Force: Force
- Avail: 8 | Cost: Force x 500¥
- Bond: -
- Rules: SG empowered compound. Active (Potency x 10) min. Inactive: Potency -1/day. Active dispel: contact + Disenchant vs 2x Force; net hits reduce Force; Force 0 ends + aftereffects. Powers use Potency as Spellcasting / Force as Magic. Repeat activation: Drain = Force (Willpower alone or tradition). Vs augmented subjects: reduce Force and Potency by Essence lost to augs. Trigger Contact. If Potency > target Magic, negate Mist Form for duration. If already Mist Form when sprayed: force solid that CT regardless of Potency; (Force + 4)S damage. Aftereffect: Nauseated. Reagent: refined silver.
### BDNB (Bad Dog! No Biscuit!)
- Cat: SGCompound
- Src: SG p.217-220
- Force: Force
- Avail: 8 | Cost: Force x 500¥
- Bond: -
- Rules: SG empowered compound. Active (Potency x 10) min. Inactive: Potency -1/day. Active dispel: contact + Disenchant vs 2x Force; net hits reduce Force; Force 0 ends + aftereffects. Powers use Potency as Spellcasting / Force as Magic. Repeat activation: Drain = Force (Willpower alone or tradition). Vs augmented subjects: reduce Force and Potency by Essence lost to augs. Trigger Contact. Reduce Magic by Force when using Paralyzing Howl; if Force > Magic, negate Howl for duration. Aftereffect: Unable to Speak. Reagent: refined hell hound's tongue.
### Lot's Curse
- Cat: SGCompound
- Src: SG p.217-220
- Force: Force
- Avail: 14F | Cost: Force x 1,000¥
- Bond: -
- Rules: SG empowered compound. Active (Potency x 10) min. Inactive: Potency -1/day. Active dispel: contact + Disenchant vs 2x Force; net hits reduce Force; Force 0 ends + aftereffects. Powers use Potency as Spellcasting / Force as Magic. Repeat activation: Drain = Force (Willpower alone or tradition). Vs augmented subjects: reduce Force and Potency by Essence lost to augs. Trigger Contact. Petrify spell; secondary internal petrify; permanent on death; if alive at end of duration, revert. Aftereffect: Slow Death (2P unresisted / minute). Reagent: refined Gomorrah apple.
### Sage
- Cat: SGCompound
- Src: SG p.217-220
- Force: Force
- Avail: (Force x 6)R | Cost: Force x 800¥
- Bond: -
- Rules: SG empowered compound. Active (Potency x 10) min. Inactive: Potency -1/day. Active dispel: contact + Disenchant vs 2x Force; net hits reduce Force; Force 0 ends + aftereffects. Powers use Potency as Spellcasting / Force as Magic. Repeat activation: Drain = Force (Willpower alone or tradition). Vs augmented subjects: reduce Force and Potency by Essence lost to augs. Trigger Contact. Detect Magic, Extended. Aftereffect: Blinded (both eyes). Reagent: refined Cladonia stellaris lichen (N. American tundra). Creation needs >=1 refined lichen dram; extra refined to raise Potency.
### Spirit Strength
- Cat: SGCompound
- Src: SG p.217-220
- Force: Force
- Avail: (Force x 6)R | Cost: Force x 3,000¥
- Bond: -
- Rules: SG empowered compound. Active (Potency x 10) min. Inactive: Potency -1/day. Active dispel: contact + Disenchant vs 2x Force; net hits reduce Force; Force 0 ends + aftereffects. Powers use Potency as Spellcasting / Force as Magic. Repeat activation: Drain = Force (Willpower alone or tradition). Vs augmented subjects: reduce Force and Potency by Essence lost to augs. Trigger Contact. Hardened Mystic Armor. Aftereffect: Physical limit 1 for equal duration. Reagent: refined teonanacatl (Aztlan).
### Witch's moss
- Cat: SGCompound
- Src: SG p.217-220
- Force: Force
- Avail: (Force x 6)R | Cost: Force x 1,600¥
- Bond: -
- Rules: SG empowered compound. Active (Potency x 10) min. Inactive: Potency -1/day. Active dispel: contact + Disenchant vs 2x Force; net hits reduce Force; Force 0 ends + aftereffects. Powers use Potency as Spellcasting / Force as Magic. Repeat activation: Drain = Force (Willpower alone or tradition). Vs augmented subjects: reduce Force and Potency by Essence lost to augs. Trigger Contact. Paralyzing Touch. Aftereffect: both arms Broken Grip + Weak Side. Reagent: refined barghest blood.
## CHROME FLESH MAGICAL COMPOUNDS
### Animal Tongue
- Cat: CFCompound
- Src: CF p.186-189
- Force: dose
- Avail: 6R | Cost: 1,500¥
- Bond: -
- Rules: Vector Ingestion; Speed 3D6 min; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 3 / Thresh 2. Grants Animal Control. After: Fear from animals for equal duration (spirits not animals). Ingredient: manzana cactus radical pulp (Aztlan).
### Immortal Flower
- Cat: CFCompound
- Src: CF p.186-189
- Force: dose
- Avail: 14R | Cost: 2,500¥
- Bond: -
- Rules: Vector Ingestion; Speed 16 Combat Rounds; Duration Essence + 1D6 h (max 12). Addiction Both; Rating 8 / Thresh 3. Grants Regeneration. Per 20 boxes damage while under: -0.1 Essence permanent. Cyber/bioware users: 2D6P unresisted when wears off (regen 'repairs' implants). Ingredient: immortal flower petals (Mojave).
### Little Smoke
- Cat: CFCompound
- Src: CF p.187-189
- Force: dose
- Avail: 12F | Cost: 1,800¥
- Bond: -
- Rules: Vector Inhalation; Speed 2D6 min; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 6 / Thresh 3. Grants Concealment + Confusion. After: Perception and Willpower = 1 for equal duration. Ingredient: 3 units refined Great Plains grasses.
### Rock Lizard Blood
- Cat: CFCompound
- Src: CF p.187-189
- Force: dose
- Avail: 10R | Cost: 1,700¥
- Bond: -
- Rules: Vector Ingestion; Speed 30 min; Duration Essence + 1D6 h (max 12). Addiction Physical; Rating 6 / Thresh 3. Grants Immunity (Diseases and Toxins). After: 2P unresisted + -4 resist disease/toxin for equal duration. Ingredient: weeping tree radical pulp (N. America).
### Shade
- Cat: CFCompound
- Src: CF p.187-189
- Force: dose
- Avail: 6R | Cost: 1,000¥
- Bond: -
- Rules: Vector Inhalation; Speed Immediate; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 7 / Thresh 3. Forces astral projection (even mundanes); metaplanes with spirit guide/initiate. After: 10S unresisted. Must return before duration ends or die. Awakened: adds duration to normal astral time. Ingredient: red orchid pollen radical (SE Asia).
### Wudu'aku
- Cat: CFCompound
- Src: CF p.187-189
- Force: dose
- Avail: 12F | Cost: 2,350¥
- Bond: -
- Rules: Vector Ingestion/Inhalation; Speed 2D6 min; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 4 / Thresh 1. +2 Conjuring group; +2 Charisma vs spirits of man. After: -2 Conjuring and -2 Charisma vs other spirit types for 24h. Ingredient: powdered fossil radical (Australian Outback).
### Zombie Dust
- Cat: CFCompound
- Src: CF p.187-189
- Force: dose
- Avail: 12F | Cost: 1,500¥
- Bond: -
- Rules: Vector Contact/Injection; Speed 2 Combat Turns; Duration Essence + 1D6 h (max 12). Addiction Physiological; Rating 2 / Thresh 3. Prepares target for possession (still Intuition + Willpower resist). Ingredient: exotic metahuman remains + traditional animal powders.
## FA ALCHEMICAL TOOLS
### Atomizer
- Cat: FATool
- Src: FA p.193-194
- Force: -
- Avail: 4 | Cost: 500¥
- Bond: -
- Rules: Converts one solid/liquid compound to aerosol. Contact-trigger compounds do not fire until sprayed substance contacts target. Ranged attack max 3 m. Device contact does not trigger payload.
### Atomizer cartridge (empty)
- Cat: FATool
- Src: FA p.194
- Force: -
- Avail: 2 | Cost: 5¥
- Bond: -
- Rules: Consumable cartridge for atomizer.
### Alembic
- Cat: FATool
- Src: FA p.193
- Force: -
- Avail: not on tools table | Cost: 3,000¥
- Bond: -
- Rules: Doubles yield when refining raw->refined or refined->radical (10 base -> 2 instead of 1).
### Athanor
- Cat: FATool
- Src: FA p.193-194
- Force: -
- Avail: 4 | Cost: 1,000¥
- Bond: -
- Rules: Furnace: may leave up to 1 hour during 10h refine; orichalcum attendance every 12h instead of 10h.
### Crucible
- Cat: FATool
- Src: FA p.193-194
- Force: -
- Avail: 2 | Cost: 500¥
- Bond: -
- Rules: 10h process upgrades reagent quality one step (max to Prime).
### Vault of ages
- Cat: FATool
- Src: FA p.193-194
- Force: Rating 1-5
- Avail: (Rating + 4)R | Cost: 2,000¥ x Rating
- Bond: -
- Rules: Stores compounds/preparations: capacity = 2 x creator Magic; stored item Rating <= 2 x vault Rating. No Potency decay while inside; clock resumes on removal.
## FA COMPOUNDS
### Alchemical Duct Tape
- Cat: FACompound
- Src: FA p.194-195
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Command. On activate: each hit repairs 1 Structure or 1 damage box (Fix spell, SG). Aftereffect Stunned. Reagent: refined mallard fat. Only magical repair; then mundane fixes.
### Astral Increase
- Cat: FACompound
- Src: FA p.194-195
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. Doubles time magician may remain manifested while projecting. Aftereffect Winded. Reagent: radical ghost orchid petals.
### Astral Bond
- Cat: FACompound
- Src: FA p.195
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. While lasting, while manifesting may activate command triggers. Aftereffect Can't Speak. Reagent: refined insect-host organ.
### Baobhan's Tears
- Cat: FACompound
- Src: FA p.195
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. Poison: 4P resist Body only; if any damage unresisted, -1 Essence for 24h (max 1 Essence loss / 24h from repeats). Aftereffect Stunned. Reagent: refined baobhan tears (CoS).
### Drain Away
- Cat: FACompound
- Src: FA p.195
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. Next Physical Drain damage negated. Aftereffect Nauseated. Reagent: refined adept veins.
### Dulled Edges
- Cat: FACompound
- Src: FA p.195
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. Physical limit -2 for 3 turns. Aftereffect Fatigued. Reagent: radical killdeer antler (HS).
### Feel No Pain
- Cat: FACompound
- Src: FA p.195-196
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Command. Each net hit = 1 hour sleep for fatigue + skip 1 meal. When ends, dehydration/starvation apply immediately. >3 consecutive days: Addiction 4/2 risk. Aftereffect Fatigued. Reagent: radical kayeri mushroom.
### Force of Personality
- Cat: FACompound
- Src: FA p.196
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Command. Apply to skin; +2 Charisma for astral combat only. Aftereffect Stunned. Reagent: radical ghost orchid petals.
### HMHVV II Inhibitor
- Cat: FACompound
- Src: FA p.196
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. Dose every 7 days; halts HMHVV II progress (not a cure). Missed dose: virus resumes, often worse. Addiction 3/1. Aftereffect Fatigued. Reagent: refined drop bear saliva (HS).
### Laminate
- Cat: FACompound
- Src: FA p.196
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. Aerosol protects writing/runes from scuffing (1P destroys layer). Aftereffect Blinded (one eye). Reagent: refined slug glands.
### Perfect Sight
- Cat: FACompound
- Src: FA p.196-197
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Command. Apply to eyes: astral perception; ambient Noise + net hits (Interference, SG). Aftereffect Stunned. Reagent: refined ghost orchid petals.
### Sharpshooter
- Cat: FACompound
- Src: FA p.197
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Command. Eyes or pill: per net hit reduce Range category one step; +1 visual Perception. Aftereffect Blinded (one eye). Reagent: radical bird-of-prey eyes.
### Unstoppable Vigor
- Cat: FACompound
- Src: FA p.197
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. +Potency boxes on Stun CM usable only vs Drain; vanish when Potency ends or filled. Addiction 6/3. Aftereffect Slowed. Reagent: refined drake scales.
### Water Breathing
- Cat: FACompound
- Src: FA p.197
- Force: Force+Potency priced
- Avail: 14R | Cost: Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price.
- Bond: -
- Rules: Trigger Contact. Gills power; while active may only breathe water (air suffocates). Cancel restores air breathing. Aftereffect Winded. Reagent: refined salmon scales.
## FA NAMED PREPARATIONS
### Abandon All Hope
- Cat: FAPrep
- Src: FA p.198
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Contact. Enacts Foreboding (SG).
### Barricade
- Cat: FAPrep
- Src: FA p.198
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Reinforce (SG) on applied object.
### Burn, Baby, Burn
- Cat: FAPrep
- Src: FA p.198
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Ignite (Core).
### Do Your Best
- Cat: FAPrep
- Src: FA p.198
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Increase Inherent Limits (SG); only one limit at a time; new activation replaces prior.
### Get Away From My Ride
- Cat: FAPrep
- Src: FA p.198
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Protect Vehicle (SG).
### High as a Kite
- Cat: FAPrep
- Src: FA p.199
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Enabler (SG).
### Noise on the Line
- Cat: FAPrep
- Src: FA p.199
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Increase Noise (SG).
### NOMW (Not On My Watch)
- Cat: FAPrep
- Src: FA p.199
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Contact. Enacts Stabilize (Core).
### Lightning Blade
- Cat: FAPrep
- Src: FA p.199
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Written on weapon; next successful attack cannot be resisted by metal armor. Required spell listed: Lightning Bolt (Core).
### Spirit Zapper
- Cat: FAPrep
- Src: FA p.199
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Mana Barrier (Core) or Offensive Mana Barrier (SG) depending on preparation.
### Stink Bomb
- Cat: FAPrep
- Src: FA p.199
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command or Contact. Enacts Stench (SG); affects friend and foe.
### Stop Thief!
- Cat: FAPrep
- Src: FA p.199-200
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Glue Strip (SG).
### Truth Serum
- Cat: FAPrep
- Src: FA p.200
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Compel Truth (SG).
### Up and At 'Em
- Cat: FAPrep
- Src: FA p.200
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command or Contact. Enacts Awaken (SG).
### Watch Your Step
- Cat: FAPrep
- Src: FA p.200
- Force: Force+Potency priced
- Avail: 14R | Cost: Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here.
- Bond: -
- Rules: Trigger Command. Enacts Ice Sheet (Core).
## FA RARE / EXOTIC REAGENT INGREDIENTS (no shop Avail/Cost)
### Baobhan sith bone or hair
- Cat: FAReagent
- Src: FA p.188-189; CoS p.114 cited
- Force: Superior+ specialty
- Avail: no printed Avail/Cost | Cost: no printed (Superior+ market)
- Bond: -
- Rules: Even lowest quality = Superior reagent. Refined: regeneration/heal compounds or poison vs body+Magic. Used refined as Baobhan's Tears tears variant; bone/hair for related preps.
### Baobhan sith tears (refined)
- Cat: FAReagent
- Src: FA p.195 Baobhan's Tears
- Force: Superior+ specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Required reagent for Baobhan's Tears compound.
### Drop bear saliva
- Cat: FAReagent
- Src: FA p.189; HS p.60
- Force: Superior+ specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Awakened koala (HMHVV II carriers). Refined saliva: HMHVV II Inhibitor compound.
### Ghost orchid petals
- Cat: FAReagent
- Src: FA p.190
- Force: Superior+ specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Moon-blooming; hard to cultivate. Refined: vision compounds (Perfect Sight). Radical: Astral Increase, Force of Personality.
### Killdeer antler (ground)
- Cat: FAReagent
- Src: FA p.190; HS p.97
- Force: Superior+ specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Easy to counterfeit vs whitetail. Radical: Dulled Edges. Also healing/regen/toxin-resistance compounds.
### Kayeri mushroom
- Cat: FAReagent
- Src: FA p.190-191; CoS p.121 cited
- Force: Prime-quality inherent (text)
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: From kayeri (Tir na nOg / CoS). Radical: Feel No Pain. Curatives for toxins/disease.
### Drake scales
- Cat: FAReagent
- Src: FA p.191; HS p.162
- Force: exotic specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Refined: Unstoppable Vigor. Any type of drake scales.
### Insect spirit host organ
- Cat: FAReagent
- Src: FA p.191-192
- Force: exotic specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Refined: Astral Bond compound.
### Adept veins
- Cat: FAReagent
- Src: FA p.192
- Force: exotic specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Refined: Drain Away. Harvest implies killing/maiming an adept.
### Mallard fat (refined)
- Cat: FAReagent
- Src: FA p.194 Alchemical Duct Tape
- Force: specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Required for Alchemical Duct Tape.
### Slug glands (refined)
- Cat: FAReagent
- Src: FA p.196 Laminate
- Force: specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Required for Laminate.
### Bird-of-prey eyes (radical)
- Cat: FAReagent
- Src: FA p.197 Sharpshooter
- Force: specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Required for Sharpshooter.
### Salmon scales (refined)
- Cat: FAReagent
- Src: FA p.197 Water Breathing
- Force: specialty
- Avail: no printed Avail/Cost | Cost: no printed
- Bond: -
- Rules: Required for Water Breathing.
## RELATED OPTICS (also Sensors and Optics.md)
### Mage Sight Goggles
- Cat: Related
- Src: Core Street Gear Optical Devices p.444 / table; also Sensors and Optics.md
- Force: -
- Avail: 12R | Cost: 3,000¥
- Bond: -
- Rules: Heavy goggles + myomeric rope around fiber-optic ending in optical lens. Rope lengths 10, 20, or 30 m. Pure optical (not electronic): magician can get spellcasting LOS from cover; spellcasting through optics -3 dice. Cannot take vision enhancements. Primary catalog also Sensors and Optics.md.
## RF MAGIC PACKS (bundles)
### Basic Magician PACK
- Cat: RFPack
- Src: RF p.251-252
- Force: -
- Avail: 8 | Cost: 2,000¥ / 1 Karma
- Bond: included
- Rules: Contents: Magical lodge materials (Force 4). Bundle of Core SKUs.
### Advanced Magician PACK
- Cat: RFPack
- Src: RF p.251-252
- Force: -
- Avail: 12 | Cost: 4,000¥ / 2 Karma
- Bond: included
- Rules: Contents: Magical lodge materials (Force 6) + 50 drams reagents.
### Magic Wand PACK
- Cat: RFPack
- Src: RF p.251-252
- Force: -
- Avail: 8R | Cost: 36,000¥ / 18 Karma (+12 Karma)
- Bond: included
- Rules: Contents: Power focus (Force 2). +Karma is bonding.
### Magic Staff PACK
- Cat: RFPack
- Src: RF p.251-252
- Force: -
- Avail: 12R | Cost: 54,000¥ / 27 Karma (+18 Karma)
- Bond: included
- Rules: Contents: Power focus (Force 3).
### Basic Medicine Bag PACK
- Cat: RFPack
- Src: RF p.251-252
- Force: -
- Avail: 6R | Cost: 8,000¥ / 4 Karma (+4 Karma)
- Bond: included
- Rules: Contents: Spell focus Spellcasting (Health) Force 2. Same cost for other category/type examples (counterspelling dreamcatcher, sustaining amulet, ritual drum).
### Advanced Medicine Bag PACK
- Cat: RFPack
- Src: RF p.252
- Force: -
- Avail: 12R | Cost: 16,000¥ / 8 Karma (+8 Karma)
- Bond: included
- Rules: Contents: Spell focus Spellcasting (Health) Force 4.
### Basic Spirit Stick PACK
- Cat: RFPack
- Src: RF p.252
- Force: -
- Avail: 6R | Cost: 8,000¥ / 4 Karma (+4 Karma)
- Bond: included
- Rules: Contents: Spirit focus Summoning (beast spirits) Force 2. Other spirit-type themed foci same cost.
### Advanced Spirit Stick PACK
- Cat: RFPack
- Src: RF p.252
- Force: -
- Avail: 12R | Cost: 16,000¥ / 8 Karma (+8 Karma)
- Bond: included
- Rules: Contents: Spirit focus Summoning (beast spirits) Force 4.
### Magic Spear PACK
- Cat: RFPack
- Src: RF p.252
- Force: -
- Avail: 8R | Cost: 14,000¥ / 7 Karma (+6 Karma)
- Bond: included
- Rules: Contents: Weapon focus Force 2 (spear form narrative; any melee weapon focus at that Force).
## Inventory checklist
Total entries: 129

Foci subtypes (16): Enchanting Alchemical/Disenchanting; Metamagic Centering/Flexible Signature/Masking/Spell Shaping; Power; Qi; Spell Counterspelling/Ritual/Spellcasting/Sustaining; Spirit Summoning/Banishing/Binding; Weapon.

Formulae (6): Focus formula; Spell Combat/Detection/Health/Illusion/Manipulation.

Lodge (1): Magical Lodge Materials.

Reagents (13): Core raw; FA Tainted/Inferior/Subpar/Baseline/Superior/Prime; Refined; Radical; Orichalcum craft; Shadow Spells Reagent buy table (Refined/Radical/Orichalum flat prices); Tool cleanser.

SG shop (23): Aqua fictus/fortis/regia/vitae; Astral powder; FAB I/II/III; Fetish; Govi; Hand of Glory; Mana-sensitive film; Mortis optigram; Quicksilver camera; Shofar; Symbolic link (Force table); Paper lotus + Fake Magic Items table; Magecuff; Magemask; Mystic cuff/mask/jacket; Inanimate Vessel Preparation (craft).

SG compounds (6): AgHexHex; BDNB; Lot's Curse; Sage; Spirit Strength; Witch's moss.

CF compounds (7): Animal Tongue; Immortal Flower; Little Smoke; Rock Lizard Blood; Shade; Wudu'aku; Zombie Dust.

FA tools (6): Atomizer; cartridge; Alembic; Athanor; Crucible; Vault of ages.

FA compounds (14): Alchemical Duct Tape; Astral Increase; Astral Bond; Baobhan's Tears; Drain Away; Dulled Edges; Feel No Pain; Force of Personality; HMHVV II Inhibitor; Laminate; Perfect Sight; Sharpshooter; Unstoppable Vigor; Water Breathing.

FA preps (15): Abandon All Hope; Barricade; Burn Baby Burn; Do Your Best; Get Away From My Ride; High as a Kite; Noise on the Line; NOMW; Lightning Blade; Spirit Zapper; Stink Bomb; Stop Thief; Truth Serum; Up and At 'Em; Watch Your Step.

FA rare/exotic ingredients (13): baobhan bone/hair; baobhan tears; drop bear saliva; ghost orchid; killdeer antler; kayeri mushroom; drake scales; insect-host organ; adept veins; mallard fat; slug glands; bird-of-prey eyes; salmon scales (no printed Avail/Cost; Superior+/exotic).

Related optics (1): Mage Sight Goggles (also Sensors and Optics.md).

RF packs (9): Basic/Advanced Magician; Magic Wand/Staff; Basic/Advanced Medicine Bag; Basic/Advanced Spirit Stick; Magic Spear.

Still out of scope (not Magical Goods SKUs): spell/ritual/adept lists; mentor spirits; ally/free-spirit formulae; Philosopher's Stone (legend); CF Awakened drugs/BADs -> Drugs Toxins and Chemicals.md (file is filled).

## Cutting Aces / Hard Targets magical supplies

| Name | Src | Avail | Cost | Notes |
| --- | --- | --- | --- | --- |
| Mana Compass | CA | 22R | 32,000¥ | Points to largest active magic within Force meters; ignores Masking; not astral-only sources. |
| Shaman Tuxedo | CA | 9 | 1,000¥ | Ritual garb for one tradition/spirit type; +1 free Summoning hit (favors owed only). |
| Enchanting Gloves | HT | 8 | 2,000¥ | Blocks alchemist aura reading of wearer; attuned to creator. Also listed under Tools. |

