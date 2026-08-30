class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows, cols = len(matrix), len(matrix[0])

        result = [[None]*rows for _ in range(cols)]
        for i in range(cols):
            for j in range(rows):
                result[i][j] = matrix[j][i]

        return result
        