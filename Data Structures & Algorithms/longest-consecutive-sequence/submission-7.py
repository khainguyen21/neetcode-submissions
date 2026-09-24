class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        numSet = set(nums)
        
        longest = 0
        for num in nums: 

            maxLength = 0
            
            # Check if the its start of the sequence
            if num - 1 not in numSet:

                while num + maxLength in numSet: 
                    maxLength += 1

            longest = max(longest , maxLength)

        return longest

        # removeDup = set(nums)
        # nums.sort()
        # output = []

        # for i in range(1, len(nums)): 
        #     if nums[i] - 1 == nums[i]: 
        #         output
                

                



            
            