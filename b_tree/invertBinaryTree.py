Question 226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
	Def dfs(root)
		if(root is None):
			Return

		Root.left = dfs(root.right)
		Root.right = dfs(root.left)

		Return root

Test:
Input: root = [2,1,3]
Output: [2,3,1]

Root.left = 3
Root.right =1

dfs(3) = 3
dfs(2) = 21


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if(root is None): return None

            left  = dfs(root.right)
            right = dfs(root.left)
            root.left  = left
            root.right = right

            return root


        return dfs(root)


# Pseudo code:
# BFS or DFS works similarly 1st try DFS that is recursive
# Depth tree until reach leave
# When getting back
# Assign right tree to root.left  assing left tree to root.left
