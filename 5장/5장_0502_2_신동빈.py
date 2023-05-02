'''
파일 저장 명 : 5장_0502_2_신동빈.py

작성일 : 2023년 5월 2일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
문제 : 두수를 입력 받아 두 수 사이의 모든 정수 값을 더하여 출력하는 프로그램을 작성하시오.
'''

# 1. 정수 입력 받기
num1 = int(input('첫 번째 수 : '))
num2 = int(input('두 번째 수 : '))

# 1) 판단 | 변수 값 교환
if num1 > num2 :
    temp = num1
    num1 = num2
    num2 = temp 
# 2. 합계는 0부터
sum = 0
# 3. 수는 num1 부터
num = num1
# 4. 수는 num 부터 num2 까지
while num <= num2 :
    # 1) 합계 계산
    sum = sum + num
    # 2) 증감식 | 
    num = num + 1
# 5. 합계 출력
print('{}부터 {}까지의 합 : {}' .format(num1, num2, sum))