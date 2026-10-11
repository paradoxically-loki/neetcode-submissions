class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        maxLen = 0
        for num in nums:
            if num - 1 not in seen:
                curLen = 1
                while num + curLen in seen:
                    curLen += 1
                maxLen = max(maxLen, curLen)

        return maxLen



        