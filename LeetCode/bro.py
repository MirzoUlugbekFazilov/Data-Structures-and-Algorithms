class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def add_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

bro = LinkedList(Node(5, Node(3, Node(6, Node(7)))))

cur = bro.head
while cur:
    print(cur.val, end="  ")
    cur = cur.next

bro.add_beginning(4)

cur = bro.head
while cur:
    print(cur.val, end=" ")
    cur = cur.next
