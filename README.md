# CS404 — Graph Traversal Algorithms

A Python implementation and performance comparison of Depth-First Search (DFS) and Breadth-First Search (BFS) on randomly generated undirected, unweighted connected graphs.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Output](#output)
- [Algorithm Details](#algorithm-details)
- [Stretch Goals](#stretch-goals)

---

## Overview

This project generates random connected graphs of increasing size, runs DFS and BFS on each, records average execution times over three trials per graph size, and produces visualizations comparing algorithm performance. Results are analyzed against the theoretical O(V + E) time complexity shared by both algorithms.

---

## Project Structure

```
graph_traversal/
├── graph.py          # Graph class (adjacency list representation)
├── generator.py      # Random connected graph generator
├── algorithms.py     # DFS and BFS implementations
├── visualizer.py     # Matplotlib chart generation
├── main.py           # Main runner: timing, output table, and plot calls
├── README.md         # Project documentation
└── report.docx       # Written report with analysis and visualizations
```

---

## Requirements

- Python 3.7 or higher
- matplotlib
- python-docx *(required only for report generation, not for running the program)*

Standard library modules used (no installation required): `random`, `time`, `collections`, `os`

---

## Installation

**1. Verify Python version**
```bash
python --version
```
Python 3.7 or higher is required.

**2. Check for required libraries**
```bash
pip show matplotlib
pip show python-docx
```

**3. Install any missing libraries**
```bash
pip install matplotlib
pip install python-docx
```

**4. Clone the repository**
```bash
git clone https://github.com/jsb58p/CS404-Graph_Traversal_Algorithms.git
cd CS404-Graph_Traversal_Algorithms
```

---

## Usage

**Run the full program**
```bash
python main.py
```
This will:
1. Run a sanity check on a small test graph
2. Generate random connected graphs for each node count in `[10, 50, 100, 250, 500, 750, 1000, 2500, 5000]`
3. Time DFS and BFS on each graph (3 trials per size, averaged)
4. Print a formatted execution time table to the terminal
5. Save two chart files: `execution_times.png` and `execution_times_bar.png`

**Test individual modules**
```bash
python graph.py        # Tests Graph class construction and methods
python generator.py    # Tests random connected graph generation
python algorithms.py   # Tests DFS and BFS traversal correctness
python visualizer.py   # Tests chart generation with dummy data
```
Each module contains an isolated `if __name__ == "__main__":` test block that runs only when the file is executed directly and is ignored on import.

---

## Modules

### `graph.py`
Defines the `Graph` class representing an undirected, unweighted graph as an adjacency list (dictionary of node → neighbor list).

| Method | Description |
|---|---|
| `__init__(num_nodes)` | Initializes nodes labeled 0 through num_nodes - 1 |
| `add_edge(node_a, node_b)` | Adds an undirected edge between two nodes |
| `get_neighbors(node)` | Returns the neighbor list for a given node |
| `get_all_nodes()` | Returns a list of all node labels |
| `__str__()` | Returns a readable string of the full adjacency list |

---

### `generator.py`
Provides `generate_random_connected_graph(num_nodes, extra_edges)`.

Connectivity is guaranteed by first building a random spanning tree (shuffle nodes, connect each to an already-connected node), then adding `extra_edges` additional random edges while skipping duplicates and self-loops.

---

### `algorithms.py`
Implements two traversal functions, each returning a list of nodes in visitation order.

| Function | Method | Data Structure | Time Complexity |
|---|---|---|---|
| `depth_first_search(graph, start_node)` | Iterative | Stack (list) | O(V + E) |
| `breadth_first_search(graph, start_node)` | Iterative | Queue (deque) | O(V + E) |

Both functions handle disconnected graphs gracefully by returning only nodes reachable from `start_node`.

---

### `visualizer.py`
Provides `plot_results(node_counts, dfs_times, bfs_times)`.

Generates and saves two charts to the working directory:
- `execution_times.png` — line chart of DFS vs BFS average execution time vs. node count
- `execution_times_bar.png` — grouped bar chart of the same data

---

### `main.py`
Main entry point. Orchestrates graph generation, timing, terminal output, and visualization.

- Graph density: `extra_edges = num_nodes` (moderate density)
- Trials per size: 3 (averaged)
- Timer: `time.perf_counter()`
- Traversal always starts from node `0`

---

## Output

**Terminal table (example)**
```
     Nodes |    DFS Avg Time |    BFS Avg Time
---------------------------------------------
        10 |        0.000006 |        0.000004
        50 |        0.000020 |        0.000015
       ...
      5000 |        0.002939 |        0.002014
```

**Generated files**
- `execution_times.png` — line chart
- `execution_times_bar.png` — grouped bar chart

---

## Algorithm Details

### Graph Representation
Graphs are represented as adjacency lists. Each node maps to a Python list of its neighbors. All graphs generated are undirected, unweighted, and connected.

### DFS
Explores as deep as possible along each branch before backtracking. Uses an explicit stack to avoid Python's recursion limit. Neighbor lists are reversed before pushing to maintain consistent left-to-right traversal order.

### BFS
Explores nodes level by level. Uses a `collections.deque` for O(1) enqueue and dequeue. Nodes are marked visited at enqueue time to prevent duplicate processing.

### Time Complexity
Both DFS and BFS operate in O(V + E) time, where V is the number of vertices and E is the number of edges. Empirical results confirm linear growth. BFS consistently shows lower absolute execution times due to lower constant-factor overhead in the deque implementation.

---

## Stretch Goals

The following enhancements are planned as future additions in the order they should be implemented:

1. **Dijkstra's Algorithm** — Add weighted edge support to `graph.py` and `generator.py`, implement Dijkstra's in `algorithms.py`, and extend timing and visualization to include a third algorithm. Note: Dijkstra's theoretical complexity is O((V + E) log V).
2. **Space Complexity Comparison** — Track peak stack and queue sizes during traversal to compare memory usage alongside execution time.
3. **Real-World Graph Testing** — Load and test on graph datasets from [SNAP (Stanford Network Analysis Project)](https://snap.stanford.edu/data/) to observe performance under real-world graph structures.

---

## Course Information

**Course:** CS404 — Algorithms and Complexity  
**Institution:** Undergraduate  
**Language:** Python 3  
**Editor:** Visual Studio Code
