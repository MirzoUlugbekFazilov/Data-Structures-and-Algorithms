# Define a node of the tree
class Node:
    def __init__(self, value):
        self.value = value      # store the number
        self.left = None        # left child (smaller values)
        self.right = None       # right child (bigger values)


def insert(root, value):
    # If tree is empty, create a new node
    if root is None:
        return Node(value)

    # If value is smaller, go left
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        # If value is bigger or equal, go right
        root.right = insert(root.right, value)

    return root


# Traverse the tree in sorted order (Left → Root → Right)
def inorder(root, result):
    if root is not None:
        inorder(root.left, result)     # visit left subtree
        result.append(root.value)      # visit current node
        inorder(root.right, result)    # visit right subtree


# Main function to sort array
def tree_sort(arr):
    root = None

    # Step 1: Build the tree
    for num in arr:
        root = insert(root, num)

    # Step 2: Get sorted values
    result = []
    inorder(root, result)

    return result


# Example
arr = [5, 2, 8, 1, 3]
print(tree_sort(arr))   # Output: [1, 2, 3, 5, 8]