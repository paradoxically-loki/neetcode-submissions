class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, curr = [], []
        used = [False] * len(nums)

        def dfs(i):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i, n in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    curr.append(n); dfs(i+1); curr.pop()
                    used[i] = False

        dfs(0)
        return res

            