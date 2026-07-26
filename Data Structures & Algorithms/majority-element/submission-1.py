class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq = {}
        # for i, num in enumerate(nums):
        #     if num in freq:
        #         freq[num] +=1
        #     else:
        #         freq[num] = 1
        
        # for key in freq:
        #     if freq[key] > len(nums)/2:
        #         return key
        # return -1

    
        # Boyer Moore's Voting Algorithm
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate != num:
                count -= 1
            else:
                count += 1
        return candidate

        