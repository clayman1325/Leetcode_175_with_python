class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      def find_min_prefix(word1, word2):
        prefix = ""
        idx = 0
        while(idx < min(len(word1), len(word2)) and word1[idx] == word2[idx]):
          prefix += word1[idx]
          idx +=1
        return prefix
      def divide_and_conquer(input):
        if len(input) == 1: return input[0]
        if len(input) == 2:
          return find_min_prefix(input[0], input[1])

        left = input[:len(input)//2]
        right = input[len(input)//2:]

        word1 = divide_and_conquer(left)
        word2 = divide_and_conquer(right)

        return find_min_prefix(word1, word2)

      if len(strs) < 2: return strs[0] if len(strs) == 1 else ""

      return divide_and_conquer(strs)