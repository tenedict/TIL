n = int(input())
list_ = []
for i in range(n):
    list_ += (input().split())
setlist_ = set(list_)

a = max(list_)
maxti = list_.count(a)

sup =  []

for j in setlist_:
    print(j)
    cou = list_.count(j)
    if cou == maxti:
        sup += j

print(sup)


# a = max(list_)
# list_ = sorted(list_)
# b = max(list_)
# print(list_)
# print(a)
# print(b)