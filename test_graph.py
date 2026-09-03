import networkx as nx

from graph_visualizer import graph_to_plotly


graph = nx.DiGraph()


graph.add_node(
    "attacker@example.com",
    type="sender"
)

graph.add_node(
    "suspicious-domain.com",
    type="domain"
)

graph.add_node(
    "185.220.101.10",
    type="ip"
)


graph.add_edge(
    "attacker@example.com",
    "suspicious-domain.com"
)

graph.add_edge(
    "suspicious-domain.com",
    "185.220.101.10"
)


figure = graph_to_plotly(graph)

figure.show()