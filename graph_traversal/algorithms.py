"""
algorithms.py

This module implements graph traversal algorithms (DFS and BFS) for an
undirected, unweighted graph represented by the Graph class from graph.py.
"""

from collections import deque
from graph import Graph


def depth_first_search(graph, start_node):
    """
    Perform an iterative Depth-First Search (DFS) traversal.

    Uses an explicit stack to avoid recursion limits. Traverses as deep as
    possible along each branch before backtracking.

    Args:
        graph (Graph): The graph to traverse.
        start_node (int): The node to start traversal from.

    Returns:
        list: A list of nodes in the order they were visited.

    Time Complexity:
        O(V + E), where V is the number of nodes and E is the number of edges.
    """
    visited_nodes = set()
    traversal_order = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)
        traversal_order.append(current_node)

        # Add neighbors to stack (reverse order to maintain consistent traversal)
        neighbors = graph.get_neighbors(current_node)
        for neighbor in reversed(neighbors):
            if neighbor not in visited_nodes:
                stack.append(neighbor)

    return traversal_order


def breadth_first_search(graph, start_node):
    """
    Perform a Breadth-First Search (BFS) traversal.

    Uses a queue (deque) to explore nodes level by level.

    Args:
        graph (Graph): The graph to traverse.
        start_node (int): The node to start traversal from.

    Returns:
        list: A list of nodes in the order they were visited.

    Time Complexity:
        O(V + E), where V is the number of nodes and E is the number of edges.
    """
    visited_nodes = set([start_node])
    traversal_order = []
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # Explore all unvisited neighbors
        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                queue.append(neighbor)

    return traversal_order


if __name__ == "__main__":
    # Create graph with 6 nodes
    graph = Graph(6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)

    # DFS from node 0
    dfs_result = depth_first_search(graph, 0)
    print("DFS traversal from node 0 (should include all 6 nodes):")
    print(dfs_result)

    # BFS from node 0
    bfs_result = breadth_first_search(graph, 0)
    print("BFS traversal from node 0 (should include all 6 nodes):")
    print(bfs_result)

    # Confirm different orderings
    print("DFS vs BFS comparison:")
    print("DFS:", dfs_result)
    print("BFS:", bfs_result)

    # Disconnected graph
    graph_disconnected = Graph(4)
    graph_disconnected.add_edge(0, 1)
    graph_disconnected.add_edge(2, 3)

    dfs_disconnected = depth_first_search(graph_disconnected, 0)
    bfs_disconnected = breadth_first_search(graph_disconnected, 0)

    print("\nDisconnected graph DFS from node 0 (should be [0, 1]):")
    print(dfs_disconnected)

    print("Disconnected graph BFS from node 0 (should be [0, 1]):")
    print(bfs_disconnected)