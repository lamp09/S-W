'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395019
이름: 신동빈
설명 : 7장 시퀀스 자료형
        01. 세트

순서가 없으면서 중복을 허용하지 않는 자료구조
'''
# 랜덤으로 로또 번호 알려줘~
# 1. 로또 번호 저장 할 세트 만들기
# 2. 6번 반복하면서 
#   1) 1~45 사이의 값을 세트변수에 추가
# 3. 로또 번호 출력

import random

lotto = set()

for i in range(6) :
    lotto.add(random.randint(1,45))
    if len(lotto) != 6 :
        continue
print('로또 번호 : ', lotto)

lotto2 = set()
while len(lotto2) != 6 :
    lotto2.add(random.randint(1,45))
print('로또 번호 : ', lotto2)


lotto3 =set()
while True :
    lotto3.add(random.randint(1,45))
    if len(lotto3) == 6 :
        break
print('로또 번호 : ',lotto3 )