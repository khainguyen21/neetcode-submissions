class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l , r = 0 , 0 
        result = []

        while r < len(temperatures):
            if temperatures[l] < temperatures[r]:
                result.append(r - l)
                l += 1
                r = l

            elif temperatures[l] >= temperatures[r] and r == len(temperatures) - 1: 
                result.append(0)
                l += 1
                r = l 

            else: 
                r += 1

        # result.append(0)

        return result