"""
    Kódgarázs
    Python Big Data április 16

    Adatok kinyerése szövegből, függvényekkel tagolva
"""
import random as r

file = open("lotr.txt", "r")
szoveg = file.read().split("\n")
file.close()
print(r.choice(szoveg))

abece = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#kivesszük a szövegből a nem-betű, nem-szóköz karaktereket
def csakabetuk(szoveg):
    uj_szoveg = []
    for sor in szoveg:
        uj_sor = ""
        for karakter in sor:
            if karakter in abece or karakter == " ":
                uj_sor += karakter
        uj_szoveg.append(uj_sor)
    return uj_szoveg

def szavakra_bont(szoveg):
    szavak = []
    for sor in szoveg:
        szavak += sor.split(" ")
    szavak_nemures = [szo for szo in szavak if szo != ""]
    return szavak_nemures

def palindrom(szo):
    if len(szo) < 2:
        return True
    elif szo[0] != szo[-1]:
        return False
    else:
        return palindrom(szo[1:-1])

def palindrom_szamlalo(szavak):
    szamlalo = 0
    maxpal = ""
    for szo in szavak:
        if 2 < len(szo) and palindrom(szo):
            szamlalo += 1
            if len(maxpal) < len(szo):
                maxpal = szo
    return szamlalo, maxpal

def szogyakorisag(szavak):
    elofordulasok = {}
    for szo in szavak:
        if szo in elofordulasok:
            elofordulasok[szo] += 1
        else:
            elofordulasok.update({szo:1})
    return elofordulasok

# legtobbszor

csupasz_szoveg = csakabetuk(szoveg)
print(r.choice(csupasz_szoveg))

szavak = szavakra_bont(csupasz_szoveg)
print(r.choice(szavak))

szo_elofordulasok = szogyakorisag(szavak)

nevek = ["Gandalf", "Gollum", "Frodo", "Bilbo", "Mordor"]
fajok = ["hobbits", "elves", "dwarves", "ents", "orcs"]

for szo in nevek + fajok:
    if szo in szo_elofordulasok:
        print(szo + ":", szo_elofordulasok[szo])
    else:
        print(szo + ":", 0)

palindrom_szam, leghosszabb_palindrom = palindrom_szamlalo(szavak)
print(palindrom_szam, "palindrom összesen", len(szavak), "szóból")
print("A leghosszabb pedig:", leghosszabb_palindrom)

legtobb = max(szo_elofordulasok.values())
leggyakoribb_szavak = [szo for szo in szo_elofordulasok if szo_elofordulasok[szo] == legtobb]
print("Legtöbb:", legtobb)
print(leggyakoribb_szavak)
