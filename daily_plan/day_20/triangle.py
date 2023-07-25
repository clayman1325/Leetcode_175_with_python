class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                prev_values = []
                cur_val = triangle[row][col]
                if col < len(triangle[row -1]):
                    prev_values.append(triangle[row-1][col] + cur_val)
                if col - 1 >= 0:
                    prev_values.append(triangle[row-1][col -1] + cur_val)
                triangle[row][col] = min(prev_values)
        return min(triangle[len(triangle) - 1])