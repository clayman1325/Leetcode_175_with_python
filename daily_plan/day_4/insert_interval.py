class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if(len(intervals) < 1): return [newInterval]
        if(newInterval[1] < intervals[0][0]):
            intervals.insert(0,newInterval)
            return intervals
        if(newInterval[0] > intervals[len(intervals)-1][1]):
            intervals.append(newInterval)
            return intervals

        for idx in range(len(intervals) - 1):
            if(
                intervals[idx][1] < newInterval[0] and
                intervals[idx + 1][0] > newInterval[1]
            ):
                aux = intervals[0:idx+1] + [newInterval] + intervals[idx+1:]

                return aux

        idx = 0
        while  idx < len(intervals):
            if(
                newInterval[0] < intervals[idx][0] and newInterval[1] > intervals[idx][0] or
                intervals[idx][1] >= newInterval[0]
            ):
                intervals[idx][0] = min(intervals[idx][0], newInterval[0])
                intervals[idx][1] = max(intervals[idx][1], newInterval[1])
                idx = len(intervals)
            else:
                idx += 1
        idx = 0
        while  idx < len(intervals) - 1:
            if intervals[idx][1] >= intervals[idx + 1][0]:
                intervals[idx][0] = min(intervals[idx][0], intervals[idx+1][0])
                intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
                aux = intervals[0:idx+1] + intervals[idx+2:]
                intervals = aux
            else:
                idx += 1