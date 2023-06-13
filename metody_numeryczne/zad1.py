import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Definicja funkcji
funkcje = [(lambda x: -2 * x**3 - 2 * x - 2, -2, 2, "-2x^3 - 2x - 2"),
           (lambda x: -np.cos(-x/2), 0, np.pi/2, "-cos(-x/2)"),
           (lambda x: np.log(x/3), 1, 3, "ln(x/3)")]

# Metoda prostokątów
def metoda_prostokatow(funkcja, a, b, n):
    h = (b - a) / n
    return sum([funkcja(a + i*h) for i in range(n)]) * h

# Metoda trapezów
def metoda_trapezow(funkcja, a, b, n):
    h = (b - a) / n
    return (0.5 * (funkcja(a) + funkcja(b)) + sum([funkcja(a + i*h) for i in range(1, n)]) ) * h

# Metoda Simpsona
def metoda_simpsona(funkcja, a, b, n):
    h = (b - a) / (2*n)
    return (1/3) * h * (funkcja(a) + funkcja(b) + 4 * sum([funkcja(a + i*h) for i in range(1, 2*n, 2)]) + 2 * sum([funkcja(a + i*h) for i in range(2, 2*n, 2)]))

# Tworzenie wykresów
N = range(1, 101)

for funkcja, a, b, label in funkcje:
    dokladna_wartosc, _ = spi.quad(funkcja, a, b)
    
    bledy_prostokatow = [abs(metoda_prostokatow(funkcja, a, b, n) - dokladna_wartosc) for n in N]
    bledy_trapezow = [abs(metoda_trapezow(funkcja, a, b, n) - dokladna_wartosc) for n in N]
    bledy_simpsona = [abs(metoda_simpsona(funkcja, a, b, n) - dokladna_wartosc) for n in N]
    
    plt.figure()
    plt.plot(N, bledy_prostokatow, label="Metoda prostokątów")
    plt.plot(N, bledy_trapezow, label="Metoda trapezów")
    plt.plot(N, bledy_simpsona, label="Metoda Simpsona")
    plt.xlabel('Liczba podprzedziałów')
    plt.ylabel('Błąd bezwzględny')
    plt.title(f'Błąd bezwzględny metod całkowania dla funkcji {label}')
    plt.legend()
    plt.grid()

plt.show()
