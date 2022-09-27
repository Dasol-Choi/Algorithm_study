# BaekJoon 10809
# https://www.acmicpc.net/problem/10809

s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for x in alpha:
    print(s.find(x), end=' ')


s = input()

for i in range(97,123) :
    print(s.find(chr(i)), end=' ')