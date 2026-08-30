class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digit = 0
        for i in range(n):
            digit += digits[n-1-i]*10**(i)

        digit += 1

        res = []
        while digit:
            last = digit % 10
            res.append(last)
            digit = digit // 10

        return res[::-1]

        