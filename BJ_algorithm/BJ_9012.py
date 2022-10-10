# BaekJoon 9012
# https://www.acmicpc.net/problem/9012
# 조건에 잘 맞추어 스택을 구현하는 문제. 천천히 따라가면 쉽게 구현할 수 있는 문제!

import sys
ip = sys.stdin.readline

t = int(ip())
for _ in range(t):
    stack = []
    a =ip().rstrip()
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                print('NO')
                break
    else:
        print('NO') if stack else print('YES')