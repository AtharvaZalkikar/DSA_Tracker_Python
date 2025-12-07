# Maximum Subarray - KADANE'S ALGORITHM - LEETCODE #53

'''
Docstring for Maximum Subarray - KADANE'S ALGORITHM - LEETCODE #53
------------------------------------------------------------------------------------------
Given an integer array nums, find the subarray with the largest sum, and return its sum.
or
Given an array nums, return the maximum sum of any contiguous subarray.
------------------------------------------------------------------------------------------

'''
def Kadane(nums):

    # 🧠 Step 1 — Initialize Two Variables

    current_sum = 0
    max_sum = -float('inf')

    '''
    Why?

    current_sum builds the running subarray sum
    max_sum keeps track of the best sum we have seen so far
    max_sum starts at negative infinity so that any real sum will be larger
    '''

    # 🧠 Step 2 — Loop through each element
    for num in nums:
        current_sum = current_sum + num
        max_sum = max(max_sum, current_sum)

        if current_sum<0:
            current_sum=0
        
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]

largest_sum = Kadane(nums)

print(largest_sum)
