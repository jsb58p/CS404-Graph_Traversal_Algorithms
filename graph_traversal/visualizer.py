"""
visualizer.py

This module provides a function to generate and save visualizations comparing
DFS and BFS execution times using matplotlib.
"""

import os
import matplotlib.pyplot as plt


def plot_results(node_counts, dfs_times, bfs_times):
    """
    Generate and save line and bar charts comparing DFS and BFS execution times.

    Args:
        node_counts (list of int): List of graph sizes (number of nodes).
        dfs_times (list of float): Average DFS execution times for each graph size.
        bfs_times (list of float): Average BFS execution times for each graph size.
    """
    # --- Line Chart ---
    plt.figure()
    plt.plot(node_counts, dfs_times, label="DFS")
    plt.plot(node_counts, bfs_times, label="BFS")

    plt.title("DFS vs BFS Execution Time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Execution Time (seconds)")
    plt.legend()
    plt.grid()

    plt.savefig("execution_times.png")
    plt.close()

    # --- Bar Chart ---
    plt.figure()

    x_positions = range(len(node_counts))
    bar_width = 0.4

    dfs_positions = [x - bar_width / 2 for x in x_positions]
    bfs_positions = [x + bar_width / 2 for x in x_positions]

    plt.bar(dfs_positions, dfs_times, width=bar_width, label="DFS")
    plt.bar(bfs_positions, bfs_times, width=bar_width, label="BFS")

    plt.title("DFS vs BFS Execution Time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Execution Time (seconds)")
    plt.xticks(ticks=x_positions, labels=node_counts, rotation=45)
    plt.legend()
    plt.grid()

    plt.savefig("execution_times_bar.png")
    plt.close()


if __name__ == "__main__":
    # Dummy test data
    node_counts = [10, 50, 100, 250, 500]
    dfs_times = [0.0001, 0.0005, 0.001, 0.003, 0.007]
    bfs_times = [0.00009, 0.00045, 0.0009, 0.0025, 0.006]

    plot_results(node_counts, dfs_times, bfs_times)

    # Verify files exist
    if os.path.exists("execution_times.png"):
        print("Plot saved: execution_times.png")
    else:
        print("TEST FAILED: file not found")

    if os.path.exists("execution_times_bar.png"):
        print("Plot saved: execution_times_bar.png")
    else:
        print("TEST FAILED: file not found")