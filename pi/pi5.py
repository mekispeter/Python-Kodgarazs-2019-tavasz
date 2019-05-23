"""
    Kódgarázs
    Python Big Data április 23

    Felvezető projekt: pi kiszámolása matekórásan. Az egységsugarú kör köré
    írt szabályos sokszög kerületét számoljuk ki. (Táblán rajzolgattunk.)

    Valószínűleg csalunk, mert a radiánból fokra váltáshoz kell a pi.
"""
from math import sin
from math import radians
n = int(input("Hányszöggel közelítünk? "))
pi = sin(radians(180/n))*n
print(n, "oldalú sokszöggel közelítve:", pi)
