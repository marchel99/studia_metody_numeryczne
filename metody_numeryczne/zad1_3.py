import numpy as np
import scipy.integrate

# Definicja funkcji
def f1(x, a=-2, b=-2, c=-2):
    return c*x**3 + b*x + a

def f2(x, d=-1, e=-2):
    return d * np.cos(x/e)

def f3(x, f=3):
    return np.log(x/f)

# Przedziały całkowania
intervals = [(-2, 2), (0, np.pi/2), (1, 3)]

# Węzły i wagi dla kwadratur Gaussa-Legendre’a
nodes_weights = [
    ([0.0], [2.0]),
    ([-0.5773502692, 0.5773502692], [1.0, 1.0]),
    ([-0.7745966692, 0.0, 0.7745966692], [0.5555555556, 0.8888888889, 0.5555555556]),
    # Dodaj więcej punktów według potrzeb
]

# Obliczanie całek za pomocą kwadratur Gaussa-Legendre’a
for i, (nodes, weights) in enumerate(nodes_weights, start=1):
    print(f"For n={i}:")
    for j, (f, (a, b)) in enumerate(zip([f1, f2, f3], intervals), start=1):
        # Przeprowadzenie mapowania przedziałów całkowania na przedział [-1, 1]
        nodes_transformed = [(b - a) / 2 * x + (a + b) / 2 for x in nodes]
        weights_transformed = [(b - a) / 2 * w for w in weights]
        # Obliczenie całki
        result = sum(w * f(x) for x, w in zip(nodes_transformed, weights_transformed))
        print(f"  Result for function {j}: {result}")
