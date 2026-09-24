class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s) - 1
        k = 1
        while l < r: 
            if s[l] != s[r]: 
                skippedL , skippedR = s[l + 1: r + 1], s[l:r]

                if skippedL[::-1] ==  skippedL or skippedR[::-1] ==  skippedR:
                    return True
                else: 
                    return False

                 
            l += 1
            r -= 1

        return True

        