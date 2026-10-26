class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        mem = [[-1] * (n + 1) for _ in range(n)]
        
        def dfs(i, prev):
            if i == n:
                return 0

            if mem[i][prev + 1] != -1:
                return mem[i][prev + 1]
            # skip
            LIS = dfs(i + 1, prev)

            # take
            if nums[prev] < nums[i] or prev == -1:
                LIS = max(LIS, 1+ dfs(i + 1, i))
                mem[i][prev + 1] = LIS
            return LIS
        return dfs(0, -1)