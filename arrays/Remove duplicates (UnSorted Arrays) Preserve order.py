# Problem: Remove Duplicates from an Unsorted Array

'''
Input:  [4, 2, 1, 4, 3, 2, 5]
Output: [4, 2, 1, 3, 5]

Goal:

Return a new list with duplicates removed, preserving the order of first appearance.

'''

'''
💡 Step 1: Concept

When the array isn’t sorted, we can’t use the two-pointer trick.
Instead, we can track what we’ve already seen using a set.

Logic:

Create an empty set → seen = set()

Create an empty list → unique = []

Loop through each element in the input list:

If it’s not in seen, add it to both seen and unique.

'''

nums = [4, 2, 1, 4, 3, 2, 5]

# seen = set(nums)
seen = set()        #empty set
print(seen)

unique = []         #empty list

for num in nums:
    if num not in seen:
        seen.add(num)
        unique.append(num)

print(seen)
print(unique)

'''
🔁 Step 2 — Do It In-Place (without extra list)

We’ll now modify the original array itself instead of creating a new one.

Hint:

We’ll still use a set to track what we’ve seen.

But instead of building a new unique list, we’ll overwrite the input array (nums) as we go.

We’ll use an index pointer i to mark where to place the next unique element.

'''

nums = [4, 2, 1, 4, 3, 2, 5]

seen = set()

i=0

for num in nums:
    if num not in seen:
        seen.add(num)
        nums[i] = num
        i=i+1

print(f"i is {i}") # i =5

# print(f"final nums: {nums[:i+1]}") #incorrect i+1is wrong here bcoz we are adding plus  1 to i above in the if loop

print(f"final nums: {nums[:i]}")  # correct i is 5 so it will print till nums[4] as per slicing rules.