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

# Import bibliotek
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import optimize

# Definiowanie funkcji
def F(X):
    x1, x2 = X
    return [x1 - 3*x2 - 2, x2 - x1**3 + 4]

# Definiowanie Jacobianu (macierzy pochodnych cząstkowych)
def jacobian(X):
    x1, x2 = X
    return [[1, -3], [-3*x1**2, 1]]

# Punkt startowy
X0 = [1, 1]

# Metoda Newtona-Raphsona
for i in range(100):  # max liczba iteracji
    delta = np.linalg.solve(jacobian(X0), F(X0))  # obliczenie delta X
    X0 -= delta  # aktualizacja punktu startowego
    if np.linalg.norm(delta) < 0.001:  # sprawdzenie kryterium stopu
        break

solution = X0

# Definiujemy nasze funkcje
def f1(x1, x2):
    return x1 - 3*x2 - 2

def f2(x1, x2):
    return x2 - x1**3 + 4

x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)

X1, X2 = np.meshgrid(x1, x2)

# Tworzymy wykres 3D
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X1, X2, f1(X1, X2))
ax1.set_title('$f_{1}(x_{1}, x_{2})$')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X1, X2, f2(X1, X2))
ax2.set_title('$f_{2}(x_{1}, x_{2})$')

# Dodanie równania do wykresu
equation_text_1 = r"$x_{1} = 3x_{2} + 2,$"
equation_text_2 = r"$x_{2} = x_{1}^{3} - 4.$"

plt.figtext(0.44, 0.08, '{', ha="center", fontsize=36, va="center")
plt.figtext(0.507, 0.10, equation_text_1, ha="center", fontsize=15, va="center")
plt.figtext(0.5, 0.05, equation_text_2, ha="center", fontsize=15, va="center")

# Dodanie rozwiązania do wykresu
solution_text = f"Rozwiązanie: $x_{{1}}$={solution[0]:.3f}, $x_{{2}}$={solution[1]:.3f}"
plt.figtext(0.5, 0.001, solution_text, ha="center", fontsize=15, va="center")

plt.show()
