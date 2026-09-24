class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [ [] for _ in range(0, len(nums) + 1) ]
        freq = defaultdict(int)
        res = []
        
        for num in nums: 
            freq[num] += 1
        
        for key in freq: 
            bucket[freq[key]].append(key)

        for i in range(len(bucket) - 1, -1, -1):
            while bucket[i] and k > 0:
                res.append(bucket[i][-1]) 
                bucket[i].pop()
                k -= 1

        return res