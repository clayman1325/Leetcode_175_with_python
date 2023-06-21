class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        path = path.split("/")
        up = []

        while(len(path)>0):
            last_elem = path.pop()
            if(last_elem == "" or last_elem == "."): result
            elif(last_elem == ".."): up.append(True)
            else:
                if(len(up) == 0):
                    result.append(last_elem)
                elif(len(up) > 0): up.pop()

        if(result == []): return "/"
        path = '/'.join(result[::-1])

        return f'/{path}'