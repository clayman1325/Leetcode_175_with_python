class Solution:
    def reverseBits(self, n: int) -> int:
        sum = 0
        pow = 31
        while(n):
            cur = n & 1
            n = n >> 1
            sum += cur * 2 ** pow
            pow -= 1

        return sum