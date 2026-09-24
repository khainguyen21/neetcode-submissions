class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []

        # check = {"/", "//", "///"}

        splitedPath = path.split('/')
        print(splitedPath)
        for c in splitedPath:
            
            if c == '' or c == '.':
                continue

            if c == '..':
                if res:  
                    res.pop()
                    continue
                else: 
                    continue
            
            res.append(c)
        
        return '/' + '/'.join(res)