"""
    Kódgarázs
    Python Big Data április 2

    Levezető projekt. Egy kis vidámkodás, amivel a
    stringkezelést is gyakoroltuk. 
"""

import time

def mutasd():
    time.sleep(0.05)
    print("\n"*25) # ezzel törlünk képernyőt
    print(szoveg)

szoveg = input("Mi legyen a szöveg?")
szoveg +=  " " * (50 - len(szoveg))
while 1 == 1:
    while szoveg[-1] == " ":
        szoveg = szoveg[-1] + szoveg[:-1]
        mutasd()
    while szoveg[0] == " ":
        szoveg = szoveg[1:] + szoveg[0]
        mutasd()
