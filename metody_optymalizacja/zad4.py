"""
Zadanie 4. Rozwiązać układ równań metoda Newtona i Newtona-Rapsona dla
przypadku;
Dany jest układ równań:
{
𝑥1 = 3𝑥2 + 𝐼1
𝑥2 = 𝑥13 − 𝐼2
}
gdzie x=[x1,x2]^T
Punkt startowy: x0=[1,1]^T
Dla kryterium stopu eps=0.001 (abserror).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def F(X):
    x1, x2 = X
    return [x1 - 3*x2 - 2, x2 - x1**3 + 4]

def jacobian(X):
    x1, x2 = X
    return [[1, -3], [-3*x1**2, 1]]

X0 = [1, 1]

for i in range(100):
    delta = np.linalg.solve(jacobian(X0), F(X0))
    X0 -= delta
    if np.linalg.norm(delta) < 0.001:
        break

solution = X0

def f1(x1, x2):
    return x1 - 3*x2 - 2

def f2(x1, x2):
    return x2 - x1**3 + 4

#
x = np.linspace(-5, 5, 100)

plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.plot(x, f1(x, (x + 2) / 3))
plt.xlabel('$x_{1}$')
plt.ylabel('$f_{1}(x_{1}, x_{2})$')
plt.title('$f_{1}(x_{1}, x_{2})$')

plt.subplot(122)
plt.plot(x, f2(x, x**3 - 4))
plt.xlabel('$x_{1}$')
plt.ylabel('$f_{2}(x_{1}, x_{2})$')
plt.title('$f_{2}(x_{1}, x_{2})$')

solution_text = f"Rozwiązanie: $x_{{1}}$={solution[0]:.3f}, $x_{{2}}$={solution[1]:.3f}"
plt.figtext(0.5, 0.15, solution_text, ha="center", fontsize=15, va="center")

plt.subplots_adjust(bottom=0.25)

plt.show()
print("Rozwiązanie:")
print("x1 =", solution[0])
print("x2 =", solution[1])