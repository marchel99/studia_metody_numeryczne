import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize



# Definiowanie funkcji celu
def func(x):
    return 9 + x[0]**2 + x[1]**2

# Początkowe punkty sympleksu
initial_simplex = np.array([[6, 6], [8, 5], [8, 4]])

# Minimizacja funkcji celu z użyciem algorytmu Nelder-Meada
res = minimize(func, x0=[0, 0], method='Nelder-Mead', options={'initial_simplex': initial_simplex, 'return_all': True})

# Utworzenie siatki dla wizualizacji funkcji celu
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = func([X, Y])

# Wizualizacja funkcji celu
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')

# Dodanie punktów sympleksu do wizualizacji
allvecs = res.allvecs
for vec in allvecs:
    ax.plot([vec[0]], [vec[1]], [func(vec)], 'ro')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
