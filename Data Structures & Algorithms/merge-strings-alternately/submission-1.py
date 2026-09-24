class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        i = 0 
        j = 0
        length = 0
        
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1

        if len(word1) > len(word2):
            res += word1[len(word2): len(word1)]
        else: 
            res += word2[len(word1): len(word2)]

        return res
