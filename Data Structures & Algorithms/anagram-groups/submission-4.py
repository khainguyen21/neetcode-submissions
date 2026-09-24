class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped_anagrams = defaultdict(list)

        for word in strs: 
            count = [0] * 26

            for char in word: 
                count[ord(char) - ord("a")] += 1     

            grouped_anagrams[tuple(count)].append(word)

        return list(grouped_anagrams.values())

