class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0


        l , r = 0 , len(heights) - 1

        while l < r: 
            if heights[l] < heights[r]: 
                con = (r - l) * heights[l]

                output = max(con, output)
                l += 1
            
            elif heights[l] > heights[r]: 

                con = (r - l) * heights[r]

                output = max(con, output)
                r -= 1

            else: 
                con = (r - l) * heights[r]

                output = max(con, output)
                l += 1
                r -= 1

        return output
