class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def insertLevelOrder(arr, i, n):
            root = None
            if i < n:
                root = TreeNode(arr[i])
                root.left = insertLevelOrder(arr, 2 * i + 1, n)
                root.right = insertLevelOrder(arr, 2 * i + 2, n)

            return root

        ans = []
        q = [root]
        level = 0
        while q:
            current_level = []
            for i in range(len(q)):
                d = q.pop(0)
                if d.left:
                    q.append(d.left)
                if d.right:
                    q.append(d.right)
                current_level.append(d.val)
            if level%2 == 0:
                ans.extend(current_level)
            else:
                ans.extend(current_level[::-1])
            level+=1
        root = None
        n = len(ans)
        root = insertLevelOrder(ans,0,n)
        return root



        # qodd = [2]
        # qeven= []
        # element = 2
        # qeven = [1,2]
        # qeven = [1,2,2]
        # element = 2
        # element.left =2
        # q¿even = 0,0
        # element.right = 1
        # q_even =  0,0, 0,0
        # element = 0
        # qodd = 1,1
        # qodd = 1,1,0
        # qodd = 1,1,0,1,1,0
        # qodd = 1,1,0,1,1,0,2,0,2,2,0