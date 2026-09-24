class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        res = 0 

        while l < r: 
            length = r - l 
            
            if heights[l] < heights[r]: 
                width = heights[l]
                res = max(res, length * width)
                l += 1
            else: 
                width = heights[r]
                res = max(res, length * width)
                r -= 1
            
        return res