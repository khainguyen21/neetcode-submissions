class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i in range(len(nums)): 
            difference = target - nums[i]

            if difference in myMap: 
                return [myMap[difference], i]

            else : 
                myMap[nums[i]] = i               


