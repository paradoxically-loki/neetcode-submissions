class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res: int = len(nums)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right - left)//2 + left
            if nums[mid] == target: return mid
            elif nums[mid] > target: 
                res = mid
                right = mid - 1
            else: left = mid + 1
        return res