class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if not nums: return 0

      validator = set(nums)
      max_length = 1

      for num in validator:
        if num - 1 not in validator:
          cur_length = 1
          seq_num = num
          while seq_num + 1 in validator:
            cur_length += 1
            seq_num += 1
          max_length = max(max_length, cur_length)

      return max_length