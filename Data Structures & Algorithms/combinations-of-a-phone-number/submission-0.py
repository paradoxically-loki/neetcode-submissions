class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        curr = []
        def backtrack(i):
            if i == len(digits):
                res.append(''.join(curr))
                return
            
            for c in mapping[digits[i]]:
                curr.append(c)
                backtrack(i+1)
                curr.pop()

        backtrack(0)

        return res

        