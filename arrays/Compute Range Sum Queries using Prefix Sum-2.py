'''
nums = [3, 1, 4, 1, 5, 9, 2]
queries = [(0, 3), (2, 5), (1, 6)]

✅ Your task:

Build the prefix sum array manually (no libraries).

Then, using it, compute the sum for each (L, R) pair.

Print results in this format:

Sum of elements from L to R = result

Try to write your full code (including prefix sum logic + query handling).
'''


nums = [3, 1, 4, 1, 5, 9, 2]
queries = [(0, 3), (2, 5), (1, 6)]

prefix = [0]*len(nums)

print(prefix)

prefix[0]=nums[0]

for i in range(1,len(nums)):
    prefix[i] = prefix[i-1]+nums[i]

print(f"Running total of each index is stored in prefix list as: {prefix}\n")

print("Now lets calculate the sum of elements between the two given indices(range of indices) in each query. this is known as range sum.")

'''
if query is (2,5)  we want total(range sum) of elements between index 2 to index 5 of list called nums[] wiz input list.
Now,
here L=2 and R=5 
range_sum = prefix[R] - prefix[L-1]

and if L==0 then 
range_sum = prefix[R]
'''

for L,R in queries:
    if L==0:
        range_sum = prefix[R]
    else:
        range_sum = prefix[R] - prefix[L-1]
    
    print(f"Sum of elements from {L} to {R} = {range_sum}.")

print("THE END")

