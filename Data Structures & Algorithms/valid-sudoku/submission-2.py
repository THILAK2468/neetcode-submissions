class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row = defaultdict(set)
        column= defaultdict(set)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if (val in row[r] or val in column[c] or val in box[(r//3,c//3)]):
                    return False
                row[r].add(val)
                column[c].add(val)
                box[(r//3,c//3)].add(val)
        return True