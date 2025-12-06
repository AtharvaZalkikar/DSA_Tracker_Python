# In-Place Merge of Two Sorted Arrays

'''
Docstring for arrays.In-Place Merge of Two Sorted Arrays

This problem appears in interviews at FAANG, Adobe, Microsoft, etc.

You are given, for example:

nums1 = [1, 3, 5, 7, _, _, _]   # size = m + n (extra space at end)
nums2 = [2, 4, 6]               # size = n

Goal:
Merge nums2 into nums1 so that nums1 becomes:
[1, 2, 3, 4, 5, 6, 7]

👉 Everything must be done in-place inside nums1.

------------------------------------------------------------

❗ Why normal merging doesn’t work in-place

If you try to merge from the front, you overwrite elements of nums1 before you compare them.

Example:
If you start merging at the beginning:
nums1 = [1, 3, 5, 7, _, _, _]
nums2 = [2, 4, 6]

We compare 1 and 2 — correct.
But then eventually we want to place 2 before 3.
That means 3, 5, 7 need to shift right — expensive and messy.

This is why merging from the front is impossible without extra space.

💡 Key Trick: Merge from the END

This is the core insight.

Instead of merging from the front:

We compare the last elements of nums1 and nums2,

Place the larger one into the end of nums1.

So we use three pointers:

Pointer	Meaning
i	last index of nums1’s valid part (m - 1)
j	last index of nums2 (n - 1)
k	last index of nums1 (m + n - 1)
⭐ Why merging from the back works

Because the end of nums1 has empty space.
We are free to fill it from right → left without overwriting anything important.

🔧 Step-by-step Logic (Concept)

Given:
nums1 = [1,3,5,7,_,_,_]
nums2 = [2,4,6]

m = 4
n = 3

Initialize pointers:
i = m - 1   → 3  (points to 7)
j = n - 1   → 2  (points to 6)
k = m+n-1   → 6  (last index of nums1)

Now compare from the end:

1️⃣ Compare 7 and 6
→ bigger is 7 → put 7 at nums1[k] → k-- → i--

2️⃣ Compare 5 and 6
→ bigger is 6 → put 6 at nums1[k] → k-- → j--

3️⃣ Compare 5 and 4
→ bigger is 5 → put 5 → k-- → i--

Continue until either:

j < 0 (nums2 fully placed)

i < 0 (place the rest of nums2)

📌 Special Condition

If nums2 still has leftovers (j >= 0),
copy all remaining nums2 elements into nums1.

If nums1 has leftovers (i >= 0),
no need to copy — they are already in the correct position.

🧠 Why this works elegantly

We NEVER overwrite elements we still need to compare.

Working backwards lets us fill nums1 safely.

Time complexity = O(m + n)

Space complexity = O(1) ← in place

✔️ Summary of the Concept

To merge in-place:

Start from the end of both arrays.

Fill nums1 from the backwards using pointer k.

Compare and place the larger element.

Continue until nums2 is fully merged.

This is the cleanest, most efficient merging strategy.

'''

# This problem appears in interviews at FAANG, Adobe, Microsoft, etc.

'''
🔥 Concept: In-Place Merge of Two Sorted Arrays
(Without using extra space for "merged" list)

We have:

nums1 = [1, 3, 5, 7, _, _, _]   # size = m + n  (empty space at end)
nums2 = [2, 4, 6]               # size = n

Goal:
nums1 → [1, 2, 3, 4, 5, 6, 7]

Done in-place, meaning:

No new list like merged = []

We use the empty space at the back of nums1

This is the LeetCode #88: Merge Sorted Array pattern.
'''


nums1 = [1,3,5,7,0,0,0]
nums2 = [2,4,6]

m=4
n=3

print(len(nums1))

#initialise 3 pointers

i = m-1
j = n-1
k = m+n-1

# Then compare nums1[i] and nums2[j] and fill nums1 from right to left.

'''
nums1 = [1,3,5,7,_,_,_]
nums2 = [2,4,6]

i = 3 (nums1[3] = 7)
j = 2 (nums2[2] = 6)
k = 6
'''

while i>=0 and j>=0:
    if nums1[i]>nums2[j]:
        nums1[k]=nums1[i]
        i-=1
    else:
        nums1[k]=nums2[j]
        j-=1
    k-=1

# After one list finishes:
# If nums2 still has remaining elements → copy them into nums1.
# If nums1 has remaining elements → they are already correctly placed.

while j>=0:
    nums1[k]=nums2[j]
    j-=1
    k-=1
    
print(nums1)