class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for i in range(n+1):
            results.append(self.countOnes(i))
        return results

    def countOnes(self, n: int) -> int:
        res = 0
        while n:
            n = n&(n-1)
            res += 1
        return res
        