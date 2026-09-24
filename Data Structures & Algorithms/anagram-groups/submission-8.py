class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAg = defaultdict(list)

        for word in strs: 
            count = [0] * 26 

            for char in word: 
                count[ord(char) - ord('a')] += 1

            groupAg[tuple(count)].append(word)
            
        # Return the values of all keys
        return list(groupAg.values())