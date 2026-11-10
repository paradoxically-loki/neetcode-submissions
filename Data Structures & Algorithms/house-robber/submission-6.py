from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= len(nums):
                return 0

            take = nums[i] + dfs(i+2)
            notTake = dfs(i+1)

            return max(take, notTake)

        return dfs(0)