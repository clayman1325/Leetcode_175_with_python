class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bfs(mat, cell, directions, seen):
            count = 0
            q = [[cell, count]]

            while(q):
                cur_cell = q.pop(0)

                if mat[cur_cell[0][0]][cur_cell[0][1]] == 0: return cur_cell[1]

                for dir in directions:
                    row = cur_cell[0][0] + dir[0]
                    col = cur_cell[0][1] + dir[1]

                    if(
                        row >=0 and row < len(mat) and col >=0 and col < len(mat[0])
                    ):
                        if (row, col) not in seen:
                            q.append([(row,col), cur_cell[1] + 1])

            return -10000

        seen = set()
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        result = []
        for row in range(len(mat)):
            result.append([0] * len(mat[0]))
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    seen.add((row,col))
                    count = bfs(mat, (row,col), directions, seen)
                    result[row][col] = count

        return result