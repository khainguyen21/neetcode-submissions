class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        maxA = 0 

        while l < r: 
            if heights[l] < heights[r]:
                currA = heights[l] * (r - l)
                maxA = max(currA, maxA)
                l += 1
            else: 
                currA = heights[r] * (r - l)
                maxA = max(currA, maxA)
                r -= 1

        return maxA