class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        delta = [0]*(n+1)

        for o,i in trust:
            delta[o] -= 1
            delta[i] += 1

        for i in range(1,n+1):
            if delta[i] == n-1:
                return i

        return -1        