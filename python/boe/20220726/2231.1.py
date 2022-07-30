n = input()
len_n = len(n)
answer = []
n= int(n)

for i in range(len_n-1,-1,-1):
    print(i)
    cha = n//((10**i)+1)
    answer.append(cha)
    print(cha)
    n = n%((10**i)+1)
    
print(answer)