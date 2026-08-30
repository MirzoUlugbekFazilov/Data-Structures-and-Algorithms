#An array is a collection of elements stored in a sequence, 
#where each element can be accessed using an index.

#| Operation             |                          Time   |
#| --------------------- | ------------------------------- |
#| Access by index       |                          O(1)   |
#| Update by index       |                          O(1)   |
#| Search unsorted array |                          O(n)   |
#| Search sorted array   |      O(log n) + binary search   |
#| Append                |                          O(1)   |
#| Insert at beginning   |                          O(n)   |
#| Insert in middle      |                          O(n)   |
#| Delete from beginning |                          O(n)   |
#| Delete from middle    |                          O(n)   |
#| Delete from end       |                          O(1)   |
#| Traverse              |                          O(n)   |

# ==========================================
# ARRAYS / LISTS IN PYTHON — DSA BASICS
# ==========================================


# 1. CREATE AN ARRAY
numbers = [2, 5, 7, 9, 3]

print(numbers)


# 2. ACCESS AN ELEMENT
print(numbers[1])       # 5
print(numbers[0])       # 2
print(numbers[-1])      # 3 (last element)


# 3. UPDATE AN ELEMENT
numbers[1] = 100

print(numbers)
# [2, 100, 7, 9, 3]


# 4. GET THE LENGTH
print(len(numbers))


# 5. TRAVERSE / LOOP THROUGH ARRAY
for number in numbers:
    print(number)


# 6. LOOP USING INDEX
for i in range(len(numbers)):
    print(numbers[i])


# 7. ADD TO THE END — O(1) amortized
numbers.append(20)

print(numbers)


# 8. INSERT AT A SPECIFIC INDEX — O(n)
numbers.insert(2, 50)

print(numbers)


# 9. REMOVE BY VALUE — O(n)
numbers.remove(50)

print(numbers)


# 10. REMOVE BY INDEX — O(n) generally
removed = numbers.pop(2)

print(removed)
print(numbers)


# 11. REMOVE LAST ELEMENT — O(1)
numbers.pop()

print(numbers)


# 12. CHECK IF AN ELEMENT EXISTS — O(n)
if 7 in numbers:
    print("7 exists")


# 13. FIND THE INDEX OF AN ELEMENT — O(n)
index = numbers.index(7)

print(index)


# 14. COUNT HOW MANY TIMES AN ELEMENT APPEARS — O(n)
numbers.append(7)
numbers.append(7)

print(numbers.count(7))


# 15. FIND MAXIMUM — O(n)
print(max(numbers))


# 16. FIND MINIMUM — O(n)
print(min(numbers))


# 17. SUM — O(n)
print(sum(numbers))


# 18. SORT — O(n log n)
numbers.sort()

print(numbers)


# 19. SORT IN DESCENDING ORDER
numbers.sort(reverse=True)

print(numbers)


# 20. REVERSE — O(n)
numbers.reverse()

print(numbers)


# 21. CREATE A COPY
copy_numbers = numbers.copy()

print(copy_numbers)


# 22. CONCATENATE TWO ARRAYS
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)
# [1, 2, 3, 4, 5, 6]


# 23. SLICE AN ARRAY
numbers = [2, 5, 7, 9, 3]

print(numbers[1:4])
# [5, 7, 9]


# 24. FIRST THREE ELEMENTS
print(numbers[:3])


# 25. FROM INDEX 2 TO THE END
print(numbers[2:])


# 26. REVERSE USING SLICING
print(numbers[::-1])


# 27. DELETE USING DEL
del numbers[1]

print(numbers)


# 28. CLEAR THE ENTIRE ARRAY
numbers.clear()

print(numbers)
# []


# ==========================================
# IMPORTANT DSA OPERATIONS
# ==========================================

numbers = [2, 5, 7, 9, 3]


# FIND MAXIMUM MANUALLY
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Maximum:", maximum)


# FIND MINIMUM MANUALLY
minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("Minimum:", minimum)


# CALCULATE SUM MANUALLY
total = 0

for number in numbers:
    total += number

print("Sum:", total)


# LINEAR SEARCH
target = 9
found = False

for number in numbers:
    if number == target:
        found = True
        break

print("Found:", found)


# LINEAR SEARCH WITH INDEX
target = 9

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        break


# ==========================================
# TWO POINTERS
# ==========================================

numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:

    # Swap
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(numbers)
# [5, 4, 3, 2, 1]


# ==========================================
# PREFIX SUM
# ==========================================

numbers = [2, 4, 1, 5, 3]

prefix = [0]

for number in numbers:
    prefix.append(prefix[-1] + number)

print(prefix)
# [0, 2, 6, 7, 12, 15]


# ==========================================
# 2D ARRAY
# ==========================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])
# 2


# Traverse 2D array

for row in matrix:
    for number in row:
        print(number)


# ==========================================
# TIME COMPLEXITY CHEAT SHEET
# ==========================================

"""
Operation                         Complexity

numbers[i]                        O(1)
numbers[i] = value                O(1)

append()                          O(1) amortized

insert(i, value)                  O(n)

remove(value)                     O(n)

pop()                             O(1)

pop(i)                            O(n)

value in numbers                  O(n)

numbers.index(value)              O(n)

numbers.count(value)              O(n)

max(numbers)                      O(n)

min(numbers)                      O(n)

sum(numbers)                      O(n)

sort()                            O(n log n)

reverse()                         O(n)
"""