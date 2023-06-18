def rotate2(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 0
    while(count < k):
        swap = 0
        aux = nums[swap]
        while(swap < len(nums)-1):
            next_aux = nums[swap+1]
            nums[swap+1] = aux
            aux = next_aux
            swap += 1
        nums[0] = aux
        count += 1