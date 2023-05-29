def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    row,col=len(matrix),len(matrix[0])-1
    top, bot = 0, row - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    for n in matrix[row]:
        if target==n:
            return True
    return False
print(searchMatrix([[1,3],[5,6]],3))