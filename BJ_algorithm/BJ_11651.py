# BaekJoon 11651
# https://www.acmicpc.net/problem/11651

import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())  # x, y값 입력받기
    t = (y, x)  # x, y값 바꿔서 튜플로 묶기
    li.append(t)  # 튜플을 리스트에 삽입
li.sort()  # 리스트 오름차순 정렬                 
for i in li:
    print(i[1], i[0])  # x, y값 다시 바꿔서 출력