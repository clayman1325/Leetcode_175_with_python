class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(start, finish, graph, visited):
            if start == finish:
                return 1
            visited.add(start)
            value = 0
            if graph[start]:
                for neig in graph[start]:
                    if neig[0] not in visited:
                        value = dfs(neig[0], finish, graph, visited)
                        if not value:
                            continue
                        else:
                            return neig[1] * value
                    else:
                        value = False
            return value
        graph = defaultdict(defaultdict)
        for i in range(len(equations)):
            eq = equations[i]
            val = values[i]
            if graph[eq[1]]:
                graph[eq[1]].append([eq[0], 1/val])
            else:
                graph[eq[1]] = [[eq[0], 1/val]]
            if graph[eq[0]]:
                graph[eq[0]].append([eq[1], val])
            else:
                graph[eq[0]] = [[eq[1], val]]
        valid_values = set(graph.keys())
        request = []
        for q in queries:
            if q[0] not in valid_values and q[1] not in valid_values:
                request.append(-1)
            elif q[0] == q[1]:
                request.append(1)
            else:
                value = dfs(q[0],q[1], graph, set([]))
                if value == 0: value = -1
                request.append(value)
        return request