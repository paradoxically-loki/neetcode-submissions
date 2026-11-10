class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1
        for num in nums:
            tmp = (num, num * curr_min, num * curr_max)
            curr_min, curr_max = min(tmp), max(tmp)
            res = max(res, curr_max)
        return res