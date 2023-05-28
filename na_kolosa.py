import matplotlib.pyplot as plt
import numpy as np

def find_zeros(f, x_range):
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = f(x)

    # Znajdowanie indeksów, gdzie znaki funkcji się zmieniają (miejsca zerowe)
    zero_indices = np.where(np.diff(np.sign(y)))[0]
    zeros = x[zero_indices]

    return zeros

def plot_function(f, x_range):
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    zeros = find_zeros(f, x_range)
    ax.plot(zeros, f(zeros), 'ro', label='Miejsca zerowe')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Wykres funkcji')

    plt.show()

if __name__ == '__main__':
    # Funkcja f(x) = x^3 + x + 4
    def funkcja(x):
        return x**3 + x + 4

    # Zakres osi x na wykresie
    x_range = (-5, 5)

    plot_function(funkcja, x_range)
