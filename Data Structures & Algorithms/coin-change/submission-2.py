from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)

        @lru_cache(maxsize = None)
        def dfs(i, required):
            if required == 0:
                return 0
            if required < 0 or i >= len(coins):
                return float('inf')

            take = 1 + dfs(i,required - coins[i])
            skip = dfs(i+1, required)

            return min(take, skip)


        return dfs(0,amount) if dfs(0, amount) != float('inf') else -1




        
        