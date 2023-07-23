# Programmers_괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

# 올바른 문자열 확인 함수(오른쪽 왼쪽 괄호의 쌍이 맞는지)
def correct(x): 
    stack = []  #스택구조 사용
    for i in x:
        if i == '(':  #왼쪽 괄호가 들어오면 무조건 스택에 삽입
            stack.append(i)
        else:  #오른쪽 괄호가 들어오면 
            if stack and stack[-1] =='(': #스택의 마지막이 왼쪽 괄호인지 확인
                stack.pop()  #맞으면 스택의 왼쪽괄호를 삭제
            else:
                return False  #스택의 마지막이 오른쪽 괄호이면 False 반환
                break
    else:
        return True  # for문에서 break 당하지 않았다면 True 반환

# 균형잡힌 괄호 문자열 확인 함수(오른쪽 왼쪽 괄호의 개수가 같은지)
def seperate(x):
    cnt = 0  
    for i in range(len(x)):  #왼쪽 괄호 나타나면 +1
        if x[i] == '(':
            cnt += 1
        else:  #오른쪽 괄호 나타나면 -1
            cnt -=1
        if cnt == 0:  # += 해서 0이 나오면 개수가 같음
            idx = i  # 이 때의 index 값을 저장하고 break
            break
    u, v = x[:idx+1], x[idx+1:] #index 이하를 분리해서 u, 이후를 분리해서 v에 저장
    return u, v  # 변수 반환

# 답을 도출하는 함수
def solution(p):
    if len(p) == 0: #입력이 빈 문자열이면, 빈 문자열 반환
        return ''
    else:
        u, v = seperate(p) #문자열 분리한 결과 변수에 할당
        if correct(u) == True: # u가 "올바른 괄호 문자열" 이라면
            return u + solution(v) # u와 solution(v)를 더함(재귀함수 호출)
        else:  # u가 "올바른 괄호 문자열" 이 아니라면
            res = '(' + solution(v) + ')' # 조건에 맞게 문자들 결합해서 결과변수에 저장
            for x in u[1:-1]: # u에서 첫번째와 마지막 문자를 제거 한후 
                if x=='(' :   # 남은 문자열의 괄호방향을 뒤집어서 결과변수 뒤에 삽입
                    res += ')'
                else:
                    res += '('
            return res  #결과 반환!
