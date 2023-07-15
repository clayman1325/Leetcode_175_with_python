lass Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [[1,2],[2,1],[2,-1],[-2,1],[-2,-1],[-1,-2],[-2,1],[-1,2]]

        pos = (0,0)
        count = 0
        q = [pos]
        visited = set()

        while q:
            len_q = len(q)

            for _ in range(len_q):
                pos = q.pop(0)

                if pos[0] == x and pos[1] == y: return count

                for move in moves:
                    next_move = (pos[0] + move[0], pos[1] + move[1])
                    if next_move not in visited:
                        visited.add(next_move)
                        q.append(next_move)
            count += 1

        return count