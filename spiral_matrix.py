matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

if not matrix or not matrix[0]:
             print('error')

res = []
top, bottom = 0, len(matrix) - 1
left, right = 0, len(matrix[0]) - 1

while left <= right and top <= bottom:
    # Traverse top row
    
    for i in range(left, right + 1):
        res.append(matrix[top][i])
    top += 1

    # Traverse right column
    for i in range(top, bottom + 1):
        res.append(matrix[i][right])
    right -= 1

    # Check if there's still a valid row and column to traverse
    if top <= bottom:
        # Traverse bottom row
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        # Traverse left column
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

print(res)