# 🧩 Final Prefix Challenge: Quick Subarray Sum Queries

'''
Problem:

You’re given:
nums = [2, 4, 6, 8, 10]
queries = [(0, 2), (1, 3), (2, 4)]


You need to use prefix sums to answer each query:

“What is the sum of elements from index L to R (inclusive)?”
Expected Output:
Sum from 0 to 2 = 12
Sum from 1 to 3 = 18
Sum from 2 to 4 = 24

🏗️ Task:

Write the full code that:

Builds the prefix array.

Uses it to answer all queries efficiently.

Prints each query’s result in a neat format.

'''


nums = [2, 4, 6, 8, 10]
queries = [(0, 2), (1, 3), (2, 4)]

prefix = [0]*len(nums)

prefix[0]=nums[0]

for i in range(1, len(nums)):
    prefix[i]=prefix[i-1]+nums[i]

# print(prefix)

for L,R in queries:
    if L!=0:
        range_sum = prefix[R]-prefix[L-1]
    else:
        range_sum = prefix[R]
    print(f"Sum from {L} to {R} = {range_sum}")
