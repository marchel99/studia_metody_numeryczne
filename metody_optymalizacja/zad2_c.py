"""
Znaleźć miejsce zerowe podanej funkcji w zadanym przedziale wykorzystując metodę
złotego podziału
f(x) = sin(x*I2) * cos(x) / (1 - x^2) w przedziale [-5, 5]
Dla kryterium stopu eps=0.001 (abserror)
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.sin(x**2) * np.cos(x)) / (1 - x**2)

def golden_section_search(a, b, epsilon):
    ratio = (np.sqrt(5) - 1) / 2 

    while abs(b - a) > epsilon:
        c = b - ratio * (b - a)
        d = a + ratio * (b - a)
        fc = f(c)
        fd = f(d)

        if fc < fd:
            b = d
        else:
            a = c

    return (a + b) / 2


a = -5
b = 5


epsilon = 0.001


zero_point = golden_section_search(a, b, epsilon)
zero_point_value = f(zero_point)


x = np.linspace(-5, 5, 1000)
y = f(x)

plt.plot(x, y, label='f(x) = sin(x^2) * cos(x) / (1 - x^2)')
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=zero_point, color='red', linestyle='--', label='Miejsce zerowe')
plt.scatter(zero_point, 0, color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji')
plt.legend()


plt.text(-7, 78, 'Nr indeksu: 249842, I2=4', fontsize=12)
plt.text(-7, 73, 'Przedział: [-5, 5]', fontsize=12)
plt.text(-7, 68, 'Miejsce zerowe: x = {:.4f}'.format(zero_point), fontsize=12)


plt.show()


print("Miejsce zerowe:", zero_point)
print("Wartość funkcji w miejscu zerowym:", zero_point_value)
