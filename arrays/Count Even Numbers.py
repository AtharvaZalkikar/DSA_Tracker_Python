'''
🧩 Task 2 — Count how many numbers are even

Input → [3, 8, 12, 5, 7, 6]
Output → 3 (because 8, 12, 6 are even)
'''

nums = [3, 8, 12, 5, 7, 6]
even_count = 0

for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:                  #can skip the else loop - The else: pass isn’t wrong, but it’s not needed — Python just skips the rest of the loop body if the if condition isn’t met.
        pass

print(even_count)
