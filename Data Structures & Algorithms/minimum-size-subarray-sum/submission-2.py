class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0 , 0

        currentSum = 0
        minLength = float('inf')
 
        
        while r < len(nums):                   
            currentSum += nums[r]

            while currentSum >= target: 
                minLength = min(minLength, (r - l) + 1)
                currentSum -= nums[l]
                l += 1 
                
            r += 1

        if minLength == float('inf'): 
            minLength = 0

        return minLength
