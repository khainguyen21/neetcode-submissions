class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Eliminated duplicates , O(1) looks up

        longest = 0

        for i in range(len(nums)):

            # Find the potential starter of the sequence 
            if nums[i] - 1 not in numSet: 
                checkNext = 0 

                # Check if next number in the set
                while checkNext + nums[i] in numSet: 
                    checkNext += 1

                # Update the longest cons seq
                longest = max(longest, checkNext)

        return longest
                
                




