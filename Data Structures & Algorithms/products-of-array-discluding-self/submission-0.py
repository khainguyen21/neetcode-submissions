class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [1]
        postfixArr = [1]

        num = prefixArr[0]
        for i in range(len(nums) - 1): 
            num *= nums[i]
            prefixArr.append(num)
        
        num = postfixArr[0]
        for j in range(len(nums) - 1, 0, -1):
            num *= nums[j]
            postfixArr.append(num)

        postfixArr.reverse()

        output = []
        for i in range(len(prefixArr)): 
            output.append(prefixArr[i] * postfixArr[i])

        return output
