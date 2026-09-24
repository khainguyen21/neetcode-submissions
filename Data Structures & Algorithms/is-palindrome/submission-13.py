class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNum(n):
            return ord('A') <= ord(n) <= ord('Z') or ord('a') <= ord(n) <= ord('z') or ord('0') <= ord(n) <= ord('9') 

        i , j = 0 , len(s) - 1

        while i < j: 
            if not isAlphaNum(s[i]): 
                i += 1
                continue
            if not isAlphaNum(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower(): 
                return False
            i += 1
            j -= 1

        return True

