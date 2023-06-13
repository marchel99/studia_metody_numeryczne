import numpy as np
import matplotlib.pyplot as plt

def f2(x):
    return -np.cos(x/-2)

def simpson_method(f, interval, n):
    if n % 2 != 0:
        n += 1

    h = (interval[1] - interval[0]) / n
    x = np.linspace(interval[0], interval[1], n+1)
    y = f(x)

    result = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))
    return result

# Definicja przedziału
interval = [0, np.pi/2]
n = 100

# Obliczenie wartości przybliżonej
x_vals = np.linspace(interval[0], interval[1], 100)
y_vals = f2(x_vals)

# Obliczenie próbek metody Simpsona
x_samples = np.linspace(interval[0], interval[1], n)
y_samples = f2(x_samples)

# Wykres
plt.plot(x_vals, y_vals, label='Funkcja: -cos(x/(-2))')
plt.scatter(x_samples, y_samples, color='green', label='Próbki (Metoda Simpsona)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Wykres przybliżenia metody Simpsona dla funkcji')
plt.grid(True)

# Zaznaczanie obszarów między wykresem a osią x
plt.fill_between(x_vals, y_vals, where=(y_vals > 0), color='lightgray', alpha=0.3)
plt.fill_between(x_vals, y_vals, where=(y_vals < 0), color='gray', alpha=0.3)

# Dodanie linii poziomej w zerze
plt.axhline(y=0, color='black', linewidth=0.5)

plt.show()
