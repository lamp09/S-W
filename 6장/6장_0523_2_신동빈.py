'''
작성일 : 2023년 5월 23일
학과 : 컴퓨터공학부
학번 : 202395019
이름: 신동빈
설명 : 6장 시퀀스 자료형
        04. 다중 리스트
'''
# 다중 리스트
num = [[11,12,13],[22,23,24],[31,32,33,34],[41,42]]
# 리스트 내의 각각 리스트의 합계를 계산하여 출력
for i in range(len(num)) :  # num 리스트의 길이 만큼 반복
    total = 0
    for j in range(len(num[i])) : # 0번지의 길이까지 반복
        total = total + num[i][j]
    print(i + 1,'번째 줄의 합 : ', total)
print()

# 실습 예제 6-5 
# 1~100 사이에 랜덤 수 10개를 발생시켜 리스트에 저장하고 
# 합계, 최대값, 최소값을 출력하시오.
#오름차순으로 정렬도 하시오.
import random # 랜덤 함수를 포함.
num = []

for i in range(10) :
    num.append(random.randint(1,100)) # 1 부터 100까지 랜덤으로 생성 된 수를 num 에 추가

print("생성된 리스트 : ", num)
num.sort()
print('오름차순으로 정렬 : ', num)
print('가장 큰 값 : ', max(num))
print('가장 작은 값 : ',min(num))
print('리스트의 합 : ', sum(num))