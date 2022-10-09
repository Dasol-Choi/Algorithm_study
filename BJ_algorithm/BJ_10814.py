# BaekJoon 10814
# https://www.acmicpc.net/problem/10814

n = int(input())
names = []  
li = []
for i in range(n):
    age, name = input().split() #age, name 입력받기
    names.append(name)  #name 먼저 따로 저장
    t = (int(age), i)  #나이와 인덱스번호(가입순서)를 튜플로 저장
    li.append(t)  #튜플을 리스트에 저장(정렬을 위해)
li.sort() #튜플이 저장된 리스트를 오름차순 정렬
for x in li:
    print(x[0], names[x[1]]) 
    #정렬된 리스트에서 나이 선택, names 리스트에서 인덱스에 해당하는 이름 선택