
n = 1
mo = ['a', 'e', 'i', 'o', 'u']
while n != '#':
    n = input()
    n = n.lower()
    answer = 0
    if n == '#':
        break
    for i in mo:
        k = n.count(i)
        answer += k
    print(answer)