class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        if rows == cols:
            for r in range(rows):
                for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            return matrix

        else:
            res = [[None]*rows for _ in range(cols)]

            for c in range(cols):
                for r in range(rows):
                    res[c][r] = matrix[r][c]

            return res

            
        