# BaekJoon 11650
# https://www.acmicpc.net/problem/11650

import sys 
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    t = tuple(map(int, input().split()))  # 입력값을 튜플로 저장
    li.append(t)  # 튜플을 리스트에 삽입
li.sort()  # 리스트 정렬                 
for i in li:
    print(i[0], i[1])  # 리스트 안의 튜플값 출력