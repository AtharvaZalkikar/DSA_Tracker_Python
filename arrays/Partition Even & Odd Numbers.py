
# ⚙️ Problem: Partition Even & Odd Numbers

'''
this one will feel familiar but helps you generalize partitioning logic
(a key skill for real interview questions like “Dutch National Flag”, “QuickSort partition”, etc.).

⚙️ Problem: Partition Even & Odd Numbers

nums = [3, 1, 4, 2, 5, 8, 7]
-------------------------------------
Goal:
Rearrange the array so that all even numbers come first and odd numbers come after,
but we’ll test two versions:

Unstable (swap-based) – fast but may break order

Stable (order-preserving) – slower but keeps the order of even & odd numbers intact

----------------------------------------
🧠 Step 1: Unstable (Swap-Based)

Let’s try to derive logic (you can write your version after thinking a bit):

Hint:

Use a pointer j = 0

Loop through array with i

If nums[i] is even, swap with nums[j], and increment j

This is identical to what we did for negatives earlier — just the condition changes.

🧠 Step 2: Stable (Shift-Based)

Here, you can:

Loop through array

Whenever you find an even number that appears after some odds,
remove it (pop) and insert it at the position after the last even element.

This preserves order but may be O(n²).

🎯 Your Turn:

Try implementing Step 1 (swap-based) yourself first for input
nums = [3, 1, 4, 2, 5, 8, 7]
and share your code + output.

Then we’ll analyze its behavior and move to the stable version.

'''
#my easiest approach but more time complex and most space complex because of extra lists

nums = [3, 1, 4, 2, 5, 8, 7]
print(f"input: {nums}")

even = []
odd= []

for num in nums:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

# print(even)
# print(odd)

nums = even+odd

print(f"my easiest appraoch: {nums}")

#----------------------------------------------------------------------------------------------

# 🧠 Step 1: Unstable (Swap-Based)

nums = [3, 1, 4, 2, 5, 8, 7]

i=0
j=0

for i in range(len(nums)):
    if (nums[i]%2)==0:
        nums[i],nums[j]=nums[j],nums[i]
        j=j+1
    
print(f"unstable (swap based): {nums}")

#-------------------------------------------------------------------------------------------------

#🧠 Step 2: Stable (Shift-Based)

nums = [3, 1, 4, 2, 5, 8, 7]

last_even_index = 0
temp =0

for i in range(len(nums)):
    if nums[i]%2==0:        #if even
        temp = nums[i]      #store even number in temp
        j=i                 #j is fast pointer if j is greater than last_even_index which is slow pointer then -> while loop for swapping or shifting numbers

        while j>last_even_index:        
            nums[j]=nums[j-1]                 # shift numbers ahead till j becomes equal to last even index (reducing j)
            j=j-1                      # thats why reducing index j=j-1

        nums[last_even_index]=temp        #store value of the even number in the last even index 
        last_even_index +=1           #increment index to next value (helpful for shifting odd elements as done in above while loop!)

print(f"stabe approach shift based: {nums}")


#---------------------------------------------------------------------------------------


'''
🧩1️⃣ Your “Easiest Approach” (Extra Lists)

✅ Output: [4, 2, 8, 3, 1, 5, 7]
✅ Stable, Simple, Intuitive
❌ Needs O(n) extra space

💡 Conceptually, this is like a “two-pass stable partition”.
You traverse once to build even + odd lists, then merge them.
Space = O(n), Time = O(n).
This is fine for small or medium inputs — and perfectly valid for clarity.

🧩 2️⃣ Unstable (Swap-Based, In-Place)

✅ Output: [4, 2, 8, 1, 5, 3, 7]
⚙️ Fastest (O(n)), O(1) extra space
❌ Order of odd numbers not preserved

👉 You correctly used the “two-pointer partition” logic —
this is the same mechanism used in QuickSort’s partition step.
That’s why we call it unstable: it doesn’t preserve order.

For example:

Original odds: [3, 1, 5, 7]

After swap-based: [1, 5, 3, 7] → order changed ✅ observation!

So this is the “QuickSort partition” version —
efficient, but not stable.

🧩 3️⃣ Stable (Shift-Based)

✅ Output: [4, 2, 8, 3, 1, 5, 7]
✅ Preserves order
❌ O(n²) in worst case (because of shifting)

This is the “in-place stable” version — what’s used in Insertion Sort internally!
Each even number is inserted before the first odd after it,
so order of both categories is preserved.

Beautiful job correctly maintaining and updating last_even_index 👏

🧭 Summary Table
Approach	Stable?	Space	Time	Notes
Extra lists	✅ Yes	O(n)	O(n)	Easiest to code
Swap-based	❌ No	O(1)	O(n)	Used in QuickSort
Shift-based	✅ Yes	O(1)	O(n²)	Similar to Insertion Sort

✅ You’ve now mastered:

Partition by sign

Partition by even/odd

Stable vs. unstable reordering

Prefix sums and in-place updates

'''