class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]: # the whole array is sorted
                res = min(res, nums[l])
                break

            m = (r - l)//2 + l
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # the left half is sorted and we already know the min, so, we go to the right half
                l = m + 1
            else: # same commentary as the previous one
                r = m - 1
        
        return res

        