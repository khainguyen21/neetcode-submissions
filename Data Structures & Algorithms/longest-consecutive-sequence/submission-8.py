class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        removeDup = set(nums)
        
        output = []
        for num in nums: 

            maxLength = []
            
            # Check if it's the start of the sequence
            if num - 1 not in removeDup:
                
                nextNum = 0

                while nextNum + num in removeDup: 
                    maxLength.append(num)
                    nextNum += 1

            output.append(len(maxLength))

        return max(output)    