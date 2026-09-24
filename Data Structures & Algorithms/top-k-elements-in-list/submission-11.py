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
            for num in bucket[i]:
                res.append(num)
                if len(res) == k: 
                    return res