def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    directions = [[1,0], [0,1], [-1,0], [0, -1]]
    starting_color = image[sr][sc]
    q = []
    q.append([sr,sc])
    count = 0
    while(q and count < 20):
        len(q)
        pixel = q.pop(0)
        image[pixel[0]][pixel[1]] = color

        for dir in directions:
            row = pixel[0] + dir[0]
            col = pixel[1] + dir[1]

            if(
                row >=0 and row < len(image) and col >= 0 and col < len(image[0]) and
                image[row][col] == starting_color
            ):
                q.append([row, col])
        count += 1
    return image