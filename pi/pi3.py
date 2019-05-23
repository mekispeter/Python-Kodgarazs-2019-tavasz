"""
    Kódgarázs
    Python Big Data április 16

    Pi kiszámolás bigdatásan. Leejtegetjük a tollat egy négyzet alakú papírra,
    és megnézzük, hányszor esik a beírt körön belülre. (Némi töprengés után
    arra jutottunk, hogy csak a papír jobb felső negyedét nézzük.)

    Ez is egy nagyon lassú algoritmus. Azért érdekes, mert statisztikával
    közelíti a pi-t nagyokos sorozat helyett.
"""

import random

# 0 es 1 kozotti random szamot ad vissza,
# d tizedesjegy pontossaggal.
def randomszam(d):
    nevezo = 10**d
    szamlalo = random.randint(0, nevezo)
    return szamlalo / nevezo

# True, ha belul vagyunk a koron;
# False maskor
def belul_vagyunk(x,y):
    return x*x + y*y < 1

darab = int(input("Hány pont legyen? "))
jegyek = int(input("És hány tizedesjegy pontossággal?" ))

# 1. verzió: két listát is generálunk.
# pontok = [(randomszam(jegyek), randomszam(jegyek)) for i in range(darab)]
# belso_pontok = [(x, y) for (x, y) in pontok if belul_vagyunk(x, y)]

# 2. verzió: csak egy listát generálunk.
# pontok = [belul_vagyunk(randomszam(jegyek), randomszam(jegyek)) for i in range(darab)]
# pi = sum(pontok) / darab * 4

# 3. verzió: nem csinálunk listát, mert úgyis csak a sum érdekel minket belőle.
belso_pontok = sum(belul_vagyunk(randomszam(jegyek), randomszam(jegyek)) for i in range(darab))
pi = belso_pontok / darab * 4

print(pi)
