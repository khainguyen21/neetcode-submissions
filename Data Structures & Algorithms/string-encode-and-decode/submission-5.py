class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for i in range(len(strs)):
            result.append(str(len(strs[i])) + '#' + strs[i])
        
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i , j = 0 , 0
        while i < len(s):
            while s[j] != '#' and j < len(s):
                j += 1
            else: 
                result.append(s[j+1 : j+1+int(s[i:j])])
                i = j + 1 + int(s[i:j])
                j = i

        return result