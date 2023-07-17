class Solution:
    def decodeString(self, s: str) -> str:
        def buid_string(num, chars):
            string = ""
            count = 0
            while count < num:
                string += chars
                count += 1
            return string

        nums = set(["0","1","2","3","4","5","6","7","8","9"])
        stack = []
        chars = ""
        num = ""
        for idx in range(len(s)):
            if s[idx] == "]":
                char_queue = []
                num_queue = []
                while(stack[-1] != "["):
                    char_queue.insert(0, stack.pop())
                stack.pop()
                while stack and stack[-1] in nums:
                    num_queue.insert(0, stack.pop())
                str = buid_string(int("".join(num_queue)), "".join(char_queue))
                stack.append(str)
                chars = ""
                num = ""
            else:
                stack.append(s[idx])
        return "".join(stack)
