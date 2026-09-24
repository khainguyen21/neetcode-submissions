class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]

        freq = defaultdict(int)

        for num in nums: 
            freq[num] = 1 + freq.get(num, 0)

        for n, c in freq.items(): 
            count[c].append(n)

        output = []

        for i in range(len(count) - 1, 0, -1): 
            for j in count[i]:
                output.append(j)
                if len(output) == k: 
                    return output
                 
        