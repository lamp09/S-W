'''
파일 저장 명 : 4장_0411_4_신동빈.py

작성일 : 2023년 4월 11일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 두 수를 입력 받아 큰 수를 출력하는 프로그램을 작성하시오.
'''

# 1. 첫 번째 수를 입력받아 num1 변수에 저장
num1 = int(input("첫 번째 숫자 : "))
# 2. 두 번째 수를 입력받아 num2 변수에 저장
num2 = int(input("두 번째 숫자 : "))
# 3. 만약 첫 번째 숫자가 더 크다면
if num1 > num2 :
#   1) num1 출력하기
    print(num1)
# 4. 아니면
else :
#   1) num2 출력하기
    print(num2)