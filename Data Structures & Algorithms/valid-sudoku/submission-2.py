class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate each row
        for row in range(len(board)):
            checkDup = set()

            for col in range(len(board)):
                eachColumn = board[row][col]
                
                if eachColumn != '.':
                    if eachColumn not in checkDup: 
                        checkDup.add(eachColumn)
                    else: 
                        return False

        # Validate each column
        for col in range(len(board)):
            checkDup = set()

            for row in range(len(board)):
                eachRow = board[row][col]
                
                if eachRow != '.':
                    if eachRow not in checkDup: 
                        checkDup.add(eachRow)
                    else: 
                        return False

        # Validate 3 x 3: 
        for row in range(0, len(board), 3):

            for col in range(0, len(board), 3):
                checkDup = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            if board[i][j] not in checkDup: 
                                checkDup.add(board[i][j])
                            else: 
                                return False

        return True

                        




