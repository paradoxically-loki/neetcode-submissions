class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        # for each number, run a two pointer search?

        res = set()

        for i in range(len(nums)):
            target = - nums[i]

            l = i + 1; r = len(nums) -1

            while l < r:
                current = nums[l] + nums[r]

                if current == target:
                    res.add((nums[i], nums[l], nums[r]))
                    
                    # while l < r and nums[l+1] == nums[l]:
                    #     l += 1
                    # while l < r and nums[r-1] == nums[r]:
                    #     r -= 1

                    l += 1
                    r -= 1

                elif current < target:
                    l += 1

                else:
                    r -= 1

        ans = []
        for (val1, val2, val3) in res:
            ans.append([val1, val2, val3])

        return ans