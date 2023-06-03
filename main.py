import math

# Zaokrąglenie wyników do 2 miejsc po przecinku

def stozek(r, l, h):
    pole= round(math.pi*r**2,2) + math.pi*r*l
    objetosc= round(1/3*math.pi*r**2*h,2)
    return(pole, objetosc)

# testy

assert (stozek(10, 10, 10)) == (628.3192653589794, 1047.2)
assert (stozek(5, 5, 5)) == (157.07981633974484, 130.9)
assert (stozek(2, 2, 2)) == (25.136370614359173, 8.38)
