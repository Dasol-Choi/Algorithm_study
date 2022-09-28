# BaekJoon 1712
# https://www.acmicpc.net/problem/1712
# while문으로 짰다가 시간초과가 떠서 한참 고심한 코드


a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(int(a/(c-b)) +1)  