def findPeakElement(self, nums: List[int]) -> int:
    def b_search(l,r, nums):
        if(l <= r):
            m = (l + r) // 2

            if(nums[m] > nums[m-1] and nums[m] > nums[m+1]):
                return m

            left  = b_search(l,   m-1,nums)
            right = b_search(m+1, r,  nums)
            return left or right
        return False

    n = len(nums)
    if(n == 1 or nums[0] > nums[1]): return 0
    if(nums[n-1] > nums[n-2]): return n - 1
    return b_search(0, n-1, nums)

def findPeakElement(self, nums: List[int]) -> int:
    n = len(nums)
    l = 0
    r = n - 1
    while(l < r):
        mid = (l+r) // 2

        if(nums[mid] < nums[mid+1]):
            l = mid + 1
        else:
            r = mid
    return l
