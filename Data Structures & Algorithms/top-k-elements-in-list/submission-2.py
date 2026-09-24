class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        result = [[] for i in range(len(nums) + 1)]

        output = []
        for num in nums: 
            if num not in myMap: 
                myMap[num] = 1

            else : 
                myMap[num] += 1

        for num, count in myMap.items() :
            result[count].append(num)

        i = len(nums)
        while k > 0 and i >= 0: 
            if result[i] != None and k > 0: 
                for j in result[i]:
                    output.append(j)
                    k -= 1
            i -= 1


        # for i in range(len(result) - 1, -1, -1):
        #     if result[i] != None and k > 0: 
        #         for j in result[i]:
        #             output.append(j)
        #             k -= 1


        return output

            
        

        