# BaekJoon 2650
# https://www.acmicpc.net/problem/2750
# 간단한 srot 함수를 사용하는 대신에 직접 구현해보고자 노력했다. 결과가 잘 나오는 게 얼떨떨하고 신기하다. 

n = int(input())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)

for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
for i in l:
    print(i)