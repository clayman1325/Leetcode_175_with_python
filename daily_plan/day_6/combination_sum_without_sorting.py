class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(index, seq, target, result):
            print(index)
            if target == 0:
                result.append(seq[:])
                return

            if index >= len(candidates):
                return

            if candidates[index] <= target:
                seq.append(candidates[index])
                solve(index, seq, target - candidates[index],result)
                seq.pop()

            solve(index + 1, seq, target,result)

        seq = []
        result = []
        solve(0, seq, target, result)

        return result