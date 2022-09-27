# BaekJoon 1157
# https://www.acmicpc.net/problem/1157

s = input().upper()
a = {}
for x in s:
    a[x]= s.count(x)
a = list(a.values())

if a.count(max(a)) >= 1:
    print('?')
else:
    print(max(a))