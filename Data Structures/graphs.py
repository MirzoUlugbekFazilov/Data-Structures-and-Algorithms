from collections import deque


# ==========================================================
# GRAPH REPRESENTATION
# ==========================================================

# Adjacency List
#
#       A
#      / \
#     B   C
#     \   /
#       D
#
# Each key = node
# Each value = neighbouring nodes

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


# ==========================================================
# ADJACENCY MATRIX
# ==========================================================

# Same graph represented as a matrix.
#
#     A B C D
# A   0 1 1 0
# B   1 0 0 1
# C   1 0 0 1
# D   0 1 1 0

matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]


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
# CONNECTED COMPONENTS
# ==========================================================

def connected_components(graph):

    visited = set()
    count = 0

    for node in graph:

        if node not in visited:

            count += 1

            # BFS from this node
            queue = deque([node])
            visited.add(node)

            while queue:

                current = queue.popleft()

                for neighbour in graph[current]:

                    if neighbour not in visited:

                        visited.add(neighbour)
                        queue.append(neighbour)

    return count


# ==========================================================
# UNDIRECTED CYCLE DETECTION
# ==========================================================

def has_cycle_undirected(graph):

    visited = set()

    def dfs(node, parent):

        visited.add(node)

        for neighbour in graph[node]:

            if neighbour not in visited:

                if dfs(neighbour, node):
                    return True

            elif neighbour != parent:

                return True

        return False

    for node in graph:

        if node not in visited:

            if dfs(node, None):
                return True

    return False


# ==========================================================
# DIRECTED CYCLE DETECTION
# ==========================================================

def has_cycle_directed(graph):

    visited = set()
    current_path = set()

    def dfs(node):

        visited.add(node)
        current_path.add(node)

        for neighbour in graph[node]:

            if neighbour not in visited:

                if dfs(neighbour):
                    return True

            elif neighbour in current_path:

                return True

        current_path.remove(node)

        return False

    for node in graph:

        if node not in visited:

            if dfs(node):
                return True

    return False


# ==========================================================
# DIJKSTRA - SHORTEST PATH
# ==========================================================

import heapq


def dijkstra(graph, start):

    distances = {}

    for node in graph:
        distances[node] = float("inf")

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:

                distances[neighbour] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    return distances


# Example weighted graph for Dijkstra

weighted_graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8)],
    "D": [("B", 5), ("C", 8)]
}


# ==========================================================
# TOPOLOGICAL SORT - KAHN'S ALGORITHM
# ==========================================================

def topological_sort(graph):

    indegree = {}

    for node in graph:
        indegree[node] = 0

    # Calculate indegree
    for node in graph:

        for neighbour in graph[node]:

            indegree[neighbour] += 1

    # Nodes with no incoming edges
    queue = deque()

    for node in indegree:

        if indegree[node] == 0:

            queue.append(node)

    order = []

    while queue:

        node = queue.popleft()

        order.append(node)

        for neighbour in graph[node]:

            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:

                queue.append(neighbour)

    # If not all nodes are processed,
    # the graph contains a cycle.

    if len(order) != len(graph):

        return []

    return order


# Example DAG

dag = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}


# ==========================================================
# UNION-FIND / DISJOINT SET
# ==========================================================

class UnionFind:

    def __init__(self, n):

        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:

            return False

        if self.rank[root_x] < self.rank[root_y]:

            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:

            self.parent[root_y] = root_x

        else:

            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


# ==========================================================
# KRUSKAL'S ALGORITHM - MINIMUM SPANNING TREE
# ==========================================================

def kruskal(n, edges):

    edges.sort(key=lambda edge: edge[2])

    uf = UnionFind(n)

    mst = []
    total_weight = 0

    for u, v, weight in edges:

        if uf.union(u, v):

            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# ==========================================================
# PRIM'S ALGORITHM - MINIMUM SPANNING TREE
# ==========================================================

def prim(graph, start):

    visited = set()
    min_heap = [(0, start)]

    total_weight = 0

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        total_weight += weight

        for neighbour, edge_weight in graph[node]:

            if neighbour not in visited:

                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbour)
                )

    return total_weight


# ==========================================================
# EXAMPLES
# ==========================================================

print("BFS:")
bfs(graph, "A")

print("\n\nDFS:")
dfs(graph, "A")

print("\n\nConnected Components:")
print(connected_components(graph))

print("\nUndirected Cycle:")
print(has_cycle_undirected(graph))

print("\nDijkstra:")
print(dijkstra(weighted_graph, "A"))

print("\nTopological Sort:")
print(topological_sort(dag))

print("\nUnion-Find:")

uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)

print(uf.find(0))
print(uf.find(2))

print("\nKruskal:")

edges = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, 1),
    (1, 3, 5),
    (2, 3, 8)
]

print(kruskal(4, edges))

print("\nPrim:")
print(prim(weighted_graph, "A"))


# ==========================================================
# COMPLEXITY
# ==========================================================

# Operation                  | Time              | Space
# ----------------------------------------------------------
# Adjacency List             | O(V + E)          | O(V + E)
# Adjacency Matrix            | O(V²)             | O(V²)
#
# BFS                         | O(V + E)          | O(V)
# DFS                         | O(V + E)          | O(V)
#
# Connected Components        | O(V + E)          | O(V)
#
# Undirected Cycle Detection  | O(V + E)          | O(V)
# Directed Cycle Detection    | O(V + E)          | O(V)
#
# Dijkstra (Heap)             | O((V + E)log V)   | O(V + E)
#
# Topological Sort            | O(V + E)          | O(V)
#
# Union-Find                  | O(α(V))*          | O(V)
#
# Kruskal                     | O(E log E)        | O(V + E)
#
# Prim (Heap)                 | O((V + E)log V)   | O(V + E)
#
# V = Number of vertices
# E = Number of edges
#
# * α(V) is the inverse Ackermann function.
#   It grows extremely slowly and is effectively O(1)
#   for practical input sizes.
#
# Important:
# BFS and DFS are O(V + E) because they can visit
# every vertex and every edge.