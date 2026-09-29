class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * (n)
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]