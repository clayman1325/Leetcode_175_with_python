class HitCounter:
    def __init__(self):
        self.queue = []

    def hit(self, timestamp: int) -> None:
        if self.queue:
            last_record = self.queue[0][0]
            if last_record == timestamp:
                self.queue[0].append(timestamp)
            else:
                self.queue.insert(0,[timestamp])
        else:
            self.queue.insert(0,[timestamp])

    def getHits(self, timestamp: int) -> int:
        time_now = timestamp
        count = 0
        for i in range(len(self.queue)):
            if time_now - self.queue[i][0] < 300:
                count += len(self.queue[i])
        return count