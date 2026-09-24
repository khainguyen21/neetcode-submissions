class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        listNum = []

        hashtable = collections.defaultdict(int)

        for num in nums:
            hashtable[num] += 1

        for key in hashtable: 
            if hashtable[key] > len(nums) // 3: 
                listNum.append(key)
            
        return listNum 
