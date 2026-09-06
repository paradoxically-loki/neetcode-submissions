class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(i, amount):
            if i == len(nums) and amount == target:
                return 1

            if i >= len(nums):
                return 0

            if (i, amount) in memo:
                return memo[(i, amount)]

            memo[(i,amount)] = dfs(i+1, amount + nums[i]) + dfs(i+1, amount - nums[i])
            return memo[(i, amount)]

        return dfs(0, 0)