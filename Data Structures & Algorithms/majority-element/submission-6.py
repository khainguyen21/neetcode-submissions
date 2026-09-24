class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = collections.defaultdict()

        for num in nums:    
            if num not in hashtable: 
                hashtable[num] = 1
            else: 
                hashtable[num] += 1

        for key in hashtable: 
            if hashtable[key] > len(nums) / 2: 
                return key

        
       
        