class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers) - 1

        while l < r: 
            currentTarget = numbers[r] + numbers[l]
            
            # Check current target
            if currentTarget < target: 
                l += 1
            elif currentTarget > target: 
                r -= 1
            else: 
                return [l + 1, r + 1]