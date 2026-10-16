class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0

        l, r = 0, n - 1
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax <= rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res