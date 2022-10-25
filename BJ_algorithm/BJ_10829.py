# BaekJoon 10829
# https://www.acmicpc.net/problem/10829
# 구현 자체는 너무 간단해서 딱히 설명할 거리가 없을 것 같다.
# n을 2로 나눈 나머지를 문자열에 하나씩 쌓은 후 순서를 뒤집어 주니 이진수가 완성됐다.

n = int(input())
res = ''
while n > 0:
    res += str(n % 2)
    n = n //2
print(res[::-1])