class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)

        longest_cons = 0
        for num in uniqueNums:
            if (num - 1) not in uniqueNums:
                length_cons = 0
                while (num + length_cons) in uniqueNums: 
                    length_cons += 1

                longest_cons = max(length_cons, longest_cons)

        return longest_cons