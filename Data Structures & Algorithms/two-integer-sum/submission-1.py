class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {} # val: index 

        for i, num in enumerate(nums): 
            difference = target - num

            if difference in myMap: 
                return [myMap[difference], i]

            else : 
                myMap[num] = i               



    # Time: O (n) Because we only iterate through the array once and 
    # add and check each value in the hashmap which is O(1)

    # Space: O(n) Because we potentially added every values to 
    # the hashmap

