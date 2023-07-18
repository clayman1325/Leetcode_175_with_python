class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        self.aux = None

    def insert(self, val: int) -> bool:
        if val in self.dict: return False

        self.dict[val] = len(self.list)
        self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element = self.list[-1]
            idx =  self.dict[val]
            self.list[idx] = last_element
            self.dict[last_element] = idx
            self.list.pop()
            del self.dict[val]
            return True
        return False