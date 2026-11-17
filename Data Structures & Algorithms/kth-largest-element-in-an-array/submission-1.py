class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickselect(left, right):
            pivot = nums[right]
            p = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[right], nums[p] = nums[p], nums[right]

            if p > k: 
                return quickselect(left, p - 1) # left side
            elif p < k: 
                return quickselect(p + 1, right)
            else:  
                return nums[p]
        return quickselect(0, len(nums) - 1)