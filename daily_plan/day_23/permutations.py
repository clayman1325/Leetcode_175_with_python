class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursivePermutations(cur_permutation):
            if len(cur_permutation) == len(nums):
              result.append(cur_permutation[:])
              return

            for num in nums:
              if num not in cur_permutation:
                cur_permutation.append(num)
                recursivePermutations(cur_permutation)
                cur_permutation.pop()
        result = []
        recursivePermutations([])
        return result