'''
🧩 Problem Statement
You’re given an array nums, e.g.:

nums = [3, -2, -5, 4, -1, 6]

👉 Goal: Move all negative numbers to the left and all positive numbers to the right, while preserving the relative order of elements.

So the expected output is:

[-2, -5, -1, 3, 4, 6]

Notice how:

All negatives are still in the same order they appeared in (-2, -5, -1)

All positives are still in the same order (3, 4, 6)

But the groups are rearranged.
'''


# ⚙️ Approach 1: Using an Extra List (Simple + Clear)

nums = [-2, -5, -1, 3, 4, 6]

i=0
j=0

neg=[]
pos=[]

for num in nums:
    if num<0:
        neg.append(num)
    else:
        pos.append(num)

# Combine back

result = neg+pos
print(result)

#=============================== Approach 2: Inplace ===========================

#
nums = [3, -2, -5, 4, -1, 6]

last_negative_index = 0

for i in range(len(nums)):
    if nums[i]<0:
        temp = nums[i]     
                
        # shift everything right between last_negative_index and i-1

        j=i
        while j>last_negative_index:      # j>0
            nums[j]=nums[j-1]             # for e.g nums[1]=nums[0] so means nums[1]=3
            j = j-1                       # j= 1-1= 0
        nums[last_negative_index]=temp    # nums[0] = -2
        last_negative_index +=1           # last_negative_index = 0+1 = 1

print(nums)
#[-2, -5, -1, 3, 4, 6]


