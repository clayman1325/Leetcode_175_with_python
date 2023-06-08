class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        while(y):
            print(x, y)
            sum = x ^ y

            carry = (x & y) << 1
            x = sum
            y = carry

        return bin(x)[2:]