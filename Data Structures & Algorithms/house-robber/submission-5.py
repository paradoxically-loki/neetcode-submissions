from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize = None)
        def dfs(i):
            if i == len(nums)-1:
                return nums[i]

            if i > len(nums):
                return 0

            one = dfs(i+2) + (nums[i] if i < len(nums) else 0)
            two = dfs(i+1)

            return max(one, two)

        return dfs(0)
        