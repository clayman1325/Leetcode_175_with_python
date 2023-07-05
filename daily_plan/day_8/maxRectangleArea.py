class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        if(len(height) < 1): return max_area

        while(l < r):
            area = (r - l) * min(height[r], height[l])
            max_area = max(max_area, area)

            if(height[r] < height[l]):
                r -= 1
            else:
                l += 1
        return max_area