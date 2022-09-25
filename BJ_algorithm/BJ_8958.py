# BaekJoon8958
# https://www.acmicpc.net/problem/8958

t = int(input())
for _ in range(t):
    quiz = input()
    res = 0
    cnt = 0
    for x in quiz:
        if x == 'O':
            cnt += 1
        else:
            cnt = 0
        res += cnt
    print(res)