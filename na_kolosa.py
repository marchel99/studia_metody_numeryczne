import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def find_extrema(f):
    x = sp.symbols('x')
    f_prime = sp.diff(f, x)  # Obliczenie pochodnej funkcji

    extrema = sp.solve(f_prime, x)  # Znalezienie miejsc zerowych pochodnej

    return extrema

if __name__ == "__main__":
    f = lambda x: x**3 + x + 4

    extrema = find_extrema(f)

    print("Potencjalne punkty ekstremalne:")
    for ext in extrema:
        print("x =", ext)

    x_vals = np.linspace(-10, 10, 1000)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label='f(x) = x^3 + x + 4')
    plt.scatter(extrema, [f(x) for x in extrema], color='red', label='Potencjalne punkty ekstremalne')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Wykres funkcji')
    plt.grid(True)
    plt.show()
