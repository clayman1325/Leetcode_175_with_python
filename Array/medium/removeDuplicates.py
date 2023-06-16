def removeDuplicates(self, nums: List[int]) -> int:
    def reorder(p, nums, limit):
        while(p < limit):
            aux = nums[p]
            nums[p] = nums[p+1]
            nums[p+1] = aux
            p += 1
        return nums
    l = 0
    r = 0
    equals = 0
    count = 0
    while(r < len(nums) - 1):
        if(nums[r] != nums[r+1]):
            l = r + 1
            count = 0
        else:
            count += 1
        if(count > 1 and r < len(nums) - 1 and  len(nums)-1-equals >= 0):
            aux = nums[r]
            nums[r] = nums[len(nums)-1-equals]
            nums[len(nums)-1-equals] = aux
            equals += 1
            nums = reorder(r, nums,len(nums)-1-equals)
            r -= 1
        r+=1

    return len(nums) - equals