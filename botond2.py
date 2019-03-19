#pizzavalasztos
def pizza():
    nev=input("mi a pizza neve")
    meret=int(input("Mekkora a pizza átmérője?"))
    ar=int(input("pizza ara"))
    egysegar = ar/((meret/2)**2)*3.1416
    return egysegar, nev
arlista={}
megyunk=True
while megyunk:
    ujar, ujnev=pizza()
    """
    arlista.append[ujar]
    arlista = arlista + [ujar]
    arlista+=[ujar]
    """
    arlista[ujnev]=ujar
    if not input("folytatjuk") == "igen":
        megyunk=False
print(arlista)
"""
min_ar =min(arlista)
sorszam=1+arlista.index(min_ar)
print("Teso szerintem a(z)", sorszam, "a nyerő!")
"""
