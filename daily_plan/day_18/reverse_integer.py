class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0

        lst = list(str(x))

        sign = lst.pop(0) if lst[0] == "-" else "+"
        while(lst and lst[-1] == "0"):
            lst.pop()
        lst.reverse()

        number = "".join(lst)
        number = int(number)

        if number > 2147483647: return 0

        return number if sign == "+" else -1 * number