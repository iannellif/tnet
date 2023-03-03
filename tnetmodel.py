import networkx as nx
import random
import matplotlib.pyplot as plt

# Define the static backbone network
G = nx.erdos_renyi_graph(20, 0.2)

# Define the number of time steps
T = 10

# Define the activation probability for each edge at each time step
p = [[random.random() for j in range(G.number_of_edges())] for i in range(T)]

# Define the active edges at each time step
active_edges = [[(u, v) for (u, v) in G.edges() if random.random() < p[i][j]] for i in range(T) for j in range(G.number_of_edges())]

# Define a list to store the fraction of active edges at each time step
frac_active_edges = []

# Define the initial plot of the static backbone network
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
plt.axis('off')
plt.show()

# Plot the temporal network and the fraction of active edges at each time step
for t in range(T):
    # Define the edges and nodes for the current time step
    edges = active_edges[t]
    nodes = set([u for (u, v) in edges] + [v for (u, v) in edges])
    
    # Compute the fraction of active edges for the current time step
    frac_active = len(edges) / G.number_of_edges()
    frac_active_edges.append(frac_active)

    # Define the plot of the temporal network for the current time step
    plt.figure(figsize=(6,6))
    plt.title("Time Step: " + str(t+1))
    nx.draw_networkx_nodes(nodes, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(edges, pos, width=1.0, alpha=0.5)
    plt.axis('off')
    plt.show()

# Plot the fraction of active edges over time
plt.figure()
plt.plot(range(1,T+1), frac_active_edges, marker='o')
plt.xlabel('Time Step')
plt.ylabel('Fraction of Active Edges')
plt.show()
