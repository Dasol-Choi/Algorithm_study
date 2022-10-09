
# Programmers_크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    stack = []
    cnt = 0
    for i in moves:       
        for j in range(len(board)):
            doll = board[j][i-1]
            if doll!=0:                 
                board[j][i-1] = 0
                if len(stack)!=0 and stack[-1]==doll:
                    stack.pop()
                    cnt +=2
                    break
                elif len(stack)==0 or len(stack)!=0 and stack[-1]!=doll:
                    stack.append(doll)
                    break                      
    return cnt