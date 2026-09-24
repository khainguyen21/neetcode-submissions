class Solution:
    def isValid(self, s: str) -> bool:
        l , r = 0 , len(s) - 1
        hashBracket = {')': '(', '}': '{', ']': '['}
        
        stackBracket = []

        for b in s: 
            if b == '(' or b == '{' or b == '[':
                stackBracket.append(b)
            elif stackBracket and stackBracket[-1] == hashBracket[b]:
                stackBracket.pop()
            else: 
                return False

        return len(stackBracket) == 0



            