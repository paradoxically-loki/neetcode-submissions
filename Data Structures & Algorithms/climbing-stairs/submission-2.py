class Solution:
    def climbStairs(self, n: int) -> int:
        prev = current = 1
        for _ in range(0, n-1):
            temp = current
            current = current + prev
            prev = temp
        return current