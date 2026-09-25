class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(i, current):
            if sum(current) == target:
                res.append(current[:])
                return

            if i >= n or sum(current) > target: 
                return

            backtrack(i+1, current) # exclude
            current.append(nums[i])
            backtrack(i, current) # include
            current.pop() # backtrack

        backtrack(0, [])
        return res
        