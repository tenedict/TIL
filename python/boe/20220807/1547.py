answer = 1
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    if a == answer:
        answer = b 
    elif answer == b:
        answer = a
    
print(answer)