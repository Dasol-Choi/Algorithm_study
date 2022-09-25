# # BaekJoon 1546
# https://www.acmicpc.net/problem/1546

n = int(input())
a = list(map(int, input().split()))
new_a = []
max = max(a)
for i in a:
    new_a.append(i / max*100)
print(sum(new_a)/len(a))
