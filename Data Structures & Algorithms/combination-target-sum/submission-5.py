class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        nums.sort()

        def dfs(i, curr):
            if i == len(nums):
                if curr == target:
                    res.append(path[:])
                    return
                return
            if curr > target:
                return
            path.append(nums[i])
            dfs(i, curr + nums[i])
            path.pop()
            dfs(i+1, curr)

        dfs(0, 0)
        return res
