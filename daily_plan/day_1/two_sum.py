def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    for x in range(len(nums)):
        dict[target - nums[x]] = x

    for x in range(len(nums)):
        if(dict.get(nums[x]) and x != dict[nums[x]]):
            return [x, dict[nums[x]]]
