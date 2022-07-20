a = input()
a= int(a)

h=1
kk = 1
for i in range(1,a+1):
    b = int(input())
    if b == 1:
        print('#%d 1'%i)
    elif b == 2:
        print('#%d -1'%i)

    elif b == 3:
        print('#%d 2'%i)

    elif b == 4:
        print('#%d -2'%i)

    elif b == 5:
        print('#%d 3'%i)

    elif b == 6:
        print('#%d -3'%i)

    elif b == 7:
        print('#%d 4'%i)

    elif b == 8:
        print('#%d -4'%i)

    elif b == 9:
        print('#%d 5'%i)
    
    elif b == 10:
        print('#%d -5'%i) 