class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredStr = ""



        for c in s: 
            if c.isalnum():
                filteredStr += c.lower()


        left = 0 
        right = len(filteredStr) - 1


        while left < right:
            if filteredStr[right] != filteredStr[left]:
                return False
            else: 
                left += 1
                right -= 1

        return True