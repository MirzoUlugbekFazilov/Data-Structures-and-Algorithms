# Sliding Fixed Window
def sliding_window_fixed(nums: list[int], k: int) -> int:
    window_sum = 0

    for i in range(k):
        window_sum+=nums[i]
    
    largest = window_sum 

    for right in range(k, len(nums)):
        left = right - k
        window_sum-=nums[left]
        window_sum+=nums[right]
        largest = max(window_sum, largest)
    return largest

bro = [1,2,3,4,5,6,7,10,15]

print(sliding_window_fixed(bro, 3))


# Sliding Dynamic Window
from collections import defaultdict   

def longest_substring(s: str) -> int:
    largest = 0
    left = 0
    counter: dict[str, int] = defaultdict(int)

    for right in range(len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1
        largest = max(largest, right-left+1)

    return largest

print(longest_substring("abcdefa"))

    
