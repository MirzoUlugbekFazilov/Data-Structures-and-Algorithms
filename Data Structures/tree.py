from collections import deque


# =========================
# TREE NODE
# =========================

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# =========================
# CREATE TREE
# =========================

root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)


# =========================
# PREORDER
# Root → Left → Right
# =========================

def preorder(root):

    if root is None:
        return

    print(root.data)

    preorder(root.left)
    preorder(root.right)


# =========================
# INORDER
# Left → Root → Right
# =========================

def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data)

    inorder(root.right)


# =========================
# POSTORDER
# Left → Right → Root
# =========================

def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.data)


# =========================
# LEVEL ORDER / BFS
# =========================

def level_order(root):

    if root is None:
        return

    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# =========================
# BST INSERT
# =========================

def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root


# =========================
# BST SEARCH
# =========================

def search(root, value):

    if root is None:
        return False

    if root.data == value:
        return True

    if value < root.data:
        return search(root.left, value)

    return search(root.right, value)


# =========================
# FIND MIN
# =========================

def find_min(root):

    if root is None:
        return None

    current = root

    while current.left:
        current = current.left

    return current.data


# =========================
# FIND MAX
# =========================

def find_max(root):

    if root is None:
        return None

    current = root

    while current.right:
        current = current.right

    return current.data


# =========================
# HEIGHT
# =========================

def height(root):

    if root is None:
        return 0

    left_height = height(root.left)

    right_height = height(root.right)

    return 1 + max(left_height, right_height)


# =========================
# COUNT NODES
# =========================

def count_nodes(root):

    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


# =========================
# EXAMPLES
# =========================

print("Preorder:")
preorder(root)

print("Inorder:")
inorder(root)

print("Postorder:")
postorder(root)

print("Level order:")
level_order(root)

print("Search 7:", search(root, 7))

print("Minimum:", find_min(root))

print("Maximum:", find_max(root))

print("Height:", height(root))

print("Number of nodes:", count_nodes(root))


# =========================================================
# COMPLEXITY
# =========================================================

# n = number of nodes
# h = height of tree
# w = maximum width of tree


# Tree Node
# Time:  O(1)
# Space: O(1)


# Preorder
# Time:  O(n)
# Space: O(h)


# Inorder
# Time:  O(n)
# Space: O(h)


# Postorder
# Time:  O(n)
# Space: O(h)


# Level Order / BFS
# Time:  O(n)
# Space: O(w)


# BST Insert
# Average Time: O(log n)
# Worst Time:   O(n)
# Space: O(h)


# BST Search
# Average Time: O(log n)
# Worst Time:   O(n)
# Space: O(h)


# Find Minimum
# Average Time: O(log n)
# Worst Time:   O(n)
# Space: O(1)


# Find Maximum
# Average Time: O(log n)
# Worst Time:   O(n)
# Space: O(1)


# Height
# Time:  O(n)
# Space: O(h)


# Count Nodes
# Time:  O(n)
# Space: O(h)


# =========================================================
# COMPLEXITY SUMMARY
# =========================================================

# Operation       | Average Time | Worst Time | Space
# -----------------------------------------------------
# Create Node     | O(1)         | O(1)       | O(1)
# Preorder        | O(n)         | O(n)       | O(h)
# Inorder         | O(n)         | O(n)       | O(h)
# Postorder       | O(n)         | O(n)       | O(h)
# Level Order     | O(n)         | O(n)       | O(w)
# BST Insert      | O(log n)     | O(n)       | O(h)
# BST Search      | O(log n)     | O(n)       | O(h)
# Find Min        | O(log n)     | O(n)       | O(1)
# Find Max        | O(log n)     | O(n)       | O(1)
# Height          | O(n)         | O(n)       | O(h)
# Count Nodes     | O(n)         | O(n)       | O(h)