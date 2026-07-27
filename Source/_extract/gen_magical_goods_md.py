# -*- coding: utf-8 -*-
"""Generate Encyclopedia/Magical Goods.md - LLM agent reference."""
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Encyclopedia\Magical Goods.md")

def E(**kw):
    return kw

ITEMS = []

# ========== FOCI (Core categories; subtypes listed) ==========
ITEMS += [
E(name="Enchanting Focus (Alchemical)", cat="Focus", src="Core p.318-319 / Magical Goods p.326 / Street Gear p.461",
  force="Force", avail="(Force x 3)R", cost="Force x 5,000¥", bond="Force x 3 Karma",
  rules="Adds Force dice to Alchemy skill tests. Activate Simple; must be in possession; Free to deactivate. Max bonded foci = Magic; total Force of bonded foci <= Magic x 5. Only one focus may add Force to a given test. Focus addiction risk if total Force of active foci > Magic."),
E(name="Enchanting Focus (Disenchanting)", cat="Focus", src="Core p.318-319 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 5,000¥", bond="Force x 3 Karma",
  rules="While in contact with another artifact, add Force dice to Disenchanting Tests. Same bonding/activate/limits as other foci."),
E(name="Metamagic Focus (Centering)", cat="Focus", src="Core p.319 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 9,000¥", bond="Force x 3 Karma",
  rules="Adds Force to initiate grade when using Centering on Drain Resistance Tests."),
E(name="Metamagic Focus (Flexible Signature)", cat="Focus", src="Core p.319 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 9,000¥", bond="Force x 3 Karma",
  rules="Adds Force to grade when increasing observers' Assensing Test thresholds via Flexible Signature."),
E(name="Metamagic Focus (Masking)", cat="Focus", src="Core p.319 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 9,000¥", bond="Force x 3 Karma",
  rules="Add Force dice when resisting someone else's Assensing Test. Does not increase how many bonded foci you can mask."),
E(name="Metamagic Focus (Spell Shaping)", cat="Focus", src="Core p.319 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 9,000¥", bond="Force x 3 Karma",
  rules="Treat Magic as increased by Force when determining how much you can shape spells."),
E(name="Power Focus", cat="Focus", src="Core p.319 / p.326",
  force="Force", avail="(Force x 4)R", cost="Force x 18,000¥", bond="Force x 6 Karma",
  rules="Temporarily increases effective Magic rating: adds Force to Sorcery, Conjuring, Enchanting pools and any Magic-involved test. Popular forms: rings, amulets."),
E(name="Qi Focus", cat="Focus", src="Core p.319-320 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 3,000¥", bond="Force x 2 Karma",
  rules="Adepts only. Object or body mod (tattoo/scar/pierce). Tied to one adept power at a set level. While active: gain that power, or add levels if you already have it (leveled powers only). Force must be 4 x Power Point cost of the held power. Example: Improved Ability (Unarmed) L1 = Force 2; Improved Reflexes L1 = Force 6 if you have no PP in it, Force 4 if you already have levels."),
E(name="Spell Focus (Counterspelling)", cat="Focus", src="Core p.320 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 4,000¥", bond="Force x 2 Karma",
  rules="Attuned to one spell category (Combat/Detection/Health/Illusion/Manipulation) at creation. Add Force dice to Counterspelling vs that category; also adds Force to spell defense pool."),
E(name="Spell Focus (Ritual Spellcasting)", cat="Focus", src="Core p.320 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 4,000¥", bond="Force x 2 Karma",
  rules="Category-attuned. Add Force dice to Ritual Spellcasting (leader or participant). Usable on non-spell rituals; cannot help a spell ritual of a different category than the focus."),
E(name="Spell Focus (Spellcasting)", cat="Focus", src="Core p.320 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 4,000¥", bond="Force x 2 Karma",
  rules="Category-attuned. Add Force dice to Spellcasting for spells in that category."),
E(name="Spell Focus (Sustaining)", cat="Focus", src="Core p.320 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 4,000¥", bond="Force x 2 Karma",
  rules="Category-attuned. Cast a matching-category spell through it; focus sustains (no -2 sustain penalty). Sustained spell Force cannot exceed focus Force. Disrupted spell ends but focus stays active/bound. Cannot sustain a spell ritual."),
E(name="Spirit Focus (Summoning)", cat="Focus", src="Core p.320-321 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 4,000¥", bond="Force x 2 Karma",
  rules="Attuned to one spirit type. Add Force dice to Summoning that type."),
E(name="Spirit Focus (Banishing)", cat="Focus", src="Core p.320-321 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 4,000¥", bond="Force x 2 Karma",
  rules="Attuned to one spirit type. Adds Force to the limit of Banishing Tests vs that type."),
E(name="Spirit Focus (Binding)", cat="Focus", src="Core p.320-321 / p.326",
  force="Force", avail="(Force x 3)R", cost="Force x 4,000¥", bond="Force x 2 Karma",
  rules="Attuned to one spirit type. Add Force dice to Binding Tests vs that type."),
E(name="Weapon Focus", cat="Focus", src="Core p.321 / p.326",
  force="Force", avail="(Force x 4)R", cost="Force x 7,000¥", bond="Force x 3 Karma",
  rules="Always a melee weapon form (use that weapon's Acc/Reach/DV/AP). Physical combat: +Force dice to melee Attack Test. Astral: +Force to Astral Combat Tests; takeable while projecting; astral DV = weapon DV but choose Stun or Physical."),
]

