n = int(input())

for  __ in range(n):
    a, b = map(int,input().split())
    bw = [list(map(int,input().split())) for _ in range(a)]

    count = 0
    answer = 0
    for j in range(b):
    # i가 인덱스 0부터 3까지
        for i in range(a-1,-1,-1):
    #j가 인덱스 4부터 0까지
            if i == a-1:
                count = 0
            if bw[i][j] == 0:
                count += 1
                
            elif bw[i][j] == 1:
                answer += count
    print(answer)
