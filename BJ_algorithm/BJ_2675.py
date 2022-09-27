# BaekJoon 2675
# https://www.acmicpc.net/problem/2675

t = int(input())

for _ in range(t):
    r, s = input().split()
    p =''
    for x in s:
        p += x*int(r)
    print(p)