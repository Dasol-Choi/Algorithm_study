# BaekJoon 10818
# https://www.acmicpc.net/problem/10818
# 최대, 최소값을 구현하는 기본 문제

n = int(input())
a = list(map(int, input().split()))

max = -1000000
min = 1000000
for i in a:
    if i > max:
        max = i
    if i < min:
        min = i
print(min, max)
