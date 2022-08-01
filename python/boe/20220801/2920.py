n = input().split('-')
print(n)

a = ''
for i in n:
    a += i[0]

print(a)


a = list(input().split('-'))
for i in a:
    print(i[0], end = '')