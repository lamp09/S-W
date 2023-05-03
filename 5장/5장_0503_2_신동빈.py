'''
파일 저장 명 : 5장_0502_1_신동빈.py

작성일 : 2023년 5월 2일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
문제 : 하나의 수를 입력받아 팩토리얼을 구하는 프로그램을 작성하시오.
'''

# 1. 수 입력 받기
# 2. total 에 1 입력
# 3. 입력 받은 수 부터
# 4. 1이 될 때 까지
#   1) 팩토리얼 계산
#   2) 증감식
# 5. 결과 출력

num = int(input('수 입력 : '))
total = 1
num1 = num
# while num > 1 :
    # total = total * num
    # num = num - 1
    
# print('{}!는 {}입니다.' .format(num1,total))


for num1 in range(num, 1, -1) :
    total = total * num1

print('{}!는 {}입니다.' .format(num,total))