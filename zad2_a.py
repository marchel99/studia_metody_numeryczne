"""
Znaleźć miejsce zerowe podanej funkcji w zadanym przedziale wykorzystując metodę
złotego podziału
a) Dla osób z parzystą cyfrą I2:
f(x)=x^2 – x - 2-I1 w przedziale [-5, 5]
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - x - 2

def golden_section_search(a, b, epsilon):
    ratio = (math.sqrt(5) - 1) / 2  # Stosunek złotego podziału

    while abs(b - a) > epsilon:
        c = b - ratio * (b - a)
        d = a + ratio * (b - a)
        fc = f(c)
        fd = f(d)

        if fc < fd:
            b = d
        else:
            a = c

    return (a + b) / 2

a = -5
b = 5

epsilon = 0.0001

zero_point = golden_section_search(a, b, epsilon)
zero_point_value = f(zero_point)

x = np.linspace(-6, 6, 100)
y = f(x)

plt.plot(x, y, label='f(x) = x^2 - x - 2')
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=zero_point, color='red', linestyle='--', label='Miejsce zerowe')
plt.scatter(zero_point, 0, color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji')
plt.legend()

plt.text(-7, 52, 'Nr indeksu: 249842, I2=4', fontsize=12)
plt.text(-7, 49, 'Przedział: [-5, 5]', fontsize=12)
plt.text(-7, 46, 'Miejsce zerowe: x = {:.4f}'.format(zero_point), fontsize=12)

plt.show()

print("Miejsce zerowe:", zero_point)
print("Wartość funkcji w miejscu zerowym:", zero_point_value)
