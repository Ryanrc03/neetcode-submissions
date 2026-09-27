class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            levelNode = []
            for i in range(len(q)):
                node = q.popleft()
                levelNode.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelNode)
        return res