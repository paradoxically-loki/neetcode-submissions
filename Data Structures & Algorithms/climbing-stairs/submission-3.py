from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(maxsize = None)
        def helper(i):
            if i >= n:
                return i == n

            return helper(i+1) + helper(i+2)

        return helper(0)
        