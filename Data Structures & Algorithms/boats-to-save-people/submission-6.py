class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        
        l , r = 0 , len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit: 
                boat += 1
                l += 1
                r -= 1

            elif people[r] <= limit: 
                boat += 1
                r -= 1
        
        return boat