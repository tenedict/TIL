import sys

sys.stdin = open("_Flatten.txt")


um = 10 
    
for num in range(1,um+1):
    dump = int(input())

    li = input().split()
    li = list(map(int,li))

    for i in range(dump):
        li.sort()
        a = li.pop()
        li.sort(reverse =True)
        b = li.pop()
        if a == b:
            print(f'#{num} {0}')
            break
        if a - b == 1:
            print(f'#{num} {1}')
            break
        li.append(a-1)
        li.append(b+1)
    li.sort()
    a1 = li.pop()
    li.sort(reverse =True)
    b1 = li.pop()
    
    print(f'#{num} {a1-b1}')