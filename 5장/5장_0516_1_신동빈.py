'''
파일 저장 명 : 5장_0516_1_신동빈.py

작성일 : 2023년 5월 16일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
문제 : 10개의 정수를 입력 받아 합을 구하는 프로그램ㅇ을 작성하시오. 
    단, 짝수 번째에 입력되는 숫자는 양수를 음수로, 음수는 양수로 바꾸어 합을 구하시오.
'''

#1. sum = 0 , count = 1 로 지정

sum = 0
count = 1
# 2. count 가 10이 될 때 까지 반복
while count <= 10 :
    # 1) num을 입력 받기
    num = int(input('{}번째 점수를 입력하시오.' .format(count)))
    # 2) 만약 짝수 번째 라면
    if count % 2 == 0 :
        # (1) 음수는 양수로, 양수는 음수로 바꾸기
        num = num * -1
    # 3) 합계 계산
    sum = sum + num
    # 4 ) count + 1 해주기  
    count = count + 1
# 3. 출력하기
print('합계 : {}' .format(sum))
    
    
print('===============for문==============')

sum = 0

for count in range(1,11) :
    num = int(input('{}번째 수 입력 : ' .format(count)))
    if count % 2 == 0 :
        num = num * -1
    sum = sum + num

print('합계 : {}' .format(sum)) 

print('=====================')

count = 1
sum = 0
while True : # 무한 반복 코드
    num = int(input('{}번째 수 입력 : ' .format(count)))
    if count % 2 == 0 :
        num = -num 
    sum += num 
    count += 1
    
    if count > 10 :
        break   # 반복 종료 
print('합계 : {}'.format(sum))