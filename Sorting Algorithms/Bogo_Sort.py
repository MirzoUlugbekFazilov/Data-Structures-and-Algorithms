import random

# Best Complexity: O(n)
# Average Complexity: O(n * n!)
# Worst Complexity: O(∞)  # theoretically unbounded


# ✅ Best Case — O(n)
numbers = [1, 2, 3, 4, 5]  # already sorted

while True:
    checker = True

    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            checker = False
            break

    if checker:
        print("Sorted!")
        break
    else:
        random.shuffle(numbers)

print("Result:", numbers)



# ⚠️ Average Case — O(n * n!)
numbers = [3, 1, 4, 2, 5]  # random order

shuffle_count = 0

while True:
    checker = True

    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            checker = False
            break

    if checker:
        print("Sorted!")
        break
    else:
        random.shuffle(numbers)
        shuffle_count += 1

print("Result:", numbers)
print("Shuffles:", shuffle_count)



# ❌ Worst Case — O(∞)
numbers = [5, 4, 3, 2, 1]  # reverse sorted

shuffle_count = 0

while True:
    checker = True

    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            checker = False
            break

    if checker:
        print("Sorted!")
        break
    else:
        random.shuffle(numbers)
        shuffle_count += 1

print("Result:", numbers)
print("Shuffles:", shuffle_count)