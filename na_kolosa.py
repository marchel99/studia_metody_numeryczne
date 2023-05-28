import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def f(x):
    return x**3 + x + 4

# Znalezienie punktu ekstremalnego
result = minimize_scalar(f)
extremum = result.x

print("Potencjalny punkt ekstremalny:")
print("x =", extremum)

# Wygenerowanie wykresu
x_vals = np.linspace(-10, 10, 1000)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = x^3 + x + 4')
plt.scatter(extremum, f(extremum), color='red', label='Potencjalny punkt ekstremalny')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji')
plt.grid(True)
plt.show()
