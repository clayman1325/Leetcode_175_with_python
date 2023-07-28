class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda prop: prop[1])
        shoot = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if not (points[i][0] <= shoot and shoot <= points[i][1]):
                shoot = points[i][1]
                count += 1
        return count