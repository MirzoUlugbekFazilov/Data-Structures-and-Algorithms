# Best Compexity: O(1)
# Average Complexity: O(n/2)
# Worst Complexity: O(n)


# Best Case — O(1)
numbers = [7, 2, 3, 4, 5]
finder = 7
for i, num in enumerate(numbers):
    if num == finder:
        print("Found at index:", i)
        break


# Average Case — O(n)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
finder = 6

for i, num in enumerate(numbers):
    if num == finder:
        print("Found at index:", i)
        break
    



# ❌ Worst Case — O(n)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
finder = 100  # not in list

for i, num in enumerate(numbers):
    if num == finder:
        print("Found at index:", i)
        break
else:
    print("Not found")



# print(numbers)

