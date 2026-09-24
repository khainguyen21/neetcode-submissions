class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        l , r = 0 , len(nums) - 1

        # Reversed the whole array 
        while l < r: 
            nums[l] , nums[r] = nums[r] , nums[l]
            l , r = l + 1 , r - 1


        # Reversed at index k 
        l = 0 
        b = k - 1
        while l < b: 
            nums[l] , nums[b] = nums[b] , nums[l]
            l , b = l + 1 , b - 1

        r = len(nums) - 1
        while k < r: 
            nums[k] , nums[r] = nums[r] , nums[k]
            k , r = k + 1 , r - 1

 






        