from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(maxsize = None)
        def dfs(curr,prev):
            if curr == len(nums):
                return 0

            LIS = dfs(curr+1,prev) # not include the current one

            if prev == -1 or nums[prev] < nums[curr]:
                LIS = max(LIS, 1 + dfs(curr+1, curr)) # include

            return LIS

        return dfs(0,-1)
            
        