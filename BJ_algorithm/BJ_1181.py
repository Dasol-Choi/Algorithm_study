# BaekJoon 1181
# https://www.acmicpc.net/problem/1181

n = int(input())
li = []
for i in range(n):
    s = input()  #문자받기
    t = (len(s), s)  #문자의 길이와 문자를 튜플로 묶기
    if t not in li:  #튜플을 리스트에 삽입
        li.append(t)
li.sort()  #리스트 오름차순 정렬
for i in li:  # 리스트 -> 튜플 -> 문자 선택해 출력
    print(i[1])