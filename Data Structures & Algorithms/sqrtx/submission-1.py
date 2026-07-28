class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (right - left)//2 + left
            if mid*mid == x: return mid
            elif mid*mid > x: right = mid -1
            else: left = mid + 1
        return mid if mid*mid < x else mid-1
        