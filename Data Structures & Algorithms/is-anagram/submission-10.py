class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashMap = {}
        for char in s: 
            if char in hashMap: 
                hashMap[char] += 1
            else : 
                hashMap[char] = 1


        for char in t: 
            if char in hashMap and hashMap[char] > 0: 
                hashMap[char] -= 1
            else: 
                return False

        return True
            