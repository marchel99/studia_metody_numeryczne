import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return -2*x**3 - 2*x - 2

def rectangle_method(f, range, n):
    h = (range[1] - range[0]) / n
    result = 0
    for i in range(n+1):
        result += f(range[0] + h * (i + 0.5))
    result *= h
    return result

# Definicja przedziału
range = [-2, 2]
n = 100

# Obliczenie wartości przybliżonej
x_vals = np.linspace(range[0], range[1], n+1)
y_vals = f1(x_vals)
approx_vals = np.ones_like(x_vals) * rectangle_method(f1, range, n)

# Wykres
plt.plot(x_vals, y_vals, label='Funkcja')
plt.plot(x_vals, approx_vals, '--', label='Metoda prostokątów (n=100)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Wykres przybliżenia metody prostokątów dla funkcji 1')
plt.grid(True)
plt.show()
