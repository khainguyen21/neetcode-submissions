class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs: 
            res.append(str(len(s)) + '#' + s)

        return "".join(res)
    def decode(self, s: str) -> List[str]:
        l = 0 
        r = l + 1
        res = []
        print(s)
        while r < len(s):
            if s[r] == '#':
                res.append(s[r + 1 : r + 1 + int(s[l:r])])
                l = r + 1 + int(s[l:r])
                r = l

            r += 1
            
        return res