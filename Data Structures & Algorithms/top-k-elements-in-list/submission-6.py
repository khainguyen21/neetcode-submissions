class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        
        hashmap = defaultdict(int)

        for num in nums: 
            hashmap[num] = hashmap.get(num, 0) + 1

        for key in hashmap: 
            bucket[hashmap[key]].append(key)
            
        output = []

        for item in reversed(bucket):
            if len(item) > 0:
                i = len(item) - 1
                while k > 0 and i >= 0:
                    output.append(item[i])
                    k -= 1
                    i -= 1

        return output


