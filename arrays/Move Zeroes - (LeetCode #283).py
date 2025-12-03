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



#  APPROACH 2 -  CODE SWAP - MORE DSA STYLE

nums2 = [0, 1, 0, 3, 12]

i = 0

for j in range(len(nums2)):
    if nums2[j] != 0:
        nums2[i], nums2[j] = nums2[j], nums2[i]
        i += 1

print(nums2)

'''
✅ Swap-Based Two Pointer Method (In-Place & Stable)

Idea
Use two pointers i and j
j → scans the array
i → tracks the position where the next non-zero should go

When you see a non-zero at j, swap it with index i
Increase i

This method avoids the “fill-zero afterwards” step — it keeps swapping as it goes.
'''

# Both are correct.
# Most interviewers prefer the swap approach because it follows the two-pointer pattern used in many array problems.