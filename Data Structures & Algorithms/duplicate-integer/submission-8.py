class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1, 2, 3]

        hashtable = {}

        # 1: 1
        for num in nums: 
            if num not in hashtable: 
                hashtable[num] = 1
            else: 
                hashtable[num] += 1

        # 1: 1 
        # 2: 1
        # 3: 2

        for k, c in hashtable.items(): 
            if c > 1: 
                return True
                
        return False
