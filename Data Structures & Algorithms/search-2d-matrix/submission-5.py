class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        top , bot = 0 , ROWS - 1

        while top <= bot:
            # Find middle row that may contain target
            midRow = (top + bot) // 2  

            if target < matrix[midRow][0]:
                bot = midRow - 1
            elif target > matrix[midRow][-1]:
                top = midRow + 1
            else: 
                break

        if top > bot: 
            return False

        l , r = 0 , COLUMNS - 1
        row = (top + bot) // 2
        while l <= r: 
            m = (r + l) // 2

            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True

        return False