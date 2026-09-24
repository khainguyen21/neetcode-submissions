class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thresHold = len(nums) / 2
        myMap = {}


        result, maxCount = 0, 0 
        for i , num in enumerate(nums):
            if num not in myMap: 
                myMap[num] = 1

            else: 
                myMap[num] += 1


            if myMap[num] > maxCount: 
                result = num 

            maxCount = max(myMap[num], maxCount)

        return result