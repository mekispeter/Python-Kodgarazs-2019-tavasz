"""
    Kódgarázs
    Python Big Data március 26

    Adatok kinyerése szövegből
"""

file = open("lotr.txt", encoding = "utf-8")
szoveg = file.read()
print(szoveg[99].split(" "))

abece = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

szavak = []
szo = ""
for karakter in szoveg:
    if karakter in abece:
        szo += karakter
    elif karakter in [" ", "\n", "-"]:
        if szo != "":
            szavak.append(szo)
            szo = ""
if szo != "":
    szavak += szo

print(szavak)

kulonlegessegek = []
for szo in szavak:
    if szo != "Gandalf" and szo != "Gandalfs" and "Gandalf" in szo:
        kulonlegessegek.append(szo)

print(kulonlegessegek)
