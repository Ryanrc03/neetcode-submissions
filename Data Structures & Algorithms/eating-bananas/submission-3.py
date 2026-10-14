class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def canFinish(speed):
            time = 0
            for pile in piles:
                time += (pile + speed - 1) // speed # upper 
            return time <= h

        # binary search
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if canFinish(mid): # search in left
                r = mid
            else:
                l = mid + 1
        return l