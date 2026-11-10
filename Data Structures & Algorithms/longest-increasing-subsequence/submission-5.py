from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(maxsize = None)
        def dfs(i, j):
            if i == len(nums):
                return 0

            lis = dfs(i+1, j) # not include
            
            if j == -1 or nums[j] < nums[i]:
                lis = max(lis, 1 + dfs(i+1, i))
            
            return lis

        return dfs(0,-1)