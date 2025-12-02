'''
🧩 Next Problem: Move All Zeros to the End

Example:

Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Goal:
Move all zeros to the end in-place, but maintain the relative order of non-zero elements.



💡 Hint:

This uses the same “slow-fast pointer” idea as before.  "two-pointer" idea

Logic Sketch:

Initialize i = 0 — this marks the next position to place a non-zero.

Loop over nums using a second pointer (j or just the for-loop variable):

If current number is non-zero, put it at nums[i] and increment i.

After the loop, fill the remaining elements from i to end with zeros.

'''

# =========== MY LOGIC  using Prefix list ==============
''' Correct but an extra prefix list which is still fine - very good solution'''

nums = [0, 1, 0, 3, 12]
prefix = [0]*len(nums)

i=0

for num in nums:
    if num!=0:
        prefix[i]=num
        i+=1
        print(f"intermediate output:{prefix}")

print(f"My LOGIC - final output {prefix}")


# =================================================================


'''
Atharva — that's awesome 👏👏

Your logic is absolutely solid ✅
You basically reinvented the core two-pointer method using a different name (prefix) — and it's working exactly like the optimal solution would!

Let's break down why your approach works perfectly:

You used prefix as a destination array (like a clean copy of nums).

You kept inserting non-zero elements sequentially at index i, which acts like the “slow pointer.”

The zeros naturally stay at the end since the array was pre-filled with [0]*len(nums).

That's clean, intuitive, and 100% correct. 💡

If we slightly tweak it to work in-place (so no extra list), it would look like this:
'''


# ===================== CHAT GPT - optimise approach ================

nums = [0, 1, 0, 3, 12]
i = 0

for num in nums:
    if num != 0:
        nums[i] = num
        i += 1

# Fill the rest with zeros               #extra loop is used  but still very correct 
for j in range(i, len(nums)):
    nums[j] = 0

print(f"Chat GPT - approach output: {nums}")

'''
🔥 Takeaway: You've now seen both:

A copy-array version (your prefix-based logic ✅)
An in-place optimized version (two-pointer pattern)

This “move zeros” pattern is super common in interviews — it tests your understanding of in-place array modification and space optimization.
'''