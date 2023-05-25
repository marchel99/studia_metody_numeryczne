"""
Zadanie 5. Optymalizacja
Znaleźć minimalną wartość podanej funkcji wykorzystując algorytm mrówkowy,
pszczółkowy lub genetyczny:

𝑓(𝑎, 𝑏) = 𝐼2 ∗ (23 + 𝐼1 − 𝑎 ∙ 3
𝑏
)
2
, 𝑎 ∈ [0; 1], 𝑏 ∈ [0; 1].

"""
import numpy as np
import random
import matplotlib.pyplot as plt

# Wartości parametrów
alpha = 0.5
beta = 5
tau_start = 1e-5
eta = 0.01
Q = 1
rho = 0.1
num_ants = 1
num_iterations = 1000
a_start = 0.85
b_start = 0.95
I1 = 1   # Domyślna wartość, jeśli nie jest podana
I2 = 1   # Domyślna wartość, jeśli nie jest podana

# Funkcja celu
def f(a, b):
    return I2 * (23 + I1 - a * 3 / b) ** 2

# Inicjalizacja
a = a_start
b = b_start
tau = np.array([tau_start, tau_start])
best_a = a
best_b = b
best_val = f(a, b)

# Historia wartości funkcji celu
history = [best_val]

# Algorytm mrówkowy
for _ in range(num_iterations):
    # Losowe zmiany w a i b
    delta_a = (random.random() - 0.5) * eta
    delta_b = (random.random() - 0.5) * eta
    # Uaktualnij a i b
    a = np.clip(a + delta_a, 0, 1)
    b = np.clip(b + delta_b, 0, 1)
    # Oblicz wartość funkcji celu
    val = f(a, b)
    # Aktualizuj tau
    tau = (1 - rho) * tau + Q / val
    # Jeżeli nowe rozwiązanie jest lepsze, zapisz je
    if val < best_val:
        best_val = val
        best_a = a
        best_b = b
    # Dodaj wartość do historii
    history.append(best_val)

print(f"Najlepsze rozwiązanie: a={best_a}, b={best_b}, f(a, b)={best_val}")

# Wykres historii wartości funkcji celu
plt.figure(figsize=(10, 6))
plt.plot(history)
plt.title('Historia wartości funkcji celu')
plt.xlabel('Iteracja')
plt.ylabel('Wartość funkcji celu')
plt.grid(True)
plt.show()
