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

i=0
last_zero_index = 0
temp=None

for i in range(len(nums)):
    if nums[i]==0:
        temp=nums[i]
        j=i
        while j>last_zero_index:
            nums[j]=nums[j-1]
            j-=1
        nums[last_zero_index]=temp
        last_zero_index+=1

print(nums)
