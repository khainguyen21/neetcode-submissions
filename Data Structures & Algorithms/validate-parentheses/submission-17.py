class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s: 

            if len(stack) > 0 and char in dictionary:
                if dictionary[char] != stack.pop():
                    return False
            else: 
                stack.append(char)
        
        return len(stack) == 0

        


