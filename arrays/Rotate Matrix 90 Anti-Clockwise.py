# Rotate Matrix 90° Anti-Clockwise

'''
Docstring for Rotate Matrix 90° Anti-Clockwise

⭐ Key Concept

Clockwise was:
Transpose
Reverse each row

Anti-clockwise flips the operations:
To rotate 90° anti-clockwise:
👉 Step 1: Transpose the matrix
(same as before)

👉 Step 2: Reverse each column
(not rows this time)

That's it.
'''

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

n=len(matrix)
print(matrix)
# Step 1 : Transpose matrix

for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # print(f"for {i} and {j} the matrix is: {matrix}")                  #for debugging

print(f'Transposed Matrix:{matrix}')

# for column in matrix:
#     column.reverse()                    <---------> THIS IS WRONG FOR ANTICLOCKWISE AS THIS LOGIC REVERSES ROWS not COLUMNS

# print(f"Rotated Matrix: {matrix}")        

for col in range(n):
    top = 0
    bottom = n-1
    while top<bottom:
        matrix[top][col],matrix[bottom][col] = matrix[bottom][col],matrix[top][col]
        top +=1
        bottom -=1
    print(f"for col:{col}, top:{top}, bottom:{bottom} the matrix is:{matrix} ")

print(f"90 degree Anticlockwise Rotated Matrix:{matrix}")


'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Transposed Matrix:[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
for col:0, top:1, bottom:1 the matrix is:[[3, 4, 7], [2, 5, 8], [1, 6, 9]]
for col:1, top:1, bottom:1 the matrix is:[[3, 6, 7], [2, 5, 8], [1, 4, 9]]
for col:2, top:1, bottom:1 the matrix is:[[3, 6, 9], [2, 5, 8], [1, 4, 7]]
90 degree Anticlockwise Rotated Matrix:[[3, 6, 9], [2, 5, 8], [1, 4, 7]]
'''