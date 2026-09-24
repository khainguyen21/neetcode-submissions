class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        l = 0 
        subSum = 0

        for r in range(len(nums)):
            subSum += nums[r]

            while subSum >= target:
                res = min(res, r - l + 1)
                subSum -= nums[l]
                l += 1
        
        if res == len(nums) + 1: 
            res = 0

        return res