# 4344
# https://www.acmicpc.net/problem/4344
# 문제 구현 자체는 쉬웠지만, 마지막 출력부분에 조금 어려움을 겼었다. python에서는 round함수가 정확한 반올림이라고 할 수 없기 때문에 문자열 포맷팅 방법으로 변경하였다.

c = int(input())
for _ in range(c):
    cnt = 0
    a = list(map(int, input().split()))
    stu = a[0]
    scores = a[1:]
    avg = sum(scores)/stu
    for x in scores:
        if x > avg:
            cnt+=1
    perc = cnt/stu * 100
    print('{:.3f}%'.format(perc))