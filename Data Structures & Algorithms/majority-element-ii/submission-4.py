class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashtable = defaultdict(int)
        res = []
        for n in nums: 
            hashtable[n] += 1

        for k in hashtable: 
            if hashtable[k] > len(nums) // 3:
                res.append(k)

        return res