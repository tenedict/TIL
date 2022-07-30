list_=[]
for i in range(10):
    a = int(input())
    a = a%42
    list_.append(a)
list_ = set(list_)
print(len(list_))