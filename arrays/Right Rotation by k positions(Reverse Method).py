# ✅ Right Rotation (Reverse Method) — Full Explanation

'''
Docstring for arrays.Right Rotation by k positions(Reverse Method)

Right rotation by k means:

[1, 2, 3, 4, 5] rotated right by 2 → [4, 5, 1, 2, 3]

⭐ The key catch:

If k > n, rotating more than the size of array is meaningless because rotations repeat.

Example: rotating by 7 on an array of length 5
➡ same as rotating by 7 % 5 = 2

So, always normalize k:
k = k % n

✔ Right Rotation – Reverse Technique

Right rotation by k:

1️⃣ Reverse the whole array
2️⃣ Reverse first k
3️⃣ Reverse remaining n−k

Formula:

right rotate k steps:
reverse(0, n-1)
reverse(0, k-1)
reverse(k, n-1)

'''

# CODE

nums = [1, 2, 3, 4, 5]
k=7         # example where k > n

def reverse(nums,l,r):
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l +=1
        r -=1
    return nums

n = len(nums)

k=k%n     # <-- IMPORTANT STEP

# Step 1: reverse whole array
reverse(nums,0, n-1)

# Step 2: reverse first k elements
reverse(nums,0,k-1)

# Step 3: reverse rest
reverse(nums,k,n-1)

print(nums)


'''
🧠 Why only 3 reversals?

Because reverse-move technique always works in exactly 3 steps:

✔ Reverse all
✔ Reverse first segment
✔ Reverse second segment

Even if k is 1000 or 1 crore —
k = k % n reduces it to a number < n
so you always do exactly 3 reverses.
'''