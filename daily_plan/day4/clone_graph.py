class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def rec_clone(visited, node):
            if(visited.get(node)): return visited[node]

            visited[node] = Node(node.val, [])
            if node.neighbors:
                for neighbor in node.neighbors:
                    visited[node].neighbors.append(rec_clone(visited, neighbor))
            return visited[node]

        if(not node): return node

        visited = {}
        visited[node] = Node(node.val, [])

        if node.neighbors:
            for neighbor in node.neighbors:
                nei = rec_clone(visited, neighbor)
                visited[node].neighbors.append(nei)

        return visited[node]