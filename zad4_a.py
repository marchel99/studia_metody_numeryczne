"""
Zadanie 4. Rozwiązać układ równań metoda Newtona i Newtona-Rapsona dla
przypadku;
Dany jest układ równań:
{
𝑥1 = 3𝑥2 + 𝐼1
𝑥2 = 𝑥1
3 − 𝐼2
gdzie x=[x1,x2]
T
.
Punkt startowy: x0=[1,1]T
Dla kryterium stopu eps=0.001 (abserror).
"""


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    x1 = x[0]
    x2 = x[1]
    eq1 = x1 - 3*x2 - 2
    eq2 = x2 - x1**3 + 4
    return np.array([eq1, eq2])

def jacobian(x):
    x1 = x[0]
    x2 = x[1]
    jacobian_matrix = np.array([[1, -3], [-3*x1**2, 1]])
    return jacobian_matrix

def newton_method(f, jacobian, x0, epsilon, max_iterations):
    x = x0
    iterations = 0

    while np.linalg.norm(f(x)) > epsilon and iterations < max_iterations:
        delta_x = np.linalg.solve(jacobian(x), -f(x))
        x = x + delta_x
        iterations += 1

    if iterations == max_iterations:
        print("Nie udało się znaleźć rozwiązania w zadanej liczbie iteracji.")

    return x

# Punkt startowy
x0 = np.array([1, 1])

# Kryterium stopu
epsilon = 0.001

# Maksymalna liczba iteracji
max_iterations = 100

# Rozwiązanie układu równań metodą Newtona
solution_newton = newton_method(f, jacobian, x0, epsilon, max_iterations)

# Rozwiązanie układu równań metodą Newtona-Raphsona
solution_newton_raphson = newton_method(f, jacobian, x0, epsilon, max_iterations)

# Wykres
x1_vals = np.linspace(-5, 5, 100)
x2_vals = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
F = f([X1, X2])
fig, ax = plt.subplots()
ax.contour(X1, X2, F[0], levels=[0], colors='red', linestyles='dashed')
ax.contour(X1, X2, F[1], levels=[0], colors='blue', linestyles='dashed')
ax.scatter(solution_newton[0], solution_newton[1], color='red', label='Metoda Newtona')
ax.scatter(solution_newton_raphson[0], solution_newton_raphson[1], color='blue', label='Metoda Newtona-Raphsona')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Rozwiązanie układu równań')
ax.legend()
equation_text = r'$f(x) = \frac{{\sin(x^2) \cos(x)}}{{1 - x^2}}$'
plt.text(-7, 9, equation_text, fontsize=12, )

plt.text(-7, 8, 'Przedział: [-5, 5]', fontsize=12)

plt.show()
