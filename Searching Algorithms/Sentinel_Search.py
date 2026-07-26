# Best Complexity: O(1)
# Average Complexity: O(n)
# Worst Complexity: O(n)

# Best Case — O(1)
numbers = [7, 2, 3, 4, 5]
finder = 7

last = numbers[-1]
numbers[-1] = finder  # sentinel

i = 0
while numbers[i] != finder:
    i += 1

numbers[-1] = last  # restore

if i < len(numbers) - 1 or last == finder:
    print("Found at index:", i)
else:
    print("Not found")


# Average Case — O(n)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
finder = 6

last = numbers[-1]
numbers[-1] = finder

i = 0
while numbers[i] != finder:
    i += 1

numbers[-1] = last

if i < len(numbers) - 1 or last == finder:
    print("Found at index:", i)
else:
    print("Not found")


# ❌ Worst Case — O(n)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
finder = 100  # not in list

last = numbers[-1]
numbers[-1] = finder

i = 0
while numbers[i] != finder:
    i += 1

numbers[-1] = last

if i < len(numbers) - 1 or last == finder:
    print("Found at index:", i)
else:
    print("Not found") 