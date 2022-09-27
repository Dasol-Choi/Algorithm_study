# BaekJoon 1110
# https://www.acmicpc.net/problem/1110

n = new_n = int(input()) 
def func(x):
    right_num = x % 10 
    sum_num = x % 10 + x // 10
    return right_num * 10 + sum_num % 10

cnt = 1
while func(new_n) != n:
        new_n  = func(new_n) 
        cnt += 1
print(cnt)