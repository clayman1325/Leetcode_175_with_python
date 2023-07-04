class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key):
            self.store[key].append([timestamp, value])
        else:
            self.store[key] = [[timestamp, value]]


    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key): return ""

        values = self.store[key]

        if(values[0][0] > timestamp): return ""

        if(values[len(values) - 1][0] <= timestamp): return values[len(values) - 1][1]
        print("david mejia")
        for idx in range(len(values)):
            value = values[idx]
            next_idx = idx + 1
            if(next_idx == len(values)): next_idx = len(values) - 1
            next_value = values[next_idx]
            print(timestamp, value[0], next_value[0])
            print(value[0] >= timestamp, value[1])
            if(next_value[0] > timestamp and value[0]<= timestamp): return value[1]
