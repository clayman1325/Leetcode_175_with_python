    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        i = 0
        subArray = []
        curSubArrSum = 0

        nums.sort(reverse=True)

        for i in range(0, len(nums)):
            curSubArrSum += nums[i]
            subArray.append(nums[i])
            if(curSubArrSum >= target):
                return len(subArray)


        return 0