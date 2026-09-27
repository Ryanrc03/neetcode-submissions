class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mid > r, right
        # mid < r, sorted, left
        # 5 1 2 3 4 

        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
            # binary
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return res