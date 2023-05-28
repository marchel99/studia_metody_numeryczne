import sympy as sp

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
