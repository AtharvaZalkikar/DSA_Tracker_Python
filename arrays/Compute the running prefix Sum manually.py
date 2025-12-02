# 🧩 Task 5 — Compute the running (prefix) sum manually

# Input → [1, 2, 3, 4]
# Output → [1, 3, 6, 10]

nums = [1, 2, 3, 4]
prefix = [0]*len(nums)

prefix[0]=nums[0]
print(prefix)

for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

print(prefix)
    