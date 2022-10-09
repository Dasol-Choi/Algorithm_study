# BaekJoon 10828
# https://www.acmicpc.net/problem/10828
# 기본적인 스택 구현 문제


n = int(input())
li = []
cmd = list(input() for _ in range(n))  # 명령어들을 리스트로 저장
for x in cmd:
    if 'push' in x:  # push 옆에 정수를 따로 떼서 리스트에 삽입
        c, num = x.split()
        li.append(int(num))
    elif x == 'top':
      print(li[-1] if len(li) > 0 else -1)       
    elif x == 'size':
        print(len(li))
    elif x == 'empty':
      print(1 if len(li)==0 else 0)
    elif x == 'pop':
      print(li.pop() if len(li) > 0 else -1)
          print(li.pop())