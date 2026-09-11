```python
from collections import deque
import heapq


# =========================================================
# BINARY TREE NODE
# =========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# =========================================================
# CREATE BINARY TREE
# =========================================================

root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)


# =========================================================
# TREE TRAVERSALS
# =========================================================

# ---------------------------------------------------------
# PREORDER
# Root → Left → Right
# ---------------------------------------------------------

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# ---------------------------------------------------------
# INORDER
# Left → Root → Right
# ---------------------------------------------------------

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# ---------------------------------------------------------
# POSTORDER
# Left → Right → Root
# ---------------------------------------------------------

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# ---------------------------------------------------------
# LEVEL ORDER / BFS
# Top → Bottom, Left → Right
# ---------------------------------------------------------

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# =========================================================
# BINARY SEARCH TREE (BST)
# =========================================================

# BST rule:
#
# Left subtree  <  Root  <  Right subtree
#
# Example:
#
#         10
#        /  \
#       5    15
#      / \   / \
#     2   7 12 20


# ---------------------------------------------------------
# BST INSERT
# ---------------------------------------------------------

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# ---------------------------------------------------------
# BST SEARCH
# ---------------------------------------------------------

def search(root, value):
    if root is None:
        return False

    if root.data == value:
        return True

    if value < root.data:
        return search(root.left, value)

    return search(root.right, value)


# ---------------------------------------------------------
# FIND MINIMUM IN BST
# ---------------------------------------------------------

def find_min(root):
    if root is None:
        return None

    current = root

    while current.left:
        current = current.left

    return current.data


# ---------------------------------------------------------
# FIND MAXIMUM IN BST
# ---------------------------------------------------------

def find_max(root):
    if root is None:
        return None

    current = root

    while current.right:
        current = current.right

    return current.data


# =========================================================
# GENERAL BINARY TREE OPERATIONS
# =========================================================

# ---------------------------------------------------------
# HEIGHT
#
# This version counts the number of nodes on the
# longest path from the root to a leaf.
#
# Empty tree = 0
# One-node tree = 1
# ---------------------------------------------------------

def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


# ---------------------------------------------------------
# COUNT NODES
# ---------------------------------------------------------

def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


# =========================================================
# MIN HEAP
# =========================================================

# Python's heapq is a MIN HEAP by default.
#
# Smallest value is always at the top.
#
# Example:
#
#          2
#        /   \
#       5     7
#      / \
#     10  8
#
# The heap guarantees:
#
# Parent <= Children


min_heap = []

# Insert values
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 7)


# ---------------------------------------------------------
# MIN HEAP PEEK
# See the smallest value without removing it.
# ---------------------------------------------------------

def min_heap_peek(heap):
    if not heap:
        return None

    return heap[0]


# ---------------------------------------------------------
# MIN HEAP EXTRACT
# Remove and return the smallest value.
# ---------------------------------------------------------

def min_heap_extract(heap):
    if not heap:
        return None

    return heapq.heappop(heap)


# =========================================================
# MAX HEAP
# =========================================================

# Python does not have a built-in max heap.
#
# We can simulate one by storing negative values.
#
# Example:
#
# Value:       10
# Stored as:  -10
#
# The smallest negative number represents
# the largest original value.


max_heap = []

heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -7)


# ---------------------------------------------------------
# MAX HEAP PEEK
# See the largest value without removing it.
# ---------------------------------------------------------

def max_heap_peek(heap):
    if not heap:
        return None

    return -heap[0]


# ---------------------------------------------------------
# MAX HEAP EXTRACT
# Remove and return the largest value.
# ---------------------------------------------------------

def max_heap_extract(heap):
    if not heap:
        return None

    return -heapq.heappop(heap)


# =========================================================
# TRIE
# =========================================================

# A Trie is a tree-like data structure used mainly
# for storing and searching strings.
#
# Example words:
#
# cat
# car
# can
#
# Trie:
#
#          root
#           |
#           c
#           |
#           a
#         / | \
#        t  r  n
#
# Each path represents a word.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


# ---------------------------------------------------------
# TRIE INSERT
# ---------------------------------------------------------

def insert_word(self, word):
    current = self.root

    for character in word:
        if character not in current.children:
            current.children[character] = TrieNode()

        current = current.children[character]

    current.is_end = True


# Attach the method to the Trie class
Trie.insert = insert_word


# ---------------------------------------------------------
# TRIE SEARCH
# ---------------------------------------------------------

def search_word(self, word):
    current = self.root

    for character in word:
        if character not in current.children:
            return False

        current = current.children[character]

    return current.is_end


Trie.search = search_word


# ---------------------------------------------------------
# TRIE STARTS WITH
#
# Checks whether any stored word starts with a prefix.
# ---------------------------------------------------------

def starts_with(self, prefix):
    current = self.root

    for character in prefix:
        if character not in current.children:
            return False

        current = current.children[character]

    return True


Trie.starts_with = starts_with


# =========================================================
# EXAMPLES
# =========================================================

print("\n========== BINARY TREE ==========")

print("Preorder:")
preorder(root)
print()

print("Inorder:")
inorder(root)
print()

print("Postorder:")
postorder(root)
print()

print("Level order / BFS:")
level_order(root)
print()


print("\n========== BST ==========")

print("Search 7:", search(root, 7))
print("Search 100:", search(root, 100))

print("Minimum:", find_min(root))
print("Maximum:", find_max(root))


print("\n========== TREE INFORMATION ==========")

print("Height:", height(root))
print("Number of nodes:", count_nodes(root))


print("\n========== MIN HEAP ==========")

print("Min heap:", min_heap)
print("Minimum:", min_heap_peek(min_heap))
print("Extract minimum:", min_heap_extract(min_heap))
print("After extraction:", min_heap)


print("\n========== MAX HEAP ==========")

print("Max heap:", max_heap)
print("Maximum:", max_heap_peek(max_heap))
print("Extract maximum:", max_heap_extract(max_heap))
print("After extraction:", max_heap)


print("\n========== TRIE ==========")

trie = Trie()

trie.insert("cat")
trie.insert("car")
trie.insert("can")
trie.insert("dog")

print("Search 'cat':", trie.search("cat"))
print("Search 'cap':", trie.search("cap"))

print("Starts with 'ca':", trie.starts_with("ca"))
print("Starts with 'do':", trie.starts_with("do"))
print("Starts with 'xy':", trie.starts_with("xy"))


# =========================================================
# COMPLEXITY
# =========================================================

# n = number of nodes
# h = height of tree
# w = maximum width of tree
# L = length of a word


# ---------------------------------------------------------
# BINARY TREE
# ---------------------------------------------------------

# Create Node
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


# Height
# Time:  O(n)
# Space: O(h)


# Count Nodes
# Time:  O(n)
# Space: O(h)


# ---------------------------------------------------------
# BINARY SEARCH TREE (BST)
# ---------------------------------------------------------

# Insert
# Average Time: O(log n)
# Worst Time:   O(n)
# Space: O(h)


# Search
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


# ---------------------------------------------------------
# MIN HEAP / MAX HEAP
# ---------------------------------------------------------

# Peek
# Time:  O(1)
# Space: O(1)


# Insert / Push
# Time:  O(log n)
# Space: O(1) auxiliary


# Extract min / max
# Time:  O(log n)
# Space: O(1) auxiliary


# Build heap from n elements
# Time:  O(n)


# ---------------------------------------------------------
# TRIE
# ---------------------------------------------------------

# Insert word
# Time:  O(L)
# Space: O(L) for new characters


# Search word
# Time:  O(L)
# Space: O(1) auxiliary


# Prefix search
# Time:  O(L)
# Space: O(1) auxiliary


# =========================================================
# COMPLEXITY SUMMARY
# =========================================================

#| Operation             | Complexity |
#| --------------------- | ---------- |
#| Create Node           | O(1)       |
#| Preorder              | O(n)       |
#| Inorder               | O(n)       |
#| Postorder             | O(n)       |
#| Level Order / BFS     | O(n)       |
#| Height                | O(n)       |
#| Count Nodes           | O(n)       |
#| --------------------- | ---------- |
#| BST Insert            | O(log n)   |
#| BST Search            | O(log n)   |
#| BST Find Min          | O(log n)   |
#| BST Find Max          | O(log n)   |
#| --------------------- | ---------- |
#| Heap Peek             | O(1)       |
#| Heap Insert           | O(log n)   |
#| Heap Extract          | O(log n)   |
#| Build Heap            | O(n)       |
#| --------------------- | ---------- |
#| Trie Insert           | O(L)       |
#| Trie Search           | O(L)       |
#| Trie Prefix Search    | O(L)       |