class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        removeDup = set(nums)
        
        longest = 0
        for num in nums: 
            
            nextNum = 0
            # Check if it's the start of the sequence
            if num - 1 not in removeDup:
            
                while nextNum + num in removeDup: 
                    nextNum += 1

            longest = max(longest, nextNum)

        return longest   