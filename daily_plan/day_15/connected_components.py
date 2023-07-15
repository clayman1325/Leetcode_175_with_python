class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, adj,visited):
            visited.add(node)
            if(not adj.get(node)): return

            for n in adj[node]:
                if n not in visited:
                    dfs(n, adj, visited)
            return

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
        count = 0
        for node in range(n):
            if not node in visited:
                dfs(node, adj, visited)
                count += 1
        return count