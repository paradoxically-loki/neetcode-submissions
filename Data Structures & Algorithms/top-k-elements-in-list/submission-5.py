class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        count = list(count.items())
        count.sort(key = lambda p : p[1])
        # print(count)

        res = []
        for i in range(k):
            res.append(count[len(count)-1-i][0])
        return res
        