class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = nums[0], 0 

        for num in nums: 
            if num != result and count == 0:
                result = num
                count = 1

            elif num != result: 
                count -= 1

            else: 
                count += 1
            
        return result
