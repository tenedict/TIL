n = list(input())

g = 0

for i in range(102):
    a = input()
    if a == '문제':
        g += 1
    elif a == '고무오리':
        if g == 0:
            g += 2
        else:
            g -= 1
    else:
        break
if g == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
