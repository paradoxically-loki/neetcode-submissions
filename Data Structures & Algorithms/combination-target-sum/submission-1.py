class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total+nums[i])  # this must be i, as we're choosing to reuse it

            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res