# import json

dictionary = {
    "converter": [
        'Area Converter',
        "Angle Converter",
        'Length Converter',
        'Time Converter',
        'Temperature Converter',
        "Volume Converter",
        'Weight Converter',
        "Speed Converter",
        "Storage Converter",
        "Energy Converter",
    ],

    'angle': {
        "degree": 1,
        'radian': 57.2957795131,
        'second': 0.0002777778,
        "minute": 0.0166666667,
        'gon': 0.9,
        'mil': 0.05625,
        'sign': 30,
        'grad': 0.9,
        'turn': 360,
        'circle': 360,
        'sextant': 60,
        'quadrant': 90,
        'revolution': 360,
        'right angle': 90,
    },

    'time_common': {
        'Millisecond': 0.001,
        'Microsecond': 1.0E-6,
        'Nanosecond': 1.0E-9,
        'Picosecond': 1.0E-12,
        'Second': 1,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Month': 2628000,
        'Year': 31557600,
        'Decade': 315576000,
        'Century': 3155760000,
    },

    'time_all': {
        "second": 1,
        'millisecond': 0.001,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2628000,
        'year': 31557600,
        'decade': 315576000,
        'century': 3155760000,
        'millennium': 31557600000,
        'microsecond': 1.0E-6,
        'nanosecond': 1.0E-9,
        'picosecond': 1.0E-12,
        'femtosecond': 1.0E-15,
        'attosecond': 1.0E-18,
        'shake': 1.0E-8,
        'fortnight': 1209600,
        'septennial': 220752000,
        'octennial': 252288000,
        'novennial': 283824000,
        'quindecennial': 473040000,
        'quinquennial': 157680000,
        'planck time': 5.39056E-44,
        'second(sidereal)': 0.9972695602,
        'minute(sidereal)': 59.8361736111,
        'hour(sidereal)': 3590.1704166667,
        'day(sidereal)': 86164.09,
        'month(synodic)': 2551443.84,
        'year(leap)': 31622400,
        'year(julian)': 31557600,
        'year(tropical)': 31556930,
        'year(sidereal)': 31558149.54,
    },

    'storage_common': {
        'bit': 1,
        'nibble': 4,
        'byte': 8,
        'kilobyte': 8192,
        'megabyte': 8388608,
        'gigabyte': 8589934592,
        'terabyte': 8796093022208,
        'petabyte': 9.007199254741E+15,
        'exabyte': 9.2233720368548E+18,
    },

    'storage_all': {
        'bit [b]': 1,
        'nibble': 4,
        'byte [B]': 8,
        'character': 8,
        'word': 16,
        'MAPM-word': 32,
        'quadruple-word': 64,
        'block': 4096,
        'kilobit': 1024,
        'kilobyte': 8192,
        'megabit': 1048576,
        'megabyte': 8388608,
        'gigabit': 1073741824,
        'gigabyte': 8589934592,
        'terabit': 1099511627776,
        'terabyte': 8796093022208,
        'petabit': 1.1258999068426E+15,
        'petabyte': 9.007199254741E+15,
        'exabit': 1.1529215046068E+18,
        'floppy disk (3.5", DD)': 5830656,
        'exabyte': 9.2233720368548E+18,
        'floppy disk (3.5", HD)': 11661312,
        'Zip 100': 803454976,
        'floppy disk (3.5", ED)': 23322624,
        'Zip 250': 2008637440,
        'floppy disk (5.25", DD)': 2915328,
        'Jaz 1GB': 8589934592,
        'floppy disk (5.25", HD)': 9711616,
        'Jaz 2GB': 17179869184,
        'DVD (1 layer, 1 side)': 40372692582.4,
        'CD (74 minute)': 5448466432,
        'DVD (2 layer, 1 side)': 73014444032,
        'CD (80 minute)': 5890233976,
        'DVD (1 layer, 2 side)': 80745385164.8,
        'DVD (2 layer, 2 side)': 146028888064,
    },

    "length_common": {
        'Meter': 1,
        'mile': 1609.344,
        'kilometer': 1000,
        'yard': 0.9144,
        'decimeter': 0.1,
        'foot': 0.3048,
        'centimeter': 0.01,
        'inch': 0.0254,
        'millimeter': 0.001,
        'nautical mile': 1852,
        'micrometer': 1.0E-6,
        'light year [ly]': 9.46073047258E+15,
        'nanometer': 1.0E-9,
    },

    "length_all": {
        'Meter': 1,
        'mile': 1609.344,
        'kilometer': 1000,
        'yard': 0.9144,
        'decimeter': 0.1,
        'foot': 0.3048,
        'centimeter': 0.01,
        'inch': 0.0254,
        'millimeter': 0.001,
        'nautical mile': 1852,
        'micrometer': 1.0E-6,
        'light year': 9.46073047258E+15,
        'nanometer': 1.0E-9,
        'exameter': 1.0E+18,
        'petameter': 1.0E+15,
        'terameter': 1000000000000,
        'gigameter': 1000000000,
        'megameter': 1000000,
        'hectometer': 100,
        'dekameter': 10,
        'micron': 1.0E-6,
        'picometer': 1.0E-12,
        'femtometer': 1.0E-15,
        'attometer': 1.0E-18,
        'megaparsec': 3.08567758128E+22,
        'kiloparsec': 3.08567758128E+19,
        'parsec': 3.08567758128E+16,
        'astronomical unit': 149597870691,
        'league': 4828.032,
        'nautical league (int.)': 5556,
        'kiloyard': 914.4,
        'furlong': 201.168,
        'chain': 20.1168,
        'rope': 6.096,
        'rod': 5.0292,
        'perch': 5.0292,
        'pole': 5.0292,
        'fathom': 1.8288,
        'ell': 1.143,
        'link': 0.201168,
        'hand': 0.1016,
        'span (cloth)': 0.2286,
        'finger (cloth)': 0.1143,
        'nail (cloth)': 0.05715,
        'barleycorn': 0.0084666667,
        'microinch': 2.54E-8,
        'angstrom': 1.0E-10,
        'X-unit': 1.00208E-13,
        'arpent': 58.5216,
        'pica': 0.0042333333,
        'point': 0.0003527778,
        'twip': 1.76389E-5,
        'aln': 0.5937777778,
        'famn': 1.7813333333,
        'caliber': 0.000254,
        'centiinch': 0.000254,
        'ken': 2.11836,
        'Electron radius (classical)': 2.81794092E-15,
        'long reed': 3.2004,
        "Earth's equatorial radius": 6378160,
        'reed': 2.7432,
        "Earth's distance from sun": 149600000000,
        'long cubit': 0.5334,
        "Earth's polar radius": 6356776.9999999,
        'handbreadth': 0.0762,
        'Planck length': 1.61605E-35,
        'fingerbreadth': 0.01905,
        "Sun's radius": 696000000,
    },

    "energy_common": {
        "joule": 1,
        'kilowatt-hour [kW*h]': 3600000,
        'kilojoule [kJ]': 1000,
        'megaelectron-volt [MeV]': 1.6021766339999E-13,
        'megajoule [MJ]': 1000000,
        'kiloelectron-volt [keV]': 1.6021766339999E-16,
        'gigajoule [GJ]': 1000000000,
        'electron-volt [eV]': 1.6021766339999E-19,
        'millijoule [mJ]': 0.001,
        'gigawatt-hour [GW*h]': 3600000000000,
        'microjoule [µJ]': 1.0E-6,
        'megawatt-hour [MW*h]': 3600000000,
        'nanojoule [nJ]': 1.0E-9,
        'horsepower hour [hp*h]': 2684519.5368856,
        'attojoule [aJ]': 1.0E-18,
        'calorie (nutritional)': 4186.8,
        'watt-hour [W*h]': 3600,
        'kilowatt-second [kW*s]': 1000,
        'erg': 1.0E-7,
        'watt-second [W*s]': 1,
        'newton meter [N*m]': 1,
        'gigaton [Gton]': 4.184E+18,
        'megaton [Mton]': 4.184E+15,
        'kiloton [kton]': 4184000000000,
    },

    "energy_all": {
        "joule": 1,
        'Btu (IT) [Btu (IT), Btu]': 1055.05585262,
        'kilojoule [kJ]': 1000,
        'megaelectron-volt [MeV]': 1.6021766339999E-13,
        'megajoule [MJ]': 1000000,
        'kiloelectron-volt [keV]': 1.6021766339999E-16,
        'gigajoule [GJ]': 1000000000,
        'kilocalorie (IT) [kcal (IT)]': 4186.8,
        'millijoule [mJ]': 0.001,
        'kilocalorie (th) [kcal (th)]': 4184,
        'microjoule [µJ]': 1.0E-6,
        'calorie (IT) [cal (IT), cal]': 4.1868,
        'nanojoule [nJ]': 1.0E-9,
        'horsepower hour [hp*h]': 2684519.5368856,
        'kilowatt-hour [kW*h]': 3600000,
        'mega Btu (IT) [MBtu (IT)]': 1055055852.62,
        'attojoule [aJ]': 1.0E-18,
        'ton-hour (refrigeration)': 12660670.23144,
        'watt-hour [W*h]': 3600,
        'calorie (nutritional)': 4186.8,
        'Btu (th) [Btu (th)]': 1054.3499999744,
        'horsepower (metric) hour': 2647795.5,
        'electron-volt [eV]': 1.6021766339999E-19,
        'fuel oil equivalent @kiloliter': 40197627984.822,
        'erg': 1.0E-7,
        'fuel oil equivalent @barrel (US)': 6383087908.3509,
        'gigawatt-hour [GW*h]': 3600000000000,
        'calorie (th) [cal (th)]': 4.184,
        'kilowatt-second [kW*s]': 1000,
        'dyne centimeter [dyn*cm]': 1.0E-7,
        'megawatt-hour [MW*h]': 3600000000,
        'gram-force meter [gf*m]': 0.00980665,
        'watt-second [W*s]': 1,
        'gram-force centimeter': 9.80665E-5,
        'newton meter [N*m]': 1,
        'kilogram-force centimeter': 0.0980665,
        'gigaton [Gton]': 4.184E+18,
        "pound-force foot [lbf*ft]": 1.3558179483,
        'megaton [Mton]': 4.184E+15,
        "pound-force inch [lbf*in]": 0.112984829,
        'kiloton [kton]': 4184000000000,
        "ounce-force inch [ozf*in]": 0.0070615518,
        'ton (explosives)': 4184000000,
        'kilogram-force meter': 9.8066499997,
        "therm": 105505600,
        'kilopond meter [kp*m]': 9.8066499997,
        "therm (EC)": 105505600,
        "foot-pound [ft*lbf]": 1.3558179483,
        "therm (US)": 105480400,
        "inch-pound [in*lbf]": 0.112984829,
        "Hartree energy": 4.3597482E-18,
        "inch-ounce [in*ozf]": 0.0070615518,
        "Rydberg constant": 2.1798741E-18,
        "poundal foot [pdl*ft]": 0.04214011,
    },

    "speed_common": {
        "meter/second [m/s]": 1,
        "kilometer/hour [km/h]": 0.2777777778,
        "mile/hour [mi/h]": 0.44704,
        "kilometer/minute [km/min]": 16.6666666667,
        "meter/hour [m/h]": 0.0002777778,
        "kilometer/second [km/s]": 1000,
        "meter/minute [m/min]": 0.0166666667,
        "centimeter/minute [cm/min]": 0.0001666667,
        "centimeter/hour [cm/h]": 2.7777777777778E-6,
        "millimeter/minute [mm/min]": 1.66667E-5,
        "centimeter/second [cm/s]": 0.01,
        "millimeter/hour [mm/h]": 2.7777777777778E-7,
        "foot/hour [ft/h]": 8.46667E-5,
        "millimeter/second [mm/s]": 0.001,
        "foot/minute [ft/min]": 0.00508,
        "foot/second [ft/s]": 0.3048,
        "yard/hour [yd/h]": 0.000254,
        "yard/minute [yd/min]": 0.01524,
        "yard/second [yd/s]": 0.9144,
        "mile/minute [mi/min]": 26.8224,
        "mile/second [mi/s]": 1609.344,
    },

    "speed_all": {
        "meter/second [m/s]": 1,
        "kilometer/hour [km/h]": 0.2777777778,
        "mile/hour [mi/h]": 0.44704,
        "kilometer/minute [km/min]": 16.6666666667,
        "meter/hour [m/h]": 0.0002777778,
        "kilometer/second [km/s]": 1000,
        "meter/minute [m/min]": 0.0166666667,
        "centimeter/minute [cm/min]": 0.0001666667,
        "centimeter/hour [cm/h]": 2.7777777777778E-6,
        "millimeter/minute [mm/min]": 1.66667E-5,
        "centimeter/second [cm/s]": 0.01,
        "millimeter/hour [mm/h]": 2.7777777777778E-7,
        "foot/hour [ft/h]": 8.46667E-5,
        "millimeter/second [mm/s]": 0.001,
        "foot/minute [ft/min]": 0.00508,
        "foot/second [ft/s]": 0.3048,
        "yard/hour [yd/h]": 0.000254,
        "yard/minute [yd/min]": 0.01524,
        "yard/second [yd/s]": 0.9144,
        "mile/minute [mi/min]": 26.8224,
        "mile/second [mi/s]": 1609.344,
        "Cosmic velocity - first": 7899.9999999999,
        "knot [kt, kn]": 0.5144444444,
        "Cosmic velocity - second": 11200,
        "knot (UK) [kt (UK)]": 0.5147733333,
        "Cosmic velocity - third": 16670,
        "Earth's velocity": 29765,
        "Velocity of light in vacuum": 299792458,
        "Mach (20°C, 1 atm)": 343.6,
        "Velocity of sound in pure water": 1482.6999999998,
        "Mach (SI standard)": 295.0464000003,
        "Velocity of sound in sea water (20°C, 10 meter deep)": 1521.6,
    },

    "weight_all": {
        "kilogram [kg]": 1,
        "gram [g]": 0.001,
        "milligram [mg]": 1.0E-6,
        "ton (metric) [t]": 1000,
        "pound [lbs]": 0.45359237,
        "ounce [oz]": 0.0283495231,
        "carat [car, ct]": 0.0002,
        "ton (short) [ton (US)]": 907.18474,
        "ton (long) [ton (UK)]": 1016.0469088,
        "Atomic mass unit [u]": 1.6605402E-27,
        "exagram [Eg]": 1.0E+15,
        "petagram [Pg]": 1000000000000,
        "teragram [Tg]": 1000000000,
        "gigagram [Gg]": 1000000,
        "megagram [Mg]": 1000,
        "hectogram [hg]": 0.1,
        "dekagram [dag]": 0.01,
        "decigram [dg]": 0.0001,
        "centigram [cg]": 1.0E-5,
        "microgram [µg]": 1.0E-9,
        "nanogram [ng]": 1.0E-12,
        "picogram [pg]": 1.0E-15,
        "femtogram [fg]": 1.0E-18,
        "attogram [ag]": 1.0E-21,
        "dalton": 1.6605300000013E-27,
        "kilogram-force square second/meter": 9.80665,
        "kilopound [kip]": 453.59237,
        "kip": 453.59237,
        "slug": 14.5939029372,
        "pound-force square second/foot": 14.5939029372,
        "pound (troy or apothecary)": 0.3732417216,
        "poundal [pdl]": 0.0140867196,
        "ton (assay) (US) [AT (US)]": 0.02916667,
        "ton (assay) (UK) [AT (UK)]": 0.0326666667,
        "kiloton (metric) [kt]": 1000000,
        "quintal (metric) [cwt]": 100,
        "hundredweight (US)": 45.359237,
        "hundredweight (UK)": 50.80234544,
        "quarter (US) [qr (US)]": 11.33980925,
        "quarter (UK) [qr (UK)]": 12.70058636,
        "stone (US)": 5.669904625,
        "stone (UK)": 6.35029318,
        "tonne [t]": 1000,
        "pennyweight [pwt]": 0.0015551738,
        "scruple (apothecary) [s.ap]": 0.0012959782,
        "grain [gr]": 6.47989E-5,
        "gamma": 1.0E-9,
        "talent (Biblical Hebrew)": 34.2,
        "mina (Biblical Hebrew)": 0.57,
        "shekel (Biblical Hebrew)": 0.0114,
        "bekan (Biblical Hebrew)": 0.0057,
        "gerah (Biblical Hebrew)": 0.00057,
        "talent (Biblical Greek)": 20.4,
        "mina (Biblical Greek)": 0.34,
        "tetradrachma (Biblical Greek)": 0.0136,
        "didrachma (Biblical Greek)": 0.0068,
        "drachma (Biblical Greek)": 0.0034,
        "denarius (Biblical Roman)": 0.00385,
        "assarion (Biblical Roman)": 0.000240625,
        "quadrans (Biblical Roman)": 6.01563E-5,
        "lepton (Biblical Roman)": 3.00781E-5,
        "Planck mass": 2.17671E-8,
        "Electron mass (rest)": 9.1093897E-31,
        "Muon mass": 1.8835327E-28,
        "Proton mass": 1.6726231E-27,
        "Neutron mass": 1.6749286E-27,
        "Deuteron mass": 3.343586E-27,
        "Earth's mass": 5.9760000000002E+24,
        "Sun's mass": 2.0E+30,
    },
}

