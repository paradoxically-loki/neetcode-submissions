class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k: int) -> int:
            res = 0
            for pile in piles:
               # res += pile//k, we actually need the ceiling division
               res += -(-pile//k) #note this trick
            return res

        l = 1; r = max(piles)
        output = r

        while l <= r:
            k = (r-l)//2 + l
            if check(k) <= h:
                output = k
                r = k-1
            else:
                l = k+1

        return output


        