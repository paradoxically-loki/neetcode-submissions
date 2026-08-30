from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        temp = c.most_common(k)
        res = []
        for i in range (k):
            res.append(temp[i][0])
        return res
            
        