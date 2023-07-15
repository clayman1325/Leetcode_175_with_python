class Solution:
    def myPow(self, x: float, n: int) -> float:
        count = 0
        value = 1
        m = n
        while(abs(n) > 0):
            if n % 2 == 1:
                value *= x
            x *= x
            n = abs(n)//2
        print(value)
        if m < 0: value = float(1/value)

        return value