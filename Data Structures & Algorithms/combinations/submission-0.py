class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        nums = []
        for i in range(1,n+1):
            nums.append(i)

        subset = []
        def dfs(i):
            if i >= len(nums):
                if len(subset) == k:
                    res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
        