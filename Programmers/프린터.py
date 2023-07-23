# Programmers_프린터
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 하루 종일 고민했던 문제. 개념자체는 큐를 구현하면 되는 문제이지만, 조건이 좀 까다로웠다.
# any라는 문법을 찾아 본 후에야 완성이 가능했다. enumerate도 까먹지 않게 자주자주 써보자!

from collections import deque
def solution(priorities, location):
    Q = deque()
    answer = 0
    for idx, prio in enumerate(priorities):
        Q.append((idx, prio))
    while True:        
        pl = Q.popleft()
        if any(pl[1] < x[1] for x in Q):
            Q.append(pl)
        else:
            answer += 1
            if pl[0] == location:
                return answer
                break