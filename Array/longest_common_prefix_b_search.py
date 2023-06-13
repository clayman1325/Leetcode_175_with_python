class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == None or len(strs) == 0): return ""
        if(strs[0] == ""): return ""
        def binary_search(l, r, strs):
            while(l < r):

                pivot = (l + r) // 2

                equal  = True
                target = strs[0][pivot]

                for x in range(len(strs)):
                    if(strs[x][pivot] != target): equal = False

                if(equal):
                    l = pivot + 1
                else:
                    r = pivot - 1
            print(r)
            return r

        min_length = 10000
        for x in strs:
            min_length = min(min_length, len(x))

        for x in range(len(strs)):
            strs[x] = strs[x][:min_length]

        end_idx = binary_search(0, min_length, strs)
        end_idx = end_idx + 1 if strs[0][0] == strs[1][0]  else 0
        return strs[0][:end_idx]