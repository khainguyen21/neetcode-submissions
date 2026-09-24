class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens: 

            if token != '+' and token != '-' and token != '*' and token != '/': 
                stack.append(int(token))

            elif stack:

                firstNum = stack.pop()
                secondNum = stack.pop()

                if token == '+':
                    stack.append(firstNum + secondNum)
                elif token == '-':
                    stack.append(secondNum - firstNum)
                elif token == '*':
                    stack.append(secondNum * firstNum)
                else: 
                    stack.append(int(secondNum / firstNum))

        return stack[0]








                
                
