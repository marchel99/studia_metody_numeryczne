import numpy as np
from scipy.integrate import quad

# Definicja funkcji
a, b, c, d, e, f, g = -2, -2, -2, -1, -2, 3, 3
funkcje = [(lambda x: c*x**3 + b*x + a, -2, 2), 
           (lambda x: d*np.cos(x/e), 0, np.pi/2),
           (lambda x: np.log(x/f), 1, g)]

# Metoda prostokątów
def metoda_prostokatow(funkcja, a, b, n):
    h = (b - a) / n
    return sum([funkcja(a + i*h) for i in range(n)]) * h

# Metoda trapezów
def metoda_trapezow(funkcja, a, b, n):
    h = (b - a) / n
    return (0.5 * (funkcja(a) + funkcja(b)) + sum([funkcja(a + i*h) for i in range(1, n)])) * h

# Metoda Simpsona
def metoda_simpsona(funkcja, a, b, n):
    h = (b - a) / (2*n)
    return (1/3) * h * (funkcja(a) + funkcja(b) + 4 * sum([funkcja(a + i*h) for i in range(1, 2*n, 2)]) + 2 * sum([funkcja(a + i*h) for i in range(2, 2*n, 2)]))

# Obliczenia i wypisanie wyników
liczba_podprzedzialow = [10, 20, 50, 100]

for i, (funkcja, a, b) in enumerate(funkcje):
    calka, _ = quad(funkcja, a, b)
    print(f"Funkcja {i+1}:")
    for n in liczba_podprzedzialow:
        wynik_prostokaty = metoda_prostokatow(funkcja, a, b, n)
        wynik_trapezy = metoda_trapezow(funkcja, a, b, n)
        wynik_simpsona = metoda_simpsona(funkcja, a, b, n)

        print(f"  Liczba podprzedziałów = {n}")
        print(f"    Metoda prostokątów:    {wynik_prostokaty}, Błąd: {abs(wynik_prostokaty - calka)}")
        print(f"    Metoda trapezów:       {wynik_trapezy}, Błąd: {abs(wynik_trapezy - calka)}")
        print(f"    Metoda Simpsona:       {wynik_simpsona}, Błąd: {abs(wynik_simpsona - calka)}")
    print()
