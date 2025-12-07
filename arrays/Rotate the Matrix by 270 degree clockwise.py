'''
Docstring for Rotate the Matrix by 270 degree clockwise

🧠 Two Approaches for 270° Rotation:

1. Approach 1 → Transpose + Reverse Columns
(Same as 90° anti-clockwise)

You already know this.
That alone rotates 90° anti-clockwise = 270° clockwise.

2.Approach 2 → Reverse Rows + Transpose
-----------------------------------------
This is the classic formula for 270°.
✔ Reverse each row
✔ Then transpose

This rotates the matrix 270° clockwise.

Let's do this one now because it's NEW.
'''

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

n = len(matrix)

# STEP 1: Reverse rows
matrix.reverse()
print(matrix)

# STEP 2: Transpose
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
