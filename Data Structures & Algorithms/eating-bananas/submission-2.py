class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        minRate = float('inf')
        
        while l <= r: 
            m = (r + l) // 2
            currRate = 0 

            for p in piles: 
                currRate += math.ceil(p / m)
            
            if currRate <= h: 
                r = m - 1
                minRate = min(minRate, m)
            else: 
                l = m + 1

        return minRate