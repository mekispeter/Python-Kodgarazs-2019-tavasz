"""
    Kódgarázs
    Python Big Data április 9

    Levezető projekt: másodszor is kiszámoljuk a pi-t. A Ramanujan-Chudnovsky
    algoritmust követjük:

    Ez egy elképesztően gyors algoritmus, ezért minden lépésben kiíratjuk a
    kapott értéket.
"""

from math import pi
from math import factorial
from decimal import Decimal, getcontext

D = Decimal
getcontext().prec = 120
print("math.pi:", D(pi))
osszeg = D(0)
for n in range(10):
    szamlalo = D(factorial(6*n) * (13591409 + 545140134 * n))
    nevezo = D(factorial(n) ** 3 * factorial(3*n) * (640320**3)**(n+0.5))
    tort = szamlalo / nevezo
    if n % 2 == 0:
        osszeg += tort
    else:
        osszeg -= tort
    my_pi = 1 / (12 * osszeg)
    print(n+1, "lépés:", D(my_pi))
