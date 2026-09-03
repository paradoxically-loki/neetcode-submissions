class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        nums[-2] = max(nums[-2], nums[-1])
        for i in range(len(nums)-3, -1, -1):
            first = nums[i] + nums[i+2]
            second = nums[i+1]
            out = max(first, second)
            nums[i] = out

        return max(nums[0], nums[1])
        