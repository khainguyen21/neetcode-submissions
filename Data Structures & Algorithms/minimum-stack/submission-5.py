class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Add a new number
        self.stack.append(val)
        
        if len(self.minStack) > 0: 
            # Check if we just found a new minimum
            if self.minStack[-1] > self.stack[-1]:
                self.minStack.append(self.stack[-1])
            # Otherwise, we add the current minimum to extra stack 
            else: 
                self.minStack.append(self.minStack[-1])
        else: 
            self.minStack.append(val)

    def pop(self) -> None:
        
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

# Time Complexity: O(1)
# Space Complexity: O(n)