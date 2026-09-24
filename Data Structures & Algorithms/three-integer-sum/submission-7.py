class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()
        # [-4,-4,-1,0,1,2]

        # (-1 + 2) - 1
        # (-1 + 1) - 0

        output = []

        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            
            while j < k: 
                if nums[i] + nums[j] + nums[k] > 0: 
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0: 
                    j += 1
                else: 
                    output.append([nums[i] , nums[j] , nums[k]])

                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1

        return output





