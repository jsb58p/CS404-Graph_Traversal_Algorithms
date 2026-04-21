"""
graph.py

This module defines a Graph class representing an undirected, unweighted graph
using an adjacency list. The adjacency list is implemented as a dictionary
mapping each node to a list of its neighboring nodes.
"""


class Graph:
    """Represents an undirected, unweighted graph using an adjacency list."""

    def __init__(self, num_nodes):
        """
        Initialize the graph with a specified number of nodes.

        Each node is labeled from 0 to num_nodes - 1, and each node starts
        with an empty list of neighbors.

        Args:
            num_nodes (int): The total number of nodes in the graph.
        """
        self.adjacency_list = {}
        for node in range(num_nodes):
            self.adjacency_list[node] = []

    def add_edge(self, node_a, node_b):
        """
        Add an undirected edge between two nodes.

        This method adds node_b to node_a's neighbor list and node_a to
        node_b's neighbor list.

        Args:
            node_a (int): The first node.
            node_b (int): The second node.
        """
        self.adjacency_list[node_a].append(node_b)
        self.adjacency_list[node_b].append(node_a)

    def get_neighbors(self, node):
        """
        Retrieve the neighbors of a given node.

        Args:
            node (int): The node whose neighbors are requested.

        Returns:
            list: A list of neighboring nodes.
        """
        return self.adjacency_list[node]

    def get_all_nodes(self):
        """
        Retrieve all node labels in the graph.

        Returns:
            list: A list of all node labels.
        """
        return list(self.adjacency_list.keys())

    def __str__(self):
        """
        Return a string representation of the graph's adjacency list.

        Returns:
            str: A readable string showing each node and its neighbors.
        """
        lines = []
        for node in self.adjacency_list:
            lines.append(f"{node}: {self.adjacency_list[node]}")
        return "\n".join(lines)


if __name__ == "__main__":
    # Create a graph with 5 nodes
    graph = Graph(5)

    # Add edges: (0,1), (0,2), (1,3), (2,4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    # Print the full adjacency list
    print("Adjacency List:")
    print(graph)

    # Print neighbors of node 0
    print("Neighbors of node 0 (expected: [1, 2]):")
    print(graph.get_neighbors(0))

    # Print neighbors of node 3
    print("Neighbors of node 3 (expected: [1]):")
    print(graph.get_neighbors(3))

    # Print all nodes
    print("All nodes (expected: [0, 1, 2, 3, 4]):")
    print(graph.get_all_nodes())

    # Attempt to get neighbors of node 4
    print("Neighbors of node 4 (expected: [2]):")
    print(graph.get_neighbors(4))