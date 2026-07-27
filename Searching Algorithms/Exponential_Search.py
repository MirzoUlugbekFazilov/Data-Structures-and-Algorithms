# Exponential Search

# Best Complexity: O(1)
# Average Complexity: O(log n)
# Worst Complexity: O(log n)


# Best Case — O(1)
numbers = [2, 4, 6, 8, 10]
finder = 2

if numbers[0] == finder:
    print("Found at index:", 0)


# Average Case — O(log n)
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18]
finder = 14

i = 1
n = len(numbers)

while i < n and numbers[i] <= finder:
    i *= 2

left = i // 2
right = min(i, n - 1)

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == finder:
        print("Found at index:", mid)
        break
    elif numbers[mid] < finder:
        left = mid + 1
    else:
        right = mid - 1


# ❌ Worst Case — O(log n)
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18]
finder = 15  # not in list

i = 1
n = len(numbers)

while i < n and numbers[i] <= finder:
    i *= 2

left = i // 2
right = min(i, n - 1)

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == finder:
        print("Found at index:", mid)
        break
    elif numbers[mid] < finder:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Not found")