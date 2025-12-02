# 💡 Concept: Dynamic (Incremental) Prefix Sum Update

nums = [3, 1, 4, 1, 5]


prefix = [0]*len(nums)
print(prefix)

prefix[0]=nums[0]


for i in range(1, len(nums)):
    prefix[i] = prefix[i-1]+nums[i]

print(prefix)

# Now dynamically add a number to the input list and then recalculate the prefix

nums.append(7)

# so now we add newly added number in nums list to the prefix by using negative indexing 
# so that we dont have to recalculate the whole prefix again

new_prefix_element = prefix[-1]+nums[-1]
prefix.append(new_prefix_element)

print(f"Prefix after adding new elemnt in input list is: {prefix}")