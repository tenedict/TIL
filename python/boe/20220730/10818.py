n = input()

num_list_ = list(map(int,input().split()))

a = num_list_[0]
for i in num_list_:
    if int(i) <= a:
        a = i
    else:
        continue
b = num_list_[0]
for i in num_list_:
    if int(i) >= b:
        b = i
    else:
        continue
print(a,b)
