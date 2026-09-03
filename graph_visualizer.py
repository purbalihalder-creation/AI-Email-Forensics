import plotly.graph_objects as go
import networkx as nx


def graph_to_plotly(graph):

    positions = nx.spring_layout(
        graph,
        seed=42
    )

    edge_x = []
    edge_y = []

    for source, target in graph.edges():

        x1, y1 = positions[source]
        x2, y2 = positions[target]

        edge_x.extend([
            x1, x2, None
        ])

        edge_y.extend([
            y1, y2, None
        ])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines"
    )

    node_x = []
    node_y = []
    labels = []

    for node in graph.nodes():

        x, y = positions[node]

        node_x.append(x)
        node_y.append(y)

        labels.append(node)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=labels,
        textposition="top center"
    )

    figure = go.Figure(
        data=[
            edge_trace,
            node_trace
        ]
    )

    return figure