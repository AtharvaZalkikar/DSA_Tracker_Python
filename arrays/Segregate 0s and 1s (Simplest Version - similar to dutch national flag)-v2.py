'''
🧩 Variation 1: Segregate 0s and 1s (Simplest Version)

Problem:

Given an array of 0s and 1s, sort it in-place so all 0s come before 1s.
No counting allowed — must use the two-pointer (partition) technique.

Example:
Input:  [0, 1, 1, 0, 1, 0, 0]
Output: [0, 0, 0, 0, 1, 1, 1]

'''

nums = [0, 1, 1, 0, 1, 0, 0]

low=0
high=len(nums)-1

while low<high:
    if nums[low]==0:
        low+=1
    elif nums[low]==1:
        nums[high],nums[low]=nums[low],nums[high]
        high -=1

print(nums)