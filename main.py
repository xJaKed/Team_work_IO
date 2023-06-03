import math

# Zaokrąglenie wyników do 2 miejsc po przecinku

def stozek(r, l, h):
    pole= round(math.pi*r**2,2) + math.pi*r*l
    objetosc= round(1/3*math.pi*r**2*h,2)
    return(pole, objetosc)

