t = int(input()) #t만큼 10개의 값을 입력받는다.
 
for te in range(1,t+1):   #1부터 t까지 한바퀴 돌면서 인풋받는다.
    a = map(int, input().split()) #인풋에 들어오는 숫자들 이 스플릿으로 나눠짐
    
    h =0
    for i in a:
        if i%2 != 0:
            h +=i

    print(f'#{te} {h}')