class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
   


        k = 0
        i = 0
        while i < len(nums):
            
            if nums[i] != val: 
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
            
                
                
            
        

        # Time Complexity: O(N)
        # The time complexity is O(N), where N is the number of elements in the list nums. 
        # This is also known as linear time.


        # Space Complexity: O(1)
        # This is because the algorithm modifies the input list in-place and only uses a fixed amount of extra memory.



