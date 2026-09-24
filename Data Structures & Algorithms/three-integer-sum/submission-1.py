class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            
            # Skipped if the current number is equal the previous number
            # To avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            target = -(nums[i])

            j = i + 1

            k = len(nums) - 1

            while j < k: 
                if j > i + 1 and nums[j] == nums[j-1] and k < len(nums) - 1 and nums[k] == nums[k+1]:
                    j += 1
                    k -= 1
                    continue

                if (nums[j] + nums[k]) < target: 
                    j += 1

                elif (nums[j] + nums[k]) > target: 
                    k -= 1
                
                else: 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

        return res



                     
