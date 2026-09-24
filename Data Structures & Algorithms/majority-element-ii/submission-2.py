class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums: 
            count[num] += 1

            if len(count) > 2: 
                new_count = defaultdict(int)
                
                for k , v in count.items(): 
                    if v > 1:
                       new_count[k] = v - 1  

                count = new_count # copy the temp hashmap to main hashmap

        res = []
        for k in count: 
            # nums.count counts how many numbers of k appear in nums list
            if nums.count(k) > len(nums) // 3: 
                res.append(k)
        return res

            
