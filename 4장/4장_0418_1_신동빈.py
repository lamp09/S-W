'''
파일 저장 명 : 4장_0418_1_신동빈.py

작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 한 과목이 점수를 입력 받아 점수에 따라 학점을 부여하는 프로그램을 작성하시오.
    A학점 : 90~100
    B학점 : 89~80  
    C학점 : 79~70
    D학점 : 69~60
    F학점 : 59~0
단, 입력 받는 점수는 0 ~ 100 사이여야 합니다.
잘못된 점수를 입력하면 " 점수를 잘못 입력하셨습니다. " 출력하시오.
'''
# 1. 점수를 입력 받는다.
score = int(input("점수 입력 : "))

# 2. 만약 score가 0 ~ 100 사이라면
if 0 <= score <= 100 :
    # 1) 만약 점수가 90점 이상이면 "A학점입니다." 출력
    if score >= 90 :
        print("A학점입니다.")
    # 2) 만약 점수가 80점 이상이라면 "B학점입니다." 출력
    elif score >= 80 :
        print("B학점입니다.")
    # 3) 만약 점수가 70점 이상이라면 "C학점입니다." 출력
    elif score >= 70:
       print("C학점입니다.")
    # 4) 만약 score값이 69~60이라면 "D학점입니다." 출력
    elif score >= 60:
       print("D학점입니다.")
    # 5) 아니면
    else :
        print("F학점입니다.")
# 3. 아니면 "점수를 잘못 입력하셨습니다." 출력
else :
    print("점수를 잘못 입력하셨습니다.")