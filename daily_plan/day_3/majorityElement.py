def majorityElement(self, nums: List[int]) -> int:
    if(len(nums) < 2): return nums[0]
    threshold = len(nums) // 2
    nums.sort()
    return nums[threshold]

    dict = {}
    for x in nums:
        if(dict.get(x)):
            dict[x] += 1
            if(dict[x] > threshold): return x
        else:
            dict[x] = 1