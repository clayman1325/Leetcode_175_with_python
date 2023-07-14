class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
      if not nums: 0
      cum_sum = [0] * len(nums)
      cum_sum.append(0)
      idx = 1
      for num in nums:
        sum = 1 if num == 1 else -1
        sum += cum_sum[idx - 1]

        cum_sum[idx] += sum
        idx += 1

      dict = Counter(cum_sum)
      crossed = {}

      for idx in range(len(cum_sum)):
        value = cum_sum[idx]
        if crossed.get(value):
          crossed[value].append(idx)
        else:
          crossed[value] = [idx]

      max_length = 0
      for key in crossed:
        cur_length = crossed[key][-1] - crossed[key][0]
        max_length = max(max_length, cur_length)
      return max_length