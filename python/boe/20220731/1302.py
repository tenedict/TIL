n = int(input())
list_ = []
for i in range(n):
    list_ += (input().split())
setlist_ = set(list_)
print(list_)
origin = list_.count(list[0])
for i in list_:
    a = list_.count(i)
    if a >= origin:
        origin = a
print(origin)

sup =  []

for j in setlist_:
    cou = list_.count(j)
    print(cou)
    if cou >= origin:
        sup += (j.split())
sup .sort()
print(sup)
answer = (sup[0])
print(answer)