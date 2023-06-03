import math

# Zaokrąglenie objętości kuli do 2 miejsc po przecinku

def obj_kuli(r):
    objetosc=round(4/3*math.pi*r**3,2)
    return(objetosc)

# test

assert (obj_kuli(10)) == 4188.79
assert (obj_kuli(11)) == 5575.28
assert (obj_kuli(12)) == 7238.23
assert (obj_kuli(13)) == 9202.77
assert (obj_kuli(14)) == 11494.04
