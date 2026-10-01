class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #first we need to create 3 dictionaries
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        gridSet = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowSet[row]
                or board[row][col] in colSet[col]
                or board[row][col] in gridSet[(row//3, col//3)]):
                    return False
                rowSet[row].add(board[row][col])
                colSet[col].add(board[row][col])
                gridSet[(row//3, col//3)].add(board[row][col])

        return True
                    

        