class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1]*len(nums)
        def helper(i):
            if i >= len(nums):
                return 0
            first = nums[i] + (memo[i+2] if (i+2 < len(nums) and memo[i+2] != -1 ) else helper(i+2))
            second = (memo[i+1] if (i+1 < len(nums) and memo[i+1] != -1) else helper(i+1))
            ans = max(first, second)
            memo[i] = ans
            return ans

        return max(helper(0), helper(1))
        