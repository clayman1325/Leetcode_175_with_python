class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        power   = 31

        while(n):
            print(reverse)
            reverse += (n & 1) << power
            n = n >> 1
            power -= 1
        return reverse