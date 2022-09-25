# BaekJoon 2562
# https://www.acmicpc.net/problem/2562
# 최대값을 활용하는 기본 문제

for i in range(10):
    n = int(input())
    if n > max:
        max = n
        idx = i+1
print(max)
print(idx)
