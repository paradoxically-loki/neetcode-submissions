class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0]*n
        right_max[-1] = nums[-1]
        suffix_sum = nums[-1]

        for i in range(n-2,-1,-1):
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i+1], suffix_sum)

        max_sum = nums[0]
        curr_max = 0
        prefix_sum = 0

        for i in range(n):
            curr_max = max(curr_max, 0) + nums[i]
            max_sum = max(max_sum, curr_max)
            prefix_sum += nums[i]
            if i + 1 < n:
                max_sum = max(max_sum, prefix_sum + right_max[i+1])
        
        return max_sum
        