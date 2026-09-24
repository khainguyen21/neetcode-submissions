class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix: 
            l , r = 0 , len(arr) - 1

            if target > arr[r]:
                continue

            while l <= r: 
                m = (r + l) // 2
                if target < arr[m]: 
                    r = m - 1
                elif target > arr[m]: 
                    l = m + 1
                else: 
                    return True

        return False

# Time Complexity: O(R * log(C))
# Space Complexity: O(1)