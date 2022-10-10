# BaekJoon 2164
# https://www.acmicpc.net/problem/2164
# 아주 기초적인 큐 구현 문제

import sys
from collections import deque
n = int(sys.stdin.readline())
card = list(i for i in range(1, n+1))
Q = deque(card)
while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())       
print(Q[0])