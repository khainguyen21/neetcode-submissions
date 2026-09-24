class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = max(piles) + 1

        while l <= r: 
            eatRate = (l + r) // 2
            currH = 0 

            for p in piles: 
                currH += math.ceil(p / eatRate)

            if currH > h: 
                l = eatRate + 1
            else: 
                r = eatRate - 1
                res = min(res, eatRate)

        return res