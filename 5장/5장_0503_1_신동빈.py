'''
파일 저장 명 : 5장_0503_1_신동빈.py

작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
문제 : 사용자로부터 ㅣㅇㅂ력 받은 숫자에 해당하는 구구단을 출력하는 프로그램을 작성하시오.
'''

# 1. 구구단을 입력받는다.
dan = int(input('단 입력 : '))
# 2. 곱하는 수를 1부터 9까지 반복하면서. :
for num in range(1,10) :
#   1) 구구단을 출력한다.
    print('{} * {} = {} ' .format(dan,num, dan*num))
    

num0 = 1
while num0 <= 9 :
    num = dan * num0
    num0 = num0 + 1

print('{} * {} = {}' .format(dan,num0,dan*num))
