class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = [False] * (1440 + 720)
        visited = set()
        for time in timePoints:
            hour, min = time.split(":")
            minutes = int(hour) * 60 + int(min)
            if minutes in visited: return 0
            if minutes < 720 :
                arr[minutes + 1440] = minutes + 1440
            arr[minutes] = minutes
            visited.add(minutes)

        min_time = 1500
        cur_dif = 1500
        prev = arr[0]
        i = 0
        while not prev:
            prev = arr[i]
            i += 1

        for idx in range(i, len(arr)):
            if arr[idx]:
                cur_dif = arr[idx] - prev
                prev = arr[idx]
                if min_time > cur_dif: min_time = cur_dif

        return min_time


    def findMinDifference2(self, timePoints: List[str]) -> int:
        arr = []
        for time in timePoints:
            hour, min = time.split(":")
            if int(hour) * 60 + int(min) < 720 :
                arr.append(1440 + int(hour) * 60 + int(min))
            arr.append(int(hour) * 60 + int(min))

        dict = {}
        for time in arr:
            if dict.get(time):
                dict[time] += 1
            else:
                dict[time] = 1
        for key in dict:
            if dict[key] > 1: return 0
        visited = set()
        min_time = 1500

        for key in dict:
            time = int(key)
            next_time = time + 1
            while(next_time <= 1440 + 721):
                if dict.get(next_time) and dict[next_time]:
                    cur_diff = next_time - int(time)
                    if min_time > cur_diff: min_time = cur_diff
                    visited.add(next_time)
                    time = next_time
                next_time += 1