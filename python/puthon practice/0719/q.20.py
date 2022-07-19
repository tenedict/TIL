#정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

t = (input())
n = (len(t))
t = int(t)


s = 0
for i in range(1,n+1):
    a = t//((10**n)/10)
    t = t - (a*(10**(n-1)))
    s += a
    n -= 1
    
print(round(s))