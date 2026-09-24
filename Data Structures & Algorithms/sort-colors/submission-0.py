class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        bucket = {0: 0, 1: 0, 2: 0}

        for num in nums: 
            bucket[num] = 1 + bucket.get(num, 0)

        i = 0 
        for key in bucket:
            while bucket[key] > 0: 
                nums[i] = key
                i+=1
                bucket[key] -= 1

        


        