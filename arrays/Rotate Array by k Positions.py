# 🧩 Problem: Rotate Array by k Positions

'''
🧠 Concept: Left Rotation

Rotate array to the left by k positions.

nums = [1, 2, 3, 4, 5]
k = 2
Output = [3, 4, 5, 1, 2]

Explanation:

The first k elements move to the end in the same order.

The remaining elements shift left.
'''
# -------------------------------------------------------------------------------

'''
Approach 2 — In-Place Rotation (By Reversing)

We can do it without extra list (important for interviews):

Steps for Left Rotation by k:

Reverse first k elements.

Reverse remaining n - k elements.

Reverse the entire array.

This works because reversing twice restores order in rotated form.
'''


nums = [1, 2, 3, 4, 5]

k=2

# ---------------------------------------------------------
# ✅ Hint 1 — Write a reverse() helper
# ---------------------------------------------------------
def reverse(nums,l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
    return nums

# ---------------------------------------------------------
# ✅ Hint 2 — Reverse the first k elements
# ---------------------------------------------------------
    
reverse(nums,0,k-1)
print(nums)

# ---------------------------------------------------------
# Hint 3 — Reverse the remaining elements
# ---------------------------------------------------------

n=len(nums)

reverse(nums,k,n-1)
print(nums)

# ---------------------------------------------------------
# 👉Finally Reverse the entire array
# ---------------------------------------------------------

reverse(nums,0,n-1)
print(nums)


'''
Even when k value is changes but less than lenght of array,
even then we use the same three reversal technique to rotate arrays by k positions


🔥 What you just demonstrated

This is the reverse algorithm for rotation:

Reverse the first k elements

Reverse the remaining n - k elements

Reverse the entire array

This gives O(n) time and O(1) space — optimal.

✅ If k is larger than array length, you still only do 3 reversals.
👉 But what changes when k is large?

If k > n, rotating by k positions is the same as rotating by k % n.


nums = [1,2,3,4,5]
k = 12
n = 5
k % n = 2
So rotating left by 12 steps = rotating left by 2 steps.
'''