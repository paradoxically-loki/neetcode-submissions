class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # freq, val
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res[::-1]

        