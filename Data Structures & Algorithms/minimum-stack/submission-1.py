class MinStack:
    
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        minNum = self.stack[0] 

        for n in self.stack: 
            minNum = min(minNum, n)
        
        return minNum

# Time Complexity: O(n)
# Space Complexity: O(n)