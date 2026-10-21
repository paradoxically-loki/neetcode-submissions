class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * stone for stone in stones]
        heapq.heapify(maxHeap) 

        while len(maxHeap) > 1:
            first = -1 * heapq.heappop(maxHeap)
            second = -1 * heapq.heappop(maxHeap)

            if first == second: continue
            elif first < second:
                res = second - first
                heapq.heappush(maxHeap, -res)
            else:
                res = first - second
                heapq.heappush(maxHeap, -res)

        if len(maxHeap) == 1:
            return -1 * maxHeap[0]
        return 0
        