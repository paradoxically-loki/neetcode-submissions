class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(0, nums)
        return self.res

    def backtrack(self, idx, nums):
        if idx == len(nums):
            self.res.append(nums[:])
            return

        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(idx+1, nums)
            nums[idx], nums[i] = nums[i], nums[idx]


        

    
                    