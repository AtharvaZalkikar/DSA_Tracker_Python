# Rotate Array (LeetCode #189)

'''
------------------------------------------------------------
Docstring for arrays.Rotate Array (LeetCode #189)
-------------------------------------------------------------
Problem:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Constraints:

Rotate in-place
O(1) extra space
Right rotation by k means the last k elements move to the front.
'''

nums = [1,2,3,4,5,6,7]
k=3

def reverse(nums,l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
    return nums

n=len(nums)

if k>n:
    k=k%n

# STEP-1
reverse(nums,0,n-1)

# STEP-2
reverse(nums,0,k-1)

# STEP-3
reverse(nums,k,n-1)
    
print(f"rotated array : {nums}")