# ========== FORMULAE ==========
ITEMS += [
E(name="Focus Formula", cat="Formula", src="Core p.306 Artificing / Magical Goods p.326",
  force="as designed focus", avail="as the Focus", cost="Focus Cost x 0.25", bond="-",
  rules="Complex Arcana recipe for a specific focus type/Force. Too complex to memorize; must be recorded. Bought from lore stores/talismongers."),
E(name="Spell Formula (Combat)", cat="Formula", src="Core p.299 Learning Spells / p.326",
  force="-", avail="8R", cost="2,000¥", bond="-",
  rules="Buy to learn alone (need lodge of your tradition). Teacher alternate cost ~ Instruction skill x formula cost."),
E(name="Spell Formula (Detection)", cat="Formula", src="Core p.326",
  force="-", avail="4R", cost="500¥", bond="-",
  rules="Same learning rules as other spell formulae."),
E(name="Spell Formula (Health)", cat="Formula", src="Core p.326",
  force="-", avail="4R", cost="500¥", bond="-",
  rules="Same learning rules as other spell formulae."),
E(name="Spell Formula (Illusion)", cat="Formula", src="Core p.326",
  force="-", avail="8R", cost="1,000¥", bond="-",
  rules="Same learning rules as other spell formulae."),
E(name="Spell Formula (Manipulation)", cat="Formula", src="Core p.326",
  force="-", avail="8R", cost="1,500¥", bond="-",
  rules="Same learning rules as other spell formulae."),
]

# ========== LODGE + REAGENTS ==========
ITEMS += [
E(name="Magical Lodge Materials", cat="Lodge", src="Core p.280 / Magical Goods p.326",
  force="Force", avail="Force x 2", cost="Force x 500¥", bond="-",
  rules="Tradition-specific materials. Setup: days = Force dedicating space. Active lodge = mana barrier + your astral signature. Tear-down to materials: 1 day; rebuild elsewhere. Improve: add materials + days = new Force. Temporary lodge: spend reagents equal to Force; 1 hour/Force to create; lasts until next sunrise or sunset."),
E(name="Reagents (raw, Core street)", cat="Reagent", src="Core p.316-317 / Magical Goods p.326",
  force="per dram", avail="-", cost="20¥ / dram", bond="-",
  rules="Talismonger price. Cross-tradition: half strength. Spent reagents lose mana (cease being reagents). Uses: set Alchemy/Banishing/Counterspelling/Disjoining/Spellcasting/Summoning limits to drams spent; Binding requires reagents; ritual offering; artificing; temporary lodge. Harvest: Alchemy + Magic [Mental] after 1 hour astral search; 1 dram / 2 hits (suited environ) or / 4 hits (unsuitable). Area tapped 2 days per dram harvested."),
E(name="Reagent grade: Tainted", cat="Reagent", src="FA p.187",
  force="per dram", avail="-", cost="20¥", bond="-",
  rules="Refine time +100%. FA graded market (optional/advanced vs Core flat 20¥)."),
E(name="Reagent grade: Inferior", cat="Reagent", src="FA p.187",
  force="per dram", avail="1", cost="30¥", bond="-",
  rules="Refine time +50%."),
E(name="Reagent grade: Subpar", cat="Reagent", src="FA p.187",
  force="per dram", avail="4", cost="40¥", bond="-",
  rules="Refine time +25%."),
E(name="Reagent grade: Baseline", cat="Reagent", src="FA p.187",
  force="per dram", avail="6R", cost="50¥", bond="-",
  rules="No refine-time change."),
E(name="Reagent grade: Superior", cat="Reagent", src="FA p.187",
  force="per dram", avail="14R", cost="60¥", bond="-",
  rules="Refine time -25%. FA rare reagents (baobhan, ghost orchid, etc.) are at least Superior; no separate Avail/Cost rows."),
E(name="Reagent grade: Prime", cat="Reagent", src="FA p.187",
  force="per dram", avail="20R", cost="70¥", bond="-",
  rules="Refine time -50%."),
E(name="Reagent grade: Refined (from type)", cat="Reagent", src="FA p.187-188; SG p.210",
  force="per dram", avail="Type Avail +4", cost="Type cost x 5", bond="-",
  rules="10 raw -> 1 refined via Alchemy lab (~10h) Alchemy + Magic [Astral] (3). Fail: replace (threshold - hits) raw drams and retry. Critical glitch: entire batch wasted. FA leverage: -2 Drain Sorcery group; -1 Drain Binding; +5 Magic limits; make SG magical compounds; refine to radical (10 refined -> 1 radical). Bonus effects total <= Magic; Radical effects not cumulative with Refined of same reagent."),
E(name="Reagent grade: Radical (from type)", cat="Reagent", src="FA p.187-188; SG p.210",
  force="per dram", avail="Type Avail +8", cost="Type cost x 25", bond="-",
  rules="Same distill method: 10 refined -> 1 radical. Same fail/critical-glitch rules. FA leverage: -2 Drain Conjuring; -4 Drain Sorcery; -1 Object Resistance per dram; no Force limit on Magic tests (Drain normal); reduce Spirit Index; make orichalcum/fetish/inanimate vessel."),
E(name="Orichalcum (craft)", cat="Reagent", src="SG p.209-210 sidebar Creating Orichalcum; FA p.192",
  force="1 dram / batch", avail="craft only", cost="craft (30 radical: 10 gold + 10 copper + 10 cinnabar)", bond="-",
  rules="~28 days circulation (traditions +/- a day); attend ~every 10h (8h hermetic / sunrise-sunset shaman). End: Alchemy + Magic [Astral] (3). Success: 1 dram. Fail: reagents -> slag; Body + Magic (3) vs lead vapors; fail vapors = disorientation/hallucinations 8h x net deficit (stressful moments); each later orichalcum fail permanently +8h to next vapor duration. Aqua regia dissolves 1 dram/~8 oz (recoverable by neutralize/precipitate). Alloys with iron (weapon foci). Barter: vials of aqua regia + 1 dram orichalcum. FA: orichalcum can remove Force limit / +5 Magic in listed uses."),
E(name="Tool cleanser (15 uses)", cat="Reagent", src="SG p.230 Tool Cleansers",
  force="-", avail="10", cost="50¥", bond="-",
  rules="Per tool: Artificing + Magic [4, 10 minutes] Extended to clean before harvest. Unclean tools: roll 1D6; on 1, harvested reagents quality -1 grade. Laser/flame tools that cannot cross-contaminate: exempt."),
E(name="Inanimate Vessel Preparation", cat="SGShop", src="SG p.214; FA Advanced Alchemy (create inanimate vessel)",
  force="min = spirit Force", avail="craft only", cost="radical reagents = 5 x spirit Force", bond="-",
  rules="Prepare vessel for possession/inhabitation. Alchemy must exceed vessel Object Resistance or Force (whichever higher). Time: 10 days - net hits (min 1 day). Fail: lose reagents equal to Opposed Test hits; restart. Requires Channeling."),
]

