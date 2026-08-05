# Best Complexity: O(n + range)
# Average Complexity: O(n + range)
# Worst Complexity: O(n + range)


# Best Case — small range (efficient)
numbers = [3, 1, 2, 3]

min_val = min(numbers)
max_val = max(numbers)

size = max_val - min_val + 1
holes = []

for i in range(size):
    holes.append([])

for num in numbers:
    holes[num - min_val].append(num)

sorted_numbers = []
for hole in holes:
    sorted_numbers.extend(hole)

print(sorted_numbers)  # [1, 2, 3, 3]



numbers = [4, 1, 2]

min_val = min(numbers)
max_val = max(numbers)

size = max_val - min_val + 1
holes = []

for i in range(size):
    holes.append([])

for num in numbers:
    holes[num - min_val].append(num)

sorted_numbers = []
for hole in holes:
    sorted_numbers.extend(hole)

print(sorted_numbers)  # [1, 2, 4]



# ❌ Worst Case — large range (inefficient)
numbers = [1, 1000000]

min_val = min(numbers)
max_val = max(numbers)

size = max_val - min_val + 1
holes = []

for i in range(size):
    holes.append([])

for num in numbers:
    holes[num - min_val].append(num)

sorted_numbers = []
for hole in holes:
    sorted_numbers.extend(hole)

print(sorted_numbers)  # works, but wastes huge memory