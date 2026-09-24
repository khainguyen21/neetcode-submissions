class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i]) 


            elif not stack: 
                return False
            else:
                if s[i] == '}' and '{' != stack.pop():
                    return False
                elif s[i] == ')' and '(' != stack.pop():
                    return False
                elif s[i] == ']' and '[' != stack.pop():
                    return False

        return len(stack) == 0


