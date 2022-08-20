
for _ in range(int(input())):
    m = input()
    m1 =set(input().split())
    h = input()
    h1 = list(input().split())
    for i in h1:
        print(1 if i in m1 else 0)


for _ in range(int(input())):
    N = int(input())
    li1 = set(map(int, input().split()))
    M = int(input())
    li2 = list(map(int, input().split()))
    for n in li2:
        print(1 if n in li1 else 0)