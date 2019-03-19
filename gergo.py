def pizza():
    nev=input("Pizza neve:")
    ar1=int(input("Pizza Ára?"))
    meret1=int(input("Mérete?"))
    egysegar= ar1 / ((meret1/2) **2*3.1416)
    return nev, egysegar


arlista={}
while True:
    uj_nev, uj_ar = pizza()
    arlista[uj_nev]=uj_ar
    if input("folytatjuk i/n:") == "n":
        break
    else:
        continue

print(arlista)
'''legolcsobb=min(arlista)
index = arlista.index(legolcsobb)+1
print("a(z)", index, "-dik pizza a legolcsobb")'''
