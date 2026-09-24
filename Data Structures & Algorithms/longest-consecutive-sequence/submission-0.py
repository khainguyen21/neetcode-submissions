class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)

        longestCons = 0
        for num in uniqueNums:
            if num - 1 not in uniqueNums:
                counter = 0
                while num in uniqueNums: 
                    counter += 1
                    num += 1
                longestCons = max(counter, longestCons)

        return longestCons