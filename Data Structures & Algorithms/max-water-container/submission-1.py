class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        maxA = 0 

        while l < r: 

            currA = min(heights[l], heights[r]) * (r - l)
            maxA = max(currA, maxA)

            if heights[l] < heights[r]:    
                l += 1
            else: 
                r -= 1

        return maxA

        # Time Complexity: O(N)
        # Space Complexity: O(1)