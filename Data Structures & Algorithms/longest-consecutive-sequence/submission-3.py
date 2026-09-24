class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        removeDup = set(nums)
        
        output = []
        for num in nums: 
            maxLength = []
            if num - 1 not in removeDup:
                maxLength.append(num)
                nextNum = num + 1

                while nextNum in removeDup: 
                    maxLength.append(nextNum)
                    nextNum += 1  
            output.append(len(maxLength))

        return max(output)

        # removeDup = set(nums)
        # nums.sort()
        # output = []

        # for i in range(1, len(nums)): 
        #     if nums[i] - 1 == nums[i]: 
        #         output
                

                



            
            