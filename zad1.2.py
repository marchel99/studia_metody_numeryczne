import math

# Funkcja podcałkowa 1


def f1(x):
    a = 1
    b = 2
    c = 3
    return c*x**3 + b*x + a

# Funkcja podcałkowa 2


def f2(x):
    d = 1
    e = 2
    return d*math.cos(x/e)

# Funkcja podcałkowa 3


def f3(x):
    f = 1
    g = 2
    return math.log(x/f)

# Metoda prostokątów


def rectangle_method(f, a, b, num_intervals):
    h = (b - a) / num_intervals
    integral = 0
    for i in range(num_intervals):
        x = a + i * h
        integral += f(x) * h
    return integral

# Metoda trapezów


def trapezoidal_method(f, a, b, num_intervals):
    h = (b - a) / num_intervals
    integral = (f(a) + f(b)) / 2
    for i in range(1, num_intervals):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

# Metoda parabol (Simpsona)


def simpsons_method(f, a, b, num_intervals):
    h = (b - a) / num_intervals
    integral = f(a) + f(b)
    for i in range(1, num_intervals):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    integral *= h / 3
    return integral


# Obliczanie wartości całek dla różnej liczby podprzedziałów
# Można dostosować tę listę do własnych potrzeb
num_intervals = [2, 4, 8, 16, 32]

# Obliczanie wartości całek dla funkcji 1
a1 = -2
b1 = 2
print("Funkcja 1:")
for num in num_intervals:
    rectangle_result = rectangle_method(f1, a1, b1, num)
    trapezoidal_result = trapezoidal_method(f1, a1, b1, num)
    simpsons_result = simpsons_method(f1, a1, b1, num)
    error_rectangle = abs(rectangle_result - 48/5)  # Wartość dokładna całki
    error_trapezoidal = abs(trapezoidal_result - 48/5)
    error_simpsons = abs(simpsons_result - 48/5)
    print(f"Num. podprzedziałów: {num}")
    print(f"Metoda prostokątów: {rectangle_result}, błąd: {error_rectangle}")
    print(f"Metoda trapezów: {trapezoidal_result}, błąd: {error_trapezoidal}")
    print(f"Metoda parabol: {simpsons_result}, błąd: {error_simpsons}")
print()

# Obliczanie wartości całek dla funkcji 2

a2 = 0
b2 = math.pi/2
print("Funkcja 2:")
for num in num_intervals:
rectangle_result = rectangle_method(f2, a2, b2, num)
trapezoidal_result = trapezoidal_method(f2, a2, b2, num)
simpsons_result = simpsons_method(f2, a2, b2, num)
error_rectangle = abs(rectangle_result - 1)  # Wartość dokładna całki
error_trapezoidal = abs(trapezoidal_result - 1)
error_simpsons = abs(simpsons_result - 1)
print(f"Num. podprzedziałów: {num}")
print(f"Metoda prostokątów: {rectangle_result}, błąd: {error_rectangle}")
print(f"Metoda trapezów: {trapezoidal_result}, błąd: {error_trapezoidal}")
print(f"Metoda parabol: {simpsons_result}, błąd: {error_simpsons}")
print()

# Obliczanie wartości całek dla funkcji 3

a3 = 1
b3 = 2
print("Funkcja 3:")
for num in num_intervals:
rectangle_result = rectangle_method(f3, a3, b3, num)
trapezoidal_result = trapezoidal_method(f3, a3, b3, num)
simpsons_result = simpsons_method(f3, a3, b3, num)
# Wartość dokładna całki
error_rectangle = abs(rectangle_result - (math.log(b3) - math.log(a3)))
error_trapezoidal = abs(trapezoidal_result - (math.log(b3) - math.log(a3)))
error_simpsons = abs(simpsons_result - (math.log(b3) - math.log(a3)))
print(f"Num. podprzedziałów: {num}")
print(f"Metoda prostokątów: {rectangle_result}, błąd: {error_rectangle}")
print(f"Metoda trapezów: {trapezoidal_result}, błąd: {error_trapezoidal}")
print(f"Metoda parabol: {simpsons_result}, błąd: {error_simpsons}")
print()
