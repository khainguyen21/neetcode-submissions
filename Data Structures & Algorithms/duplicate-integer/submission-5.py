class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = {}

        for n in nums: 
            if n in ans: # Check if the key exists and updating or setting a value take constant time O(1)
                ans[n] += 1
            else : 
                ans[n] = 1

        for val in ans.values(): 
            if val >= 2: 
                return True
        
        return False

         