# ========== SG SHOP ==========
ITEMS += [
E(name="Aqua fictus", cat="SGShop", src="SG p.211-217 / Price Index p.217",
  force="-", avail="8", cost="1,000¥", bond="-",
  rules="Craft: Alchemy (3), 10h, materials 850¥. Coats object to fake concentrated-mana aura (false reagents, fake prep/circle). Detect: Alchemy + Magic [Mental] (3). Coating fades after 12 hours. Used in paper lotus counterfeits."),
E(name="Aqua fortis", cat="SGShop", src="SG p.211-217",
  force="-", avail="4", cost="50¥", bond="-",
  rules="Craft: Alchemy (3), 10h, mat 43¥. Spray ~1 m2 (8 oz bottle). Orichalcum traces glow gold; other Awakened elements violet. Observe in Detail to detect; GM sets threshold."),
E(name="Aqua regia", cat="SGShop", src="SG p.211-217",
  force="-", avail="5", cost="100¥", bond="-",
  rules="Craft: Alchemy (3), 10h, mat 85¥. Dissolves 1 dram orichalcum per ~8 oz without destroying it; neutralize to precipitate recoverable orichalcum. Acid DV 14P AP -4. Common barter vial with 1 dram dissolved orichalcum."),
E(name="Aqua vitae", cat="SGShop", src="SG p.211-217",
  force="-", avail="1", cost="15¥", bond="-",
  rules="Craft: Alchemy (3), 4h, mat 13¥. Magical alcohol (more potent than standard). Addiction Rating 4."),
E(name="Astral powder", cat="SGShop", src="SG p.212-217",
  force="-", avail="4", cost="120¥", bond="-",
  rules="Craft: Alchemy (4), 2 days, mat 70¥. Requires Psychometry. Paper-sphere prep (in formula) detonates into 3 m radius cloud. Clings to spirits, projecting beings, wards, sustained/quickened spells; mundanes Observe in Detail (won't ID type). Physical: stops at walls; drops if spell ends; no FAB glow (visibility mods apply); rain washes off in minutes."),
E(name="FAB I", cat="SGShop", src="SG p.212-217",
  force="-", avail="10", cost="50¥ / m3", bond="-",
  rules="Fluorescing astral bacteria. Dies when astral form or magical force (e.g. spell) passes through; death chemical visible under UV."),
E(name="FAB II", cat="SGShop", src="SG p.212-217",
  force="Force", avail="16R", cost="Force x 50¥ / m3", bond="-",
  rules="Dual-natured strain; difficult for astral forms to pass; displacement visible on physical plane."),
E(name="FAB III", cat="SGShop", src="SG p.212-217",
  force="Force", avail="20F", cost="Force x 25,000¥ / m3", bond="-",
  rules="Mutant strain actively seeks and feeds on astral forms; can be lethal to dual-natured creatures. Often treated as environmental hazard."),
E(name="Fetish", cat="SGShop", src="SG p.212-217",
  force="-", avail="4", cost="2,000¥", bond="-",
  rules="Craft: Artificing (2), 1 day, mat 1,700¥ + 1 radical dram. Spell must be learned specifically with the fetish (learn twice to cast with and without). Spellcasting or Ritual Spellcasting with fetish: -2 Drain (min 2)."),
E(name="Govi", cat="SGShop", src="SG p.212-217",
  force="Force (= watcher Force)", avail="Force", cost="Force x 50¥", bond="-",
  rules="Requires Invocation. Prep Drain: roll (Force x 2); hits = Drain (+ trigger mods); resist Watcher ritual Drain separately. Potency -1 Force/week. Offer Potency x 25 drams after create to pause decay 6 months (repeatable). Release watcher: Simple. Destroy govi = destroy watcher (in or out). Found govi: only creator commands watcher; attuning found govi dispels its watcher."),
E(name="Hand of Glory", cat="SGShop", src="SG p.213-217",
  force="Force", avail="(Force x Force)R", cost="Force x 1,500¥", bond="bonded on create until destroyed/used",
  rules="Requires Necromancy. Lynchpin = deceased hand; one physical Active skill of corpse; limit = ritual Force (not Accuracy). Refined+ reagents. Trigger: use skill for Potency minutes. Does not lose Potency. Talent fades 24h after use. Recharge without re-prep: take Physical DV = Force (not magically healable), transfer blood to Hand (blood magic path). Owning multiple Hands warned as dangerous."),
E(name="Mana-sensitive film plate", cat="SGShop", src="SG p.214-217",
  force="-", avail="4", cost="25¥", bond="-",
  rules="Craft: Alchemy (4), 3 days, mat 21¥. Consumable plate recording auras/spirits/background count for quicksilver camera or mortis optigram."),
E(name="Mortis optigram", cat="SGShop", src="SG p.214-217",
  force="-", avail="6", cost="3,000¥", bond="-",
  rules="Craft: Artificing (4), 1 week, mat 2,550¥. Requires Necromancy. Positions deceased eyes at plate; captures last thing seen (~20 min process). Legal weight varies by jurisdiction (lead vs evidence). Cybereyes unusable for this."),
E(name="Quicksilver camera", cat="SGShop", src="SG p.215-217",
  force="-", avail="4", cost="2,500¥", bond="-",
  rules="Craft: Artificing (4), 1 week, mat 2,125¥. Holds 5 plates; 2 min exposure (Awakened photographer as catalyst); moving camera ruins shot. Assensing captured auras: threshold +2, limit 4 (copies limit 3). Original = sympathetic link; copies = symbolic link. Wipe via smudging."),
E(name="Shofar", cat="SGShop", src="SG p.216-217",
  force="Force", avail="Force", cost="Force x 800¥", bond="-",
  rules="Opposed: spirit Force + Willpower vs shofar Force x 2. Fail: materialized/manifested spirits flee to astral (waste current service); free spirits Fear for Potency Combat Turns; inhabiting spirits -2 all actions that CT. Instant; single-use after activate; Potency -1/week. Exorcism tradition gear."),
E(name="Symbolic link", cat="SGShop", src="SG p.216-217 Symbolic Link Creation table",
  force="see Rules (2-16)", avail="-", cost="craft only (Artificing, 1 day)", bond="-",
  rules="Requires Psychometry. Viable days = Artificing net hits. Contains creator's astral signature while viable (can be used as material link against creator). Required Force: knows intimately or has material link = 2; has assensed or original astral photo = 4; copy of astral photo = 8; has met target = 12; personally unfamiliar = 16."),
E(name="Paper lotus (counterfeit magic item)", cat="SGShop", src="SG p.215-216 / Fake Magic Items table",
  force="min Artificing Force by fake type", avail="craft fraud (Masking)", cost="craft (aqua fictus units + Artificing)", bond="-",
  rules="Requires Masking. Artificing creates counterfeit magical goods (RnG Counterfeit quality). Looks real until Perception vs Artificing net hits as threshold. Force = days it appears magical. Bonding fails and exposes fakes; fake reagents do nothing when spent; illusion eventually expires. Sympathetic link while illusion lasts. Fake Magic Items min Force / aqua fictus units: Reagent (10 drams) Force 2 / 1 unit; Fetish 4 / 1; Refined (10) 4 / 2; Quicksilver Camera 5 / 1; Radical (10) 5 / 4; Alchemical Preparation 6 / (Force/2); Focus 8 / (Force/2); Artifact GM call."),
E(name="Magecuff", cat="SGShop", src="SG p.215-217",
  force="-", avail="5", cost="1,000¥", bond="-",
  rules="Glomoss + light-triggered shock. Detects spellcasting or astral projection: 15S(e) Electricity attack."),
E(name="Magemask", cat="SGShop", src="SG p.215-217",
  force="-", avail="2R", cost="200¥", bond="-",
  rules="Hood/gag cuts LOS + disorienting light/sound. Astral projection while worn: Willpower + Intuition (4)."),
E(name="Mystic cuff", cat="SGShop", src="SG p.214-217",
  force="Force (max 8)", avail="(Force)R", cost="Force x 200¥", bond="1 Karma to permanent-craft",
  rules="Artificing; Force reduces Magic (adepts lose matching PP chosen by them). Ineffective if subject has 1+ cyberarms. Retarget existing: half Force; Intuition + Magic (5, 1 hour) + assense or material link. Flux: reduce effectiveness by initiate grade while aura in flux."),
E(name="Mystic mask", cat="SGShop", src="SG p.214-217",
  force="Force (max 12)", avail="(Force)R", cost="Force x 400¥", bond="1 Karma to permanent-craft",
  rules="Same mystic restraint rules as cuff; steel/leather or ceramic."),
E(name="Mystic jacket", cat="SGShop", src="SG p.214-217",
  force="Force (max 18)", avail="(Force)R", cost="Force x 500¥", bond="1 Karma to permanent-craft",
  rules="Same mystic restraint rules; straitjacket-style with studs/woven symbols."),
]

