class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i) 
            else:
                i += 1
        return i
        
        
# nums.pop(i) removes the ith index element
# nums.remove(val) removes by value (only the first occurence)