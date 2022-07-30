# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()
a1 = a[::-1]
b1 = b[::-1]

if a1 > b1:
    print(int(a1))
else :
    print(int(b1))