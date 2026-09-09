# ==========================================
# PRIORITY QUEUE — DSA BASICS IN PYTHON
# ==========================================


# ==========================================
# 1. CREATE A PRIORITY QUEUE
# ==========================================

import heapq

priority_queue = []

print(priority_queue)

# []


# ==========================================
# 2. INSERT / PUSH
# ==========================================

heapq.heappush(priority_queue, 5)
heapq.heappush(priority_queue, 2)
heapq.heappush(priority_queue, 8)
heapq.heappush(priority_queue, 1)

print(priority_queue)


# ==========================================
# 3. REMOVE / POP
# ==========================================

value = heapq.heappop(priority_queue)

print(value)

# 1

# The smallest value has the highest priority
# in Python's normal heap.


# ==========================================
# 4. PEEK
# ==========================================

print(priority_queue[0])

# This shows the highest-priority element
# without removing it.


# ==========================================
# 5. INSERT MORE
# ==========================================

heapq.heappush(priority_queue, 3)
heapq.heappush(priority_queue, 10)

print(priority_queue)


# ==========================================
# 6. REMOVE EVERYTHING
# ==========================================

while priority_queue:

    print(heapq.heappop(priority_queue))


# Output will be in priority order:
#
# smallest
# next smallest
# next smallest
# ...


# ==========================================
# 7. CHECK IF EMPTY
# ==========================================

if not priority_queue:
    print("Priority queue is empty")


# ==========================================
# 8. GET SIZE
# ==========================================

print(len(priority_queue))


# ==========================================
# 9. PRIORITY + DATA
# ==========================================

priority_queue = []

heapq.heappush(priority_queue, (3, "Task C"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (2, "Task B"))

print(priority_queue)


# Remove highest-priority task

print(heapq.heappop(priority_queue))

# (1, 'Task A')


# ==========================================
# 10. TASK EXAMPLE
# ==========================================

tasks = []

heapq.heappush(tasks, (3, "Do homework"))
heapq.heappush(tasks, (1, "Emergency"))
heapq.heappush(tasks, (2, "Go to gym"))

while tasks:

    priority, task = heapq.heappop(tasks)

    print(priority, task)


# Output:
#
# 1 Emergency
# 2 Go to gym
# 3 Do homework


# ==========================================
# 11. MAX-HEAP
# ==========================================

numbers = []

heapq.heappush(numbers, -10)
heapq.heappush(numbers, -30)
heapq.heappush(numbers, -20)

largest = -heapq.heappop(numbers)

print(largest)

# 30


# Python's heapq is a MIN-HEAP.
#
# We use negative numbers to simulate
# a MAX-HEAP.


# ==========================================
# 12. BUILD A HEAP
# ==========================================

numbers = [5, 2, 8, 1, 3]

heapq.heapify(numbers)

print(numbers)

# Now numbers is a valid min-heap.


# ==========================================
# 13. POP FROM THE HEAP
# ==========================================

print(heapq.heappop(numbers))


# ==========================================
# 14. PUSH + POP
# ==========================================

numbers = [2, 4, 6]

heapq.heapify(numbers)

result = heapq.heappushpop(numbers, 1)

print(result)


# ==========================================
# 15. REPLACE ROOT
# ==========================================

numbers = [2, 4, 6]

heapq.heapify(numbers)

result = heapq.heapreplace(numbers, 5)

print(result)
print(numbers)


# ==========================================
# 16. FIND K SMALLEST ELEMENTS
# ==========================================

numbers = [8, 2, 5, 1, 9, 3]

print(heapq.nsmallest(3, numbers))

# [1, 2, 3]


# ==========================================
# 17. FIND K LARGEST ELEMENTS
# ==========================================

print(heapq.nlargest(3, numbers))

# [9, 8, 5]


# ==========================================
# 18. PRIORITY QUEUE CLASS
# ==========================================

class PriorityQueue:

    def __init__(self):
        self.queue = []

    def push(self, priority, data):

        heapq.heappush(
            self.queue,
            (priority, data)
        )

    def pop(self):

        if not self.queue:
            return None

        return heapq.heappop(self.queue)

    def peek(self):

        if not self.queue:
            return None

        return self.queue[0]

    def is_empty(self):

        return len(self.queue) == 0

    def size(self):

        return len(self.queue)


pq = PriorityQueue()

pq.push(3, "Task C")
pq.push(1, "Task A")
pq.push(2, "Task B")

print(pq.peek())
# (1, 'Task A')

print(pq.pop())
# (1, 'Task A')

print(pq.pop())
# (2, 'Task B')


# ==========================================
# TIME COMPLEXITY
# ==========================================

"""
Operation                     Complexity

Peek                          O(1)

Push                          O(log n)

Pop                           O(log n)

Build heap                    O(n)

Search                        O(n)

Get size                      O(1)
"""