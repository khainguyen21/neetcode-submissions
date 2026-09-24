class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        l , r = 0 , len(arr) - 1

        while l < r and (r - l) + 1 > k: 
            if abs(x - arr[l]) > abs(x - arr[r]): 
                l += 1
            else: 
                r -= 1

        return arr[l : r + 1]

# Time Complexity: O(n) 
# Space Complexity: O(k) 