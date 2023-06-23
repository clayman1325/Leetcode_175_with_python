class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recBuildSolution(idx, n_list, cur_result, k,results ):
            if(len(cur_result) == k):
                results.append(cur_result)
                return
            if(idx >= len(n_list)): return

            for x in range(idx, n):
                recBuildSolution(x + 1, n_list, cur_result + [n_list[x]], k, results)

            return

        n_list = list(range(1,n + 1))

        results = []
        for x in range(n):
            recBuildSolution(x + 1, n_list, [n_list[x]], k, results)

        return results