# ========== SG COMPOUNDS ==========
_SG_COMP = "SG empowered compound. Active (Potency x 10) min. Inactive: Potency -1/day. Active dispel: contact + Disenchant vs 2x Force; net hits reduce Force; Force 0 ends + aftereffects. Powers use Potency as Spellcasting / Force as Magic. Repeat activation: Drain = Force (Willpower alone or tradition). Vs augmented subjects: reduce Force and Potency by Essence lost to augs."
ITEMS += [
E(name="AgHexHex", cat="SGCompound", src="SG p.217-220",
  force="Force", avail="8", cost="Force x 500¥", bond="-",
  rules=f"{_SG_COMP} Trigger Contact. If Potency > target Magic, negate Mist Form for duration. If already Mist Form when sprayed: force solid that CT regardless of Potency; (Force + 4)S damage. Aftereffect: Nauseated. Reagent: refined silver."),
E(name="BDNB (Bad Dog! No Biscuit!)", cat="SGCompound", src="SG p.217-220",
  force="Force", avail="8", cost="Force x 500¥", bond="-",
  rules=f"{_SG_COMP} Trigger Contact. Reduce Magic by Force when using Paralyzing Howl; if Force > Magic, negate Howl for duration. Aftereffect: Unable to Speak. Reagent: refined hell hound's tongue."),
E(name="Lot's Curse", cat="SGCompound", src="SG p.217-220",
  force="Force", avail="14F", cost="Force x 1,000¥", bond="-",
  rules=f"{_SG_COMP} Trigger Contact. Petrify spell; secondary internal petrify; permanent on death; if alive at end of duration, revert. Aftereffect: Slow Death (2P unresisted / minute). Reagent: refined Gomorrah apple."),
E(name="Sage", cat="SGCompound", src="SG p.217-220",
  force="Force", avail="(Force x 6)R", cost="Force x 800¥", bond="-",
  rules=f"{_SG_COMP} Trigger Contact. Detect Magic, Extended. Aftereffect: Blinded (both eyes). Reagent: refined Cladonia stellaris lichen (N. American tundra). Creation needs >=1 refined lichen dram; extra refined to raise Potency."),
E(name="Spirit Strength", cat="SGCompound", src="SG p.217-220",
  force="Force", avail="(Force x 6)R", cost="Force x 3,000¥", bond="-",
  rules=f"{_SG_COMP} Trigger Contact. Hardened Mystic Armor. Aftereffect: Physical limit 1 for equal duration. Reagent: refined teonanacatl (Aztlan)."),
E(name="Witch's moss", cat="SGCompound", src="SG p.217-220",
  force="Force", avail="(Force x 6)R", cost="Force x 1,600¥", bond="-",
  rules=f"{_SG_COMP} Trigger Contact. Paralyzing Touch. Aftereffect: both arms Broken Grip + Weak Side. Reagent: refined barghest blood."),
]

