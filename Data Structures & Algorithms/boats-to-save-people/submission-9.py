class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        numBoats = 0

        l , r = 0 , len(people) - 1

        while l <= r: 

            # Calculate the remain weight for current boat 
            remain = limit - people[r]
            r -= 1
            numBoats += 1

            # Check if lightest person can be a same current boat
            if people[l] <= remain: 
                l += 1
        
        return numBoats

# Neetcode Solution: 
# Time Complexity: O(n logn)
# Space Complexity: O(n)