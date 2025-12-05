nums = [5, 4, 7, 2, 9, 6]

last_even = 0

for i in range(len(nums)):
    if nums[i]%2==0:
        temp = nums[i]
        j=i

        while j>last_even:
            nums[j]=nums[j-1]
            j-=1
        nums[last_even]= temp
        last_even +=1

print(nums)
