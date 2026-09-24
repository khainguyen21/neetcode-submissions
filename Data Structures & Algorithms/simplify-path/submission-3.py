class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        curr = ""

        for c in path + '/': 
            if c == '/':
                if curr == '..':
                    if res: res.pop()

                elif curr != '' and curr != '.':
                    res.append(curr)

                curr = ""

            else: 
                curr += c

        return "/" + "/".join(res)