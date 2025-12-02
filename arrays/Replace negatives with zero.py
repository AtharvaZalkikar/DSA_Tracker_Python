# Replace negatives with zero

nums = [5, -2, 7, -9, 3]
# print(range(len(nums)))

for i in range(len(nums)):
    if nums[i]<0:
        print(nums[i])
        nums[i] = 0
        # num = num + num
        # print(num)
        
print(nums)