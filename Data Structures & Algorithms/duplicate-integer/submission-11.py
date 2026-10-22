class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkNums = set()
        for num in nums: 
            if num in checkNums: 
                return True
            checkNums.add(num)

        return False