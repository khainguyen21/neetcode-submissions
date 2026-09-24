class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        splitedPath = path.split('/')

        for c in splitedPath:
            
            if c == '' or c == '.':
                continue

            elif c == '..':
                if res: 
                    res.pop()
                else: 
                    continue

            else: 
                res.append(c)

        return ("/" + "/".join(res))