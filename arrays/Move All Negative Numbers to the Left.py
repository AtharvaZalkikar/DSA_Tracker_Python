'''
🧩 Problem: Move All Negative Numbers to the Left

Example:
Input:  [3, -2, -5, 4, -1, 6]
Output: [-2, -5, -1, 3, 4, 6]

Goal:
Rearrange the array so that all negative numbers appear first,
but the relative order among negatives and positives doesn't matter (we just need grouping).

💡 Hint:

We'll again use the two-pointer approach, but with a small twist.
Logic Sketch (In-Place Version):

Set a pointer j = 0 → this will track the position where the next negative number should go.
Loop through the array with i:

If nums[i] is negative, swap nums[i] and nums[j], and increment j.
At the end, all negatives will be at the start (left).

'''

nums =  [3, -2, -5, 4, -1, 6]

j=0
i=0

for i in range(0,len(nums)):
    if nums[i]<0:
        nums[i],nums[j]=nums[j],nums[i]     #swap the elements
        j=j+1
    # print(f"for i {i} and j {j} the nums is: {nums}")

print(nums)

