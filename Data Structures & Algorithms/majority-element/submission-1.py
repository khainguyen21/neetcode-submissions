class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thresHold = len(nums) / 2
        myMap = {}

        for i , num in enumerate(nums):
            if num not in myMap: 
                myMap[num] = 1

            else: 
                myMap[num] += 1


        for key in myMap: 

            if myMap[key] > thresHold: 
                return key