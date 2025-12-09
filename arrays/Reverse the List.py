'''
🧩 Task 1 — Print all elements in reverse order

Without using reversed() or slicing ([::-1]), print each element from the end to the start.

Example:
Input → [10, 20, 30, 40]
Output →

40
30
20
10
'''


nums = [10, 20, 30, 40]
reverse = []

for i in range(len(nums)):
    reverse.append(nums[-(i+1)])

print(reverse) #prints list named reverse


#💡 Alternative (simpler) approach

for i in range(len(nums)-1, -1, -1):
    print(nums[i])
