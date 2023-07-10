class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for num in range(numCourses):
            adj[num] =  []
        for requisite in prerequisites:
            adj[requisite[0]].append(requisite[1])

        for num in range(numCourses):
            test_course = num
            visited = set()
            q = [num]

            while(q):
                cur_course = q.pop()

                for next_course in adj[cur_course]:
                    if adj[next_course] == True:
                        q = []
                        break
                    if next_course in visited: return False
                    visited.add(next_course)
                    q.append(next_course)
            adj[num] = True
        return True