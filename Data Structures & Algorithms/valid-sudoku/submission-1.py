class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        dicRow = defaultdict(set)
        dicCol = defaultdict(set)
        dicTable = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in dicRow[r] or board[r][c] in dicCol[c] or board[r][c] in dicTable[r // 3, c // 3]:
                    return False
                dicRow[r].add(board[r][c])
                dicCol[c].add(board[r][c])
                dicTable[r//3,c//3].add(board[r][c])
        
        return True