class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda prop: prop[0] )
        rooms = 0
        busy_rooms = 0
        last_time = []

        for i in range(len(intervals)):
            interval = intervals[i]
            while last_time and last_time[-1] <= interval[0]:
                last_time.pop()
                busy_rooms -= 1
            if rooms <= busy_rooms:
                rooms += 1
            busy_rooms +=1
            last_time.append(interval[1])
            last_time.sort()
            last_time.reverse()

        return rooms