import matplotlib.pyplot as plt
import numpy as np

def metoda_trapezow(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        suma += 2 * f(x)
    wynik = (h / 2) * suma
    return wynik

def funkcja(x):
    return x**2

a = 0 #dolna granica całkowania
b = 1 #górna granica całkowania
n = 100

x = np.linspace(a, b, 1000)  # Zakres x dla wykresu
y = funkcja(x)  # Wartości y dla wykresu funkcji

wynik = metoda_trapezow(funkcja, a, b, n)
print("Przybliżona wartość całki:", wynik)

plt.plot(x, y, label='funkcja(x)')
plt.fill_between(x, y, where=(x >= a) & (x <= b), alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres funkcji x^2')
plt.legend()
plt.grid(True)
plt.show()
