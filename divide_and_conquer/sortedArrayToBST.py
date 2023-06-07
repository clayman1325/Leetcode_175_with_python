class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide_and_conquer(nums):
            if(len(nums) <= 1):
                return TreeNode(nums[0]) if len(nums) else None

            middle   = len(nums) // 2

            new_node       = TreeNode(nums[middle])
            new_node.left  = TreeNode()
            new_node.right = TreeNode()


            if(middle > 0): new_node.left  = divide_and_conquer(nums[:middle])
            if(middle > 0): new_node.right = divide_and_conquer(nums[middle+1:])


            return new_node


        return divide_and_conquer(nums)