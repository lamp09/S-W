'''
파일 저장 명 : 5장_0516_2_신동빈.py

작성일 : 2023년 5월 16일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
문제 : 사용자로부터 가장 좋아하는 월을 입력 받아 
    그 월에 해당되는 계정을 출력하는 프로그램을 메뉴 형태로 while 문을 사용하여 작성하시오.
'''


# 1. 무한 반복
# 2. 월 입력 받기
#   1) 만약 month 가 0이면
    #   (1) 종료
#   2) 만약 3~5사이면 봄입니다 출력
#   3) 아니고 만약 6~8사이면 여름입니다 출력
#   4) 아니고 만약 9~11사이면 가을입니다 출력
#   5) 아니고 만약 1,2,12라면 겨울입니다 출력
#   6) 아니면 다시입력하시오 출력

while True :
    print('================================')
    month = int(input('가장 좋아하는 월(종료 : 0) : '))
    if month == 0 :
        break
    if 3 <= month <= 5 :
        print('****{}월****'.format(month))
        print('{}월은 봄에 해당됩니다.' .format(month))
    elif 6 <= month <= 8 :
        print('****{}월****'.format(month))
        print('{}월은 봄에 해당됩니다.' .format(month))
    elif 9 <= month <= 11 :
        print('****{}월****'.format(month))
        print('{}월은 봄에 해당됩니다.' .format(month))
    elif month == 2 or month == 1 or month == 12 :
        print('****{}월****'.format(month))
        print('{}월은 봄에 해당됩니다.' .format(month))
    else :
        print('다시 입력해주십시오. ')