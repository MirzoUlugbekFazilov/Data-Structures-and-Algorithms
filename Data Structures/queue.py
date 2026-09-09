# ==========================================
# QUEUES — DSA BASICS IN PYTHON
# ==========================================


# ==========================================
# 1. CREATE A QUEUE
# ==========================================

queue = []

print(queue)

# []


# ==========================================
# 2. ENQUEUE — ADD TO THE BACK
# ==========================================

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# [10, 20, 30]

# Front → 10
# Back  → 30


# ==========================================
# 3. DEQUEUE — REMOVE FROM THE FRONT
# ==========================================

value = queue.pop(0)

print(value)

# 10

print(queue)

# [20, 30]


# ==========================================
# 4. PEEK — LOOK AT THE FRONT
# ==========================================

print(queue[0])

# 20

# IMPORTANT:
# Peek does NOT remove the element.


# ==========================================
# 5. CHECK IF QUEUE IS EMPTY
# ==========================================

if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")


# ==========================================
# 6. GET QUEUE SIZE
# ==========================================

print(len(queue))


# ==========================================
# 7. ADD MORE ELEMENTS
# ==========================================

queue.append(40)
queue.append(50)

print(queue)

# [20, 30, 40, 50]


# ==========================================
# 8. REMOVE EVERYTHING
# ==========================================

while queue:

    print(queue.pop(0))


# Output:
# 20
# 30
# 40
# 50


# ==========================================
# 9. TRAVERSE A QUEUE
# ==========================================

queue = [10, 20, 30, 40]

for value in queue:
    print(value)


# ==========================================
# 10. SEARCH
# ==========================================

queue = [10, 20, 30, 40]

if 30 in queue:
    print("30 exists")


# ==========================================
# 11. QUEUE USING collections.deque
# ==========================================

from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# deque([10, 20, 30])


# ENQUEUE
queue.append(40)

# DEQUEUE
print(queue.popleft())

# 10

# PEEK
print(queue[0])

# 20


# ==========================================
# 12. CREATE A QUEUE CLASS
# ==========================================

from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()

    # ENQUEUE
    def enqueue(self, value):
        self.queue.append(value)

    # DEQUEUE
    def dequeue(self):

        if self.is_empty():
            return None

        return self.queue.popleft()

    # PEEK
    def peek(self):

        if self.is_empty():
            return None

        return self.queue[0]

    # CHECK EMPTY
    def is_empty(self):
        return len(self.queue) == 0

    # SIZE
    def size(self):
        return len(self.queue)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.peek())
# 10

print(queue.dequeue())
# 10

print(queue.peek())
# 20

print(queue.size())
# 2


# ==========================================
# 13. QUEUE USING A LINKED LIST
# ==========================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):

        new_node = Node(data)

        # Empty queue
        if self.rear is None:

            self.front = new_node
            self.rear = new_node

            return

        # Add to the rear
        self.rear.next = new_node

        self.rear = new_node

    def dequeue(self):

        # Empty queue
        if self.front is None:
            return None

        value = self.front.data

        self.front = self.front.next

        # Queue became empty
        if self.front is None:
            self.rear = None

        return value

    def peek(self):

        if self.front is None:
            return None

        return self.front.data

    def is_empty(self):

        return self.front is None


queue = LinkedQueue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.peek())
# 10

print(queue.dequeue())
# 10

print(queue.dequeue())
# 20

print(queue.peek())
# 30


# ==========================================
# 14. FIFO
# ==========================================

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

# FRONT
#   ↓
# A  B  C
#       ↑
#      BACK

print(queue.popleft())
# A

print(queue.popleft())
# B

print(queue.popleft())
# C


# ==========================================
# 15. QUEUE WITH MAXIMUM SIZE
# ==========================================

queue = deque(maxlen=3)

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# deque([10, 20, 30])

queue.append(40)

print(queue)

# deque([20, 30, 40])

# 10 was automatically removed.


# ==========================================
# 16. ROTATING QUEUE
# ==========================================

queue = deque([1, 2, 3, 4, 5])

queue.rotate(1)

print(queue)

# deque([5, 1, 2, 3, 4])


# ==========================================
# 17. PRIORITY QUEUE
# ==========================================

import heapq

queue = []

heapq.heappush(queue, (3, "Task C"))
heapq.heappush(queue, (1, "Task A"))
heapq.heappush(queue, (2, "Task B"))

print(heapq.heappop(queue))
# (1, 'Task A')

print(heapq.heappop(queue))
# (2, 'Task B')

print(heapq.heappop(queue))
# (3, 'Task C')


# ==========================================
# 18. BREADTH-FIRST SEARCH (BFS)
# ==========================================

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

queue = deque(["A"])

visited = set()

while queue:

    node = queue.popleft()

    if node in visited:
        continue

    visited.add(node)

    print(node)

    for neighbour in graph[node]:
        queue.append(neighbour)


# ==========================================
# TIME COMPLEXITY
# ==========================================

"""
Operation                        Complexity

Enqueue                          O(1)

Dequeue                          O(1)

Peek                             O(1)

is_empty                         O(1)

Size                             O(1)

Search                           O(n)

Traverse                         O(n)
"""