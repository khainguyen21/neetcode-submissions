class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0 , 0

        currentSum = 0
        minLength = float('inf')
 
        for r in range(len(nums)):
            currentSum += nums[r]
    
            while currentSum >= target: 
                minLength = min(minLength, (r - l) + 1)
                currentSum -= nums[l]
                l += 1 
                
        if minLength == float('inf'): 
            minLength = 0

        return minLength

# Time Complexity: O(n)
# Space Complexity: O(1)