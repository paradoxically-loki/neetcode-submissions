class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        temp = count.most_common(k)
        
        res = []
        for key, val in temp:
            res.append(key)

        return res