def f(x):
    return x**3 + x + 4

def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("Nie można zagwarantować istnienia miejsca zerowego w danym przedziale.")
        return None

    for _ in range(max_iterations):
        c = (a + b) / 2

        if abs(f(c)) < tolerance:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Nie osiągnięto zbieżności po zadanej liczbie iteracji.")
    return None

if __name__ == "__main__":
    a = -5  # Początek przedziału
    b = 5   # Koniec przedziału

    zero = bisection_method(f, a, b)
    if zero is not None:
        print("Miejsce zerowe: x =", zero)
