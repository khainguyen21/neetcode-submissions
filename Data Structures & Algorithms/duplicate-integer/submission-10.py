class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkNums = []
        for num in nums: 
            if num in checkNums: 
                return True
            checkNums.append(num)

        return False