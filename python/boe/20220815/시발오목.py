import sys
sys.stdin = open("시발오목.txt")

n = [input().split() for _ in range(19)]


dx =[1,0,1,-1]
dy =[0,1,1,1]
answerli = []

ccc = 0
for i in range(19):
    for j in range(19):
        a = n[i][j]
        if a != '0':
            for k in range(4):
                if 0<= i+dx[k] <19 and 0<= j+dy[k] < 19:
                    b = n[i+dx[k]][j+dy[k]]
                    
                    if a == b:
                        answer = []
                        answer.append(n[i][j])
                        answer.append(b)
                        for kk in range(2,6):
                            if 0<= i+dx[k]*kk <19 and 0<= j+(dy[k]*kk) < 19:
                                c = n[i+(dx[k]*kk)][j+(dy[k]*kk)]
                                answer.append(c)
                                if len(answer) == 6:
                                    if answer[1] == answer[2] and answer[2] == answer[3] and answer[3] == answer[4] and answer[4] != answer[5]:
                                        
                                        if 0<= i-dx[k] <19 and 0<= j-dy[k]<19:
                                            mok = n[i-dx[k]][j-dy[k]]
                                            if mok != a:
                                                if ccc==0:
                                                    print(a)
                                                 
                                                    print(i+1,j+1)
                                                    ccc = 1
                                                   
                                        else:
                                            if ccc==0:
                                                print(a)
                                                print(i+1,j+1)
                                                ccc = 1
                                              

                                                    
                                elif len(answer) == 5:
                                    if not 0<= i+(dx[k]*5) <19 and not 0<= j+(dy[k]*5)<19:
                                        if answer[1] == answer[2] and answer[2] == answer[3] and answer[3] == answer[4]:
                                            
                                            if ccc==0:
                                                print(a)
                                              
                                                print(i+1,j+1)
                                                ccc = 1
                                    
                                    if not 0<= i+(dx[k]*5) <19 or not 0<= j+(dy[k]*5)<19:
                                        if answer[1] == answer[2] and answer[2] == answer[3] and answer[3] == answer[4]:
                                                mok = n[i-dx[k]][j-dy[k]]
                                                if mok != a:
                                                    if ccc==0:
                                                        print(a)
                                                       
                                                        print(i+1,j+1)
                                                        ccc = 1
if ccc == 0:
    print(0)

                                                
                                            
                                

