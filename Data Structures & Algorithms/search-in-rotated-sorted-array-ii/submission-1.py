class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (r - l)//2 + l

            if nums[mid] == target: return True

            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else: # the only tricky case if when nums[l] == nums[mid], this is when we can't tell which half is sorted. in this case, we simply try again with l += 1
                l += 1

        return False
        