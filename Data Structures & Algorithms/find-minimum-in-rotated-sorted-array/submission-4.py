class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while l < r:
            mid = (r-l)//2+l
            if nums[mid] > nums[r]: # concept of drop point. the drop point is in right
                l = mid+1
            else:
                r = mid

        return nums[l]

    # key property: one half is sorted and minimum is in the unsorted part
        