class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        minRate = r
        
        while l <= r: 
            currRate = (r + l) // 2
            currH = 0 

            for p in piles: 
                currH += math.ceil(p / currRate)
            
            if currH <= h: 
                minRate = min(minRate, currRate)
                r = currRate - 1
            else: 
                l = currRate + 1

        return minRate