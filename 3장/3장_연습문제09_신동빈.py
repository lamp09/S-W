'''
파일 저장 명 : 3장_연습문제11_신동빈.py

작성일 : 2023년 3월 29일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 연습문제09
        홍길동의 본봉은 300만원이다. 이번 달 수당으로 30만원을 받았으며,
        세금으로 총액의 20%를 냈다. 홍길동의 이번 달 월급 수령액을 구하는 프로그램을 작성하시오.
'''

# 1. 본봉 300을 b변수에 저장한다.
b = 300

# 2. 수당 30을 s변수에 저장한다.
s = 30

# 3. 총액값인 b + s 값을 계산하여 c변수에 저장한다.
c = b + s

# 4. 세금값인 c * 0.2 값을 계산하여 t변수에 저장한다.
t = c * 0.2

# 5. 수령액값인 b + s - t 값을 계산하여 m변수에 저장한다.
m = b + s - t

# 6. 수령액을 출력한다.
print("홍길동이 이번 달 월급 수령액으로 받을 금액은 {}만원 입니다." .format(m))