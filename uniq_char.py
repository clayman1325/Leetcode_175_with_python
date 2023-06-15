class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = 'holamhola'

        queue = []
        set = {}
        for x in range(len(s)):
            if(s[x] not in set):
                queue.append([s[x], x])
                set[s[x]] = s[x]
            else:
                stack = []
                next = True
                while(len(queue) and next):
                    element = queue.pop(0)
                    if(element[0] == s[x]):
                        next = False
                    else:
                        stack.append(element)
                while(len(stack) > 0):
                    element = stack.pop()
                    queue[:0] = [element]

        return queue[0][1] if len(queue) > 0  else -1