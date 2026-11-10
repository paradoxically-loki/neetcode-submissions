from functools import lru_cache
class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     @lru_cache(maxsize=None)
    #     def dfs(i):
    #         if i >= len(nums):
    #             return 0

    #         take = nums[i] + dfs(i+2)
    #         notTake = dfs(i+1)

    #         return max(take, notTake)

    #     return dfs(0)

    def rob(self, nums):
        a, b = 0, 0
        for i in range(len(nums)-1, -1, -1):
            b, a = max(nums[i] + a, b), b
        return b