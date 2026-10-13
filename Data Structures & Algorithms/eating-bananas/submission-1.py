class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k : int) -> int:
            res = 0
            for pile in piles:
                res += -(-pile//k) # ceiling
            return res

        l, r = 1, max(piles)

        output = r

        while l <= r:
            mid = l + (r - l) // 2

            if check(mid) <= h:
                output = mid
                r = mid - 1
            else:
                l = mid + 1

        return output
        
        