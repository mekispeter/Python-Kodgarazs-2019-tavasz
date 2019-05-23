"""
    Kódgarázs
    Python Big Data április 9

    Felvezető projekt: kiszámoljuk a pi-t. Ezt a képletet követjük:
    pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - ...

    Ez egy nagyon lassú algoritmus, ezért növekvő lépésközben íratjuk ki a kapott értéket.
"""

from math import pi

maximum = int(input("Meddig megyünk? "))
kiiras_hatar = 1

print("pi:", round(pi, 7))
my_pi = 0
for n in range(maximum + 1):
    if n % 2 == 0: # páros n-re plusz, páratlanra mínusz
        my_pi += 4/(2*n+1)
    else:
        my_pi -= 4/(2*n+1)
    if n == kiiras_hatar:
        print(n, "lépésben: ", round(my_pi,7))
        kiiras_hatar *= 2
print(maximum, "lépésnél állunk meg: ", round(my_pi,7))
