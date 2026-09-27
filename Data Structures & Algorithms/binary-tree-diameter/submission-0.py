class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root):
            if not root:
                return 0
            leftLen = dfs(root.left)
            rightLen = dfs(root.right)
            self.diameter = max(self.diameter, rightLen + leftLen)
            return 1 + max(leftLen, rightLen)
        dfs(root)
        return self.diameter