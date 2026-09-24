class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams
        output = []
        for s in strs:
            count = [0] * 26 # a ... z
            
            for c in s: 
                count[ord(c) - ord('a')] += 1

            if tuple(count) not in res: 
                res[tuple(count)] = [s]
            else: 
                res[tuple(count)].append(s)


        for val in res.values():
            output.append(val)
        
        return output
            
