# Best Complexity: O(1)
# Average Complexity: O(log n)
# Worst Complexity: O(log n)


# Best Case — O(1)
numbers = [1, 2, 3, 4, 5]
finder = 3

# left, right = 0, len(numbers) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == finder:
#         print("Found at index:", mid)
#         break
#     elif numbers[mid] > finder:
#         right = mid - 1
#     else:
#         left = mid + 1


# Average Case — O(log n)
numbers = [1,2,3,4,5,6,7,8,9,10]
finder = 6

left, right = 0, len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == finder:
        print("Found at index:", mid)
        break
    elif numbers[mid] > finder:
        right = mid - 1
    else:
        left = mid + 1


# ❌ Worst Case — O(log n)
numbers = [1,2,3,4,5,6,7,8,9,10]
finder = 100  # not in list

left, right = 0, len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == finder:
        print("Found at index:", mid)
        break
    elif numbers[mid] > finder:
        right = mid - 1
    else:
        left = mid + 1
else:
    print("Not found")