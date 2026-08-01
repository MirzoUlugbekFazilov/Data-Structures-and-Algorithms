# Best Complexity: O(n)
# Average Complexity: O(n^2)
# Worst Complexity: O(n^2)


def bubble_sort(numbers):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                is_sorted = False
    return numbers


# Best Case — O(n)
best_case = [1, 2, 3, 4, 5]
print("Best case input: ", best_case)
print("Sorted:", bubble_sort(best_case.copy()))
print()


# Average Case — O(n^2)
avg_case = [5, 1, 4, 2, 3]
print("Average case input:", avg_case)
print("Sorted:", bubble_sort(avg_case.copy()))
print()


# ❌ Worst Case — O(n^2)
worst_case = [5, 4, 3, 2, 1]
print("Worst case input:", worst_case)
print("Sorted:", bubble_sort(worst_case.copy()))