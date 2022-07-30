a, b = map(int,input().split())
list_ = list(map(int,input().split()))

if len(list_) == a:
    for i in list_:
        if i < b:
           print(i,end=' ')
    