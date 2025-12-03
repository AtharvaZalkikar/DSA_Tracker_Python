# LEETCODE - Dutch National Flag Variant - Harder
# Move All Zeroes to the RIGHT and Move All Ones to the LEFT

'''
Docstring for arrays.Dutch National Flag Variant - LEETCODE - Move All Zeroes to the RIGHT and Move All Ones to the LEFT


🔥 Problem Variant

Given an array consisting of 0, 1, and 2, rearrange it so that:
All 1’s come first
Then all 2’s
Then all 0’s come last
Do it in one pass, in-place, O(n) time

Example:
Input:  [0, 2, 1, 0, 2, 1, 1]
Output: [1, 1, 1, 2, 2, 0, 0]

This is basically a variation of Dutch National Flag, but with a different order.

Try to solve this yourself first.

📌 HINT 1:
Use three pointers:

low → where next 1 should go
mid → current index
high → where next 0 should go

📌 HINT 2:
But the rules change:
| nums[mid] | Action                       |
| --------- | ---------------------------- |
| 1         | swap with low → low++, mid++ |
| 2         | just mid++                   |
| 0         | swap with high → high--      |

📌 HINT 3:
Loop while:
📌 HINT 3:
Loop while:
'''

nums = [0, 2, 1, 0, 2, 1, 1]

low = 0
mid = 0
high = len(nums)-1   #last index of array

while mid<=high:
    if nums[mid]==1:
        nums[mid],nums[low]=nums[low],nums[mid]
        low+=1
        mid+=1
    elif nums[mid]==2:
        mid+=1
    elif nums[mid]==0:
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1

print(nums)