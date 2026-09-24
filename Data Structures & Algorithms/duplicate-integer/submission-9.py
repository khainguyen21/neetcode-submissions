class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkList = set()

        for num in nums: 
            if num in checkList: 
                return True
            checkList.add(num)

        return False

        
