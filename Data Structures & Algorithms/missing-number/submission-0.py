class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_actual = sum(nums)
        sum_theoritical = (n/2)*(n+1)
        return int(sum_theoritical - sum_actual)
        