# ==========================================
# STACKS — DSA BASICS IN PYTHON
# ==========================================


# ==========================================
# 1. CREATE A STACK
# ==========================================

stack = []

print(stack)
# []


# ==========================================
# 2. PUSH — ADD TO THE TOP
# ==========================================

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# [10, 20, 30]

# Top is 30


# ==========================================
# 3. PEEK — LOOK AT THE TOP
# ==========================================

print(stack[-1])

# 30

# IMPORTANT:
# Peek does NOT remove the element.


# ==========================================
# 4. POP — REMOVE FROM THE TOP
# ==========================================

value = stack.pop()

print(value)
# 30

print(stack)
# [10, 20]

# 30 was removed.


# ==========================================
# 5. CHECK IF STACK IS EMPTY
# ==========================================

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")


# Python shortcut:

if not stack:
    print("Stack is empty")


# ==========================================
# 6. GET STACK SIZE
# ==========================================

print(len(stack))


# ==========================================
# 7. PUSH MORE ELEMENTS
# ==========================================

stack.append(40)
stack.append(50)

print(stack)

# [10, 20, 40, 50]


# ==========================================
# 8. POP EVERYTHING
# ==========================================

while len(stack) > 0:

    print(stack.pop())


# Output:

# 50
# 40
# 20
# 10


# ==========================================
# 9. TRAVERSE A STACK
# ==========================================

stack = [10, 20, 30, 40]

for value in stack:
    print(value)


# ==========================================
# 10. SEARCH
# ==========================================

stack = [10, 20, 30, 40]

if 30 in stack:
    print("30 exists")


# ==========================================
# 11. REVERSE A STACK
# ==========================================

stack = [10, 20, 30, 40]

stack.reverse()

print(stack)

# [40, 30, 20, 10]


# ==========================================
# 12. CREATE A STACK CLASS
# ==========================================

class Stack:

    def __init__(self):
        self.stack = []

    # PUSH
    def push(self, value):
        self.stack.append(value)

    # POP
    def pop(self):

        if self.is_empty():
            return None

        return self.stack.pop()

    # PEEK
    def peek(self):

        if self.is_empty():
            return None

        return self.stack[-1]

    # CHECK EMPTY
    def is_empty(self):
        return len(self.stack) == 0

    # SIZE
    def size(self):
        return len(self.stack)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())
# 30

print(stack.pop())
# 30

print(stack.peek())
# 20

print(stack.size())
# 2


# ==========================================
# 13. STACK USING A LINKED LIST
# ==========================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:

    def __init__(self):
        self.top = None

    def push(self, data):

        new_node = Node(data)

        new_node.next = self.top

        self.top = new_node

    def pop(self):

        if self.top is None:
            return None

        value = self.top.data

        self.top = self.top.next

        return value

    def peek(self):

        if self.top is None:
            return None

        return self.top.data

    def is_empty(self):

        return self.top is None


stack = LinkedStack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())
# 30

print(stack.pop())
# 30

print(stack.peek())
# 20


# ==========================================
# 14. STACK — LIFO
# ==========================================

stack = []

stack.append("A")
stack.append("B")
stack.append("C")

# Stack:

# TOP
#  C
#  B
#  A

print(stack.pop())
# C

print(stack.pop())
# B

print(stack.pop())
# A


# ==========================================
# 15. CHECKING PARENTHESES
# ==========================================

def is_valid_parentheses(string):

    stack = []

    for char in string:

        if char == "(":
            stack.append(char)

        elif char == ")":

            if not stack:
                return False

            stack.pop()

    return len(stack) == 0


print(is_valid_parentheses("((()))"))
# True

print(is_valid_parentheses("(()"))
# False

print(is_valid_parentheses("())"))
# False


# ==========================================
# 16. VALID PARENTHESES
# WITH (), [], {}
# ==========================================

def is_valid(string):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in string:

        if char in "([{":

            stack.append(char)

        elif char in ")]}":

            if not stack:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


print(is_valid("()[]{}"))
# True

print(is_valid("([{}])"))
# True

print(is_valid("([)]"))
# False


# ==========================================
# 17. REVERSE A STRING USING A STACK
# ==========================================

string = "hello"

stack = []

for char in string:
    stack.append(char)

reversed_string = ""

while stack:
    reversed_string += stack.pop()

print(reversed_string)

# olleh


# ==========================================
# 18. DECIMAL → BINARY USING A STACK
# ==========================================

number = 13

stack = []

while number > 0:

    remainder = number % 2

    stack.append(remainder)

    number = number // 2


while stack:

    print(stack.pop(), end="")


# 1101


# ==========================================
# TIME COMPLEXITY
# ==========================================

"""
Operation                     Complexity

Push                          O(1)

Pop                           O(1)

Peek                          O(1)

is_empty                      O(1)

Size                          O(1)

Search                        O(n)

Traverse                      O(n)
"""