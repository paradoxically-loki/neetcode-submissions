class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:]) # this slicing is important else we simply reference the same list
                return

            # inclusion
            subset.append(nums[i])
            dfs(i+1)

            # exclusion
            subset.pop() # backtracking
            dfs(i+1)


        dfs(0)
        return res