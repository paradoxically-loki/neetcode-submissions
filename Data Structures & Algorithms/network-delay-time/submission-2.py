class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        dist = defaultdict(int)
        minHeap = [(0, k)]

        while minHeap:
            d, u = heapq.heappop(minHeap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in adj[u]:
                if not v in dist:
                    heapq.heappush(minHeap, (w + d, v))
        
        return max(dist.values()) if len(dist) == n else -1