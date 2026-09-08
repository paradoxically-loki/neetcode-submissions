from functools import lru_cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(i):

            if i >= len(nums) - 1:
                return 0

            if nums[i] == 0:
                return float('inf')

            ans = float('inf')
            for j in range(1, nums[i]+1):
                ans = min(ans, dfs(i+j) + 1)

            return ans
        
        return dfs(0)

