class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = collections.defaultdict(int)
        res, maxCount = 0, 0 

        for num in nums:    
            hashtable[num] += 1
            if hashtable[num] > maxCount: 
                res = num
            maxCount = max(hashtable[num], maxCount)
            
        return res

        
       
        