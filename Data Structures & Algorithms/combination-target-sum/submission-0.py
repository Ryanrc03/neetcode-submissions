class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i, cur, total):
            # find target
            if total == target:
                res.append(cur.copy())
                return
            # cut leaf
            elif total > target or i >= len(candidates):
                return
            

            # choose
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])

            # not choose
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, cur, 0)
        return res