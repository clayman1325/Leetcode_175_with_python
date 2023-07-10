class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges and n > 1: return False
        if not edges and n == 1: return True
        adj = {}
        for edge in edges:
            if adj.get(edge[0]):
                adj[edge[0]].append(edge[1])
            else:
                adj[edge[0]] = [edge[1]]
            if adj.get(edge[1]):
                adj[edge[1]].append(edge[0])
            else:
                adj[edge[1]] = [edge[0]]

        visited = set()
        parent = {}
        stack = [edges[0][0]]
        while len(stack):
            node = stack.pop()
            visited.add(node)
            for neighboor in adj[node]:
                if parent.get(node) == neighboor: continue
                if neighboor in parent: return False
                stack.append(neighboor)
                parent[neighboor] = node

        return len(visited) == n