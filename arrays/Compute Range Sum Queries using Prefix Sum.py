'''
🧩 Task 6 — Compute Range Sum Queries using Prefix Sum

Goal:
Given an array and multiple (L, R) pairs, quickly find the sum of elements from index L to R (both inclusive).      
'''


nums = [2, 4, 6, 8, 10]
prefix = [0] * len(nums)

prefix[0] = nums[0]
for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]

print("Prefix Sum:", prefix)

# sum(L, R) = prefix[R] - prefix[L - 1]
# But if L == 0, then just:
# sum(0, R) = prefix[R]


queries = [(0, 2), (1, 3), (2, 4)]  # (L, R) pairs

for L, R in queries:
    if L == 0:
        range_sum = prefix[R]
    else:
        range_sum = prefix[R] - prefix[L - 1]
    print(f"Sum of elements from {L} to {R} = {range_sum}")

    