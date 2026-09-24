class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        noDup = set()
        longest = 0 
        l = 0

        for r in range(len(s)):
            while s[r] in noDup: 
                noDup.remove(s[l])
                l += 1
            
            noDup.add(s[r])
            longest = max(longest, r - l + 1)

        return longest