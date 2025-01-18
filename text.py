# text.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2024 Dominic Ford <https://dcford.org.uk/>
#
# This code is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# this file; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

# ----------------------------------------------------------------------------

# A list of text strings, which we can render in various languages

from typing import Dict

text: Dict[str, dict] = {
    "en":
        {
            "title": "PLANISPHERE",
            "instructions_1": "Turn the star-wheel until you find the point around its edge where today's date is marked, and line this point up with the current time. The viewing window now shows all of the constellations that are visible in the sky.",
            "instructions_2": "Go outside and face {cardinal}. Holding the planisphere up to the sky, the stars marked at the bottom of the viewing window should match those that you see in the sky in front of you.",
            "instructions_3": """Turn to face east or west, and rotate the planisphere so that the word "East" or "West" is at the bottom of the window. Once again, the stars at the bottom of the viewing window should match those that you see in the sky in front of you.""",
            "instructions_4": (
                r"A planisphere is a simple hand-held device which shows a map of which stars are visible in the night sky at any particular time. By rotating the star wheel, it shows how stars move across the sky through the night, and how different constellations are visible at different times of year.",
                "",
                r"The constellations of the night sky revolve around the celestial poles once every 23 hour and 56 minutes. The idea of representing the night sky as a flat map, which is turned to emulate the night sky's rotation, dates back to the ancient Greek astronomer Hipparchus (circa 150 BC). The fact that this rotation takes four minutes less than the length of a day means that stars rise four minutes earlier each day, or half-an-hour earlier each week. Through the year, new constellations become visible in the pre-dawn sky, and disappear into evening twilight."),
            "more_info": "For more information, see https://in-the-sky.org/planisphere       \u00A9 Dominic Ford 2014\u20132024.",
            "glue_here": "GLUE HERE",
            "cut_out_instructions": (
                "Cut out this shaded area with scissors.",
                "",
                "It will become a viewing window through which to look at the star wheel behind."
            ),
            "cardinal_points": {"n": "NORTH", "s": "SOUTH", "w": "WEST", "e": "EAST"},
            "months": [
                [31, "JANUARY"],
                [28, "FEBRUARY"],
                [31, "MARCH"],
                [30, "APRIL"],
                [31, "MAY"],
                [30, "JUNE"],
                [31, "JULY"],
                [31, "AUGUST"],
                [30, "SEPTEMBER"],
                [31, "OCTOBER"],
                [30, "NOVEMBER"],
                [31, "DECEMBER"]
            ],
            "constellation_translations": {
            }
        },
        "lt":
        {
            "title": "Planisfera",
            "instructions_1": "Sukite žvaigždžių diską, kol rasite tašką jo krašte, kuriame pažymėta atitinkama data, ir sulygiuokite šį tašką su atitinkamu laiku. Peržiūros lange bus rodomi tuo metu danguje matomi žvaigždynai.",
            "instructions_2": "Išeikite į lauką ir atsisukite į šiaurę. Laikykite planisferą akių lygyje, užrašu „Šiaurė“ į apačią. Žvaigždės stebėjimo langelio apačioje turėtų atitikti žvaigždes, kurias matote danguje priešais save.",
            "instructions_3": """Atsisukite į rytus arba vakarus ir pasukite planisferą taip, kad lango apačioje būtų užrašas „Rytai“ arba „Vakarai“. Žvaigždės langelio apačioje turi atitikti žvaigždes, kurias matote danguje priešais save.""",
            "instructions_4": (
                r"Planisfera yra sukamasis žvaigždėlapis, kuriame rodomos žvaigždždės, matomos naktiniame danguje tam tikru metu. Sukdami žvaigždžių diską matome, kaip žvaigždės juda dangumi per parą ir kokie skirtingi žvaigždynai matomi skirtingais metų laikais.",
                "",
                r"Nakties dangaus žvaigždynai aplink dangaus ašigalius apsisuka kartą per 23 valandas ir 56 minutes. Sukamąjį žvaigždėlapį arba planisferą sugalvojo senovės graikų astronomas Hiparchas (apie 150 m. pr. m. e.). Tai, kad žvaigdžių skliauto sukimasis yra keturiomis minutėmis trumpesnis už dienos ilgį, reiškia, kad žvaigždės kiekvieną dieną pakyla keturiomis minutėmis anksčiau arba pusvalandžiu anksčiau kiekvieną savaitę. Per metus nauji žvaigždynai danguje matomi prieš aušrą ir išnyksta vakaro sutemose."),
            "more_info": "Daugiau skaitykite https://in-the-sky.org/planisphere       \u00A9 Dominic Ford 2014\u20132024.",
            "glue_here": "KLIJUOTI ČIA",
            "cut_out_instructions": (
                "Iškirpkite pažymėtą sritį.",
                "",
                "Tai bus apžvalgos langas, pro kurį žiūrėsite į už jo esantį žvaigždžių diską."
            ),
            "cardinal_points": {"n": "ŠIAURĖ", "s": "PIETŪS", "w": "VAKARAI", "e": "RYTAI"},
            "months": [
                [31, "SAUSIS"],
                [28, "VASARIS"],
                [31, "KOVAS"],
                [30, "BALANDIS"],
                [31, "GEGUŽĖ"],
                [30, "BIRŽELIS"],
                [31, "LIEPA"],
                [31, "RUGPJŪTIS"],
                [30, "RUGSĖJIS"],
                [31, "SPALIS"],
                [30, "LAPKRITIS"],
                [31, "GRUODIS"]
            ],
            "constellation_translations": {
                "Andromeda": "Andromeda",
                "Antlia": "Siurblys",
                "Apus": "Rojaus_Paukštis",
                "Aquarius": "Vandenis",
                "Aquila": "Erelis",
                "Ara": "Aukuras",
                "Aries": "Avinas",
                "Auriga": "Vežėjas",
                "Boötes": "Jaučiaganis",
                "Caelum": "Skaptukas",
                "Camelopardalis": "Žirafa",
                "Cancer": "Vėžys",
                "Canes_Venatici": "Skalikai",
                "Canis_Major": "Didysis_Šuo",
                "Canis_Minor": "Mažasis_Šuo",
                "Capricornus": "Ožiaragis",
                "Carina": "Laivo_kilis",
                "Cassiopeia": "Kasiopėja",
                "Centaurus": "Kentauras",
                "Cepheus": "Cefėjas",
                "Cetus": "Banginis",
                "Chamaeleon": "Chameleonas",
                "Circinus": "Skriestuvas",
                "Columba": "Balandis",
                "Coma_Berenices": "Berenikės_Garbanos",
                "Corona_Australis": "Pietų_Vainikas",
                "Corona_Borealis": "Šiaurės_Vainikas",
                "Corvus": "Varnas",
                "Crater": "Taurė",
                "Crux": "Pietų_Kryžius",
                "Cygnus": "Gulbė",
                "Delphinus": "Delfinas",
                "Dorado": "Aukso_Žuvis",
                "Draco": "Slibinas",
                "Equuleus": "Žirgelis",
                "Eridanus": "Eridanas",
                "Fornax": "Krosnis",
                "Gemini": "Dvyniai",
                "Grus": "Gervė",
                "Hercules": "Heraklis",
                "Horologium": "Laikrodis",
                "Hydra": "Hidra",
                "Hydrus": "Pietų_Hidra",
                "Indus": "Indėnas",
                "Lacerta": "Driežas",
                "Leo": "Liūtas",
                "Leo_Minor": "Mažasis_Liūtas",
                "Lepus": "Kiškis",
                "Libra": "Svarstyklės",
                "Lupus": "Vilkas",
                "Lynx": "Lūšis",
                "Lyra": "Lyra",
                "Mensa": "Stalkalnis",
                "Microscopium": "Mikroskopas",
                "Monoceros": "Vienaragis",
                "Musca": "Musė",
                "Norma": "Matuoklė",
                "Octans": "Oktantas",
                "Ophiuchus": "Gyvatnešis",
                "Orion": "Orionas",
                "Pavo": "Povas",
                "Pegasus": "Pegasas",
                "Perseus": "Persėjas",
                "Phoenix": "Feniksas",
                "Pictor": "Tapytojas",
                "Pisces": "Žuvys",
                "Piscis_Austrinus": "Pietų_Žuvis",
                "Puppis": "Laivagalis",
                "Pyxis": "Kompasas",
                "Reticulum": "Tinklelis",
                "Sagitta": "Strėlė",
                "Sagittarius": "Šaulys",
                "Scorpius": "Skorpionas",
                "Sculptor": "Skulptorius",
                "Scutum": "Skydas",
                "Serpens": "Gyvatė",
                "Sextans": "Sekstantas",
                "Taurus": "Jautis",
                "Telescopium": "Teleskopas",
                "Triangulum": "Trikampis",
                "Triangulum_Australe": "Pietų_Trikampis",
                "Tucana": "Tukanas",
                "Ursa_Major": "Didieji_Grižulo_ratai",
                "Ursa_Minor": "Mažieji_Grižulo_ratai",
                "Vela": "Burės",
                "Virgo": "Mergelė",
                "Volans": "Skraidanti_Žuvis",
                "Vulpecula": "Laputė",
            }
        },
    "es":
        {
            "title": "PLANISFERIO",
            "instructions_1": "Gira la rueda de estrellas hasta encontrar el punto del borde donde está la fecha del día, y alínealo con la hora actual. El visor ahora muestra todas las constelaciones visibles en el cielo.",
            "instructions_2": "Ve afuera y apunta al {cardinal}. Sosteniendo el planisferio hacia el cielo, las estrellas indicadas en el borde inferior del visor deberían coincidir con las que ves en el cielo frente a ti",
            "instructions_3": """Gira hacia el Este o el Oeste, y gira el planisferio hasta que la palabra "Este" u "Oeste" esté en la parte inferior del visor. Nuevamente, las estrellas en el borde inferior deberían coincidir con lo que ves en el cielo frente a ti""",
            "instructions_4": (

                r"Un planisferio es un dispositivo portátil simple que muestra un mapa de las estrellas visibles en el cielo nocturno en cualquier momento en particular. Al rotar la rueda de estrellas se muestra cómo se mueven las estrellas en el cielo durante la noche, y qué constelaciones son visibles en diferentes momentos del año.",
                "",
                r"Las constelaciones en el cielo nocturno giran alrededor de los polos celestes cada 23 horas y 56 minutos. La idea de representar el cielo nocturno como un mapa plano que se gira para emular la rotación del cielo nocturno se remonta al astrónomo Griego antiguo Hiparco de Nicea (alrededor de 150 a.C.). Como esta rotación dura menos que la longitud del día, las estrellas surgen cuatro minutos más temprano cada día, o media hora más temprano cada semana. A lo largo del año se pueden ver nuevas constelaciones en el cielo antes del amanecer, y otras desaparecen antes del atardecer."),
            "more_info": "Para más información: https://in-the-sky.org/planisphere       \u00A9 Dominic Ford 2014\u20132024.",
            "glue_here": "PEGAR AQUÍ",
            "cut_out_instructions": (
                "Corta el area sombreada con tijeras.",
                "",
                "Esto será el visor a través del que mirarás la rueda de estrellas."
            ),
            "cardinal_points": {"n": "NORTE", "s": "SUR", "w": "OESTE", "e": "ESTE"},
            "months": [
                [31, "ENERO"],
                [28, "FEBRERO"],
                [31, "MARZO"],
                [30, "ABRIL"],
                [31, "MAYO"],
                [30, "JUNIO"],
                [31, "JULIO"],
                [31, "AGOSTO"],
                [30, "SEPTIEMBRE"],
                [31, "OCTUBRE"],
                [30, "NOVIEMBRE"],
                [31, "DICIEMBRE"]
            ],
            "constellation_translations": {

            }
        }
}
