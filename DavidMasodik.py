#pizzaválasztó
def pizza():
    nev = input("Pizza neve: ")
    meret = int(input("Pizza merete: "))
    ar = int(input("Pizza ara: "))
    egysegar = ar / ((meret / 2)**2 * 3.1416)
    return nev, egysegar

arlista = {}

folytatjuk = True
while folytatjuk:
    uj_nev, uj_ar = pizza()
    arlista.update({uj_nev:uj_ar})
    if input("Folytatjuk?") != "igen":
        folytatjuk = False

print(arlista)

"""legkisebb_egysegar = min(arlista)
sorszam = arlista.index(legkisebb_egysegar) + 1
print("Szerintem a(z)", sorszam, ". a legjobb.")"""
