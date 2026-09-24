class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDupSet = set()

        for num in nums: 
            if num in checkDupSet: 
                return True

            checkDupSet.add(num)

        return False