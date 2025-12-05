# Basic Merge (Easy Version)
# Merge Two Sorted Arrays

'''
Docstring for arrays.Merge Two Sorted Arrays-Basic

You are given two sorted arrays:
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6]

👉 Task:
Merge them into a new sorted array, using the two-pointer technique.
DO NOT use sort().
DO NOT use Python built-ins like heapq
'''
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6]

i=0
j=0
merged = []

while i<len(nums1) and j in len(nums2):
    if nums1[i]<nums2[j]:
        merged.append(nums1[i])
        i=i+1
    else:
        merged.append(nums2[j])
        j+=1
    
merged.extend(nums1[i:])
merged.extend(nums2[j:])
print(merged)