class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# the core idea is to find numbers from which a sequence may start. this is only possible if this number -1 is not the array. we can see this by forming a set out of the nums array
        