class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNum = []

        for o in tokens: 
            
            if o == '+' or o == '-' or o == '*' or o == '/':
                firstNum = stackNum.pop()
                secondNum = stackNum.pop()

                if o == '+':
                    stackNum.append(firstNum + secondNum)
                if o == '-':
                    stackNum.append(secondNum - firstNum)
                if o == '*':
                    stackNum.append(firstNum * secondNum)
                if o == '/':
                    stackNum.append(int(secondNum / firstNum))
            
            else: 
                stackNum.append(int(o))
                

        return stackNum[0]

# "truncate to 0" is a way of describing the behavior of converting a floating-point number to an integer, 
# typically using the built-in int() function