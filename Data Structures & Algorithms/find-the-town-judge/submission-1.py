class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming, outgoing = [0]*(n+1), [0]*(n+1)

        for o,i in trust:
            outgoing[o] += 1
            incoming[i] += 1

        for i in range(1,n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i

        return -1
        