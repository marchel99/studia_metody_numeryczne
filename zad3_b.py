import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

def f(x):
    return np.sin(x**2) * np.cos(x) / (1 - x**2)

# Przedział początkowy
a = -5
b = 5

# Kryterium stopu
epsilon = 0.001

# Znalezienie miejsc zerowych
zero_points = []
x = a

while x <= b:
    try:
        zero_point = brentq(f, x, b, xtol=epsilon)
        zero_points.append(zero_point)
        x = zero_point + epsilon
    except ValueError:
        x += epsilon

# Wykres funkcji
x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = sin(x^2) * cos(x) / (1 - x^2)')
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji')
plt.legend()

# Oznaczenie miejsc zerowych
if len(zero_points) > 0:
    for i, zero_point in enumerate(zero_points):
        zero_point_value = f(zero_point)
        plt.scatter(zero_point, 0, color='red')
        if i == 1:
            plt.text(zero_point, 0.85, 'x = {:.4f}'.format(zero_point), fontsize=8, ha='center')
        else:
            plt.text(zero_point, 0.5, 'x = {:.4f}'.format(zero_point), fontsize=8, ha='center')

        print("Miejsce zerowe:", zero_point)
        print("Wartość funkcji w miejscu zerowym:", zero_point_value)
        print()
else:
    print("Brak miejsc zerowych w danym przedziale.")

# Dodatkowe informacje
plt.text(-7, 10, 'Nr indeksu: 249842, I2=4', fontsize=12)

equation_text = r'$f(x) = \frac{{\sin(x^2) \cos(x)}}{{1 - x^2}}$'
plt.text(-7, 9, equation_text, fontsize=12, )

plt.text(-7, 8, 'Przedział: [-5, 5]', fontsize=12)
if len(zero_points) > 0:
    plt.text(-7, 7, 'Miejsce zerowe: x = {:.4f}'.format(zero_points[0]), fontsize=12)

# Wyświetlenie wykresu
plt.show()
