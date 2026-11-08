class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []

        def dfs(i):
            if i == len(s):
                res.append(curr[:])
                return

            for j in range(i, len(s)):
                piece = s[i: j+1]
                if piece == piece[::-1]:
                    curr.append(piece)
                    dfs(j+1)
                    curr.pop()

        dfs(0)
        return res