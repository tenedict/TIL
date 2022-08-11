n = int(input())

answer = 0
dic = {}
for _ in range(n):
    a, b = map(int,input().split())
    if a not in dic.keys():
        dic[a] = b
        
    elif a in dic.keys():
        if dic.get(a) != b:
            dic[a] = b
            answer += 1
           
print(answer)
