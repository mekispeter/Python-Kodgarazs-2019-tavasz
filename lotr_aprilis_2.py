"""
    Kódgarázs
    Python Big Data április 2

    Adatok kinyerése szövegből: folytatás
"""

file = open("lotr.txt", encoding = "utf8")
szoveg = file.read()
file.close()
nevek = ["Gandalf", "Frodo", "Pippin",
        "Gollum", "Sauron"]
for nev in nevek:
    print(nev, szoveg.count(nev))
tisztitott_betulista = [betu for betu in szoveg if betu.isalnum() or betu in [" ", "\n"]]
tisztitott_szoveg = "".join(tisztitott_betulista)
szavak = tisztitott_szoveg.split()
#print(szavak)
print("Összesen", len(szavak), "szó van.")
hosszok = [len(szo) for szo in szavak]
print("A leghosszabb szó", max(hosszok), "betűs")
