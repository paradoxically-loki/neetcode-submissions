class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda p : p[1])

        for i in range(len(trips)):
            currPass = trips[i][0]
            for j in range(i):
                if trips[j][2] > trips[i][1]:
                    currPass += trips[j][0]

            if currPass > capacity:
                return False
            

        return True

