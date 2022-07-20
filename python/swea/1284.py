a = input()
a= int(a)

for i in range(1,a+1):
    P, Q, R, S, W=map(int,input().split())
    if R < W:
        d =(Q + (W-R)*S)
        if d < P*W:
            print(f'#{i} {d}')
        else:
            print(f'#{i} {W*P}')
    else:
        if Q > P*W:
            print(f'#{i} {P*W}')
        else:
            print(f'#{i} *{Q}')

        