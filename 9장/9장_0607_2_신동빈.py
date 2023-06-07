'''
작성일 : 6월 7일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 9장 함수와 모듈
'''

import random # 무한 반복
def make_question(): # 함수 make_question() 정의
    num1 = random.randint(1,40) # num1에 1~ 40 사이의 수를 임의로 저장
    num2 = random.randint(1,20) # num2에 1 ~ 20 사이의 수를 임의로 저장
    op = random.randint(1,3) # op 에 1 ~ 3 사이의 수를 임의로 저장
    
    que = str(num1) # que 에 num1 을 문자열로 저장
    
    if op == 1: # 만약 op 가 1이면 que 에 '+' 문자 저장
        que = que + '+'
    if op == 2: # 만약 op 가 2이면 que 에 '-' 문자 저장
        que = que + '-'
    if op == 3: # 만약 op 가 2이면 que 에 '*' 문자 저장
        que = que + '*'
        
    que = que + str(num2) # que 에 num2 를 문자열로 저장 
    
    return que # que를 반환
        
R_ans = 0 # 0을 R_ans 에 저장
W_ans = 0 # 0을 W_ans 에 저장

for i in range(5): # 5번 반복
    que = make_question() # que 에 make_question()을 저장
    print(que, end='') # que 를 출력하고 '' 과 이어줌
    
    result = int(input('=')) # result 에 정수형으로 수 입력
    
    if eval(que) == result : # que 식 계산 값과 reult 에 입력된 값가 같다면 '정답입니다.' 출력하고 R_ans 에 1 추가
        print('정답입니다.')
        R_ans += 1 
    else : # 아니면 '오답입니다.' 출력하고 W_ans 에 1 추가
        print('오답입니다.')
        W_ans += 1
        
print('정답 : ', R_ans, '오답 : ', W_ans) # '정답 : ', R_ans, '오답 : ', W_ans 출력

if W_ans == 0 : # 만약 W_ans 가 0이라면 '당신은 천재입니다.' 출력
    print('당신은 천재입니다.')