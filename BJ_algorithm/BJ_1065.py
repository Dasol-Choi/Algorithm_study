# BaekJoon 1065
# https://www.acmicpc.net/problem/1065

n = int(input())

# 숫자 데이터타입 그대로 유지해서 구현한 코드
def func(n):  
    cnt = 0
    for i in range(1, n+1):
        if i >= 100:
            a1 = i %10  #셋째 자리수
            i = i // 10
            a2 = i % 10  #둘째 자리수
            a3 = i // 10   #첫째 자리수
            if a3 - a2 == a2 - a1 :  #등차수열 확인
                cnt += 1
        else:    # 일의 자리부터 십의 자리 숫자까지는 무조건 한수
            cnt += 1
    return cnt
print(func(n))


# 숫자 -> 문자열로 -> 숫자로 데이터타입 변경해서 구현한 코드
# def func(n):  
#     cnt = 0
#     for i in range(1, n+1):
#         temp = list(map(int, str(i)))
#         if i < 100:
#             cnt += 1           
#         elif temp[0] - temp[1] == temp[1] - temp[2]:   
#             cnt += 1
#     return cnt
# print(func(n))