# BaekJoon 4673
# https://www.acmicpc.net/problem/4673
# 'not in' 문법을 실질적을로 처음 써 봤다. 더 복잡해졌을 코드가 훨씬 짧고 간결해진 걸 보니 뿌듯하다. 문제에서 요구하는 게 뭔가 많아보여도 차근차근 과정대로 짜니 무사히 완성이 되었다. 

def d(n):
    s = n
    while n > 0:
        s += n % 10
        n = n // 10
    return s 

i = 1
a = []
for i in range(1, 10001):
    a.append(d(i))
    i+=1

for i in range(1, 10001):
    if i not in a:
        print(i)
