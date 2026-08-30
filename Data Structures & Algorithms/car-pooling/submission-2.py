class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda p : p[1])

        minHeap = [] # [end, numPassengers]
        currPass = 0

        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                currPass -= heapq.heappop(minHeap)[1]

            currPass += numPass
            if currPass > capacity:
                return False

            heapq.heappush(minHeap, [end, numPass])
        
        return True