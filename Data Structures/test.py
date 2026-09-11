from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def inorder(node):
#     if node is not None:
#         inorder(node.left)
#         print(node.data, end=" ")
#         inorder(node.right)

def postorder(root):

    if root is None:
        return 

    postorder(root.left)
    postorder(root.right)

    print(root.data, end=" ")


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
# CREATE BINARY TREE
# =========================

root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(3)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)


level_order(root)