# ========== CF COMPOUNDS ==========
ITEMS += [
E(name="Animal Tongue", cat="CFCompound", src="CF p.186-189",
  force="dose", avail="6R", cost="1,500¥", bond="-",
  rules="Vector Ingestion; Speed 3D6 min; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 3 / Thresh 2. Grants Animal Control. After: Fear from animals for equal duration (spirits not animals). Ingredient: manzana cactus radical pulp (Aztlan)."),
E(name="Immortal Flower", cat="CFCompound", src="CF p.186-189",
  force="dose", avail="14R", cost="2,500¥", bond="-",
  rules="Vector Ingestion; Speed 16 Combat Rounds; Duration Essence + 1D6 h (max 12). Addiction Both; Rating 8 / Thresh 3. Grants Regeneration. Per 20 boxes damage while under: -0.1 Essence permanent. Cyber/bioware users: 2D6P unresisted when wears off (regen 'repairs' implants). Ingredient: immortal flower petals (Mojave)."),
E(name="Little Smoke", cat="CFCompound", src="CF p.187-189",
  force="dose", avail="12F", cost="1,800¥", bond="-",
  rules="Vector Inhalation; Speed 2D6 min; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 6 / Thresh 3. Grants Concealment + Confusion. After: Perception and Willpower = 1 for equal duration. Ingredient: 3 units refined Great Plains grasses."),
E(name="Rock Lizard Blood", cat="CFCompound", src="CF p.187-189",
  force="dose", avail="10R", cost="1,700¥", bond="-",
  rules="Vector Ingestion; Speed 30 min; Duration Essence + 1D6 h (max 12). Addiction Physical; Rating 6 / Thresh 3. Grants Immunity (Diseases and Toxins). After: 2P unresisted + -4 resist disease/toxin for equal duration. Ingredient: weeping tree radical pulp (N. America)."),
E(name="Shade", cat="CFCompound", src="CF p.187-189",
  force="dose", avail="6R", cost="1,000¥", bond="-",
  rules="Vector Inhalation; Speed Immediate; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 7 / Thresh 3. Forces astral projection (even mundanes); metaplanes with spirit guide/initiate. After: 10S unresisted. Must return before duration ends or die. Awakened: adds duration to normal astral time. Ingredient: red orchid pollen radical (SE Asia)."),
E(name="Wudu'aku", cat="CFCompound", src="CF p.187-189",
  force="dose", avail="12F", cost="2,350¥", bond="-",
  rules="Vector Ingestion/Inhalation; Speed 2D6 min; Duration Essence + 1D6 h (max 12). Addiction Psych; Rating 4 / Thresh 1. +2 Conjuring group; +2 Charisma vs spirits of man. After: -2 Conjuring and -2 Charisma vs other spirit types for 24h. Ingredient: powdered fossil radical (Australian Outback)."),
E(name="Zombie Dust", cat="CFCompound", src="CF p.187-189",
  force="dose", avail="12F", cost="1,500¥", bond="-",
  rules="Vector Contact/Injection; Speed 2 Combat Turns; Duration Essence + 1D6 h (max 12). Addiction Physiological; Rating 2 / Thresh 3. Prepares target for possession (still Intuition + Willpower resist). Ingredient: exotic metahuman remains + traditional animal powders."),
]

