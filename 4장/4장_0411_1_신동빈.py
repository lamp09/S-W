'''
파일 저장 명 : 4장_0411_1_신동빈.py

작성일 : 2023년 4월 11일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 세 과목의 점수를 입력ㅂ다아 평균이 95점 이상이면
    "당신의 평균은 00.0점 입니다." "축하합니다.A+입니다."를 출력하고, 
    평균점수와 상관없이 "감사합니다."를 출력하는 프로그램을 작성하시오.
'''
# 1. 국어 점수를 입력 받아 변환하여 변수(kor)에 저장한다.
kor = int(input("국어 점수 입력 : "))
# 2. 수학 점수를 입력 받아 변환하여 변수(math)에 저장한다.
math = int(input("수학 점수 입력 : "))
# 3. 영어 점수를 입력 받아 변환하여 변수(eng)에 저장한다.
eng = int(input("영어 점수 입력 : "))
# 4. 평균을 계산하여 변수(avg)에 저장한다.
avg = (kor + math + eng) / 3 
# 5. 평균 점수가 95점 이상이라면 
if avg >= 95.0 :
#   1) "당신의 평균은 00.0점 입니다."
    print("당신의 평균은 {:.1f}점입니다." .format(avg))
#   2) "축하합니다. A+입니다."
    print("축하합니다. A+입니다.")
# 6. 평균과는 상관없이 무조건 "감사합니다." 출력한다
print("감사합니다.")