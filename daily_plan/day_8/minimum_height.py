class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def adj_matrix(edges):
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
            return adj

        def dfs(root, adj, visited, height):
            visited.add(root)

            heights = [height]
            for child in adj[root]:
                if child not in visited:
                    cur_height = dfs(child, adj, visited, height + 1)
                    heights.append(cur_height)

            return max(heights)

        if n == 1: return [0]

        adj = adj_matrix(edges)
        min_height = 10000
        min_roots = []

        for root in range(n):
            visited = set()

            cur_height = dfs(root, adj, visited, 0)

            if(cur_height == min_height):
                min_roots.append(root)
            if(cur_height < min_height):
                min_height = cur_height
                min_roots = [root]

        return min_roots