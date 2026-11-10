from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        nums1 = nums[:-1]
        nums2 = nums[1:]

        @lru_cache(maxsize = None)
        def dfs1(i):
            if i >= len(nums1):
                return 0

            return max(nums1[i] + dfs1(i+2), dfs1(i+1))

        @lru_cache(maxsize = None)
        def dfs2(j):
            if j >= len(nums2):
                return 0

            return max(nums2[j] + dfs2(j+2), dfs2(j+1))

        return max(dfs1(0), dfs2(0))