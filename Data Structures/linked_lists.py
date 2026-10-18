# ==========================================
# LINKED LIST — DSA BASICS IN PYTHON
# ==========================================


# ==========================================
# 1. CREATE A NODE
# ==========================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

print(node1.data)
# 10

print(node1.next)
# None


# ==========================================
# 2. CONNECT NODES
# ==========================================

node1.next = node2
node2.next = node3

# Now:

# 10 → 20 → 30 → None


print(node1.data)
print(node1.next.data)
print(node1.next.next.data)


# ==========================================
# 3. CREATE A LINKED LIST CLASS
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None


linked_list = LinkedList()

print(linked_list.head)
# None


# ==========================================
# 4. ADD TO THE BEGINNING
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

linked_list = LinkedList()

linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(10)

# 10 → 20 → 30 → None


# ==========================================
# 5. TRAVERSE / PRINT LINKED LIST
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def print_list(self):

        current = self.head

        while current is not None:

            print(current.data)

            current = current.next


linked_list = LinkedList()

linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(10)

linked_list.print_list() 


# ==========================================
# 6. INSERT AT THE END
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):

        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        # Find the last node
        while current.next is not None:
            current = current.next

        # Connect last node to new node
        current.next = new_node


linked_list = LinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

# 10 → 20 → 30 → None


# ==========================================
# 7. FIND LENGTH
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def length(self):

        count = 0

        current = self.head

        while current is not None:

            count += 1

            current = current.next

        return count


linked_list = LinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

print(linked_list.length())
# 3


# ==========================================
# 8. SEARCH FOR A VALUE
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def search(self, target):

        current = self.head

        while current is not None:

            if current.data == target:
                return True

            current = current.next

        return False


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

print(linked_list.search(20))
# True

print(linked_list.search(50))
# False


# ==========================================
# 9. FIND INDEX / POSITION
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def find_index(self, target):

        current = self.head
        index = 0

        while current is not None:

            if current.data == target:
                return index

            current = current.next
            index += 1

        return -1


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

print(linked_list.find_index(30))
# 2


# ==========================================
# 10. DELETE FROM BEGINNING
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def delete_first(self):

        if self.head is None:
            return

        self.head = self.head.next


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

# Before:
# 10 → 20 → 30

linked_list.delete_first()

# After:
# 20 → 30


# ==========================================
# 11. DELETE FROM END
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def delete_last(self):

        # Empty list
        if self.head is None:
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head

        # Find second-to-last node
        while current.next.next is not None:
            current = current.next

        # Remove last node
        current.next = None


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

# Before:
# 10 → 20 → 30

linked_list.delete_last()

# After:
# 10 → 20


# ==========================================
# 12. DELETE A SPECIFIC VALUE
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def delete_value(self, target):

        # Empty list
        if self.head is None:
            return

        # Target is the first node
        if self.head.data == target:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:

            if current.next.data == target:

                current.next = current.next.next

                return

            current = current.next


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

# Before:
# 10 → 20 → 30

linked_list.delete_value(20)

# After:
# 10 → 30


# ==========================================
# 13. INSERT AFTER A SPECIFIC VALUE
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_after(self, target, data):

        current = self.head

        while current is not None:

            if current.data == target:

                new_node = Node(data)

                new_node.next = current.next

                current.next = new_node

                return

            current = current.next


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

# Before:
# 10 → 20 → 30

linked_list.insert_after(20, 25)

# After:
# 10 → 20 → 25 → 30


# ==========================================
# 14. INSERT AT A SPECIFIC INDEX
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):

        new_node = Node(data)

        # Insert at beginning
        if index == 0:

            new_node.next = self.head
            self.head = new_node

            return

        current = self.head

        for i in range(index - 1):

            if current is None:
                return

            current = current.next

        if current is None:
            return

        new_node.next = current.next

        current.next = new_node


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

# Before:
# 10 → 20 → 30

linked_list.insert_at_index(1, 15)

# After:
# 10 → 15 → 20 → 30


# ==========================================
# 15. REVERSE A LINKED LIST
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):

        previous = None
        current = self.head

        while current is not None:

            next_node = current.next

            current.next = previous

            previous = current

            current = next_node

        self.head = previous


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)

# Before:
# 10 → 20 → 30 → None

linked_list.reverse()

# After:
# 30 → 20 → 10 → None


# ==========================================
# 16. FIND THE MIDDLE NODE
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def find_middle(self):

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

        return slow


linked_list = LinkedList()

linked_list.head = Node(10)
linked_list.head.next = Node(20)
linked_list.head.next.next = Node(30)
linked_list.head.next.next.next = Node(40)
linked_list.head.next.next.next.next = Node(50)

middle = linked_list.find_middle()

print(middle.data)
# 30


# ==========================================
# 17. DETECT A CYCLE
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def has_cycle(self):

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


linked_list = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

linked_list.head = node1

node1.next = node2
node2.next = node3

# Create cycle:
node3.next = node1

print(linked_list.has_cycle())
# True


# ==========================================
# IMPORTANT COMPLEXITIES
# ==========================================

"""
Operation                        Complexity

Access by index                  O(n)

Search                           O(n)

Insert at beginning              O(1)

Delete at beginning              O(1)

Insert at end                    O(n)
(without tail pointer)

Delete at end                    O(n)

Insert after known node          O(1)

Delete after known node          O(1)

Traverse                         O(n)

Find length                      O(n)

Reverse                          O(n)

Find middle                      O(n)

Detect cycle                     O(n)

Space                            O(n)
"""