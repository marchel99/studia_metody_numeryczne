"""
Wyznacz miejsce zerowe, metoda Brenta (złoty podział z interpolacją f.
kwadratową), wielomian 3. stopnia (dla różnych punktów startowych);

f(x)=x2 –x -2-I1 w przedziale [-5,5]
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - x - 2

# Przedział początkowy
a = -5
b = 5

# Generowanie punktów do wykresu funkcji
x = np.linspace(a, b, 100)
y = f(x)

# Wykres funkcji
plt.plot(x, y, label='f(x) = x^2 - x - 2')
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji')
plt.legend()

# Miejsca zerowe
zero_points = [-1, 2]
for zero_point in zero_points:
    zero_point_value = f(zero_point)
    plt.scatter(zero_point, 0, color='red')
    plt.text(zero_point, 2, 'x = {:.4f}'.format(zero_point), fontsize=10, ha='center')

    print("Miejsce zerowe:", zero_point)
    print("Wartość funkcji w miejscu zerowym:", zero_point_value)
    print()

# Wyświetlenie wykresu
plt.show()
