#3 Task 3: Find the second largest element (without using sort)?

'''
🧩 Task 3 — Find the second largest element (without using sort)

Input → [10, 20, 4, 45, 99]
Output → 45

Hint: Keep track of both largest and second_largest while looping.
'''

nums = [10,20,45,4,99]

largest = float('-inf')
second_largest = float('-inf')

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)