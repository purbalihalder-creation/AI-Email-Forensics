import networkx as nx


def create_email_graph(
    sender,
    domains,
    ips,
    urls
):

    graph = nx.DiGraph()

    graph.add_node(
        sender,
        type="sender"
    )

    for domain in domains:

        graph.add_node(
            domain,
            type="domain"
        )

        graph.add_edge(
            sender,
            domain,
            relationship="uses"
        )

    for ip in ips:

        graph.add_node(
            ip,
            type="ip"
        )

        for domain in domains:

            graph.add_edge(
                domain,
                ip,
                relationship="resolves_to"
            )

    for url in urls:

        graph.add_node(
            url,
            type="url"
        )

        for domain in domains:

            graph.add_edge(
                domain,
                url,
                relationship="hosts"
            )

    return graph