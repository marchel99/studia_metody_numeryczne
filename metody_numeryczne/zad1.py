import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definicja funkcji
a, b, c, d, e, f, g = -2, -2, -2, -1, -2, 3, 3
funkcje = [(lambda x: c*x**3 + b*x + a, -2, 2, "a"), 
           (lambda x: d*np.cos(x/e), 0, np.pi/2, "b"),
           (lambda x: np.log(x/f), 1, g, "c")]

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
n = 100
x_values = np.linspace(-3, 3, 400)

for i, (funkcja, a, b, label) in enumerate(funkcje):
    calka, _ = quad(funkcja, a, b)

    # Metoda prostokątów
    y_values = [metoda_prostokatow(funkcja, a, x, n) for x in x_values]
    plt.figure()
    plt.plot(x_values, y_values, label=f"Metoda prostokątów")
    plt.xlabel('x')
    plt.ylabel('Wartość całki')
    plt.title(f'Rysunek {3*i+1}. Wykres dla przykładu {label} uzyskany przy wykorzystaniu metody prostokątów, przy n=100.')
    plt.legend()
    plt.grid()
    
    # Metoda Simpsona
    y_values = [metoda_simpsona(funkcja, a, x, n) for x in x_values]
    plt.figure()
    plt.plot(x_values, y_values, label=f"Metoda Simpsona")
    plt.xlabel('x')
    plt.ylabel('Wartość całki')
    plt.title(f'Rysunek {3*i+2}. Wykres dla przykładu {label} uzyskany przy wykorzystaniu metody Simpsona, przy n=100.')
    plt.legend()
    plt.grid()
    
    # Metoda trapezów
    y_values = [metoda_trapezow(funkcja, a, x, n) for x in x_values]
    plt.figure()
    plt.plot(x_values, y_values, label=f"Metoda trapezów")
    plt.xlabel('x')
    plt.ylabel('Wartość całki')
    plt.title(f'Rysunek {3*i+3}. Wykres dla przykładu {label} uzyskany przy wykorzystaniu metody trapezów, przy n=100.')
    plt.legend()
    plt.grid()

plt.show()
