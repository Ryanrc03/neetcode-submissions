class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.res = root.val 
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.res = root.val
            dfs(root.right)
        dfs(root)

        return self.res