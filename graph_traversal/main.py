"""
main.py

This script measures and records the execution time of DFS and BFS on
randomly generated connected graphs of increasing size. It prints a
formatted table of results and passes the data to a visualization function.
"""

import time
from generator import generate_random_connected_graph
from algorithms import depth_first_search, breadth_first_search
from visualizer import plot_results


if __name__ == "__main__":
    # --- Sanity Check ---
    test_graph = generate_random_connected_graph(10, 5)

    dfs_test = depth_first_search(test_graph, 0)
    bfs_test = breadth_first_search(test_graph, 0)

    print("Sanity Check DFS traversal:")
    print(dfs_test)

    print("Sanity Check BFS traversal:")
    print(bfs_test)

    if len(dfs_test) == 10 and len(bfs_test) == 10:
        print("Sanity check passed")
    else:
        print("Sanity check FAILED")
        print("DFS length:", len(dfs_test))
        print("BFS length:", len(bfs_test))

    # --- Timing Setup ---
    node_counts = [10, 50, 100, 250, 500, 750, 1000, 2500, 5000]

    dfs_times = []
    bfs_times = []

    # --- Timing Loop ---
    for num_nodes in node_counts:
        graph = generate_random_connected_graph(num_nodes, num_nodes)

        dfs_total_time = 0.0
        bfs_total_time = 0.0

        for _ in range(3):
            # Time DFS
            start_time = time.perf_counter()
            depth_first_search(graph, 0)
            end_time = time.perf_counter()
            dfs_total_time += (end_time - start_time)

            # Time BFS
            start_time = time.perf_counter()
            breadth_first_search(graph, 0)
            end_time = time.perf_counter()
            bfs_total_time += (end_time - start_time)

        dfs_average = dfs_total_time / 3
        bfs_average = bfs_total_time / 3

        dfs_times.append(dfs_average)
        bfs_times.append(bfs_average)

    # --- Print Results Table ---
    print("\nExecution Time Results (seconds):")
    print(f"{'Nodes':>10} | {'DFS Avg Time':>15} | {'BFS Avg Time':>15}")
    print("-" * 45)

    for index in range(len(node_counts)):
        print(f"{node_counts[index]:>10} | {dfs_times[index]:>15.6f} | {bfs_times[index]:>15.6f}")

    # --- Plot Results ---
    plot_results(node_counts, dfs_times, bfs_times)