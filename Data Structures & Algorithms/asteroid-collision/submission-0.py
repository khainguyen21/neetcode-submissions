class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        astRight = []

        for a in asteroids:  
            while astRight and a < 0 and astRight[-1] > 0: 
                if astRight[-1] < -(a): 
                    astRight.pop()

                elif astRight[-1] == -(a): 
                    astRight.pop()
                    break 
                else: 
                    break
                    
            else: 
                astRight.append(a)

        return astRight
