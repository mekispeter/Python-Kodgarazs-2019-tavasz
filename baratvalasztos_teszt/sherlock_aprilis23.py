"""
    Kódgarázs
    Python Big Data április 23

    A két héttel korábbi kód folytatása. A tesztadatokat kinyerjük a fájlokból
    és kiértékeljük minden kategória minden opciója szerint. Az április 9-i
    változatban részben megcsináltuk egyetlen kategória két opciójára. Ezúttal
    a sok kinyert adatból a szélsőségeket keressük: azokat az opciókat, amikre
    25% alatt vagy 75% felett született pozitív döntés.

    Az adatok feldolgozása annyiban bigdatás, hogy egyszerre csak egy fájlt
    nyitunk meg és értékelünk ki, és csak az eredményt tároljuk el.
"""

# A tesztfájlok sorai így vannak elkódolva:
# sor[0]: + / - (balra / jobbra)
# sor[2]: 0-9 (nev)
# sor[4]: 0-9 (fej)
# sor[6]: 0-9 (kedvenc)
# sor[8]: 0-9 (hobbi)
# sor[10]: 0-9 (peldakep)
# Az 1. tesztfájl első sora például: "-n7f2k4h4p3"
# -> döntés:    - => nem jelöljük barátnak
# -> név:       7 => Emma
# -> fej:       2 => szőke copfos
# -> kedvenc:   4 => puli
# -> hobbi:     4 => videojáték
# -> példakép:  3 => Leia Organa

kategoriak = ["név", "fej", "kedvenc", "hobbi", "példakép"]
osszes_opcio = [
    ["Lilla", "Anna", "Virág", "Évi", "Dóri", "Kati", "Luca", "Emma", "Maja", "Nóra"],
    ["barna copfos szemüveges", "barna félhosszú", "szőke copfos",
        "vörös hosszú", "fekete göndör", "barna copfos",
        "barna félhosszú szemüveges", "szőke copfos szemüveges",
        "vörös hosszú szemüveges", "fekete göndör szemüveges"],
    ["hörcsög", "német juhász", "basset hund", "fekete macska", "puli",
        "papagáj", "ló", "nyúl", "cirmos cica", "teknőc"],
    ["társasjáték", "legó", "bicikli", "fényképezés", "videojáték",
        "búvárkodás", "balett", "zene", "sütés", "pingpong"],
    ["Marvel Kapitány", "Lara Croft", "Daenerys Targaryen", "Leia Organa",
        "Hermione", "Mulan", "Merida", "Selene", "Wonder Woman", "Major"]
    ]
kodok = "nfkhp"

osszeg = 0
for i in range(1,11):
    with open("tesztadatok_" + str(i) + ".txt", encoding = "utf8") as file:
        adatok = file.read()
    # Először általában nézzük meg a tesztalany barátkozási hajlandóságát:
    baratok_szama = adatok.count("+")
    sorok = adatok.split()
    barat_szazalek = round(baratok_szama / (len(sorok)) * 100)
    osszeg += barat_szazalek
    print("\ntesztalany", i)
    print("------------")
    print("barátok:", barat_szazalek, "%")
    # Most pedig sorra vesszük a kategóriákat és bennük az opciókat, és
    # szélsőségekre vadászunk (25% alatti és 75% feletti válaszok):
    print("Szélsőségek:")
    szelsosegek = 0
    for kat in range(5): #kategória-számláló
        opciok = osszes_opcio[kat]
        for opc in range(10): # név-számláló
            elofordulasok = [sor for sor in sorok if kodok[kat]+str(opc) in sor]
            baratok = [sor for sor in elofordulasok if sor[0] == "+"]
            szazalek = round(len(baratok) / (len(elofordulasok)) * 100)
            if szazalek < 25 or 75 < szazalek:
                print("  -", opciok[opc] + ":", szazalek)
                szelsosegek += 1
    print("  Összesen:", szelsosegek)
# Végül kiírjuk a barátnak jeköltek átlagos százalékát:
atlag = round(osszeg / 10)
print("\nBarátok átlagosan:", atlag, "%")
