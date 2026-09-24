class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        stack = []

        for char in s: 
            stack.append(char)

        for i in range(len(s)):
            s[i] = stack.pop()
        

        # Time: O(n) because we have iterate through the array
        # Space: O(n) because we have to use stack as a data structure


        