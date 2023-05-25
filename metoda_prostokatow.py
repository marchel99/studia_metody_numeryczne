#'JetBrains Mono', 'Courier New', monospace

import matplotlib.pyplot as plt
import numpy as np

def metoda_prostokatow(f, a, b, n):
    """""
    Oblicza przybliżoną wartość całki funkcji f na przedziale [a, b] za pomocą metody prostokątów.

    
    Parametry:
    f (function): Funkcja, której całkę chcemy obliczyć.
    a (float): Dolna granica przedziału całkowania.
    b (float): Górna granica przedziału całkowania.
    n (int): Liczba podprzedziałów.
    n  (int): Liczba podprzedziałów.
    Zwraca:
    float: Przybliżona wartość całki.
    """
    h = (b - a) / n  # Szerokość każdego podprzedziału
    suma = 0.0

    for i in range(n):
        x = a + i * h  # Wartość x w lewym końcu prostokąta
        suma += f(x)  # Dodanie wartości funkcji w lewym końcu prostokąta

    wynik = h * suma
    return wynik

def funkcja(x):
    return x**2  # Przykładowa funkcja, dla której obliczamy całkę

a = 0  # Dolna granica przedziału
b = 1  # Górna granica przedziału
n = 10  # Liczba podprzedziałów

wynik = metoda_prostokatow(funkcja, a, b, n)
print("Przybliżona wartość całki:", wynik)

# Wygenerowanie wykresu funkcji
x = np.linspace(a, b, 1000)  # Zakres x dla wykresu
y = funkcja(x)  # Wartości y dla wykresu funkcji

# Dodanie oznaczenia przedziałów
x_podprzedzialy = np.linspace(a, b, n + 1)
y_podprzedzialy = funkcja(x_podprzedzialy)
plt.vlines(x_podprzedzialy, 0, y_podprzedzialy, colors='red', linestyles='dotted')

plt.plot(x, y, label='funkcja(x)')
plt.fill_between(x, y, where=(x >= a) & (x <= b), alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres funkcji x^2')
plt.legend()
plt.grid(True)
plt.show()
