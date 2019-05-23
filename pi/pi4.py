"""
    Kódgarázs
    Python Big Data április 16

    Pi kiszámolás bigdatásan: második nekifutás.
"""

import random as r

sugar = int(input("Sugár: "))
sugar_negyzet = sugar ** 2
korterulet_mc = sum((r.random()**2 + r.random()**2) < 1 for i in range(sugar_negyzet))
pi_mc = korterulet_mc / sugar_negyzet * 4
print("mc:", pi_mc)
korterulet_pontos = sum(x**2 + y**2 < sugar_negyzet for x in range(sugar) for y in range(sugar))
pi_pontos = korterulet_pontos / sugar_negyzet * 4
print("pontos:", pi_pontos)
