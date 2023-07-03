def backtrack(candidates, sum, cur_result, results):
    if(sum == target):
        cur_result.sort()
        if cur_result not in results: results.append(cur_result)
        return
    if(sum > target): return

    for num in candidates:
        next_result = cur_result + [num]
        backtrack(candidates, sum + num, next_result, results)

results = []
backtrack(candidates, 0, [], results)
return results