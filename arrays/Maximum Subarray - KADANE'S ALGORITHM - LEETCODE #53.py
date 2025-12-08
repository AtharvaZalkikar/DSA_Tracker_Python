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
    max_sum = -float('inf')   #necessary to handle array with all negative numbers

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
            # print(f"curent sum reset")
        
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]

# 🟢 Level 1: Easy
# A simple list where the max subarray is obvious:
nums1 = [4, -1, 2, 1]

# 🟡 Level 2: Medium
# Mixed positive and negatives:
nums2 = [-2, 3, 5, -1, 4, -5]

# 🔴 Level 3: Hard
# This one tests whether your code resets correctly:
nums3 = [-3, -2, -5, -1]

# 🔥 Final Challenge
# Requires correct start/end tracking:
# Test 4
nums4 = [5, -4, -2, 6, -1, 7, -8, 4]


largest_sum = Kadane(nums)

largest_sum1 = Kadane(nums1)
largest_sum2 = Kadane(nums2)
largest_sum3 = Kadane(nums3)
largest_sum4 = Kadane(nums4)

print(largest_sum)
print(largest_sum1)
print(largest_sum2)
print(largest_sum3)
print(largest_sum4)
