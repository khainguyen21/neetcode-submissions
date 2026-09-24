class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check each row
        for i in range(len(board)):
            checkDup = set()

            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in checkDup: 
                    return False

                checkDup.add(board[i][j])

        # Check each column 
        for j in range(9): 
            checkDup = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue

                if board[i][j] in checkDup: 
                    return False

                checkDup.add(board[i][j])


        # Check each square (3 x 3)
        squares = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                if board[i][j] not in squares[(i//3, j//3)]: 
                    squares[(i//3, j//3)].add(board[i][j])
                else: 
                    return False

        return True