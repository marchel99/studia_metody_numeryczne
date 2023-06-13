import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definicja funkcji
a, b, c, d, e, f, g = -2, -2, -2, -1, -2, 3, 3
functions = [(lambda x: c*x**3 + b*x + a, -2, 2), 
             (lambda x: d*np.cos(x/e), 0, np.pi/2),
             (lambda x: np.log(x/f), 1, g)]

# Metoda prostokątów
def rectangle_rule(func, a, b, n):
    h = (b - a) / n
    return sum([func(a + i*h) for i in range(n)]) * h

# Metoda trapezów
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    return (0.5 * (func(a) + func(b)) + sum([func(a + i*h) for i in range(1, n)])) * h

# Metoda Simpsona
def simpson_rule(func, a, b, n):
    h = (b - a) / (2*n)
    return (1/3) * h * (func(a) + func(b) + 4 * sum([func(a + i*h) for i in range(1, 2*n, 2)]) + 2 * sum([func(a + i*h) for i in range(2, 2*n, 2)]))

# Wykres
x = np.arange(1, 100)
for i, (func, a, b) in enumerate(functions):
    integral, _ = quad(func, a, b)
    y1 = [abs(rectangle_rule(func, a, b, n) - integral) for n in x]
    y2 = [abs(trapezoidal_rule(func, a, b, n) - integral) for n in x]
    y3 = [abs(simpson_rule(func, a, b, n) - integral) for n in x]

    plt.figure()
    plt.plot(x, y1, label="Rectangle rule")
    plt.plot(x, y2, label="Trapezoidal rule")
    plt.plot(x, y3, label="Simpson's rule")
    plt.legend()
    plt.xlabel("Number of subintervals")
    plt.ylabel("Error")
    plt.title(f"Error comparison for function {i+1}")
    plt.yscale("log")
    plt.grid()

plt.show()
