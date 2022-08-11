n = (input())
a = n.count(':-)')
b = n.count(':-(')
if a == 0 and b == 0:
    print('none')
elif a>b:
    print('happy')
elif a<b:
    print('sad')
else:
    print('unsure')