n = int(input())



for i in range(1,n+1):
    result = 0
    for t in str(i):
        result += int(t)
    if n == i + result:
        print(i)
        break
    elif n == i:
        print(0)
        break