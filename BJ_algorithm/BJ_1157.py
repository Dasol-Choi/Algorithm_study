# BaekJoon 1157
# https://www.acmicpc.net/problem/1157

s = input().upper()  #문자열 받기
new_s = set(s)  #문자열에서 중복을 제거한 알파벳 모음
a = {}
for x in new_s:  #key는 알파벳, valu는 0으로 셋팅한 딕셔너리 생성
    a[x] = 0
for x in s:  #각 알파벳의 숫자를 카운트해서 딕셔너리에 저장
    a[x] += 1
        
nums = list(a.values())   #카운트한 숫자들의 리스트   
c = 0
for key, value in a.items():  #딕셔너리의 key와 value를 돌며 조건 확인
    if value == max(nums):  #최대값의 개수 세기
        c +=1
        k = key  #최대값일 때의 key값(알파벳) 저장
if c > 1:  #최대값이 하나보다 많을 때 '?'출력
    print('?') 
else:
    print(k) #최대값이 하나일 때 key값(알파벳) 출력