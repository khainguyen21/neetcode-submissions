class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                    output[stack[-1][0]] = i - stack[-1][0] 
                    stack.pop()
            else: 
                stack.append([i, t])

        return output

        # Time Complexity: O(n)
        # Space Complexity: O(n)