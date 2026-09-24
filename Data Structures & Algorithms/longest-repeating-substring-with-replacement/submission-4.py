class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countChar = defaultdict(int)

        l , r = 0 , 0
        longest = 0 
        while r < len(s): 
            countChar[s[r]] += 1
            
            selectedChar = ''
            currentMax = 0
            for key in countChar: 
                if currentMax < countChar[key]: 
                    currentMax = countChar[key]
                    selectedChar = key

            if r - l + 1 - countChar[selectedChar] > k:
                countChar[s[l]] -= 1
                l += 1
            
            longest = max(r - l + 1, longest)
            r += 1

        return longest

                