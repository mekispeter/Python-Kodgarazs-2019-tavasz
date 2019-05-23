"""
    Kódgarázs
    Python Big Data május 21

    Nem sikerült működésbe hozni a matplotlib csomagot, úgyhogy
    a záróprojekt közös megegyezéssel egy játék lett.
"""

import random as r

konyv = input("lotr vagy hpss? ")

with open(konyv + ".txt", encoding = "utf-8") as file:
# with open("lotr.txt", encoding = "utf-8") as file:
    szoveg = file.read()
    feladvanyok = []
    uj_mondat = ""
    for karakter in szoveg:
        if karakter != "\n":
            uj_mondat += karakter.upper()
        else:
            uj_mondat += " "
        if karakter in ".!?":
            feladvanyok.append(uj_mondat)
            uj_mondat = ""

# Az első változatban még a saját neveink voltak a feladványok:
#nevek = ["Uni-kornis Anna", "007211_#Botond*David", "Alma Dávid", "Kisss Gergő", "Mészáros AnnaVeronikaPanni", "Mikes Péter"]
#feladvanyok = [nev.upper() for nev in nevek]

feladvany = r.choice(feladvanyok)
maszk = ""
for karakter in feladvany:
    if karakter.isalpha():
        maszk += "_"
    else:
        maszk += karakter

hiba = 0
voltmar = ""
while hiba != 7 and maszk != feladvany:
    print("\n", maszk)
    print(" Hiba: ", hiba)
    tipp = input(" Tipp: ").upper()
    if not tipp in voltmar and len(tipp) == 1:
        if tipp in feladvany:
            print(" Ügyivagy!")
            uj_maszk = ""
            for i in range(len(feladvany)):
                if tipp == feladvany[i]:
                    uj_maszk += tipp
                else:
                    uj_maszk += maszk[i]
            maszk = uj_maszk
        else:
            print(" Hoppácsek!")
            hiba += 1
        if voltmar == "":
            voltmar += tipp
        else:
            voltmar += ", " + tipp
    print(" Volt már:", voltmar)

if hiba == 7:
    print("Lúúúúzer!!!")
else:
    print("Nyertél!!! Megdícsérlek!")
print("Megfejtés:", feladvany)
