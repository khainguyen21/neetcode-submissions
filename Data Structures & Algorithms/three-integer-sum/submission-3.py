class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            
            # Skipped if the current number is equal the previous number
            # To avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1

            k = len(nums) - 1

            while j < k: 
                threeSum = nums[i] + nums[j] + nums[k]


                if threeSum < 0: 
                    j += 1

                elif threeSum > 0: 
                    k -= 1
                
                else: 
                    res.append([nums[i], nums[j], nums[k]])

                    # [-2, -2, 0, 0, 2, 2]
                    
                    j += 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1

        return res



                     
