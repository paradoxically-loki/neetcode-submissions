from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(i, currSum):

            if i == len(nums) and currSum == target:
                return 1

            if i >= len(nums):
                return 0

            return dfs(i+1, currSum + nums[i]) + dfs(i+1, currSum - nums[i])

        return dfs(0,0)
            
            
        