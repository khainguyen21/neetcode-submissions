class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        maxA = 0 
        
        while l < r: 
            if heights[l] > heights[r]:
                maxA = max(maxA, (r - l) * heights[r])
                r -= 1
            else: 
                maxA = max(maxA, (r - l) * heights[l])
                l += 1
            
        return maxA