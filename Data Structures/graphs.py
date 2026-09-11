from collections import deque


# ==========================================================
# GRAPH REPRESENTATION
# ==========================================================

# Adjacency List
#
# A -- B
# |    |
# C -- D
#
# Each key is a node.
# Each value contains its neighbouring nodes.

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


# ==========================================================
# BFS - BREADTH-FIRST SEARCH
# ==========================================================

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:

        node = queue.popleft()

        print(node, end=" ")

        for neighbour in graph[node]:

            if neighbour not in visited:

                visited.add(neighbour)
                queue.append(neighbour)


# ==========================================================
# DFS - DEPTH-FIRST SEARCH
# ==========================================================

def dfs(graph, node, visited=None):

    if visited is None:
        visited = set()

    visited.add(node)

    print(node, end=" ")

    for neighbour in graph[node]:

        if neighbour not in visited:

            dfs(graph, neighbour, visited)


# ==========================================================
# CREATE GRAPH
# ==========================================================

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


# ==========================================================
# RUN BFS
# ==========================================================

print("BFS:")
bfs(graph, "A")


# ==========================================================
# RUN DFS
# ==========================================================

print("\nDFS:")
dfs(graph, "A")


# ==========================================================
# COMPLEXITY
# ==========================================================

# Operation             | Time       | Space
# ------------------------------------------------
# Create Graph          | O(V + E)   | O(V + E)
# BFS                   | O(V + E)   | O(V)
# DFS                   | O(V + E)   | O(V)
#
# V = Number of vertices (nodes)
# E = Number of edges
#
# BFS uses a queue.
# DFS uses recursion (call stack).
#
# Adjacency List:
# Space = O(V + E)