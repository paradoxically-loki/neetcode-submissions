class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        for i in range(9):
            for j in range(9):
                if not self.cross_check(i,j):
                    return False
        if not self.square_check():
            return False
        return True

    def square_check(self) -> bool:
        for square in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if self.board[row][col] == '.':
                        continue
                    if self.board[row][col] in s:
                        return False
                    s.add(self.board[row][col])
        return True

    def cross_check(self, row: int, col: int) -> bool:
        return self.row_check(row) and self.col_check(col)

    def row_check(self, row: int) -> bool:
        s = set()
        for i in range(9):
            if self.board[row][i] == '.':
                continue
            if self.board[row][i] in s:
                return False
            s.add(self.board[row][i])
        return True

    def col_check(self, col: int) -> bool:
        s = set()
        for i in range(9):
            if self.board[i][col] == '.':
                continue
            if self.board[i][col] in s:
                return False
            s.add(self.board[i][col])
        return True
        