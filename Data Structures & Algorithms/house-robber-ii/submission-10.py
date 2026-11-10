class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(arr):
            a = b = 0
            for num in arr:
                a, b = b, max(a + num, b)
            return b

        if len(nums) == 1:
            return nums[0]

        return max(dfs(nums[1:]), dfs(nums[:-1]))
        