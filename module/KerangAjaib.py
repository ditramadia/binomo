# KERANG AJAIB MODULE

from random import random
import time as time


def LCG():
    a, c, m = 2416, 374441, 1771875
    x = (time.time() * a + c) % 373737
    x = (a * x + c) % m
    return x / m


def KerangAjaib():
    question = input("Apa pertanyaanmu? ")

    randomNumber = LCG()
    if (randomNumber <= 0.1666666):
        print("Ya")
    elif (0.1666666 < randomNumber <= 2*(0.1666666)):
        print("Tidak")
    elif (2*(0.1666666) < randomNumber <= 3*(0.1666666)):
        print("Bisa Jadi")
    elif (3*(0.1666666) < randomNumber <= 4*(0.1666666)):
        print("Mungkin")
    elif (4*(0.1666666) < randomNumber <= 5*(0.1666666)):
        print("Tentunya")
    else:
        print("Tidak Mungkin")
