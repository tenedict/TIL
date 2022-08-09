#우 하 우상 우하
dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]



black = 1
white = 2
n = 19

board = []

for _ in range(n):
    temp_list = list(map(int,input().split()))
    board.append(temp_list)

for y in range(n):
    for x in range(n):
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            while True:
                if not(-1 <ny <n and -1<nx<n):
                    break
                if not(board[y][x] == board[ny][nx]):
                    break

                stone_count += 1

                ny = ny + dy[d]
                nx = ny + dx[d]

            if stone_count = 5:
                prev_y = y - dy[d]
                prev_x = x - dx[d]

                if not(-1<prev_y<n and -1 < prev_x<n) or board[y][x]