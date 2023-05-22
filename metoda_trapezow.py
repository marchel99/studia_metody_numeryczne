def metoda_trapezow(f, a, b, n):
    """
    Oblicza przybliżoną wartość całki funkcji f na przedziale [a, b] za pomocą metody trapezów.

    Parametry:
    f (function): Funkcja, której całkę chcemy obliczyć.
    a (float): Dolna granica przedziału całkowania.
    b (float): Górna granica przedziału całkowania.
    n (int): Liczba podprzedziałów.

    Zwraca:
    float: Przybliżona wartość całki.

    """
    h = (b - a) / n  # Szerokość każdego podprzedziału
    suma = f(a) + f(b)  # Suma wartości funkcji na krańcach przedziału

    for i in range(1, n):
        x = a + i * h  # Wartość x w punkcie środkowym podprzedziału
        suma += 2 * f(x)  # Dodanie wartości funkcji na punkcie środkowym

    wynik = (h / 2) * suma
    return wynik

def funkcja(x):
    return x**2  # Przykładowa funkcja, dla której obliczamy całkę

a = 0  # Dolna granica przedziału
b = 1  # Górna granica przedziału
n = 100  # Liczba podprzedziałów

wynik = metoda_trapezow(funkcja, a, b, n)
print("Przybliżona wartość całki:", wynik)

