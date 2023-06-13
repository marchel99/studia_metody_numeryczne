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
    ([-0.8611363116, 0.8611363116, -0.3399810436, 0.3399810436], [0.3478548451, 0.3478548451, 0.6521451549, 0.6521451549]),
    ([-0.9061798459, 0.9061798459, -0.5384693101, 0.5384693101, 0.0], [0.2369268851, 0.2369268851, 0.4786286705, 0.4786286705, 0.5688888889]),
    ([-0.9324695142, 0.9324695142, -0.6612093865, 0.6612093865, -0.2386191861, 0.2386191861], [0.1713244924, 0.1713244924, 0.3607615730, 0.3607615730, 0.4679139346, 0.4679139346]),
    ([-0.9491079123, 0.9491079123, -0.7415311856, 0.7415311856, -0.4058451514, 0.4058451514, 0.0], [0.1294849662, 0.1294849662, 0.2797053915, 0.2797053915, 0.3818300505, 0.3818300505, 0.4179591837]),
    ([-0.9602898565, 0.9602898565, -0.7966664774, 0.7966664774, -0.5255324099, 0.5255324099, -0.1834336425, 0.1834336425], [0.1012285363, 0.1012285363, 0.2223810345, 0.2223810345, 0.3137066459, 0.3137066459, 0.3626837834, 0.3626837834])
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
