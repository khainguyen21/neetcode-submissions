class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i  in range(len(nums) + 1)]
        
        hashmap = defaultdict(int)

        for num in nums: 
            hashmap[num] += 1

        for num, count in hashmap.items(): 
            bucket[count].append(num)
            
        output = []

        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                output.append(n)
                if len(output) == k: 
                    return output




