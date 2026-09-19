class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minSoFar = prices[0]
        maxProfit = 0

        for price in prices:
            currProfit = price - minSoFar
            maxProfit = max(maxProfit, currProfit)
            minSoFar = min(minSoFar, price)

        return maxProfit
