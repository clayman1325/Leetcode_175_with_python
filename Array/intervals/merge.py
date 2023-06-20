class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if(len(intervals) < 1): return result
        intervals.sort()
        i = 0
        j = i+1
        while(j < len(intervals)):
            if(intervals[i][1] < intervals[j][0]):
                result.append(intervals[i])
            elif(intervals[i][1]>= intervals[j][1]):
                intervals[j] = intervals[i]
            else:
                intervals[j][0] = intervals[i][0]

            i += 1
            j += 1

        result.append(intervals[len(intervals) - 1])

        return result