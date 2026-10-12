class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n^2) solution exists

        maxProf = 0

        l = 0

        for r in range(1, len(prices)):

            currProf = prices[r] - prices[l]

            maxProf = max(maxProf, currProf)

            if prices[r] < prices[l]:
                l = r

        return maxProf
        