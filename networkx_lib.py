import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()

# l = [1,2,3]
# G.add_nodes_from(l)

# # Add nodes to the graph
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

# # Add a weighted edge from node
# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(3,1)

# print(G.edges())  # print the nodes in the graph

# G = nx.complete_graph(100)
# G = nx.gnp_random_graph(20,0.5)

# nx.draw(G)
# plt.show()
# G = nx.gnp_random_graph(50,0.3)
# nx.draw(G)
# plt.show()
# print(G.nodes(),G.edges(),G.degree(0))
G = nx.barabasi_albert_graph(50,2)
nx.draw(G)
plt.show()

nx.write_gexf(G, "graph.gexf")