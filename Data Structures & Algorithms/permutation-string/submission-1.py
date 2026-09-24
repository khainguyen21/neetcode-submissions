class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        if len(s1) > len(s2):
            return False

        countS1 = [0] * 26
        for c1 in s1:
            countS1[ord(c1) - ord('a')] += 1

        l , r = 0 , 0
        countS2 = [0] * 26
        while r < len(s2): 
            countS2[ord(s2[r]) - ord('a')] += 1
            
            if r - l + 1 == len(s1): 
                if countS1 == countS2: 
                    return True

                countS2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            r += 1
                
        return False