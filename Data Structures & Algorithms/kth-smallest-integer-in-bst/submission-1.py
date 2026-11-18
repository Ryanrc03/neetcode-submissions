class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        cnt = k
        res = root.val

        def dfs(root):
            nonlocal cnt, res
            # base case
            if not root:
                return
            
            # find smallest 
            dfs(root.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = root.val
                return
            dfs(root.right)
        dfs(root)
        return res