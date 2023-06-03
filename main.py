def szescian(krawedz_a):
    objetosc = krawedz_a ** (3)
    pole = 6 * krawedz_a**(2)
    return objetosc, pole

# testy

assert szescian(5) == (125, 150)
assert szescian(1) == (1, 6)
assert szescian(10) == (1000, 600)