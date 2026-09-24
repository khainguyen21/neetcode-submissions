class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = defaultdict(int)

        for i in range (len(nums)): 
            diff = target - nums[i] 

            if diff not in hashNum: 
                hashNum[nums[i]] = i

            else: 
                return [hashNum[diff], i]


            # -1: 0
            # -2: 1
            # -3: 2
            # -4: 3