# ========== FA TOOLS ==========
ITEMS += [
E(name="Atomizer", cat="FATool", src="FA p.193-194",
  force="-", avail="4", cost="500¥", bond="-",
  rules="Converts one solid/liquid compound to aerosol. Contact-trigger compounds do not fire until sprayed substance contacts target. Ranged attack max 3 m. Device contact does not trigger payload."),
E(name="Atomizer cartridge (empty)", cat="FATool", src="FA p.194",
  force="-", avail="2", cost="5¥", bond="-",
  rules="Consumable cartridge for atomizer."),
E(name="Alembic", cat="FATool", src="FA p.193",
  force="-", avail="not on tools table", cost="3,000¥", bond="-",
  rules="Doubles yield when refining raw->refined or refined->radical (10 base -> 2 instead of 1)."),
E(name="Athanor", cat="FATool", src="FA p.193-194",
  force="-", avail="4", cost="1,000¥", bond="-",
  rules="Furnace: may leave up to 1 hour during 10h refine; orichalcum attendance every 12h instead of 10h."),
E(name="Crucible", cat="FATool", src="FA p.193-194",
  force="-", avail="2", cost="500¥", bond="-",
  rules="10h process upgrades reagent quality one step (max to Prime)."),
E(name="Vault of ages", cat="FATool", src="FA p.193-194",
  force="Rating 1-5", avail="(Rating + 4)R", cost="2,000¥ x Rating", bond="-",
  rules="Stores compounds/preparations: capacity = 2 x creator Magic; stored item Rating <= 2 x vault Rating. No Potency decay while inside; clock resumes on removal."),
]

