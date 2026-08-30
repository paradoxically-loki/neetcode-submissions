sys.setrecursionlimit(10000)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.backtrack(0, nums)
        return self.res

    def backtrack(self, idx, nums):
        if idx == len(nums):
            self.res.append(nums[:])
            return

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[idx]:
                continue

            nums[i], nums[idx] = nums[idx], nums[i]
            self.backtrack(idx+1, nums)

        
        for j in range(len(nums)-1, idx, -1):
            nums[j], nums[idx] = nums[idx], nums[j]
            
        

        