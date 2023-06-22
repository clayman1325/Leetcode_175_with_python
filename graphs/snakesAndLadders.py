def snakesAndLadders(self, board: List[List[int]]) -> int:
        dir_right = range(len(board))
        dir_left  = range(len(board)-1, -1, -1)

        new_board = []
        for x in dir_left:
            direction = dir_right if(x % 2 == 1) else dir_left
            for y in  direction:
                new_board.append(board[x][y])

        curr = 1
        q = [{"steps": 0, "position": 1 }]
        count = 0
        while(q):
            cur = q.pop(0)

            if(cur["position"] == len(board) * len(board) - 1): return cur["steps"]
            for step in range(6):
                next_step = min(cur["position"] + step, len(board) * len(board) - 1)
                if new_board[next_step] != -1:
                    next_step = new_board[next_step]

                q.append({ "steps": cur["steps"] + 1, "position": next_step })

        return -1
