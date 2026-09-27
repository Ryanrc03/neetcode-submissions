class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums:
            # start case
            if num - 1 not in s:
                cur = num + 1
                curLen = 1
                while cur in s:
                    curLen += 1
                    cur += 1
                longest = max(longest, curLen)
        return longest