# 주어진 숫자를 뒤집은 결과를 출력하시오. 
#! 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지


t = (input())
n = (len(t))
t = int(t)


s = 0
for i in range(1,n+1):
    a = t//((10**n)/10)
    t = t - (a*(10**(n-1)))
    a = a*(10**(i-1))
    print(a)
    s += a
    n -= 1
    
print(round(s))