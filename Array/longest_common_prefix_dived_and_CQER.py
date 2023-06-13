class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def calculate_com_prefix(str1, str2):
            prefix = ""
            idx = 0
            while(
                idx < len(str1) and
                idx < len(str2) and
                str1[idx] == str2[idx]
            ):
                prefix += str1[idx]
                idx += 1

            return prefix

        def divide_and_conquer(strs):
            if(len(strs) == 1): return strs[0]
            if(len(strs) == 2):
                return calculate_com_prefix(strs[0], strs[1])

            mid = len(strs) // 2

            str1 = strs[:mid]
            str2 = strs[mid:]

            prefix1 = divide_and_conquer(str1)
            prefix2 = divide_and_conquer(str2)

            return calculate_com_prefix(prefix1, prefix2)

        return divide_and_conquer(strs)
