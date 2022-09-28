# BaekJoon 2869
# https://www.acmicpc.net/problem/2869
# 살짝 고심해야 했던 수학 연산 문제

import math
a, b, v = map(int, input().split())

day = (v-a) / (a-b) + 1
print(math.ceil(day))


