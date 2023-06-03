import math

def szescian(krawedz_a):
    objetosc = krawedz_a ** (3)
    pole = 6 * krawedz_a**(2)
    return objetosc, pole

# Zaokrąglenie objętości kuli do 2 miejsc po przecinku

def obj_kuli(r):
    objetosc=round(4/3*math.pi*r**3,2)
    return(objetosc)

# testy

assert (obj_kuli(10)) == 4188.79
assert (obj_kuli(11)) == 5575.28
assert (obj_kuli(12)) == 7238.23
assert (obj_kuli(13)) == 9202.77
assert (obj_kuli(14)) == 11494.04

assert szescian(5) == (125, 150)
assert szescian(1) == (1, 6)
assert szescian(10) == (1000, 600)

def stozek(r, l, h):
    pole= round(math.pi*r**2,2) + math.pi*r*l
    objetosc= round(1/3*math.pi*r**2*h,2)
    return(pole, objetosc)

