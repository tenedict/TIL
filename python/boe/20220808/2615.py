baduk = [list(map(int,input().split())) for _ in range(19)]
answer = 0
k = 1
for i in range(19):
    for j in range(19):
        if baduk[i][j] == 1:
            if j <15:
                count = 0
                for h in range(1,6):
                    if i == 0 and j == 0:
                        if baduk[i][j+h] == 1:
                            count += 1
                            if count == 4:
                                answer = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer =99                           
                        elif baduk[i][j+h] != 1:
                            break
                    elif baduk[i][j-1] !=1:
                        if baduk[i][j+h] == 1:
                            count += 1
                            if count == 4:
                                answer = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer =99                           
                        elif baduk[i][j+h] != 1:
                            break
            
                 
            if i <15:
                count = 0
                for h in range(1,6):
                    if i == 0 and j == 0:
                        if baduk[i+h][j] == 1:
                            count += 1
                            if count == 4:
                                answer = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer =99 
                        elif baduk[i+h][j] != 1:
                            break
                    elif baduk[i-1][j] !=1:
                        if baduk[i+h][j] == 1:
                            count += 1
                            if count == 4:
                                answer = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer =99 
                        elif baduk[i+h][j] != 1:
                            break
            
                
                  
            if i<15 and j <15:
                count = 0
                for h in range(1,6):
                    if i == 0 or j == 0:
                        if baduk[i+h][j+h] == 1:
                            count += 1
                            if count == 4:
                                answer = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer =99 
                        elif baduk[i+h][j+h] != 1:
                            break
                    elif baduk[i-1][j-1] !=1:
                        if baduk[i+h][j] == 1:
                            count += 1
                            if count == 4:
                                answer = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer =99 
                        elif baduk[i+h][j] != 1:
                            break
                    

            if i<15 and 3<j:
                    count = 0
                    for h in range(1,6):
                        if i == 0 or j == 18:
                            if baduk[i+h][j-h] == 1:
                                count += 1
                                if count == 4:
                                    answer = 100
                                    real1 = i
                                    real2 = j
                                if count == 5:
                                    answer =99 
                            elif baduk[i+h][j-h] != 1:
                                break
                        elif baduk[i-1][j+1] !=1:
                            if baduk[i+h][j-h] == 1:
                                count += 1
                                if count == 4:
                                    answer = 100
                                    real1 = i
                                    real2 = j
                                if count == 5:
                                    answer =99 
                            elif baduk[i+h][j-h] != 1:
                                break
if answer == 100:
    k = 2
    print(1)
    print(real1+1,real2+1)


answer1 = 0
for i in range(19):
    for j in range(19):
        if baduk[i][j] == 2:
            if j <15:
                count = 0
                for h in range(1,6):
                    if i == 0 and j == 0:
                        if baduk[i][j+h] == 2:
                            count += 1
                            if count == 4:
                                answer1 = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer1 =99                           
                        elif baduk[i][j+h] == 2:
                            break
                    elif baduk[i][j-1] !=2:
                        if baduk[i][j+h] == 2:
                            count += 1
                            if count == 4:
                                answer1 = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer1 =99                           
                        elif baduk[i][j+h] == 2:
                            break
          
                 
            if i <15:
                count = 0
                for h in range(1,6):
                    if i == 0 and j == 0:
                        if baduk[i+h][j] == 2:
                            count += 1
                            if count == 4:
                                answer1 = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer1 =99 
                        elif baduk[i+h][j] != 2:
                            break
                    elif baduk[i-1][j] !=2:    
                        if baduk[i+h][j] == 2:
                            count += 1
                            if count == 4:
                                answer1 = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer1 =99 
                        elif baduk[i+h][j] != 2:
                            break

            
                
                  
            if i<15 and j <15:
                count = 0
                for h in range(1,6):
                    if i == 0 or j == 0:
                        if baduk[i+h][j+h] == 2:
                            count += 1
                            if count == 4:
                                answer1 = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer1 =99 
                        elif baduk[i+h][j+h] != 2:
                            break
                    elif baduk[i-1][j-1] !=2:
                        if baduk[i+h][j+h] == 2:
                            count += 1
                            if count == 4:
                                answer1 = 100
                                real1 = i
                                real2 = j
                            if count == 5:
                                answer1 =99 
                        elif baduk[i+h][j+h] != 2:
                            break\
            
            if i<15 and 3<j:
                    count = 0
                    for h in range(1,6):
                        if i == 0 or j == 18:
                            if baduk[i+h][j-h] == 2:
                                count += 1
                                if count == 4:
                                    answer1 = 100
                                    real1 = i
                                    real2 = j
                                if count == 5:
                                    answer1 =99 
                            elif baduk[i+h][j-h] != 2:
                                break
                        elif baduk[i-1][j+1] != 2:
                                if baduk[i+h][j-h] == 2:
                                    count += 1
                                    if count == 4:
                                        answer1 = 100
                                        real1 = i
                                        real2 = j
                                    if count == 5:
                                        answer1 =99 
                                elif baduk[i+h][j-h] != 2:
                                    break
if answer1 == 100:
    k = 2
    print(2)
    print(real1+1,real2+1)

if k == 1:
    print(0)