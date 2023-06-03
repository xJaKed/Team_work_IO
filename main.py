import math

def ostroslup(pp, pb, h):
    pole = pp + pb
    objetosc = 1/3 * pp * h
    return pole, objetosc

# testy

assert (ostroslup(20,10,5)) == (30, 33.33333333333333)
assert (ostroslup(50,20,10)) == (70, 166.66666666666663)
assert (ostroslup(25,15,12)) == (40, 99.99999999999999)