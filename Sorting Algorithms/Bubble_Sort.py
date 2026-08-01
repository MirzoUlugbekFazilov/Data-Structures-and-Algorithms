# Best Complexity: O(n)
# Average Complexity: O(n^2)
# Worst Complexity: O(n^2)


# Best Case — O(n)
numbers = [1, 2, 3, 4, 5]  # already sorted

is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            is_sorted = False

print("Best case result:", numbers)



# Average Case — O(n^2)
numbers = [5, 1, 4, 2, 3]

is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            is_sorted = False

print("Average case result:", numbers)



# ❌ Worst Case — O(n^2)
numbers = [5, 4, 3, 2, 1]

is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            is_sorted = False

print("Worst case result:", numbers)