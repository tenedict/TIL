a = 5 
b =4
li = [
[1,0,1,0,0]
[1,0,0,0,0]
[1,0,1,0,1]
[1,0,0,1,0]
]



dx = [0,1,1]
dy = [1,0,1]

for x in range(a-1):
    for y in range(b-1):
      
        if li[x][y] == '1':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx <a and 0<= ny < b:
                    if li[nx][ny] == 0:
                        
                                              