t = int(input())
n = list(map(int,input().split()))

dif_list = []
dif = 0
for i in range(t-1): # out of range 해결
    if n[i] - n[i+1] < 0:
        dif += n[i+1] - n[i]
        dif_list.append(dif)
    if n[i] - n[i+1] >= 0:
        dif = 0

if len(dif_list) == 0:
    print('0')
else:
    print(max(dif_list))
