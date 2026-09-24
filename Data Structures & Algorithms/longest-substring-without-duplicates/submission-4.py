class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in res: 
                res.add(s[r])

                if r == len(s) - 1: 
                    longest = max(longest, len(res))
                    return longest
            else: 
                longest = max(longest, len(res))
                while s[l] != s[r]: 
                    res.remove(s[l])
                    l += 1
                else: 
                    l += 1
            
        return longest



