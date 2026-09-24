class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums: 
            if n - 1 not in numSet:
                k = 0
                while n + k in numSet: 
                    k += 1

                longest = max(longest , k)

        return longest