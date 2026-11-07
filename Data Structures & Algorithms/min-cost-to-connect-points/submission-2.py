class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        minHeap = [(0, 0)] # (cost, point)
        totalCost = 0

        while len(seen) < n:
            c, p = heapq.heappop(minHeap)
            if p in seen:
                continue
            seen.add(p)
            totalCost += c
            xi, yi = points[p]
            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    heapq.heappush(minHeap, (abs(xi-xj) + abs(yi-yj), j))
        
        return totalCost