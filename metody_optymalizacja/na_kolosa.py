def f(x):
    return x**3 + x + 4

def f_prime(x):
    return 3*x**2 + 1
  
  
def newton_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    iter_count = 0

    while abs(f(x)) > tol and iter_count < max_iter:
        x = x - f(x) / f_prime(x)
        iter_count += 1

    if abs(f(x)) <= tol:
        return x
    else:
        return None

# Wywołanie metody Newtona
x0 = 0  # Punkt startowy
root = newton_method(f, f_prime, x0)

if root is not None:
    print("Miejsce zerowe: x =", root)
else:
    print("Nie udało się znaleźć miejsca zerowego w określonym zakresie iteracji.")
