import matplotlib.pyplot as plt
import networkx as nx

# Tworzenie drzewa za pomocą NetworkX
G = nx.DiGraph()

# Dodanie węzłów
G.add_node("Problem: Błędne wyniki dla niektórych kombinacji wejść")
G.add_node("Hipoteza 1: Problem z wejściem E")
G.add_node("Hipoteza 2: Problem z wyjściem W1")

# Dodanie krawędzi
G.add_edge("Problem: Błędne wyniki dla niektórych kombinacji wejść", "Hipoteza 1: Problem z wejściem E")
G.add_edge("Problem: Błędne wyniki dla niektórych kombinacji wejść", "Hipoteza 2: Problem z wyjściem W1")

# Rysowanie drzewa
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=12, font_weight='bold')
plt.show()