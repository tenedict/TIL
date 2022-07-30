# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt")

# a = int(input())
# b = int(input())
# c = int(input())
# n = a*b*c
# n = str(n)
# a0 = 0
# a1 = 0
# a2 = 0
# a3 = 0
# a4 = 0
# a5 = 0
# a6 = 0
# a7 = 0
# a8 = 0
# a9 = 0

# for i in n:
#     if int(i) == 0:
#         a0 += 1
#     elif int(i) == 1: 
#         a1 += 1
#     elif int(i) == 2: 
#         a2 += 1
#     elif int(i) == 3: 
#         a3 += 1
#     elif int(i) == 4: 
#         a4 += 1
#     elif int(i) == 5: 
#         a5 += 1
#     elif int(i) == 6: 
#         a6 += 1
#     elif int(i) == 7: 
#         a7 += 1
#     elif int(i) == 8: 
#         a8 += 1
#     else:
#         a9 += 1

# print(a0)
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# print(a6)
# print(a7)
# print(a8)
# print(a9)

a = int(input())
b = int(input())
c = int(input())

multiply_abc = str(a * b * c)

for i in range(10):
    cnt = 0
    for char in multiply_abc:
        if int(char) == i:
            cnt += 1
    print(cnt)