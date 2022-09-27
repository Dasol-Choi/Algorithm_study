# BaekJoon 15596
# https://www.acmicpc.net/problem/15596
# 너무 기본적인 for 문 형태, 간단한 함수 대신 최대한 직접 구현하는 것을 추구하자!

def solve(a: list) :
    s = 0 
    for i in a:
        s += i
    return s

    