# ========== FA COMPOUNDS ==========
_FA_BUY = "Buy: [(Force of spell involved) + Current Potency] x 500¥; Avail 14R. Needs Advanced Alchemy. Scarcity may raise price."
ITEMS += [
E(name="Alchemical Duct Tape", cat="FACompound", src="FA p.194-195",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Command. On activate: each hit repairs 1 Structure or 1 damage box (Fix spell, SG). Aftereffect Stunned. Reagent: refined mallard fat. Only magical repair; then mundane fixes."),
E(name="Astral Increase", cat="FACompound", src="FA p.194-195",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. Doubles time magician may remain manifested while projecting. Aftereffect Winded. Reagent: radical ghost orchid petals."),
E(name="Astral Bond", cat="FACompound", src="FA p.195",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. While lasting, while manifesting may activate command triggers. Aftereffect Can't Speak. Reagent: refined insect-host organ."),
E(name="Baobhan's Tears", cat="FACompound", src="FA p.195",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. Poison: 4P resist Body only; if any damage unresisted, -1 Essence for 24h (max 1 Essence loss / 24h from repeats). Aftereffect Stunned. Reagent: refined baobhan tears (CoS)."),
E(name="Drain Away", cat="FACompound", src="FA p.195",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. Next Physical Drain damage negated. Aftereffect Nauseated. Reagent: refined adept veins."),
E(name="Dulled Edges", cat="FACompound", src="FA p.195",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. Physical limit -2 for 3 turns. Aftereffect Fatigued. Reagent: radical killdeer antler (HS)."),
E(name="Feel No Pain", cat="FACompound", src="FA p.195-196",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Command. Each net hit = 1 hour sleep for fatigue + skip 1 meal. When ends, dehydration/starvation apply immediately. >3 consecutive days: Addiction 4/2 risk. Aftereffect Fatigued. Reagent: radical kayeri mushroom."),
E(name="Force of Personality", cat="FACompound", src="FA p.196",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Command. Apply to skin; +2 Charisma for astral combat only. Aftereffect Stunned. Reagent: radical ghost orchid petals."),
E(name="HMHVV II Inhibitor", cat="FACompound", src="FA p.196",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. Dose every 7 days; halts HMHVV II progress (not a cure). Missed dose: virus resumes, often worse. Addiction 3/1. Aftereffect Fatigued. Reagent: refined drop bear saliva (HS)."),
E(name="Laminate", cat="FACompound", src="FA p.196",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. Aerosol protects writing/runes from scuffing (1P destroys layer). Aftereffect Blinded (one eye). Reagent: refined slug glands."),
E(name="Perfect Sight", cat="FACompound", src="FA p.196-197",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Command. Apply to eyes: astral perception; ambient Noise + net hits (Interference, SG). Aftereffect Stunned. Reagent: refined ghost orchid petals."),
E(name="Sharpshooter", cat="FACompound", src="FA p.197",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Command. Eyes or pill: per net hit reduce Range category one step; +1 visual Perception. Aftereffect Blinded (one eye). Reagent: radical bird-of-prey eyes."),
E(name="Unstoppable Vigor", cat="FACompound", src="FA p.197",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. +Potency boxes on Stun CM usable only vs Drain; vanish when Potency ends or filled. Addiction 6/3. Aftereffect Slowed. Reagent: refined drake scales."),
E(name="Water Breathing", cat="FACompound", src="FA p.197",
  force="Force+Potency priced", avail="14R", cost=_FA_BUY, bond="-",
  rules="Trigger Contact. Gills power; while active may only breathe water (air suffocates). Cancel restores air breathing. Aftereffect Winded. Reagent: refined salmon scales."),
]

# ========== FA PREPARATIONS ==========
_FA_PREP = "Named alchemical preparation. Buy same as FA compounds: [(Force)+(Potency)] x 500¥, Avail 14R. Lynchpin fragile. Spell rules not reprinted here."
ITEMS += [
E(name="Abandon All Hope", cat="FAPrep", src="FA p.198",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Contact. Enacts Foreboding (SG)."),
E(name="Barricade", cat="FAPrep", src="FA p.198",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Reinforce (SG) on applied object."),
E(name="Burn, Baby, Burn", cat="FAPrep", src="FA p.198",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Ignite (Core)."),
E(name="Do Your Best", cat="FAPrep", src="FA p.198",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Increase Inherent Limits (SG); only one limit at a time; new activation replaces prior."),
E(name="Get Away From My Ride", cat="FAPrep", src="FA p.198",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Protect Vehicle (SG)."),
E(name="High as a Kite", cat="FAPrep", src="FA p.199",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Enabler (SG)."),
E(name="Noise on the Line", cat="FAPrep", src="FA p.199",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Increase Noise (SG)."),
E(name="NOMW (Not On My Watch)", cat="FAPrep", src="FA p.199",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Contact. Enacts Stabilize (Core)."),
E(name="Lightning Blade", cat="FAPrep", src="FA p.199",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Written on weapon; next successful attack cannot be resisted by metal armor. Required spell listed: Lightning Bolt (Core)."),
E(name="Spirit Zapper", cat="FAPrep", src="FA p.199",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Mana Barrier (Core) or Offensive Mana Barrier (SG) depending on preparation."),
E(name="Stink Bomb", cat="FAPrep", src="FA p.199",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command or Contact. Enacts Stench (SG); affects friend and foe."),
E(name="Stop Thief!", cat="FAPrep", src="FA p.199-200",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Glue Strip (SG)."),
E(name="Truth Serum", cat="FAPrep", src="FA p.200",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Compel Truth (SG)."),
E(name="Up and At 'Em", cat="FAPrep", src="FA p.200",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command or Contact. Enacts Awaken (SG)."),
E(name="Watch Your Step", cat="FAPrep", src="FA p.200",
  force="Force+Potency priced", avail="14R", cost=_FA_PREP, bond="-",
  rules="Trigger Command. Enacts Ice Sheet (Core)."),
]

# ========== RELATED OPTICS (mage LoS; also Sensors) ==========
ITEMS += [
E(name="Mage Sight Goggles", cat="Related", src="Core Street Gear Optical Devices p.444 / table; also Sensors and Optics.md",
  force="-", avail="12R", cost="3,000¥", bond="-",
  rules="Heavy goggles + myomeric rope around fiber-optic ending in optical lens. Rope lengths 10, 20, or 30 m. Pure optical (not electronic): magician can get spellcasting LOS from cover; spellcasting through optics -3 dice. Cannot take vision enhancements. Primary catalog also Sensors and Optics.md."),
]

# ========== FA RARE / EXOTIC REAGENT INGREDIENTS (no shop Avail/Cost) ==========
ITEMS += [
E(name="Baobhan sith bone or hair", cat="FAReagent", src="FA p.188-189; CoS p.114 cited",
  force="Superior+ specialty", avail="no printed Avail/Cost", cost="no printed (Superior+ market)", bond="-",
  rules="Even lowest quality = Superior reagent. Refined: regeneration/heal compounds or poison vs body+Magic. Used refined as Baobhan's Tears tears variant; bone/hair for related preps."),
E(name="Baobhan sith tears (refined)", cat="FAReagent", src="FA p.195 Baobhan's Tears",
  force="Superior+ specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Required reagent for Baobhan's Tears compound."),
E(name="Drop bear saliva", cat="FAReagent", src="FA p.189; HS p.60",
  force="Superior+ specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Awakened koala (HMHVV II carriers). Refined saliva: HMHVV II Inhibitor compound."),
E(name="Ghost orchid petals", cat="FAReagent", src="FA p.190",
  force="Superior+ specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Moon-blooming; hard to cultivate. Refined: vision compounds (Perfect Sight). Radical: Astral Increase, Force of Personality."),
E(name="Killdeer antler (ground)", cat="FAReagent", src="FA p.190; HS p.97",
  force="Superior+ specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Easy to counterfeit vs whitetail. Radical: Dulled Edges. Also healing/regen/toxin-resistance compounds."),
E(name="Kayeri mushroom", cat="FAReagent", src="FA p.190-191; CoS p.121 cited",
  force="Prime-quality inherent (text)", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="From kayeri (Tir na nOg / CoS). Radical: Feel No Pain. Curatives for toxins/disease."),
E(name="Drake scales", cat="FAReagent", src="FA p.191; HS p.162",
  force="exotic specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Refined: Unstoppable Vigor. Any type of drake scales."),
E(name="Insect spirit host organ", cat="FAReagent", src="FA p.191-192",
  force="exotic specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Refined: Astral Bond compound."),
E(name="Adept veins", cat="FAReagent", src="FA p.192",
  force="exotic specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Refined: Drain Away. Harvest implies killing/maiming an adept."),
E(name="Mallard fat (refined)", cat="FAReagent", src="FA p.194 Alchemical Duct Tape",
  force="specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Required for Alchemical Duct Tape."),
E(name="Slug glands (refined)", cat="FAReagent", src="FA p.196 Laminate",
  force="specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Required for Laminate."),
E(name="Bird-of-prey eyes (radical)", cat="FAReagent", src="FA p.197 Sharpshooter",
  force="specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Required for Sharpshooter."),
E(name="Salmon scales (refined)", cat="FAReagent", src="FA p.197 Water Breathing",
  force="specialty", avail="no printed Avail/Cost", cost="no printed", bond="-",
  rules="Required for Water Breathing."),
]

# ========== RF PACKS ==========
ITEMS += [
E(name="Basic Magician PACK", cat="RFPack", src="RF p.251-252",
  force="-", avail="8", cost="2,000¥ / 1 Karma", bond="included",
  rules="Contents: Magical lodge materials (Force 4). Bundle of Core SKUs."),
E(name="Advanced Magician PACK", cat="RFPack", src="RF p.251-252",
  force="-", avail="12", cost="4,000¥ / 2 Karma", bond="included",
  rules="Contents: Magical lodge materials (Force 6) + 50 drams reagents."),
E(name="Magic Wand PACK", cat="RFPack", src="RF p.251-252",
  force="-", avail="8R", cost="36,000¥ / 18 Karma (+12 Karma)", bond="included",
  rules="Contents: Power focus (Force 2). +Karma is bonding."),
E(name="Magic Staff PACK", cat="RFPack", src="RF p.251-252",
  force="-", avail="12R", cost="54,000¥ / 27 Karma (+18 Karma)", bond="included",
  rules="Contents: Power focus (Force 3)."),
E(name="Basic Medicine Bag PACK", cat="RFPack", src="RF p.251-252",
  force="-", avail="6R", cost="8,000¥ / 4 Karma (+4 Karma)", bond="included",
  rules="Contents: Spell focus Spellcasting (Health) Force 2. Same cost for other category/type examples (counterspelling dreamcatcher, sustaining amulet, ritual drum)."),
E(name="Advanced Medicine Bag PACK", cat="RFPack", src="RF p.252",
  force="-", avail="12R", cost="16,000¥ / 8 Karma (+8 Karma)", bond="included",
  rules="Contents: Spell focus Spellcasting (Health) Force 4."),
E(name="Basic Spirit Stick PACK", cat="RFPack", src="RF p.252",
  force="-", avail="6R", cost="8,000¥ / 4 Karma (+4 Karma)", bond="included",
  rules="Contents: Spirit focus Summoning (beast spirits) Force 2. Other spirit-type themed foci same cost."),
E(name="Advanced Spirit Stick PACK", cat="RFPack", src="RF p.252",
  force="-", avail="12R", cost="16,000¥ / 8 Karma (+8 Karma)", bond="included",
  rules="Contents: Spirit focus Summoning (beast spirits) Force 4."),
E(name="Magic Spear PACK", cat="RFPack", src="RF p.252",
  force="-", avail="8R", cost="14,000¥ / 7 Karma (+6 Karma)", bond="included",
  rules="Contents: Weapon focus Force 2 (spear form narrative; any melee weapon focus at that Force)."),
]

header = """# Magical Goods

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only; no flavor.

**Src PDFs:** `shadowrunfiftheditioncorerulebook_V2.pdf` · `streetgrimoire.pdf` · `forbiddenarcana.pdf` · `chromeflesh.pdf` · `runfaster.pdf`
**Books:** Core · SG · FA · CF · RF (INDEX). Shadow Spells / Court of Shadows: no local PDF (FA cites CoS reagents).
**See also:** `Mechanics/Magic Basics.md` · `Encyclopedia/Sensors and Optics.md` (optics catalog) · `Encyclopedia/Drugs Toxins and Chemicals.md` (Awakened drugs / BADs; also reprints CF magical compounds) · `Encyclopedia/Melee Weapons.md` (base Acc/Reach/DV/AP for Weapon Focus forms)

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

"""

def render(d):
    return "\n".join([
        f"### {d['name']}",
        f"- Cat: {d['cat']}",
        f"- Src: {d['src']}",
        f"- Force: {d['force']}",
        f"- Avail: {d['avail']} | Cost: {d['cost']}",
        f"- Bond: {d['bond']}",
        f"- Rules: {d['rules']}",
        "",
    ])

CAT_ORDER = [
    "Focus", "Formula", "Lodge", "Reagent", "SGShop", "SGCompound",
    "CFCompound", "FATool", "FACompound", "FAPrep", "FAReagent", "Related", "RFPack",
]
CAT_HEAD = {
    "Focus": "FOCI (Core categories + subtypes)",
    "Formula": "FORMULAE",
    "Lodge": "MAGICAL LODGE MATERIALS",
    "Reagent": "REAGENTS AND ORICHALCUM",
    "SGShop": "STREET GRIMOIRE TALISMONGERS / MANATECH",
    "SGCompound": "SG EMPOWERED MAGICAL COMPOUNDS",
    "CFCompound": "CHROME FLESH MAGICAL COMPOUNDS",
    "FATool": "FA ALCHEMICAL TOOLS",
    "FACompound": "FA COMPOUNDS",
    "FAPrep": "FA NAMED PREPARATIONS",
    "FAReagent": "FA RARE / EXOTIC REAGENT INGREDIENTS (no shop Avail/Cost)",
    "Related": "RELATED OPTICS (also Sensors and Optics.md)",
    "RFPack": "RF MAGIC PACKS (bundles)",
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
parts.append("""Foci subtypes (16): Enchanting Alchemical/Disenchanting; Metamagic Centering/Flexible Signature/Masking/Spell Shaping; Power; Qi; Spell Counterspelling/Ritual/Spellcasting/Sustaining; Spirit Summoning/Banishing/Binding; Weapon.

Formulae (6): Focus formula; Spell Combat/Detection/Health/Illusion/Manipulation.

Lodge (1): Magical Lodge Materials.

Reagents (12): Core raw; FA Tainted/Inferior/Subpar/Baseline/Superior/Prime; Refined; Radical; Orichalcum craft; Tool cleanser.

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
""")

text = "".join(parts)
for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u00d7", "x")):
    text = text.replace(a, b)
OUT.write_text(text, encoding="utf-8")
print("Wrote", OUT, "entries", len(ITEMS), "bytes", OUT.stat().st_size)
