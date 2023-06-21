class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        adjList = []
        for x in range(5):
            test = []
            adjList.append([])
        q = [node]
        visited = {}
        while(len(q) > 0):
            elem = q.pop(0)

            if elem and elem.val not in visited:
                visited[elem.val] = True
                if(not adjList[elem.val]):
                    adjList[elem.val] = Node(elem.val, [])
                for x in elem.neighbors:
                    if(not adjList[x.val]):
                        adjList[x.val] = Node(x.val, [])
                    adjList[elem.val].neighbors.append(x.val)

                    q.append(x)
        adjList.pop(0)


        return adjList[0]