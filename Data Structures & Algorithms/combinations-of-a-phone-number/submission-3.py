class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []
        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
                return

            for ch in mapping[digits[i]]:
                dfs(i+1, curr + ch)

        dfs(0, '')
        return res
