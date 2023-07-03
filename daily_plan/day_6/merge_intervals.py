class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def my_function(interval):
            return interval[0]

        if(len(intervals) == 1): return intervals

        i = 1
        intervals.sort(key=my_function)
        new_intervals = [intervals[0]]
        while i < len(intervals):
            l = len(new_intervals) - 1
            if new_intervals[l][1] >= intervals[i][0]:
                new_intervals[l][1] = max(intervals[i][1], new_intervals[l][1])
            else:
                new_intervals.append(intervals[i])
            i +=1

        l = len(intervals) - 1
        if new_intervals[len(new_intervals) - 1][1] < intervals[l][1]:
            new_intervals.append(intervals[l])
        return new_intervals