'''
🎯 Problem Statement

Given an array consisting only of 0, 1, and 2, sort it in-place so that all 0s come first, followed by 1s, then 2s.

Example:

Input:  [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

-----------------------------------

💡 Intuition

You could count the number of 0s, 1s, and 2s, then rebuild the array —
but that’s not the optimal way (and it’s not in-place).

The smarter solution uses three pointers — a pattern directly connected to what you just did with partitioning:

| Pointer | Purpose                                 |
| ------- | --------------------------------------- |
| `low`   | boundary for 0s (next 0 should go here) |
| `mid`   | current element being checked           |
| `high`  | boundary for 2s (next 2 should go here) |

⚙️ Algorithm

Initialize:

low = 0
mid = 0
high = len(nums) - 1

2 While mid <= high:

 > If nums[mid] == 0:
 swap nums[low] and nums[mid]; increment both low and mid

 > If nums[mid] == 1:
 just mid += 1

 > If nums[mid] == 2:
 swap nums[mid] and nums[high]; decrement high (don’t increment mid yet!)

3. Continue until mid > high.

✅ This runs in O(n) and O(1) space — completely in-place, and extremely elegant.
'''

nums = [2, 0, 2, 1, 1, 0]

low = 0
mid = 0
high = len(nums) - 1   #6-1=5

print(high) #->5

# for num in nums:     no need 
while mid<=high:
    if nums[mid] == 0:
        nums[low],nums[mid]=nums[mid],nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    elif nums[mid] == 2:
        nums[high],nums[mid]=nums[mid],nums[high]
        high -= 1

print(nums)





'''
🧠 Pointer Movement Summary

| Step  | Action              | low | mid | high | Array         |
| ----- | ------------------- | --- | --- | ---- | ------------- |
| Start | Init                | 0   | 0   | 5    | [2,0,2,1,1,0] |
| 1     | swap mid↔high (2↔0) | 0   | 0   | 4    | [0,0,2,1,1,2] |
| 2     | swap mid↔low (0↔0)  | 1   | 1   | 4    | [0,0,2,1,1,2] |
| 3     | mid=1, move mid     | 1   | 2   | 4    | [0,0,2,1,1,2] |
| 4     | swap mid↔high (2↔1) | 1   | 2   | 3    | [0,0,1,1,2,2] |
| 5     | mid=1, move mid     | 1   | 3   | 3    | [0,0,1,1,2,2] |
| End   | mid>high            | —   | —   | —    | [0,0,1,1,2,2] |

🚀 What You’ve Mastered

You now know:

Three-pointer partition logic

In-place sorting without comparison

Relation to QuickSort’s partition step

This is a very strong DSA milestone. 💪

Would you like to now practice a few short variations of this pattern (e.g., partition by color, sort binary array, segregate 0/1 without counting, etc.)
 — all easy once you know this 
— or move to the next big subtopic (subarray problems, like max sum, equilibrium index, etc.)?
'''
