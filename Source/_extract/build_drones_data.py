# -*- coding: utf-8 -*-
"""Build structured drone data from Rigger 5 PDF text extracts."""
import fitz
import re
import json

doc = fitz.open(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf")

# ---- Parse compiled tables into rows ----
# Manual rows from pages 189-191 (verified against PDF extract)
# Fields: name, handl, speed, accel, body, armor, pilot, sens, seats, avail, cost, ref_page, size_hint

TABLE = r"""
Ares KN-Y0 Deimos|3|2G|1|6(0)|18|5|3|—|20F|220,000¥|143|Huge
Ares KN-Y0 Eris|3|2G|1|6(0)|18|5|3|—|24F|270,000¥|143|Huge
Ares KN-Y0 Phobos|3|2G|1|6(0)|18|5|3|—|16F|250,000¥|143|Huge
NeoNET Avenging Angel|3|6J|2|6(0)|12|6|6|—|40F|1,000,000¥|145|Huge
SAAB-Thyssen Bloodhound|3|1G|1|2(0)|0|2|4|—|8|10,000¥|136|Small
Lone Star Castle Guard|4/2|1G|1|2(0)|6|3|2|—|8R|10,000¥|133|Small
Ares Cheetah|4|6G|2|2(0)|6|3|2|—|12R|14,000¥|138|Medium
Aerodesign Systems Condor LDSD-23|2|0R|0|1(1)|0|2|4|—|6R|4,000¥|129|Mini
Aztechnology Crawler|4|3|1|3|3|4|3|—|4|4,000¥|466 Core|Small
Aztechnology Criado Juan|2|2G|1|2|0|2|2|—|2|8,000¥|145|Anthro
Cyberspace Designs Dalmatian|5|5|3|5|5|3|3|—|6R|10,000¥|466 Core|Large
Saeder-Krupp Direktionssekretar|4|4G|2|4|3|4|4|—|12R|40,000¥|148|Anthro
GM-Nissan Doberman|5|3|1|4|4|3|3|—|4R|5,000¥|466 Core|Medium
Cyberspace Designs Dragonfly|4|2P|1|1(0)|3|3|2|—|12R|4,000¥|129|Mini
Ares Duelist|3|3|1|4|4|3|3|—|5R|4,500¥|466 Core|Medium
Evo Krokodil|3|2G/3W|1|3(1)|6|2|2|—|8R|12,000¥|139|Medium
Federated-Boeing Kull|3|4P|2|3(3)|0|3|2|—|4|10,000¥|140|Medium
Ferret RPD-5X|4/2|1G|1|2(1)|3|3|3|—|8R|4,000¥|132|Small
MCT Fly-Spy|4|3|2|1|0|3|3|—|8|2,000¥|466 Core|Mini
Horizon Flying Eye|4|3|2|1|0|3|3|—|8|2,000¥|466 Core|Mini
Ares Garuda|6|3J/6J|2/4|2|2|4|3|—|20F|8,500¥|149|Drone Missile
Renraku Gerbil|4/2|2G|1|1(1)|0|2|2|—|4|2,000¥|130|Mini
Sony Goldfish|2/4|1W|1|0|0|2|2|—|6|500¥|128|Micro
Mitsuhama Gun Turret|—|—|—|2(0)|6|3|2|—|4R|4,000¥|133|Small
Aztechnology Hedgehog|3|1G|1|1(0)|0|4|3|—|8F|8,000¥|129|Mini
Horizon CU^3|4|1P|1|1(1)|0|2|3|—|4|3,000¥|130|Mini
Renraku Jardinero|2/4|1G|1|2(1)|0|2|2|—|4|2,000¥|136|Small
Renraku Job-a-Mat|—|—|—|2(2)|0|2|2|—|4|3,000¥|137|Small
NeoNET Juggernaught|3|4G|1|6|12|3|3|—|14R|100,000¥|147|Anthro
Shiawase Kanmushi|4|2|1|0|0|3|3|—|8|1,000¥|465 Core|Micro
MCT Kenchiku-Kikai|2|2G|1|5|3|2|2|—|8R|20,000¥|146|Anthro
Knight Errant P5 Pursuit|4/2|6G|2|2(1)|0|3|2|—|10R|8,000¥|133|Small
Mesametric Kodiak|2/4|2G|1|6(2)|12|2|2|—|12R|40,000¥|145|Huge
Proteus A.G. Krake|5|3W|4|2(0)|2|4|3|—|18F|10,000¥|134|Small
Renraku LEBD-2|4|2P|1|3(0)|9|4|4|—|12R|20,000¥|140|Medium
Horizon Little Buddy|2|1G|1|1|0|2|2|—|4|2,000¥|146|Anthro
Steel Lynx|5|4|2|6|12|3|3|—|10R|25,000¥|466 Core|Large
Mitsuhama Malakim|3|6P|2|4(0)|9|4|4|—|20F|40,000¥|143|Large
Ares Matilda|1|2G|1|8|8|2|1|—|12R|18,000¥|141|Large
CrashCart MediCart|5|5G|1|6(2)|5|4|4|—|6|10,000¥|142|Large
Sikorsky-Bell Microskimmer|3|3|1|0|0|3|3|—|6|1,000¥|465 Core|Micro
Horizon Mini-Zep|2|0P|0|2(4)|0|2|2|4|4|2,000¥|132|Small
Ares Mule|4|1G|1|4(3)|6|2|2|—|4|8,000¥|141|Large
Saeder-Krupp Mk-17D Neptune|2|3W|1|5(0)|3|4|3|—|10R|17,500¥|143|Large
Horizon NoizQuito|4|3R|2|1|0|3|3|—|10R|2,000¥|128|Micro
Lockheed Optic-X2|4|4|3|2|2|3|3|—|10|21,000¥|466 Core|Small
Ares Paladin|5|4G|1|5(0)|18|3|2|—|8R|5,000¥|142|Large
Renraku Pelican|4|2P|1|2(1)|0|2|2|—|2|4,000¥|137|Small
Festo Pigeon 2.0|4|2P|1|1(1)|0|2|2|—|8|3,000¥|129|Mini
NeoNET Prairie Dog|2/4|2G|1|2(0)|3|3|4|—|12F|8,000¥|134|Small
Evo Proletarian|4/2|2G|1|2(1)|0|2|2|—|6|4,000¥|131|Small
Renraku Scuttler Remote Cyberhand|n/a|n/a|n/a|n/a|n/a|n/a|—|—|8|8,000¥|130|Mini
Renraku Dove|4|2P|1|2(1)|0|2|2|—|4|5,000¥|136|Small
MCT-Nissan Roto-Drone|4|4|2|4|4|3|3|—|6|5,000¥|466 Core|Medium
Ares Arms Sentry V|4/—|1G|1|2(0)|6|3|2|—|4R|4,000¥|130|Small
Mitsuhama Seven|4|1P|1|1(1)|0|2|3|—|4|3,000¥|133|Small
Mitsuhama Seven Wheelie chassis|4/2|2G|1|1(3)|0|1|1|—|—|2,000¥|133|Chassis
Mitsuhama Seven Treads chassis|3|2G|1|1(3)|0|1|1|—|2|2,000¥|133|Chassis
Mitsuhama Seven Dirty chassis|2/4|2G|1|1(3)|0|1|1|—|2|2,000¥|133|Chassis
Mitsuhama Seven Quad chassis|4|1G|1|1(3)|0|1|1|—|4|2,000¥|133|Chassis
Mitsuhama Seven Swims chassis|3|2W|1|1(3)|0|1|1|—|4|1,000¥|133|Chassis
Mitsuhama Seven Hovers chassis|4|1P|1|1(3)|0|1|1|—|6|4,000¥|133|Chassis
Mitsuhama Seven Soars chassis|3|2J|1|1(3)|0|1|1|—|8|4,000¥|133|Chassis
Festo Sewer Snake|3|1G/1W|1/1|2(1)|0|2|2|—|10|6,000¥|132|Small
Telestrian Industries Shamus|3|3G|1|4(0)|4|3|8|—|10|30,000¥|137|Small
Shiawase i-Doll|3|3G|1|3|0|3|3|—|4|20,000¥|148|Anthro
Citron-Brouillard Smoke Generator|3|1G|1|2(0)|0|2|2|—|8|4,000¥|130|Small
Transys Steed|4/2|1G|1|3(1)|0|2|2|—|2|4,000¥|140|Medium
Pratt & Whitney Sundowner|3|4P|1|2(0)|0|2|2|—|8|10,000¥|134|Small
GTS Tower|2|1P|1|4(0)|6|2|2|—|8|10,000¥|143|Large
MCT Tunneler|3|0P|0|3(2)|6|2|2|—|8R|10,000¥|140|Medium
Cyberspace Designs Wolfhound|3|2J|1|2(1)|0|2|4|—|12|30,000¥|131|Small
"""

# Need Aeroquip Dustoff - missing from compiled table! Extract from page 141
print("Looking for Dustoff on page 141:")
print(doc[140].get_text()[:3500])
