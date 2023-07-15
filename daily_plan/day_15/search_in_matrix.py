class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left  = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2
            row = min(mid // m, n - 1)
            col = min(mid % m, m -1)

            candidate = matrix[row][col]

            if candidate == target: return True

            if candidate > target:
                right = mid-1
            else:
                left = mid + 1

        return False