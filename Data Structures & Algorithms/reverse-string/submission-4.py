class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l , r = 0 , len(s) - 1

        while l < r: 
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        # Time: O(n) because we use while loop through every character in the array string
        # Space: O(1) because we do not use any data structures


        