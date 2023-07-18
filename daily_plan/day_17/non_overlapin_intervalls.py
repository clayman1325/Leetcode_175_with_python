class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        k = -1000000
        intervals.sort(key= lambda prop: prop[1])
        print(intervals)
        count = 0
        for i in range(len(intervals)):
            start = intervals[i][0]
            finish = intervals[i][1]
            if start >= k:
                k = finish
            else:
                count += 1
        return count