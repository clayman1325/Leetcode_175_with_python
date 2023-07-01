def containsDuplicate(self, nums: List[int]) -> bool:
    dict = {}

    for x in nums:
        if(dict.get(x)): return True
        dict[x] = 1

    return False