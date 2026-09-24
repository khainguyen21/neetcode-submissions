class Solution:
    def isValid(self, s: str) -> bool:
        counter = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s: 

            if len(stack) > 0 and (char == ")" or char == "}" or char == "]"):
                if counter[char] != stack.pop():
                    return False
            else: 
                stack.append(char)
        
        return len(stack) == 0

        


