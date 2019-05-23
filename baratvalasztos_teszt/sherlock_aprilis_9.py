"""
    Kódgarázs
    Python Big Data április 9

    A tesztadatokat kinyerjük a fájlokból és kiértékeljük néhány választott opció szerint.

    Az adatok feldolgozása annyiban bigdatás, hogy egyszerre csak egy fájlt
    nyitunk meg és értékelünk ki, és csak az eredményt tároljuk el.

"""


# sor[0]: + / - (balra / jobbra)
# sor[2]: 0-9 (nev)
# sor[4]: 0-9 (fej)
# sor[6]: 0-9 (kedvenc)
# sor[8]: 0-9 (hobbi)
# sor[10]: 0-9 (peldakep)

kategoriak = ["döntés", "név", "fej", "kedvenc", "hobbi", "példakép"]

opciok = [
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

# Itt kezdtük el a kódot írni. A fenti listák készen voltak.

osszeg = 0
for i in range(1,11):
    with open("tesztadatok_" + str(i) + ".txt", encoding = "utf8") as file:
        adatok = file.read()
    plusz = adatok.count("+")
    minusz = adatok.count("-")
    szazalek = round(plusz / (plusz + minusz) * 100)
    osszeg += szazalek
    print("\ntesztalany", i)
    print("barátok:", szazalek)
    sorok = adatok.split()
    feketecicasok = [sor for sor in sorok if "k3" in sor]
    feketecicas_baratok = [feketecicas for feketecicas in feketecicasok if feketecicas[0] == "+"]
    print("fekete cica:", round(len(feketecicas_baratok) / (len(feketecicasok)) * 100))
    cirmoscicasok = [sor for sor in sorok if "k8" in sor]
    cirmoscicas_baratok = [cirmoscicas for cirmoscicas in cirmoscicasok if cirmoscicas[0] == "+"]
    print("cirmos cica:", round(len(cirmoscicas_baratok) / (len(cirmoscicasok)) * 100))
atlag = round(osszeg / 10)
print("\nÁtlag:", atlag)