TemperatureConverter = {
    ("Celsius", "Celsius"): lambda x: x,
    ("Celsius", "Kelvin"): lambda x: x + 273.15,
    ("Celsius", "Fahrenheit"): lambda x: (x * 9 / 5) + 32,

    ("Kelvin", "Celsius"): lambda x: x - 273.15,
    ("Kelvin", "Kelvin"): lambda x: x,
    ("Kelvin", "Fahrenheit"): lambda x: round((x - 273.15) * 9 / 5 + 32, 2),

    ("Fahrenheit", "Celsius"): lambda x: round((x - 32) * 5 / 9, 2),
    ("Fahrenheit", "Kelvin"): lambda x: round((x - 32) * 5 / 9 + 273.15, 2),
    ("Fahrenheit", "Fahrenheit"): lambda x: x,
}

# x = json.dumps(dictionary, indent = 4)
# print(x)
# with open("dictionary.json", "w") as f:
#     f.write(x)

# "energy": {
#     "base64": 'joule',
#     'kilojoule [kJ]"' : 1000,
#     'kilowatt-hour [kW*h]"' : 3600000,
#     'watt-hour [W*h]"' : 3600,
#     'calorie (nutritional)' : 4186.8,
#     'horsepower (metric) hour' : 2647795.5,
#     'Btu (IT) [Btu (IT), Btu]"' : 1055.05585262,
#     'Btu (th) [Btu (th)]"' : 1054.3499999744,
#     'gigajoule [GJ]"' : 1000000000,
#     'megajoule [MJ]"' : 1000000,
#     'millijoule [mJ]"' : 0.001,
#     'microjoule [µJ]"' : 1.0E-6,
#     'nanojoule [nJ]"' : 1.0E-9,
#     'attojoule [aJ]"' : 1.0E-18,
#     'megaelectron-volt [MeV]"' : 1.6021766339999E-13,
#     'kiloelectron-volt [keV]"' : 1.6021766339999E-16,
#     'electron-volt [eV]"' : 1.6021766339999E-19,
#     'erg' : 1.0E-7,
#     'gigawatt-hour [GW*h]"' : 3600000000000,
#     'megawatt-hour [MW*h]"' : 3600000000,
#     'kilowatt-second [kW*s]"' : 1000,
#     'watt-second [W*s]"' : 1,
#     'newton meter [N*m]"' : 1,
#     'horsepower hour [hp*h]"' : 2684519.5368856,
#     'kilocalorie (IT) [kcal (IT)]"' : 4186.8,
#     'kilocalorie (th) [kcal (th)]"' : 4184,
#     'calorie (IT) [cal (IT), cal]"' : 4.1868,
#     'calorie (th) [cal (th)]"' : 4.184,
#     'mega Btu (IT) [MBtu (IT)]"' : 1055055852.62,
#     'ton-hour (refrigeration)' : 12660670.23144,
#     'fuel oil equivalent @kiloliter' : 40197627984.822,
#     'fuel oil equivalent @barrel (US)' : 6383087908.3509,
#     'gigaton [Gton]"' : 4.184E+18,
#     'megaton [Mton]"' : 4.184E+15,
#     'kiloton [kton]"' : 4184000000000,
#     'ton (explosives)' : 4184000000,
#     'dyne centimeter [dyn*cm]"' : 1.0E-7,
#     'gram-force meter [gf*m]"' : 0.00980665,
#     'gram-force centimeter' : 9.80665E-5,
#     'kilogram-force centimeter' : 0.0980665,
#     'kilogram-force meter' : 9.8066499997,
#     'kilopond meter [kp*m]"' : 9.8066499997,
#     "pound-force foot [lbf*ft]"" : 1.3558179483,
#     "pound-force inch [lbf*in]"" : 0.112984829,
#     "ounce-force inch [ozf*in]"" : 0.0070615518,
#     "foot-pound [ft*lbf]"" : 1.3558179483,
#     "inch-pound [in*lbf]"" : 0.112984829,
#     "inch-ounce [in*ozf]"" : 0.0070615518,
#     "poundal foot [pdl*ft]"" : 0.04214011,
#     "therm" : 105505600,
#     "therm (EC)" : 105505600,
#     "therm (US)" : 105480400,
#     "Hartree energy" : 4.3597482E-18,
#     "Rydberg constant" : 2.1798741E-18,
# }
# "length": {
#         'kilometer': 1000,
#         'decimeter': 0.1,
#         'centimeter': 0.01,
#         'millimeter': 0.001,
#         'micrometer': 1.0E-6,
#         'nanometer': 1.0E-9,
#         'mile': 1609.344,
#         'yard': 0.9144,
#         'foot': 0.3048,
#         'inch': 0.0254,
#         'light year [ly]"': 9.46073047258E+15,
#         'exameter [Em]"': 1.0E+18,
#         'petameter [Pm]"': 1.0E+15,
#         'terameter [Tm]"': 1000000000000,
#         'gigameter [Gm]"': 1000000000,
#         'megameter [Mm]"': 1000000,
#         'hectometer [hm]"': 100,
#         'dekameter [dam]"': 10,
#         'micron [µ]"': 1.0E-6,
#         'picometer [pm]"': 1.0E-12,
#         'femtometer [fm]"': 1.0E-15,
#         'attometer [am]"': 1.0E-18,
#         'megaparsec [Mpc]"': 3.08567758128E+22,
#         'kiloparsec [kpc]"': 3.08567758128E+19,
#         'parsec [pc]"': 3.08567758128E+16,
#         'astronomical unit [AU, UA]"': 149597870691,
#         'league [lea]"': 4828.032,
#         'nautical league (UK)': 5559.552,
#         'nautical league (int.)': 5556,
#         'league (statute) [st.league]"': 4828.0416560833,
#         'nautical mile (UK) [NM (UK)]"': 1853.184,
#         'nautical mile (international)': 1852,
#         'mile (statute) [mi, mi (US)]"': 1609.3472186944,
#         'mile (US survey) [mi]"': 1609.3472186944,
#         'mile (Roman)': 1479.804,
#         'kiloyard [kyd]"': 914.4,
#         'furlong [fur]"': 201.168,
#         'furlong (US survey) [fur]"': 201.1684023368,
#         'chain [ch]"': 20.1168,
#         'chain (US survey) [ch]"': 20.1168402337,
#         'rope': 6.096,
#         'rod [rd]"': 5.0292,
#         'rod (US survey) [rd]"': 5.0292100584,
#         'perch': 5.0292,
#         'pole': 5.0292,
#         'fathom [fath]"': 1.8288,
#         'fathom (US survey) [fath]"': 1.8288036576,
#         'ell': 1.143,
#         'foot (US survey) [ft]"': 0.3048006096,
#         'link [li]"': 0.201168,
#         'link (US survey) [li]"': 0.2011684023,
#         'cubit (UK)': 0.4572,
#         'hand': 0.1016,
#         'span (cloth)': 0.2286,
#         'finger (cloth)': 0.1143,
#         'nail (cloth)': 0.05715,
#         'inch (US survey) [in]"': 0.0254000508,
#         'barleycorn': 0.0084666667,
#         'mil [mil, thou]"': 2.54E-5,
#         'microinch': 2.54E-8,
#         'angstrom [A]"': 1.0E-10,
#         'a.u. of length [a.u., b]"': 5.2917724900001E-11,
#         'X-unit [X]"': 1.00208E-13,
#         'fermi [F, f]"': 1.0E-15,
#         'arpent': 58.5216,
#         'pica': 0.0042333333,
#         'point': 0.0003527778,
#         'twip': 1.76389E-5,
#         'aln': 0.5937777778,
#         'famn': 1.7813333333,
#         'caliber [cl]"': 0.000254,
#         'centiinch [cin]"': 0.000254,
#         'ken': 2.11836,
#         'Russian archin': 0.7112,
#         'Roman actus': 35.47872,
#         'vara de tarea': 2.505456,
#         'vara conuquera': 2.505456,
#         'vara castellana': 0.835152,
#         'cubit (Greek)': 0.462788,
#         'long reed': 3.2004,
#         'reed': 2.7432,
#         'long cubit': 0.5334,
#         'handbreadth': 0.0762,
#         'fingerbreadth': 0.01905,
#         'Planck length': 1.61605E-35,
#         'Electron radius (classical)': 2.81794092E-15,
#         "Earth's equatorial radius": 6378160,
#         "Earth's polar radius": 6356776.9999999,
#         "Earth's distance from sun": 149600000000,
#         "Sun's radius": 696000000,
#     }
