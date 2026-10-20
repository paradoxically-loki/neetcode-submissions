class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, curr, currSum):
            if currSum > target or i >= len(nums):
                return

            if currSum == target:
                res.append(curr[:])
                return

            # inclusion
            curr.append(nums[i])
            dfs(i, curr, currSum + nums[i])

            # exclusion
            curr.pop()
            dfs(i+1, curr, currSum)

        dfs(0, [], 0)
        return res
        