class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        i = 0 
        j = 0
        length = 0
        if len(word1) > len(word2):
            length = len(word2)
        else: 
            length = len(word1)


        for i in range(length):
            res += word1[i] + word2[i]

        if length == len(word2):
            res += word1[len(word2): len(word1)]
        else :
            res += word2[len(word1): len(word2)]

        return res