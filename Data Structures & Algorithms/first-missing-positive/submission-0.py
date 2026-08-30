class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)

        num = 1
        while True:
            if num not in seen:
                return num
            num += 1

        