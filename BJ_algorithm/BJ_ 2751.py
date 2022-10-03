# BaekJoon 2751
# https://www.acmicpc.net/problem/2751

import sys
n = int(sys.stdin.readline())
li= []
for _ in range(n):
    a = int(sys.stdin.readline())
    li.append(a)
li.sort()
for x in li:
    print(x)