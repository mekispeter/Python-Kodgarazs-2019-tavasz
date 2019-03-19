#pizzavalszto
import math

def egysegar():
    atmero=int(input("atmero:"))
    ar=int(input("ar:"))
    terulet= atmero/2**2*math.pi
    return ar/terulet

def egysegarnev():
    nev=input("Pizza neve:")
    atmero=int(input("atmero:"))
    ar=int(input("ar:"))
    terulet= atmero/2**2*math.pi
    return nev, ar/terulet

#dictionary ba mentjuk az elemeket
def dictmentes():
    ardict={}
    megyunk=True
    while megyunk:
        nev, uj_ar=egysegarnev()
        ardict[nev]=uj_ar
        if input("Folytatjuk?")!="igen":
            megyunk=False
    smallest=min(ardict.values())
    for t in ardict.items():
        if t[1]==smallest:
            legjobb=t[0]
    print("Szerintem a {} a legjobb." .format(legjobb))

#listaba mentjuk az osszeset
def listaba():
    arlista=[]
    megyunk=True
    while megyunk:
        uj_ar=egysegar()
        arlista.append(uj_ar)
        if input("Folytatjuk?")!="igen":
            megyunk=False
    print("Szerintem a {}-ik a legjobb." .format(arlista.index(min(arlista))+1))


#legjobb ár vizsgálása
def legjobbar():
    db=int(input("hány darab lesz?"))
    legjobb=egysegar()
    szam=[-1]
    for i in range(db-1):
        uj=egysegar()
        if legjobb < uj:
            legjobb=uj
            szam=[i]
        elif legjobb==uj:
            szam.append(i)
    for sz in szam:
        print(sz+2)

#primitív módszer (fgv nélkül)
def elso():
    atmero1=int(input("atmero 1:"))
    ar1=int(input("ar 1:"))
    terulet1= atmero1/2**2*math.pi
    egysegar1= ar1/terulet1

    atmero2=int(input("atmero 2:"))
    ar2=int(input("ar 2:"))
    terulet2= atmero2/2**2*math.pi
    egysegar2= ar2/terulet2

    if egysegar1<egysegar2:
        print("elsot")
    elif egysegar1>egysegar2:
        print("masodikat")
    else:
        print("mindegy")

dictmentes()
