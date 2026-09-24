class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 

        longestSub = set()
        res = 0 
        l = 0
        
        for r in range(len(s)):
            
            while s[r] in longestSub: 
                longestSub.remove(s[l])
                l += 1
            
            longestSub.add(s[r])
            res = max(res, len(longestSub))

        return res