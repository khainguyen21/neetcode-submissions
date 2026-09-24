class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs: 
            output.append(str(len(word)) + '#' + word)
        return ''.join(output)
        
    def decode(self, s: str) -> List[str]:
        output = []
        
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '#' and j < len(s):
                j += 1

            else: 
                output.append(s[j + 1 : j + 1 + int(s[ i : j ])])

                i = j + 1 + int(s[ i : j ])
                j = i

        return output 
                
