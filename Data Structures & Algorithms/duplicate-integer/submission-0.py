class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        lookup = set()
        for i, num in enumerate(nums):
            if num in lookup:
                return True
            else:
                lookup.add(num)
        return False

        