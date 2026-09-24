class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        res = 0
        
        prefixSum[0] = 1
        prefix = 0

        for num in nums:

            prefix += num
            total = prefix - k

            if total in prefixSum: 
                res += prefixSum[total]

            # Add prefix into the hashtable with its count as value
            prefixSum[prefix] += 1

        return res

            
        
        
            
            