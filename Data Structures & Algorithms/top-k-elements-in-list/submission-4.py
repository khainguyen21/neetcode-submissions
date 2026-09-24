class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_list = [[] for _ in range(len(nums) + 1)]

        output = []
        h1 = {}

        for num in nums: 
            h1[num] = h1.get(num, 0) + 1

        for key in h1: 
            my_list[h1[key]].append(key)
        
        for i, bucket in enumerate(my_list[::-1]):
            for num in bucket:
                output.append(num)
                
                if k == len(output):
                    return output

        return output