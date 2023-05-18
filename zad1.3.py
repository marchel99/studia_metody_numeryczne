import matplotlib.pyplot as plt
import networkx as nx

# Tworzenie pustego obiektu grafu
G = nx.DiGraph()

# Dodawanie krawędzi do grafu
G.add_edge('T4', 'T31')
G.add_edge('T4', 'T20')

G.add_edge('T20', 'T12')
G.add_edge('T20', 'Test Vector')

G.add_edge('T31', 'Failed Test')
 
G.add_edge('Failed Test', 'T21')

G.add_edge('T21', 'Failed Test')
G.add_edge('T21', 'Test Vector')

G.add_edge('Failed Test', 'E stuck-at-0')

# Rysowanie grafu
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')

# Wyświetlanie grafu
plt.show()