from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(maxsize = None)
        def dfs(total):
            if total == amount:
                return 0
            if total > amount:
                return float('inf')

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(total + coin))
            return res

        minCoins = dfs(0)
        return -1 if minCoins == float('inf') else minCoins

    

