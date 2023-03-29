'''
작성일 : 2023년 3월 28일
학과 : 컴퓨터공학부
학번 : 202395019
이름 : 신동빈
설명 : 변수 사용법과 자료형 알아보기
        print() 함수 사용법 익히기.
'''
# 변수 num1에 10을 배정하시오.
num1 = 10

# 변수 num2에 20을 저장하시오.
num2 = 20   # 첫 칸 띄어쓰기 하지 말 것!!!

# 변수에 3.14를 저장하시오.
PI = 3.14

# 변수에 자기 이름을 저장하시오.
name = "신동빈"

# num1, num2에 저장된 값을 더하여 total에 저장하시오.
total = num1 + num2

# 각 변수에 저장된 값을 출력한다.
print("num1변수에 저장된 값 :", num1)
print("num2변수에 저장된 값 :",num2)

print("PI변수에 저장된 값은 {}입니다." .format(PI))

# 나의 이름은 신동빈입니다.
print("나의 이름은 {}입니다." .format(name))


# 10 + 20 = 30
print("{} + {} = {}" .format(num1, num2, total))
print(num1, "+", num2, "=", total)

# 변수의 자료형 알아보기 위해서 사용하는 함수
# type()
print("num1의 자료형 : ", type(num1))
print("PI의 자료형 : ", type(PI))
print("name의 자료형 : ", type(name))