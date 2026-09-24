class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        output = []
        
        l , r = 0 , len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit: 
                output.append([people[l], people[r]])
                l += 1
                r -= 1

            elif people[r] <= limit: 
                output.append([people[r]])
                r -= 1
        
        return len(output)