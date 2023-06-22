def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    left = 0
    right = m * n -1

    while(left <= right):
        mid = left + (right - left) // 2
        row = mid // n
        col = mid % n

        if(matrix[row][col] == target): return True

        if(matrix[row][col] < target):
            left = mid + 1
        else:
            right = mid - 1

    return False