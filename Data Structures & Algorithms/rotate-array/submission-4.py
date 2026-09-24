class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # k = 7 % 5 = 2

        l , r = 0 , n - 1

        # Reversed the entire array 
        while l < r: 
            nums[l] , nums[r] = nums[r] , nums[l]
            l , r = l + 1 , r - 1

        print(nums)

        # Reversed the first k elements (0 to k - 1) 
        l1 , r1 = 0 , k - 1
        while l1 < r1: 
            nums[l1] , nums[r1] = nums[r1] , nums[l1]
            l1 , r1 = l1 + 1 , r1 - 1

        # Reversed the remaining elements (k to n - 1)
        l2 , r2 = k , n - 1
        while l2 < r2: 
            nums[l2] , nums[r2] = nums[r2] , nums[l2]
            l2 , r2 = l2 + 1 , r2 - 1        