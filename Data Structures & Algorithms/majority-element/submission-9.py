class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for num in nums: 
            if res != num: 
                if count == 0: 
                    res = num 
                else: 
                    count -= 1
            else: 
                count += 1

        return res

        

        
        




            

        
       
        