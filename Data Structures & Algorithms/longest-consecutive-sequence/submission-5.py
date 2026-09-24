class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        removeDup = set(nums)
        
        longest = 0
        for num in nums: 
            
            maxLength = 0
            
            if num - 1 not in removeDup:
                maxLength += 1

                nextNum = num + 1

                while nextNum in removeDup: 
                    maxLength += 1
                    nextNum += 1  

            longest = max(longest , maxLength)

        return longest

        # removeDup = set(nums)
        # nums.sort()
        # output = []

        # for i in range(1, len(nums)): 
        #     if nums[i] - 1 == nums[i]: 
        #         output
                

                



            
            