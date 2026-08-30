class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        first = 0
        second = third = 1

        for i in range(3,n+1):
            new_two = third
            new_one = second
            third = third + second + first
            second = new_two
            first = new_one

        return third
        