A = list(map(int,input().split()))
B = list(map(int,input().split()))

ascore = 0
bscore = 0


for i in range(0,10):
    if A[i] > B[i]:
        ascore += 3
    elif B[i] > A[i]:
        bscore += 3
    else:
        ascore += 1
        bscore += 1
print(ascore,bscore)
answer = 'k'
if ascore > bscore:
    print('A')
elif bscore > ascore:
    print('B')
elif ascore == bscore:
    if ascore == 10 and bscore ==10:
        print('D')
    else:
        for k in range(9,-1,-1):
            if A[k] > B[k]:
                print('A')
                break
            elif B[k] > A[k]:
                print('B')
                break
            else:
                continue

