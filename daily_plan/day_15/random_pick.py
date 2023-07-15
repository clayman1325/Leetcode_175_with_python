class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for i in range((len(w))):
            prefix_sum += w[i]
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum  * random.random()
        left = 0
        right = len(self.prefix_sums)
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left