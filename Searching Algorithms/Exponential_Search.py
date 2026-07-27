# numbers = [1, 3, 5, 7, 9, 13, 16 ,20, 24, 26, 29, 30]

# target = 9


# if numbers[0] == target:
#     print("Found at index 0")
# else:
#     i = 1
#     while numbers[i]<=target:
#         if numbers[i] == target:
#             print(f"Found at index {i}")
#             break
#         elif numbers[i] > target:
#             left, right = i/2, i
#             mid = (left + right) // 2

#             while left <= right:
#                 if numbers[mid] == target:
#                     print(f"Found at index {i}")
#                     break
#                 elif numbers[mid] > target:
#                     right = mid - 1
#                 elif numbers[mid] < target:
#                     left = mid + 1


#         else:
#             i = i * 2


numbers = [1, 3, 5, 7, 9, 13, 16, 20, 24, 26, 29, 30]
target = 9

if numbers[0] == target:
    print("Found at index 0")
else:
    i = 1
    n = len(numbers)

    # Phase 1: find range
    while i < n and numbers[i] <= target:
        i *= 2

    left = i // 2
    right = min(i, n - 1)

    # Phase 2: binary search
    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            print(f"Found at index {mid}")
            break
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


