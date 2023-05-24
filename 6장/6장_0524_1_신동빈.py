'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 튜플 배우기
'''
# 튜플 생성
tuple1 = () # 비어있는 튜플 생성
tuple2 = ('a', ) # 원소가 하나여도 쉼표는 필수!! (,)
tuple3 = ('a', 'b', 'c')

color = ('violet', 'white', 'blueviolet', 'white' , 'aqua', 'white', 'pink')
print('color 내용 : ', color)
print('color의 길이 : ', len(color)) # len = 길이
print('white의 갯 수 : ', color.count('white')) # count = 갯 수
print('blueviolet 의 위치 : ', color.index('blueviolet')) # index = 주소

# 실습 예제 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('사과', '배', '파인애플', '포도')
price = ('1000', '1500', '3500', '4500')

# 결과 : [사과, 2000, 배, 4500, ...]

fp_list = [] # 2개의 튜플이 저장될 리스트 생성
fp_tuple = () # 2개의 튜플 내용이 저장 될 튜플 생성

for i in range(len(fruit)) :
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    # fp_tuple.append(fruit[i]) # 튜플은 변경이 불가능 함!! (추가 불가능)
    
print('과일 목록 : ',fruit)
print('가격 모록 : ',price)
print('과일의 가격 리스트 : ', fp_list )
'''
fp_list.append(fruit[0])
fp_list.append(price[0])

fp_list.append(fruit[1])
fp_list.append(price[1])

fp_list.append(fruit[2])
fp_list.append(price[2])
'''
