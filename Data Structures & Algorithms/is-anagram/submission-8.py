class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        firstHashMap = {}
        for character in s: 
            if character in firstHashMap: 
                firstHashMap[character] += 1
            else : 
                firstHashMap[character] = 1


        secondHashMap = {}
        for character in t: 
            if character in secondHashMap: 
                secondHashMap[character] += 1
            else : 
                secondHashMap[character] = 1

        for key in firstHashMap:
            if key not in secondHashMap:
                return False
            if firstHashMap[key] != secondHashMap[key]:
                return False

        return True