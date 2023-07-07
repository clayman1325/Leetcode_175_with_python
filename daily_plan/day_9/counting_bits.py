class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        num = [0]
        carry = 0
        for i in range(n):
            next_num = num[0] ^ 1
            carry =  num[0] and 1
            cur_num = [next_num]
            idx = 1
            if carry > 0:
                while carry > 0:
                    cur_val = num[idx] if idx < len(num) else 0
                    next_num = cur_val ^ carry
                    carry = cur_val and carry
                    cur_num.append(next_num)
                    idx += 1
            while idx < len(num):
                cur_num.append(num[idx])
                idx += 1
            num = cur_num
            result.append(sum(num))

        return result