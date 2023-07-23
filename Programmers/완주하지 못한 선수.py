# Programmers_완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 딕셔너리 자료형을 이용해서 코드를 짜보았다. 
# 중복되는 단어를 따로 체크하기 위해 단어의 등장 수만큼 value 카운팅을 늘리는 방법을 사용했다. 
# 반대로 completion에 등장하는 단어를 다시 1씩 빼주면, 결과적으로 dictionary에는 value가 1인 item이 하나밖에 남지 않게 된다. 
# 그 단어를 출력하기 위해 value 값을 기준으로 내림차순 정렬을 한 후 첫번째 튜플의 첫번째 값을 인덱싱하였다. 

def solution(participant, completion):
    dict = {}
    for x in participant:
        dict[x] = 0
    for x in participant:
        dict[x] += 1
    for x in completion:
        dict[x] -= 1  
    s_dict = sorted(dict.items(), key=lambda x: -x[1])
    answer = s_dict[0][0]
    return answer