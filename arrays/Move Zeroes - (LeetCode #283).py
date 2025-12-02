# LeetCode #283 — Move Zeroes

'''
Docstring for arrays.Move Zeroes - (LeetCode #283)

Problem Statement:

Given an array nums, move all 0’s to the end while keeping the relative order of non-zero elements.
Must be done in-place.

'''

nums =  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


i=0

for num in nums:
    if num!=0:
        nums[i] = num
        i+=1
    
for j in range(i,len(nums)):
    nums[j]=0
    
print(nums)