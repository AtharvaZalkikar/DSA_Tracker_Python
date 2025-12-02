'''
Concept: Updating an Element and Fixing the Prefix Array

nums   = [3, 1, 4, 1, 5]
prefix = [3, 4, 8, 9, 14]

Now you update one element, for example:
nums[2] = 10  # (you changed index 2 from 4 → 10)

So your array becomes:
nums = [3, 1, 10, 1, 5]

🧠 What happens to prefix now?

Since only index 2 and everything after it is affected,
you don’t need to rebuild the entire prefix from scratch.
You can just recompute from that index onward:

for i in range(2, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

✅ Updated Prefix:

prefix = [3, 4, 14, 15, 20]

🔍 Summary:
| Operation               | Complexity | When to Use                 |
| ----------------------- | ---------- | --------------------------- |
| Build full prefix       | O(n)       | First time only             |
| Add new element         | O(1)       | Append case                 |
| Update existing element | O(n - i)   | Only from that index onward |

----------------------------------------------------------------------

Now, your turn 🎯
Try to:

Build prefix for [3, 1, 4, 1, 5]

Change the element at index 2 → 10

Efficiently fix the prefix using the logic above

Print updated nums and prefix

Then we’ll verify your result together.
'''

nums = [3, 1, 4, 1, 5]

print(f"nums is :{nums}")

prefix = [0]*len(nums)

prefix[0] = nums[0]

for i in range(1,len(nums)):
    prefix[i] = prefix[i-1]+nums[i]

print(f"First prefix: {prefix}")

# now change element at index 2

nums[2] = 10
print(f"New updated nums[] list is:{nums}")

#so fix the prefix

for i in range(2,len(nums)):
    prefix[i] = prefix[i-1]+nums[i]

print(f"New updated prefixt is:{prefix}")
