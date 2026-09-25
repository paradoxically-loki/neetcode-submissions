class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtracking(i, current):
            if i == n:
                res.append(current[:])
                return

            backtracking(i+1, current) # exclude
            current.append(nums[i])
            backtracking(i+1, current) # include

            current.pop()

        backtracking(0, [])
        return res

        