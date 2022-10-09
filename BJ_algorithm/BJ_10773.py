# BaekJoon 10773
# https://www.acmicpc.net/problem/10773
# 너무나도 간단한 스택 문제

import sys
i = sys.stdin.readline
k= int(i())
stack = []
for _ in range(k):
    a = int(i())
    stack.pop() if  a == 0 else stack.append(a)
print(sum(stack))