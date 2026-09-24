class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # Number of rows
        n = len(matrix[0]) # # Number of columns
        l , r = 0 , m * n - 1

        while l <= r: 
            mid = (r + l) // 2
            if target < matrix[mid // n][mid % n]: 
                r = mid - 1
            elif target > matrix[mid // n][mid % n]: 
                l = mid + 1
            else: 
                return True

        return False