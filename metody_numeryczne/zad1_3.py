import numpy as np
import math
import scipy.integrate
import matplotlib.pyplot as plt

# Definicja funkcji
def f1(x, a=-2, b=-2, c=-2):
    return c*x**3 + b*x + a

def f2(x, d=-1, e=-2):
    return d * math.cos(x/e)

def f3(x, f=3):
    return math.log(x/f)

# Metoda prostokątów
def rectangle_method(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i*h) for i in range(n))

# Metoda trapezów
def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    return h * (0.5*f(a) + 0.5*f(b) + sum(f(a + i*h) for i in range(1, n)))

# Metoda Simpsona
def simpson_method(f, a, b, n):
    h = (b - a) / n
    return h / 3 * (f(a) + f(b) + sum((4 if i % 2 == 1 else 2) * f(a + i*h) for i in range(1, n)))

# Testowanie metod
for n in [10, 100, 1000, 10000]:
    print(f"n = {n}")
    for f, a, b in [(f1, -2, 2), (f2, 0, math.pi/2), (f3, 1, 3)]:
        print(f"Rectangle: {rectangle_method(f, a, b, n)}")
        print(f"Trapezoid: {trapezoid_method(f, a, b, n)}")
        print(f"Simpson: {simpson_method(f, a, b, n)}")

# Metoda Romberga dla funkcji f2
a = 0
b = np.pi/2
result = scipy.integrate.romberg(f2, a, b, show=True)
print(f"Romberg result for f2: {result}")

# Wykresy
x = np.linspace(-2, 2, 1000)
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, f1(x))
plt.title('f1')

plt.subplot(2, 2, 2)
plt.plot(x, f2(x))
plt.title('f2')

x = np.linspace(1, 3, 1000)
plt.subplot(2, 2, 3)
plt.plot(x, f3(x))
plt.title('f3')

plt.tight_layout()
plt.show()