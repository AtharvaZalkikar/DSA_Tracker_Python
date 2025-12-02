'''
nums = [4, 5, 9, 4, 9, 8, 5]

unique_nums = list(set(nums))
print("After removing duplicates:", unique_nums)




⚙️ Approach 2: In-place Removal (Preserve Order, No Extra Space)

Version A — Using a result list (still simple but preserves order):

nums = [4, 5, 9, 4, 9, 8, 5]
unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("After removing duplicates:", unique)

Output:
After removing duplicates: [4, 5, 9, 8]

Time complexity: O(n²) (because of num not in unique).
order



Version B — True in-place (for sorted arrays only):
If the array is sorted, we can do it in O(n) and constant space.

nums = [1, 1, 2, 2, 3, 4, 4, 5]

i = 0
for j in range(1, len(nums)):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]

print("After removing duplicates:", nums[:i+1])

Output:
After removing duplicates: [4, 5, 8, 9]

'''


# Input:  [1, 1, 2, 2, 3, 3, 3, 4]
# Output: [1, 2, 3, 4]


# -------------------------------------------------------------------------

# num = [1, 1, 2, 2, 3, 3, 3, 4]     #test case 1
# num=[1,2,3,4]                        #test case 2
num = [1,1,2,3,3,5,5,6,6,6,7]        #test case 3
# num = [1,1,1,1]                      #test case 4


i=0

for j in range(1,len(num)):
    if num[j] != num[i]:
        i = i+1
        num[i]=num[j]

print(i)

print(num)
print(f"output: {num[:i+1]}") #output we want


'''
⚡ Bonus Insight: LeetCode 26

This exact question is LeetCode #26 — Remove Duplicates from Sorted Array,
one of the most popular beginner array problems asked in interviews (even by FAANG companies).
'''