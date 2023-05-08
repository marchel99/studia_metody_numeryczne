import numpy as np

def funkcja1(x):
    a = 1
    b = 2
    c = 3
    return c*x**3 + b*x + a

def funkcja2(x):
    d = 1
    e = 2.71828
    return d*np.cos(x/e)

def funkcja3(x):
    f = 2
    g = np.pi
    return np.log(x/f)

def metoda_prostokatow(funkcja, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = funkcja(x[:-1])
    pole = np.sum(y) * dx
    return pole

def metoda_trapezow(funkcja, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = funkcja(x)
    pole = (np.sum(y) - (y[0] + y[-1])/2) * dx
    return pole

def metoda_parabol(funkcja, a, b, n):
    if n % 2 != 0:
        raise ValueError("Liczba podprzedziałów musi być parzysta.")
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = funkcja(x)
    pole = (np.sum(y) - y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2])) * dx / 3
    return pole

def oblicz_całki_i_błędy():
    funkcje = [funkcja1, funkcja2, funkcja3]
    przedziały = [[-2, 2], [0, np.pi/2], [1, np.e]]

    for i in range(len(funkcje)):
        funkcja = funkcje[i]
        przedział = przedziały[i]
        a, b = przedział[0], przedział[1]

        print(f"Całkowanie funkcji {funkcja.__name__} w przedziale [{a}, {b}]")

        for n in [2, 4, 8, 16]:
            pole_prostokatow = metoda_prostokatow(funkcja, a, b, n)
            pole_trapezow = metoda_trapezow(funkcja, a, b, n)
            pole_parabol = metoda_parabol(funkcja, a, b, n)
            dokladne = 0  # Wprowadź tutaj wartość dokładną, jeśli jest dostępna

            blad_prostokatow = abs(dokladne - pole_prostokatow)
            blad_trapezow = abs(dokladne - pole_trapezow)
            blad_parabol = abs(dokladne - pole_parabol)

            print(f"Liczba podprzedziałów: {n}")
            print(f"Metoda prostokątów: {pole_prostokatow}, Błąd: {blad_prostokatow}")
            print(f"Metoda trapezów: {pole_trapezow}, Błąd: {blad_trapezow}")
            print(f"Metoda parabol: {pole_parabol}, Błąd: {blad_parabol}")
            print("-------------")

oblicz_całki_i_błędy()