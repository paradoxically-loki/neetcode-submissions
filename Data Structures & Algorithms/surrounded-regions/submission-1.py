class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def mark(r, c):
            if (0 <= r < R) and (0 <= c < C) and board[r][c] == 'O':
                board[r][c] = 'T'
                mark(r-1,c); mark(r+1,c); mark(r,c-1); mark(r,c+1)

        for r in range(R):
            mark(r, 0)
            mark(r, C-1)

        for c in  range(C):
            mark(0, c)
            mark(R-1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'