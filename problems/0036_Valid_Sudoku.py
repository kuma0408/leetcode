class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for v in row:
                if v != "." and v in s:
                    return False
                else:
                    s.add(v)

        for col_num in range(9):
            s = set()
            for row_num in range(9):
                v = board[row_num][col_num]
                if v != "." and v in s:
                    return False
                else:
                    s.add(v)

        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        v = board[i+k][j+l]
                        if v != "." and v in s:
                            return False
                        else:
                            s.add(v)
        return True
