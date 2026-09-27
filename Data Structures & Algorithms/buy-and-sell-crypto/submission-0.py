class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0 
        while r < len(prices):

            # case to move Left
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            # case to expend right
            else:
                curP = prices[r] - prices[l]
                maxP = max(curP, maxP)
                r += 1
        return maxP