n = int(input())
n1 =n

c = 0
while n1 == n:
    if n < 10:
        n = n*10
    a = n//10   
    b = (n-a*10)
    n = a + b
    c +=1
        
print(c)