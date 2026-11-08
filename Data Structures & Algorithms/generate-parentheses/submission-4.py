class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def dfs(o, c):
            if o == c == n:
                res.append(''.join(curr))
                return

            if o < n:
                curr.append('(')
                dfs(o+1, c)
                curr.pop()

            if c < o:
                curr.append(')')
                dfs(o, c+1)
                curr.pop()

        dfs(0,0)
        return res

