# BaekJoon 2562
# https://www.acmicpc.net/problem/3052
# 나머지 연산자, 세트의 특징을 묻는 기본 문제

a = set()
for i in range(10):
    n = int(input())
    a.add(n % 42)
print(len(a))
