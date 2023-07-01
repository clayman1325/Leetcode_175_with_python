def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    def my_func(interval):
        return interval[0]

    intervals.sort(key=my_func)
    for idx in range(len(intervals) - 1):
        if(intervals[idx][1] > intervals[idx + 1][0]): return False
    return True