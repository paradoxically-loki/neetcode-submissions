class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        memo = {}

        def dfs(i, flag):
            if i == len(nums)-1:
                return max(0,nums[i]) if flag else nums[i]

            if (i, flag) in memo: return memo[(i,flag)]

            ans = None
            if flag:
                ans = max(0, nums[i] + dfs(i+1, True))
            else:
                ans = max(dfs(i+1, False), nums[i]+dfs(i+1, True))

            memo[(i, flag)] = ans
            return ans

        return dfs(0, False)
        