"""
    Python Big Data május 7

    Még egyszer nekimentünk a tesztadatoknak. Új algoritmust írtunk, ami
    a korábbi kihívást megfordítva a felhasználó alapján tippeli meg, mik
    lesznek a bevitt válaszok.
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

szazalekok = {}
with open("tesztadatok_5.txt", encoding = "utf8") as file:
    adatok = file.read()
    sorok = adatok.split()
for kat in range(5):
    for opc in range(10):
        kombo = kodok[kat] + str(opc)
        poz = len([sor for sor in sorok if "+" in sor and kombo in sor])
        neg = len([sor for sor in sorok if "-" in sor and kombo in sor])
        szazalek = poz / (poz + neg) * 100
        szazalekok.update({kombo : szazalek})
        #szazalekok[kombo] = szazalek
print(szazalekok)

talalatok = 0
with open("tesztadatok_11.txt", encoding = "utf8") as file:
    tesztadatok = file.read()
    tesztsorok = tesztadatok.split()
for sor in tesztsorok:
    osszeg = 0
    for i in range(1,11,2):
        kod = sor[i:i+2]
        osszeg += szazalekok[kod]
    atlag = osszeg / 5
    if (50 <= atlag and sor[0] == "+") or (atlag < 50 and sor[0] == "-"):
        print("Hurrá!")
        talalatok += 1
    else:
        print("A manóba!")

if len(tesztsorok) * 0.6 < talalatok:
    print("\nSzuperhurrá!")
else:
    print("ˇ#_#ˇ")

print(talalatok / len(tesztsorok) * 100)
