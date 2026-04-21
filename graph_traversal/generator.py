"""
generator.py

This module provides a function to generate a random connected undirected,
unweighted graph. It guarantees connectivity by first constructing a random
spanning tree, then adds additional random edges while avoiding duplicates
and self-loops.
"""

import random
from graph import Graph


def generate_random_connected_graph(num_nodes, extra_edges):
    """
    Generate a random connected undirected graph.

    The function first ensures connectivity by creating a random spanning tree.
    Then it adds a specified number of additional random edges, skipping any
    edges that already exist or would create self-loops.

    Args:
        num_nodes (int): Number of nodes in the graph.
        extra_edges (int): Number of additional edges to add after ensuring connectivity.

    Returns:
        Graph: A connected Graph object with the specified properties.
    """
    graph = Graph(num_nodes)

    node_list = list(range(num_nodes))
    random.shuffle(node_list)

    connected_nodes = {node_list[0]}

    for index in range(1, num_nodes):
        current_node = node_list[index]
        previous_node = random.choice(list(connected_nodes))
        graph.add_edge(current_node, previous_node)
        connected_nodes.add(current_node)

    added_edges = 0

    while added_edges < extra_edges:
        node_a = random.randint(0, num_nodes - 1)
        node_b = random.randint(0, num_nodes - 1)

        if node_a == node_b:
            continue

        if node_b in graph.get_neighbors(node_a):
            continue

        graph.add_edge(node_a, node_b)
        added_edges += 1

    return graph


if __name__ == "__main__":
    # Generate graph with 5 nodes and 3 extra edges
    graph_5 = generate_random_connected_graph(5, 3)
    print("Graph with 5 nodes and 3 extra edges:")
    print(graph_5)

    all_connected_5 = all(len(graph_5.get_neighbors(node)) > 0 for node in graph_5.get_all_nodes())
    print("All nodes connected:", all_connected_5)

    total_edges_5 = sum(len(graph_5.get_neighbors(node)) for node in graph_5.get_all_nodes()) // 2
    print("Total edges:", total_edges_5)

    # Generate graph with 10 nodes and 5 extra edges
    graph_10 = generate_random_connected_graph(10, 5)
    print("\nGraph with 10 nodes and 5 extra edges:")
    print(graph_10)

    all_connected_10 = all(len(graph_10.get_neighbors(node)) > 0 for node in graph_10.get_all_nodes())
    print("All nodes connected:", all_connected_10)

    total_edges_10 = sum(len(graph_10.get_neighbors(node)) for node in graph_10.get_all_nodes()) // 2
    print("Total edges:", total_edges_10)