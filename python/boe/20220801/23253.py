import sys
a, b = map(int,sys.stdin.readline().split())


alllist = []
p = True
for j in range(1,b+1):
    books = int(input())
    bookti = list(map(int,input().split()))
    for k in range(books-1):
        if bookti[k] < bookti[k+1]:
            print('No')
            p = False
        else: 
            continue
if p:
    print('Yes')
