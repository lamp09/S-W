'''
파일 저장 명 : 4장_0419_2_신동빈.py

작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈(숫자 → 연산자 → 숫자) 순으로 입력 받아 사칙연산의 결과를 출력하는 계산기 프로그램을 작성하시오.
    단, (+,-,*,/) 이외의 연산자를 입력하면 "해당연산자가 없습니다." 출력합니다.
설명 : 
'''

# 1. 첫번째 숫자를 score1 변수에 저장
score1 = int(input("첫 번째 숫자 입력 : "))
# 2. 연산자를 입력 받아 cal 변수에 저장
cal = input("연산자 입력 : ")
# 3. 두번째 숫자를 score2 변수에 저장
score2 = int(input("두 번째 숫자 입력 : "))
# 4. 만약 cal이 + 라면 (score1 + score2 = (score1+score2)) 출력
if cal == '+' :
    print("{} + {} = {}" .format(score1, score2, score1 + score2))
# 5. 아니고 만약 cal이 - 라면 (score1 - score2 = (score1 - score2)) 출력
elif cal == '-' :
    print("{} - {} = {}" .format(score1, score2, score1 - score2))
# 6. 아니고 만약 cal이 * 라면 (score1 * score2 = (score1 * score2)) 출력
elif cal == '*' :
    print("{} * {} = {}" .format(score1, score2, score1 * score2))
# 7. 아니고 만약 cal이 / 라면 (score1 / score2 = (score1 / score2)) 출력
elif cal == '/' :
    print("{} / {} = {}" .format(score1, score2, score1 / score2))
# 8. 아니면 "해당 연산자가 없습니다." 출력
else :
    print("해당 연산자가 없습니다.")