import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def find_extrema(f):
    x = sp.symbols('x')
    f_prime = sp.diff(f, x)  # Obliczenie pochodnej funkcji

    extrema = sp.solve(f_prime, x)  # Znalezienie miejsc zerowych pochodnej

    return extrema

if __name__ == "__main__":
    x = sp.symbols('x')
    f = x**3 + x + 4

    extrema = find_extrema(f)

    print("Potencjalne punkty ekstremalne:")
    for ext in extrema:
        if sp.im(ext) == 0:  # Sprawdzenie, czy część urojona jest równa 0
            print("x =", ext)

    f_lambda = sp.lambdify(x, f, modules='numpy')  # Funkcja lambda dla funkcji f

    x_vals = np.linspace(-10, 10, 1000)
    y_vals = f_lambda(x_vals)

    plt.plot(x_vals, y_vals, label='f(x) = x^3 + x + 4')
    plt.scatter([sp.re(x) for x in extrema if sp.im(x) == 0], [f_lambda(x) for x in extrema if sp.im(x) == 0],
                color='red', label='Potencjalne punkty ekstremalne')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Wykres funkcji')
    plt.grid(True)
    plt.show()
