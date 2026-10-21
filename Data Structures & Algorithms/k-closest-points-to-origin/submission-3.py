class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = [(p[0]**2 + p[1]**2, p[0], p[1]) for p in points]
        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res

        