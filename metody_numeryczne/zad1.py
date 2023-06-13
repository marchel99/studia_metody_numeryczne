import numpy as np
import matplotlib.pyplot as plt

def f2(x):
    return -np.cos(x/-2)

def rectangle_method(f, interval, n):
    h = (interval[1] - interval[0]) / n
    result = 0
    for i in range(n):
        result += f(interval[0] + h * (i + 0.5))
    result *= h
    return result

# Definicja przedziału
interval = [0, np.pi/2]
n = 100

# Obliczenie wartości przybliżonej
x_vals = np.linspace(interval[0], interval[1], 100)
y_vals = f2(x_vals)

# Obliczenie próbek metody prostokątów
x_samples = np.linspace(interval[0], interval[1], n)
y_samples = f2(x_samples)

# Wykres
plt.plot(x_vals, y_vals, label='Funkcja: -cos(x/(-2))')
plt.scatter(x_samples, y_samples, color='blue', label='Próbki (Metoda prostokątów)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Wykres przybliżenia metody prostokątów dla funkcji')
plt.grid(True)

# Zaznaczanie obszarów między wykresem a osią x
plt.fill_between(x_vals, y_vals, where=(y_vals > 0), color='lightgray', alpha=0.3)
plt.fill_between(x_vals, y_vals, where=(y_vals < 0), color='gray', alpha=0.3)

# Dodanie linii poziomej w zerze
plt.axhline(y=0, color='black', linewidth=0.5)

plt.show()
